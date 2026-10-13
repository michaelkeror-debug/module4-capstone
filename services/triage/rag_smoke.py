"""RAG smoke test: answer one question grounded in a small doc set (stub mode)."""

DOCS = [
    {"id": "D1", "text": "For chest pain or difficulty breathing, go to the nearest emergency facility immediately."},
    {"id": "D2", "text": "For mild fever, rest, drink fluids, and seek care if symptoms last more than three days."},
    {"id": "D3", "text": "Delivery tracking for medical supplies is available through the logistics coordinator."},
]


def retrieve(question: str, k: int = 1) -> list[dict]:
    q = set(question.lower().split())
    scored = [(len(q & set(d["text"].lower().split())), d) for d in DOCS]
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for score, d in scored[:k] if score > 0]


def answer(question: str) -> dict:
    hits = retrieve(question)
    if not hits:
        return {"answer": "No grounded answer found.", "sources": []}
    return {"answer": hits[0]["text"], "sources": [h["id"] for h in hits]}


import json
from agents.tools.logistics import check_stock

if __name__ == "__main__":
    out = answer("What should I do for a mild fever?")
    assert out["sources"], "answer was not grounded in any document"

    tool_out = json.loads(check_stock("amoxicillin"))
    assert tool_out["stock"], "MCP tool returned no stock rows"

    print("rag_smoke OK", out["sources"], tool_out["item"], len(tool_out["stock"]), "clinics")