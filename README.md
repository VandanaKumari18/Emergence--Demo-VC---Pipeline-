# VC Deal Flow Pipeline

An AI-powered pipeline that automatically sources, analyses, and produces investment memos for YC W25 startups.

## What It Does

1. **Sources** startups from Hacker News YC W25 Launch threads using the Algolia API
2. **Analyses** each startup using Groq LLaMA 3.3 70B against a defined investment thesis
3. **Outputs** a one-page investment memo per startup as a markdown file

## How To Run

### 1. Clone the repo
git clone https://github.com/VandanaKumari18/vc-deal-flow-pipeline.git
cd vc-deal-flow-pipeline

### 2. Install dependencies
pip install requests beautifulsoup4 groq python-dotenv

### 3. Add your API key
Create a .env file and add:
GROQ_API_KEY=your_key_here

### 4. Run the pipeline
python run.py

Memos will be saved in the outputs/ folder.

## Investment Thesis

We invest in B2B AI tools that automate manual workflows for small and medium businesses under 200 employees, in markets currently dominated by legacy or manual processes, founded by technical founders with domain expertise, launched or gaining traction in the last 12 months.

## Output Format

Each memo covers Team, Product, Market, Risks, Score out of 100, and a final Recommendation of Pass, Watch, or Take a Meeting.

## Stack

- Sourcing: Hacker News Algolia API
- Analysis: Groq API with LLaMA 3.3 70B
- Language: Python
- Output: Markdown files

## Pre-generated Outputs

All 10 memos are committed in the outputs/ folder so you can read them without running the pipeline.
