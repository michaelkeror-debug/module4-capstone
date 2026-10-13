# Fixtures

Teaching fixture target: 200 to 500 rows (about 300 for the default triage sample).

## Rules
- **Synthetic only.** Every row is generated offline by `scripts/make_fixture.py`. No real patient data.
- **No production scrape.** Nothing is copied from live systems.
- **No mixed domains.** Clinical and marketplace records stay out of the same file.

## Current fixture
`fixtures/triage_messages_sample.jsonl`: 300 rows. Each row has `id`, `text` and `label`, where the label is one of `triage`, `logistics_lookup` or `catalog_mismatch`.

## Generate
```bash
python scripts/make_fixture.py --rows 300 --out fixtures/triage_messages_sample.jsonl
```

## Check
```bash
python scripts/diagnose_fixture.py fixtures/triage_messages_sample.jsonl
```
Expected: `diagnose OK, all rows agree with router`.

## Notes
The JSONL file itself must stay valid JSON, one record per line, with no `#` comment lines, because a loader treats every line as a record. Notes about the fixture live here, in prose.p