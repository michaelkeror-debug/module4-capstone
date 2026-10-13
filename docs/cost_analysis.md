# Cost analysis

| Call type | Calls (n) | Unit cost | Total | Assumptions |
|---|---|---|---|---|
| Stub tests (`pytest -q`, CI) | 0 live calls | $0 | $0 | CI never calls a live key |
| Live demo (`scripts/demo.sh`) | 0 live calls | $0 | $0 | Triage, RAG and the MCP tool all run in stub mode locally |
| Future live model call (not built) | ~10 per demo | teaching estimate, ~$0.10 | ~$1 | Would be capped at about $1; not part of this submission |

Teaching table, not a quote. Hosting is the laptop, and GitHub Actions on a public or free-tier repo adds no cost. A real model call would be the first non-zero line.