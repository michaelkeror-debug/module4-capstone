# Module 4 Capstone: AfyaPlus

## Overview
AfyaPlus is a triage and logistics API for clinic coordinators. A JWT-protected `/triage` endpoint flags urgent patient messages, a keyword router sends each message to triage, logistics lookup or catalog mismatch, and one MCP logistics tool answers stock questions from local clinic data. Everything runs in stub mode with synthetic data, so no live key is needed. Path chosen: the AfyaPlus Module 4 Capstone.

## Project path
- AfyaPlus Module 4 Capstone (recommended)


## Week reuse (open these)
- Week 6: afyaplus-service-platform/triage_model_call
- Week 6: afyaplus-service-platform/logistics_mcp.py
- Week 8: `services/triage/prompts/pin.json`
- Week 8: `scripts/smoke-health.py`
- Week 10: catalog deferred (`services/catalog`, optional)

## Dataset
- fixtures/: 300 synthetic rows (`fixtures/triage_messages_sample.jsonl`). No production scrape.

## Quick start
```bash
pytest -q
```

## Docs
- [docs/architecture.md](docs/architecture.md)
- [docs/deployment.md](docs/deployment.md)
- [docs/cost_analysis.md](docs/cost_analysis.md)
- [docs/user_guide.md](docs/user_guide.md)
- [docs/build_checkpoint.md](docs/build_checkpoint.md)

Also: [proposal.md](proposal.md), [skill_matrix.md](skill_matrix.md), [integration_map.json](integration_map.json), [fixtures/README.md](fixtures/README.md)

## Testing
- unit default: `pytest -q` (10 passed, 1 deselected)
- integration: `SERVICE_UP=1 pytest -o addopts="" -m integration` (service must be running)
- security: `pytest tests/test_security_smoke.py`
- eval: `python evals/run_eval.py evals/golden.jsonl` (3/3 = 1.00)

## Demo
Three commands: start the service, curl /health, curl /triage. See [docs/user_guide.md](docs/user_guide.md). One command for everything: `bash scripts/demo.sh` (transcript in `docs/demo_transcript.txt`).

## Presentation
[docs/presentation.pdf](docs/presentation.pdf), presented Week 12 Monday.

## Peer review
- review_log.md entry: [review_log.md](review_log.md) (PR #1, self-review)
- checklist: [docs/peer_review_checklist.md](docs/peer_review_checklist.md)

## Fallbacks declared
- [x] no live OpenAI key (stub agent)
- [x] no Docker (integration manual)
- [x] no cloud deploy executed (docs only)
- [x] solo reviewer (self-review with checklist)

## Submission checklist
- [x] proposal + skill_matrix + map
- [x] five docs linked
- [x] peer review completed
- [x] slides PDF in docs/ and demo command documented