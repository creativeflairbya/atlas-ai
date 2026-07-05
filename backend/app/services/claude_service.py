
# app/services/claude_service.py

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def generate_report(data):

    prompt = f"""
You are a professional trading analyst.

ONLY explain the given structured data.
DO NOT calculate indicators or guess missing values.

DATA:
{data}

Return:
- Market summary
- Trade decision explanation
- Risk explanation
- Final signal
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "analysis": response.choices[0].message.content,
        "raw_data": data
    }
