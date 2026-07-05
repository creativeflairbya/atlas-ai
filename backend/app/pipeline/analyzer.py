
# app/pipeline/analyzer.py

from app.engines.market_engine import get_market_data
from app.engines.indicator_engine import calculate_indicators
from app.engines.pattern_engine import detect_patterns
from app.engines.confluence_engine import calculate_confluence
from app.engines.risk_engine import calculate_risk
from app.engines.decision_engine import make_decision
from app.services.claude_service import generate_report

async def run_pipeline(input_type, data):

    # 1. MARKET DATA
    market = await get_market_data(data)

    # 2. INDICATORS
    indicators = calculate_indicators(market)

    # 3. PATTERNS
    patterns = detect_patterns(market)

    # 4. CONFLUENCE
    score = calculate_confluence(indicators, patterns)

    # 5. RISK
    risk = calculate_risk(market, score)

    # 6. DECISION
    decision = make_decision(score, risk)

    # 7. FINAL REPORT (LLM)
    report = await generate_report({
        "market": market,
        "indicators": indicators,
        "patterns": patterns,
        "score": score,
        "risk": risk,
        "decision": decision
    })

    return report
