# Deployment

## Run locally
```bash
uvicorn services.triage.app:app --port 8080
```
One-command demo (tests, eval, fixture check, RAG smoke, live API calls):
```bash
bash scripts/demo.sh
```

## Env vars
- `JWT_SECRET`: signing key for tokens. A development default exists for local teaching use; set a real value anywhere else.
- No model API key is needed. Triage runs as a keyword stub, so nothing calls a live model.

## Health
`GET /health` returns 200 with `{"service":"triage-api","version":"1.0.0","status":"healthy"}`.

## CI
`.github/workflows/ci.yml` installs `requirements.txt` and runs `pytest -q` on pull requests and pushes to `main`. It sets a throwaway `JWT_SECRET`, so CI never needs secrets.

## Fallback
Cloud deployment and Docker were not executed live for this capstone. A container or cloud run would use the same uvicorn command, with `JWT_SECRET` supplied by the platform's secret store. Not executed live.