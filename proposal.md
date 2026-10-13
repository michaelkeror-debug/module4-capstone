
# Capstone proposal

## Path
AfyaPlus Module 4 Capstone: integrated AI health-operations system


## Problem
Clinic coordinators in partner counties cannot quickly tell which patient messages are urgent or where medical supplies are. Messages sit in one queue, so a chest-pain report can wait behind a routine delivery question.

The system routes each message to triage, logistics lookup or catalog mismatch, flags urgent symptoms, and lets coordinators check clinic stock and delivery routes.

I will know it works when the golden-set eval stays at 1.00, the 300-row fixture agrees with the router, and the demo shows an urgent message returning `urgency: high`.

## Dataset
fixtures/triage_messages_sample.jsonl: ~300 synthetic rows (teaching only).
Do not scrape production. Do not use millions of rows.

## Milestones
- Monday: proposal, skill_matrix, integration_map, base service /health 200
- Tuesday: pytest pyramid, security smoke, CI, remaining layers, fixture diagnosis, eval score
- Thursday: docs, peer review, presentation deck
- Week 12 Monday: presentation and demo

## Out of scope
- Training a new foundation model
- Live crawl of PII
- Mixing clinical and marketplace fixtures
