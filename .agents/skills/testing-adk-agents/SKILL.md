# Testing Google ADK Multi-Agent Systems

## Overview
This skill covers testing a Google ADK (Agent Development Kit) multi-agent research assistant with sequential pipeline orchestration.

## Devin Secrets Needed
- `GOOGLE_API_KEY` — Gemini API key from https://aistudio.google.com/apikey (user-scoped)

## Setup

### 1. Install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install google-adk
```

### 2. Configure API key
```bash
echo "GOOGLE_API_KEY=$GOOGLE_API_KEY" > research_agent/.env
```

### 3. Start the ADK web server
```bash
source .venv/bin/activate
export GOOGLE_API_KEY=$GOOGLE_API_KEY
adk web
```
Server runs at http://localhost:8000. The web UI auto-selects `research_agent` from the dropdown.

## Testing Approaches

### Shell-based verification (no LLM required)
You can verify all tool functions and agent definitions work correctly without calling the Gemini API:
```python
from research_agent.agent import (
    root_agent, research_and_analysis_pipeline,
    researcher_agent, analyst_agent, writer_agent,
    search_web, get_statistics, get_current_datetime,
    evaluate_sources, check_for_bias, format_report, create_executive_summary
)
```
- Call each tool function with known inputs and verify outputs
- Verify agent hierarchy: root_agent → [pipeline(researcher, analyst), writer]
- Verify output_keys: researcher→"research_findings", analyst→"analysis_results", writer→"final_report"

### Browser-based E2E testing (requires LLM)
1. Open http://localhost:8000 in browser
2. Select `research_agent` from the agent dropdown
3. Send a query like: "Research the current state of AI agents and write a report"
4. Verify the Trace panel shows tool calls for each agent in sequence
5. Verify the final response is a structured report

**Topics with mock data:** "python", "ai agents", "climate change" — these return rich results from the hardcoded knowledge base. Other topics return generic fallback results.

## Common Issues

### Gemini API free tier quota exhaustion
- **Symptom:** 429 RESOURCE_EXHAUSTED error with `limit: 0`
- **Cause:** Free tier daily quota for `gemini-2.0-flash` is exhausted
- **Workaround:** Use shell-based verification (no LLM needed) to test tool functions and agent definitions. For full E2E testing, a paid API key is required or wait for daily quota reset.
- **Check quota:** https://ai.dev/rate-limit

### Virtual environment not found
- If the venv was created in a previous session directory, you may need to recreate it
- Always use `python3 -m venv .venv` in the repo root

### ADK web server requires .env in agent directory
- The `.env` file must be at `research_agent/.env`, not the repo root
- Format: `GOOGLE_API_KEY=your-key-here`
