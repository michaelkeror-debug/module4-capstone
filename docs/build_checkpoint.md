<!-- Change for your project: everything below. Keep the "Works" and "Deferred" headings. -->
# Build checkpoint

## Works now
- Unit tests: `pytest -q` gives 9 passed, 1 deselected (the integration test, which needs the service running).
- Triage API: `/health` returns 200; `/token` and `/triage` work with JWT and role check.
- RAG smoke: `python -m services.triage.rag_smoke` grounds an answer in the small doc set (stub mode).
- MCP tool: `check_stock` runs in stub mode from local `clinic.json` (5 clinics).
- Fixture: `fixtures/triage_messages_sample.jsonl`, ~300 rows (confirm with `wc -l`).
- Eval: `python evals/run_eval.py evals/golden.jsonl` prints golden-set score 3/3 = 1.00.
- Perf: `perf_stub.json` written by `scripts/measure_perf.py` (laptop teaching stub; not a production SLA).

## Incident note
- What broke: T-016 was mislabelled, and the router had no keyword for "order".
- How I found it: diagnose_fixture.py listed the disagreements.
- The fix: added the "order" keyword and corrected the label.

## Deferred
- Catalog service (`services/catalog`): deferred in `integration_map.json`.
- Live model call: triage uses a keyword stub, with no live key yet.
- Integration test runs only with `SERVICE_UP=1` and the service running; not part of default CI.
- Production perf numbers: current figures come from a laptop stub.




