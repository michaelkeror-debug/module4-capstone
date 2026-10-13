#!/usr/bin/env bash
set -e
pytest -q
python evals/run_eval.py evals/golden.jsonl
python scripts/diagnose_fixture.py fixtures/triage_messages_sample.jsonl
python -m services.triage.rag_smoke
uvicorn services.triage.app:app --port 8080 & PID=$!
trap "kill $PID" EXIT
sleep 3
curl -s localhost:8080/health; echo
TOKEN=$(curl -s -X POST localhost:8080/token -H "Content-Type: application/json" -d '{"username":"mercy","password":"logistics2026"}' | python -c "import sys,json;print(json.load(sys.stdin)['access_token'])")
curl -s -X POST localhost:8080/triage -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"patient_message":"child has chest pain","county":"Nairobi"}'; echo
python scripts/measure_perf.py --url http://localhost:8080/health --n 10 --out perf_stub.json