import json
from pathlib import Path
from agents.router import route

def test_fixture_rows_match_router():
    rows = [json.loads(l) for l in Path("fixtures/triage_messages_sample.jsonl").read_text().splitlines() if l.strip()]
    bad = [(r["id"], r["label"], route(r["text"])) for r in rows if route(r["text"]) != r["label"]]
    assert not bad, bad