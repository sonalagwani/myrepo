# Multi-Agent Research Assistant

A multi-agent system built with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) that demonstrates orchestrated agent patterns for producing research reports.

## Architecture

```
┌─────────────────────────────────┐
│     Research Coordinator        │  (root agent — routes requests)
│         (Gemini 2.0 Flash)      │
└──────────┬──────────────────────┘
           │
    ┌──────▼──────────────────────────────┐
    │  Research & Analysis Pipeline       │  (SequentialAgent)
    │                                     │
    │  ┌─────────────┐  ┌──────────────┐  │
    │  │ Researcher   │─▶│  Analyst      │  │
    │  │ (search,     │  │ (evaluate    │  │
    │  │  statistics) │  │  sources,    │  │
    │  └─────────────┘  │  check bias) │  │
    │                    └──────────────┘  │
    └──────────────────────────┬──────────┘
                               │
                        ┌──────▼──────┐
                        │   Writer     │
                        │ (format,    │
                        │  summarize) │
                        └─────────────┘
```

### Agents

| Agent | Role | Tools |
|-------|------|-------|
| **Research Coordinator** | Routes user requests to specialist sub-agents | — |
| **Researcher** | Gathers information via web search and statistics | `search_web`, `get_statistics`, `get_current_datetime` |
| **Analyst** | Evaluates source credibility and checks for bias | `evaluate_sources`, `check_for_bias` |
| **Writer** | Produces polished, structured reports | `format_report`, `create_executive_summary` |

### Patterns Demonstrated

- **Sequential Pipeline** — Researcher → Analyst → Writer
- **Coordinator/Dispatcher** — Root agent routes to the right sub-agents
- **Shared State** — Agents pass data via `output_key` / `session.state`

## Setup

### Prerequisites

- Python 3.10+
- A [Google Gemini API key](https://aistudio.google.com/apikey)

### Installation

```bash
# Clone the repo
git clone https://github.com/sonalagwani/myrepo.git
cd myrepo

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Edit `research_agent/.env` and add your API key:

```env
GOOGLE_API_KEY="your-api-key-here"
```

## Usage

### Web UI (recommended)

```bash
adk web
```

Open http://localhost:8000, select `research_agent`, and start chatting.

### Command Line

```bash
adk run research_agent
```

### Example Prompts

- "Research the current state of AI agents and write a report"
- "What are the latest trends in Python development?"
- "Write a report on climate change and renewable energy"

## Project Structure

```
myrepo/
├── README.md
├── requirements.txt
├── .gitignore
└── research_agent/
    ├── __init__.py      # Package init
    ├── agent.py         # Agent definitions and tools
    └── .env             # API key configuration
```

## License

MIT
