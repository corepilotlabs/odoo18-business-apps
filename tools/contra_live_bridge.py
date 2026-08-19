import base64
import json
import os
import re
import time

import requests
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from playwright.sync_api import sync_playwright

EMAIL = os.environ.get("CONTRA_LOGIN_EMAIL", "").strip()
TOKEN = os.environ.get("GH_TOKEN", "")
REPO = os.environ.get("GH_REPO", "")
ISSUE = os.environ.get("GH_ISSUE", "")
RUN_ID = os.environ.get("GH_RUN_ID", "")
API = f"https://api.github.com/repos/{REPO}/issues/{ISSUE}/comments"
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def post_comment(text):
    r = requests.post(API, headers=HEADERS, json={"body": text}, timeout=20)
    r.raise_for_status()


def comments():
    r = requests.get(API + "?per_page=100", headers=HEADERS, timeout=20)
    r.raise_for_status()
    return r.json()


def first_visible(page, selectors):
    for selector in selectors:
        loc = page.locator(selector)
        if not loc.count():
            continue
        node = loc.first
        try:
            if node.is_visible():
                return node
        except Exception:
            pass
    return None


def clean(v):
    return re.sub(r"\s+", " ", v or "").strip()


def visible_buttons(page, limit=30):
    out = []
    loc = page.locator("button, [role='button'], input[type='submit']")
    for i in range(min(loc.count(), 100)):
        node = loc.nth(i)
        try:
            if not node.is_visible():
                continue
            text = clean(node.inner_text())[:100]
        except Exception:
            continue
        if text and text not in out:
            out.append(text)
        if len(out) >= limit:
            break
    return out


def input_meta(page, limit=40):
    out = []
    loc = page.locator("input, textarea, select")
    for i in range(min(loc.count(), limit)):
        node = loc.nth(i)
        try:
            if not node.is_visible():
                continue
        except Exception:
            continue
        meta = {"tag": node.evaluate("el => el.tagName.toLowerCase()")}
        for key in ("type", "name", "id", "autocomplete", "placeholder", "inputmode", "aria-label"):
            value = node.get_attribute(key)
            if value:
                meta[key] = value[:120]
        out.append(meta)
    return out


result = {
    "status": "starting",
    "authenticated": False,
    "run_id": RUN_ID,
    "profile_completion_percent": None,
    "complete_profile_surface": None,
}

if not EMAIL:
    result["status"] = "missing_email_secret"
    print("CONTRA_LIVE_RESULT=" + json.dumps(result))
    raise SystemExit(0)

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_der = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)
public_b64 = base64.b64encode(public_der).decode("ascii")
post_comment(f"[CONTRA-LIVE-KEY] run={RUN_ID} pub={public_b64}")

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome", headless=True)
        page = browser.new_page()
        page.goto("https://contra.com/", wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(900)

        login = first_visible(page, [
            "a:has-text('Log in')", "button:has-text('Log in')",
            "a:has-text('Sign in')", "button:has-text('Sign in')",
        ])
        if login is None:
            result["status"] = "login_entry_not_found"
            raise RuntimeError("login_entry_not_found")
        login.click()
        page.wait_for_timeout(900)

        field = first_visible(page, ["#emailAddress", "input[type='email']", "input[placeholder*='email' i]"])
        if field is None:
            result["status"] = "email_field_not_found"
            raise RuntimeError("email_field_not_found")
        field.fill(EMAIL)
        submit = first_visible(page, [
            "form:has(#emailAddress) button[type='submit']",
            "button[type='submit']", "button:has-text('Continue')",
            "button:has-text('Log in')", "button:has-text('Sign in')",
        ])
        if submit is not None:
            submit.click()
        else:
            field.press("Enter")
        page.wait_for_timeout(1800)

        code_inputs = page.locator("input[id^='codeInput-id-']")
        if code_inputs.count() < 6:
            result["status"] = "otp_surface_not_found"
            raise RuntimeError("otp_surface_not_found")
        post_comment(f"[CONTRA-LIVE-WAITING] run={RUN_ID} state=otp")

        cipher_b64 = None
        deadline = time.time() + 180
        marker = f"[CONTRA-LIVE-CODE] run={RUN_ID} cipher="
        while time.time() < deadline:
            for item in reversed(comments()):
                body = item.get("body") or ""
                if marker in body:
                    cipher_b64 = body.split(marker, 1)[1].split()[0].strip()
                    break
            if cipher_b64:
                break
            time.sleep(2)
        if not cipher_b64:
            result["status"] = "otp_cipher_timeout"
            raise RuntimeError("otp_cipher_timeout")

        encrypted = base64.b64decode(cipher_b64)
        code = private_key.decrypt(
            encrypted,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        ).decode("utf-8").strip().upper()
        if not re.fullmatch(r"[A-Z0-9]{6}", code):
            result["status"] = "otp_cipher_invalid"
            raise RuntimeError("otp_cipher_invalid")

        for i, ch in enumerate(code):
            code_inputs.nth(i).fill(ch)
        page.wait_for_timeout(3500)

        if page.locator("input[id^='codeInput-id-']").count() >= 6:
            verify = first_visible(page, [
                "button:has-text('Verify')", "button:has-text('Continue')",
                "button:has-text('Confirm')", "button[type='submit']",
            ])
            if verify is not None:
                try:
                    verify.click()
                    page.wait_for_timeout(3000)
                except Exception:
                    pass

        page.goto("https://contra.com/", wait_until="domcontentloaded", timeout=45000)
        page.wait_for_timeout(1400)
        body = clean(page.locator("body").inner_text()) if page.locator("body").count() else ""
        low = body.lower()
        authenticated = any(x in low for x in ("what are you working on", "complete profile"))
        result["authenticated"] = authenticated
        if not authenticated:
            result["status"] = "session_not_authenticated"
            result["buttons"] = visible_buttons(page, 15)
        else:
            result["status"] = "authenticated"
            m = re.search(r"(\d{1,3})%\s*complete profile", body, re.I) or re.search(r"complete profile\s*(\d{1,3})%", body, re.I)
            if m:
                result["profile_completion_percent"] = int(m.group(1))

            complete = first_visible(page, ["a:has-text('Complete profile')", "button:has-text('Complete profile')"])
            if complete is not None:
                complete.click()
                page.wait_for_timeout(1200)
                result["complete_profile_surface"] = {
                    "url": page.url,
                    "inputs": input_meta(page),
                    "buttons": visible_buttons(page),
                }
            else:
                result["complete_profile_surface"] = {
                    "url": page.url,
                    "inputs": input_meta(page),
                    "buttons": visible_buttons(page),
                    "note": "complete_profile_action_not_found",
                }
        browser.close()
except Exception as exc:
    if result.get("status") == "starting":
        result["status"] = "bridge_error"
    result["error_type"] = type(exc).__name__

print("CONTRA_LIVE_RESULT=" + json.dumps(result, ensure_ascii=False))
try:
    post_comment(
        f"[CONTRA-LIVE-RESULT] run={RUN_ID} status={result.get('status')} "
        f"authenticated={str(result.get('authenticated')).lower()} "
        f"completion={result.get('profile_completion_percent')}"
    )
except Exception:
    pass
with open("contra-live-result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
