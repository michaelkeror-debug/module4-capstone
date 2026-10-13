---
marp: true
paginate: true
---

# 1. Problem and user
- **User:** clinic coordinators in partner counties
- **Problem:** urgent patient messages sit in one queue with routine delivery and catalog questions
- **Decision supported:** which message needs action first, and where supplies are
- **Success:** golden eval stays at 1.00, the fixture agrees with the router, and an urgent message returns `urgency: high`

---

# 2. Path chosen and why
- **Path:** AfyaPlus Module 4 Capstone
- **Why:** it combines every module skill (API, auth, RAG, MCP tool, tests, CI) in one product
- **Scope:** stub mode with synthetic data, so it runs offline with no live key
- **Out of scope:** training a model, live crawling of PII, mixing clinical and marketplace fixtures

---

# 3. Architecture
```
Client -> /token (JWT login) -> /triage (coordinator only)
                                   |
                  router (config.json keywords)
                 /          |            \
          triage model   RAG lookup   MCP logistics tool
         (keyword stub)  (local docs)   (clinic.json)
```
- **Boundaries:** `services/triage` (API + auth), `agents/` (router + tools), `fixtures/`, `evals/`, `tests/`
- Redaction runs before anything is written to the audit log

---

# 4. Skill coverage
| Skill | Where in repo | Req/Opt |
|---|---|---|
| API / agent path | services/triage | Required |
| MCP tools | agents/tools/logistics.py | Required |
| Pin / versioning | prompts/pin.json | Required |
| Security hygiene | tests/test_security_smoke.py | Required |
| Eval / test | tests/unit/, evals/golden.jsonl | Required |
| Docs | docs/ | Required |
| Multimodal | services/catalog | Optional (deferred) |

---

# 5. Live demo
One command: `bash scripts/demo.sh`
1. `/health` returns healthy
2. Login as coordinator, receive a token
3. Send "child has chest pain" and receive `urgency: high`

*Backup: 60-second recording of the same run.*

---

# 6. Testing evidence
- `pytest -q`: **9 passed, 1 deselected** (integration needs a live service)
- Golden-set eval: **3/3 = 1.00**
- Fixture: **300 rows**, `diagnose OK, all rows agree with router`
- Security smoke: includes a real redaction test (emails, phones, IDs, M-Pesa codes, bearer tokens)
- CI: GitHub Actions runs `pytest`

---

# 7. Security and compliance
- JWT login with a coordinator role check (patients get 403)
- Passwords stored as bcrypt hashes; demo credentials are teaching-only
- `.env` and audit logs are kept out of git
- PII redacted before logging
- Synthetic data only, no production scrape

---

# 8. Cost table

<style scoped>
table { font-size: 22px; }
</style>

| Call type | Calls (n) | Unit cost | Total | Assumptions |
|---|---|---|---|---|
| Stub tests (CI) | 0 live | $0 | $0 | CI never calls a live key |
| Live demo (`demo.sh`) | 0 live | $0 | $0 | Triage, RAG and MCP tool run in stub mode |
| Future live model call (not built) | ~10 per demo | ~$0.10 | ~$1 | Teaching estimate, capped at ~$1; not in this submission |

*Teaching table, not a quote. Hosting is the laptop; a real model call would be the first non-zero cost.*

---

# 9. What works vs deferred
**Works:** stub triage API, auth, router, RAG smoke, one MCP tool, 300-row fixture, eval, CI
**Deferred:** live model call, catalog service, production performance numbers
*Perf figure is a laptop teaching stub, not an SLA.*

---

# 10. Process
- Feature branch `feature/capstone-setup`, PR to `main`
- Review: self-review with the checklist (no peer pair), logged in `review_log.md`
- **Incident:** fixture row T-016 mislabelled and the router had no "order" keyword. Found with `diagnose_fixture.py`, fixed in config and data
- **Next:** live model behind an env flag, catalog service, whole-word keyword matching