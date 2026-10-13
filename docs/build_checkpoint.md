# Build checkpoint

## Works now
- Unit tests: `pytest -q` gives 10 passed, 1 deselected (the integration test, which needs the service running and `SERVICE_UP=1`).
- Triage API: `/health` returns 200; `/token` issues a JWT; `/triage` requires the coordinator role (patients get 403).
- Router: keyword routing from `config.json` to triage, logistics_lookup or catalog_mismatch.
- RAG smoke: `python -m services.triage.rag_smoke` returns a grounded answer from the local doc set (stub mode).
- MCP tool: logistics `check_stock` runs from local `clinic.json`, no network or key.
- Security smoke: redaction of emails, phones, national IDs, M-Pesa codes and bearer tokens.
- Fixture: `fixtures/triage_messages_sample.jsonl`, 300 synthetic rows; `diagnose OK, all rows agree with router`.
- Eval: `golden-set score: 3/3 = 1.00`.
- Perf: `perf_stub.json` written by `scripts/measure_perf.py` (laptop teaching stub, not an SLA).
- CI: GitHub Actions `ci.yml` runs `pytest -q` on every pull request and passes.
- One-command demo: `bash scripts/demo.sh` (transcript in `docs/demo_transcript.txt`).

## Incident note
- What broke: T-016 was mislabelled, and the router had no keyword for "order".
- How I found it: diagnose_fixture.py listed the disagreements.
- The fix: added the "order" keyword and corrected the label.

## Deferred
- Live model call: triage is a keyword stub (`triage-stub-v1`); no live API key is used.
- Catalog service (`services/catalog`): optional, deferred in `integration_map.json`.
- Integration test: runs only with the service up, so it is excluded from default CI.
- Production performance numbers: current figures come from a laptop stub.
- Whole-word keyword matching in the router: tracked in GitHub Issue #2.
- CI warning, Node.js 20 deprecation: `actions/checkout@v4` and `actions/setup-python@v5` are forced onto Node 24. CI still passes; bump the action versions later.
- CI notice, `ubuntu-latest` moves to Ubuntu 26 on 2026-10-19: if CI breaks after that date, pin `runs-on: ubuntu-24.04`.