# Judge Access — Amazon Developer Hackathon 2026

The repository is private, so the final submission must satisfy the official private-repository access requirement before the deadline.

## Required Amazon GitHub reviewers

Grant repository access to:

- `chris-trag`
- `knmeiss`
- `giolaq`
- `anishamalde`
- `mosesroth`
- `emersonsklar`

Also invite:

- `testing@devpost.com`

## Current verified status

At the time this file was added, the six Amazon GitHub accounts above did **not** yet have collaborator permission on this private repository.

This is a submission blocker, not a code blocker.

## Repository entry point

Judges should start at:

`YASMIN_AMAZON_HACKATHON.md`

Then follow:

`yasmin/hackathon/amazon-2026/JUDGE_QUICKSTART.md`

## Quick run

```bash
cd yasmin/hackathon/amazon-2026
npm install
npm test
npm start
```

The project exposes:

- web judge experience at the server root;
- health metadata at `/health`;
- Streamable HTTP MCP at `/mcp`.
