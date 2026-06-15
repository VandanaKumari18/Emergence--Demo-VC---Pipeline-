# Process & AI Workflow

## How I Approached This Assignment

When I first read the brief, the first decision I had to make was
which source to use for sourcing startups. The assignment mentioned
Product Hunt, YC, HN, Twitter, and Crunchbase. I decided to go with
Hacker News because:

- It has a free, open API that returns clean structured data
- HN points and comments are a built-in traction signal
- YC W25 startups post "Launch HN" threads which gives both
  startup info and community reaction in one place

This felt like a smarter choice than scraping YC directly, which
loads data via JavaScript and would have required a headless browser.

## The Thesis I Picked and Why

I defined a specific thesis before writing any analysis code:

> We invest in B2B AI tools that automate manual workflows for small
> and medium businesses (under 200 employees), in markets currently
> dominated by legacy or manual processes, founded by technical
> founders with domain expertise, launched or gaining traction in
> the last 12 months.

I kept it specific because a vague thesis like "good AI companies"
makes scoring meaningless. Every score in the memos is measured
against this thesis consistently.

## How I Used AI in This Project

I used Claude (claude.ai) as a thinking partner throughout:

- Planning the architecture before writing any code
- Debugging scraper issues when YC's website turned out to be
  JavaScript rendered
- Iterating on the analysis prompt until output was structured
  and useful
- Deciding to switch from Gemini to Groq when quota limits hit

The prompt I send to the LLM is in `prompts/analysis_prompt.txt`.
I iterated on it several times — the first version returned
unstructured prose. I added the explicit format template to force
consistent output across all 10 startups.

## Decisions I Made Along the Way

**Chose HN over YC scraper** — YC loads via JavaScript, HN has
a clean REST API. Better to go deep on one good source than
spread thin across many.

**Switched from Gemini to Groq** — Hit quota limits on Gemini free
tier. Groq with Llama 3.3 70B gave comparable output quality
for free.

**Limited to 10 startups** — The assignment said 10-20. I picked 10
to keep output quality high rather than rushing through 20 with
weaker analysis.

**Kept stack simple** — No database, no queue, no frontend. Just
Python scripts that chain together. The assignment explicitly warned
against overengineering.

## What I Would Build Next

- Add a second enrichment source per startup by fetching their
  website and summarising it for better analysis
- Add founder LinkedIn lookup to improve team section quality
- Build a simple CLI with score filters so partners can see only
  startups above a certain threshold
- Store outputs in a database so partners can search across batches
