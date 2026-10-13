import json
from pathlib import Path


def test_service_runs_in_stub_mode():
    from services.triage.app import handle_message
    out = handle_message({"text": "hello"}, stub=True)
    assert out["status"] == "ok"


def test_pin_has_model_and_version():
    pin_path = Path(__file__).resolve().parents[2] / "services/triage/prompts/pin.json"
    pin = json.loads(pin_path.read_text())
    assert pin.get("model_id") and pin.get("prompt_version")