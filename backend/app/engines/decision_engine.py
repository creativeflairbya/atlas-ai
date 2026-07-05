
# app/engines/decision_engine.py

def make_decision(score, risk):

    if score < 75:
        return "NO TRADE"

    if risk["rr"] < 2:
        return "NO TRADE"

    return "BUY"
