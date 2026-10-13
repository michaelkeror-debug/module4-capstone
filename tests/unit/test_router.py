"""Change for your project: nothing. Update config.json route_keywords instead."""
from agents.router import route


def test_route_logistics():
    assert route("track delivery") == "logistics_lookup"


def test_route_default():
    assert route("general question") == "triage"



def test_route_delivery_intent():
    assert route("where is my delivery") == "logistics_lookup"


def test_route_listing_photo_intent():
    assert route("listing photo mismatch") == "catalog_mismatch"