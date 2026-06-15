import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ["GROQ_API_KEY"])

THESIS = """
We invest in B2B AI tools that automate manual workflows for small and medium businesses (under 200 employees),
in markets currently dominated by legacy or manual processes,
founded by technical founders with domain expertise,
launched or gaining traction in the last 12 months.
"""

SCORING_RUBRIC = """
Score out of 100 based on:
- Founder credibility and technical depth (25 points)
- Product clarity and differentiation (25 points)
- Market size and timing (25 points)
- Early traction and momentum (25 points)
"""

def analyse_startup(startup):
    prompt = f"""
You are a VC analyst at a seed-stage fund. Analyse this startup against our investment thesis.

THESIS:
{THESIS}

SCORING RUBRIC:
{SCORING_RUBRIC}

STARTUP DATA:
Name: {startup['name']}
Description: {startup['description']}
Website: {startup['website']}
HN Points: {startup['hn_points']}
HN Comments: {startup['hn_comments']}
Author/Founder: {startup['author']}

Produce a structured analysis in exactly this format:

## {startup['name']}

**Website:** {startup['website']}
**HN Traction:** {startup['hn_points']} points, {startup['hn_comments']} comments

### Team
[Analyse founder background based on available info. Be honest if info is limited.]

### Product
[What they actually do in plain language. 3-4 sentences.]

### Market
[Market size hint, who are the competitors, why is now the right time.]

### Risks / Open Questions
[What could kill this startup? List 3 key risks.]

### Score
[X/100] — [one line justification against thesis]

### Recommendation
**[PASS / WATCH / TAKE A MEETING]**

Rationale: [2-3 sentences]

What would change our mind:
1. [First thing]
2. [Second thing]
3. [Third thing]
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    test_startup = {
        "name": "Browser Use",
        "description": "An easy way to connect AI agents with the browser.",
        "website": "https://browser-use.com",
        "hn_points": 259,
        "hn_comments": 100,
        "author": "MagMueller"
    }
    result = analyse_startup(test_startup)
    print(result)
