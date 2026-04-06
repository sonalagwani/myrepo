"""
Multi-Agent Research Assistant built with Google ADK.

This system demonstrates orchestrated multi-agent patterns:
- A Coordinator agent that routes user requests
- A Researcher agent that gathers information
- An Analyst agent that evaluates and critiques findings
- A Writer agent that produces polished output
- Sequential + Parallel workflow orchestration
"""

import datetime
import json
from zoneinfo import ZoneInfo

from google.adk.agents import Agent, SequentialAgent


# ---------------------------------------------------------------------------
# Tools for the Researcher agent
# ---------------------------------------------------------------------------

def search_web(query: str) -> dict:
    """Searches the web for information on a given query.

    Args:
        query: The search query string.

    Returns:
        dict: A dictionary with 'status' and 'results' keys.
    """
    knowledge_base = {
        "python": {
            "status": "success",
            "results": [
                {
                    "title": "Python Official Documentation",
                    "snippet": (
                        "Python is a high-level, interpreted programming language "
                        "known for its readability and versatility. Python 3.12 "
                        "introduced performance improvements and new typing features."
                    ),
                    "source": "docs.python.org",
                },
                {
                    "title": "Python Trends 2025",
                    "snippet": (
                        "Python continues to dominate in AI/ML, data science, and "
                        "web development. Key trends include AI-assisted coding, "
                        "improved async support, and growing adoption in embedded systems."
                    ),
                    "source": "techtrends.dev",
                },
            ],
        },
        "ai agents": {
            "status": "success",
            "results": [
                {
                    "title": "The Rise of AI Agents",
                    "snippet": (
                        "AI agents are autonomous systems that use LLMs for reasoning "
                        "and planning. They can use tools, maintain memory, and "
                        "collaborate in multi-agent architectures to solve complex tasks."
                    ),
                    "source": "ai-research.org",
                },
                {
                    "title": "Google ADK Framework",
                    "snippet": (
                        "Google's Agent Development Kit (ADK) is an open-source "
                        "framework for building multi-agent systems. It supports "
                        "sequential, parallel, and loop workflows with built-in "
                        "state management."
                    ),
                    "source": "developers.google.com",
                },
            ],
        },
        "climate change": {
            "status": "success",
            "results": [
                {
                    "title": "Climate Science Update 2025",
                    "snippet": (
                        "Global temperatures have risen approximately 1.2C above "
                        "pre-industrial levels. The Paris Agreement targets limiting "
                        "warming to 1.5C. Renewable energy adoption has accelerated, "
                        "with solar and wind now cheaper than fossil fuels in most markets."
                    ),
                    "source": "climate-science.org",
                },
                {
                    "title": "Carbon Capture Technologies",
                    "snippet": (
                        "Direct air capture (DAC) technology has seen significant "
                        "advances, with costs dropping 40% since 2023. Several "
                        "large-scale facilities are now operational worldwide."
                    ),
                    "source": "greentech-review.com",
                },
            ],
        },
    }

    query_lower = query.lower()
    for key, data in knowledge_base.items():
        if key in query_lower:
            return data

    return {
        "status": "success",
        "results": [
            {
                "title": f"Search results for: {query}",
                "snippet": (
                    f"Found relevant information about '{query}'. "
                    "This is a general-purpose search result covering the key "
                    "aspects of the topic including recent developments, "
                    "main challenges, and future outlook."
                ),
                "source": "general-knowledge.com",
            },
        ],
    }


def get_statistics(topic: str) -> dict:
    """Retrieves statistical data related to a topic.

    Args:
        topic: The topic to find statistics about.

    Returns:
        dict: A dictionary with 'status' and 'data' keys.
    """
    stats_db = {
        "python": {
            "status": "success",
            "data": {
                "popularity_rank": 1,
                "github_repos": "5.2M+",
                "stack_overflow_questions": "2.1M+",
                "average_salary_usd": 120000,
                "year_created": 1991,
                "latest_version": "3.12",
            },
        },
        "ai": {
            "status": "success",
            "data": {
                "global_market_size_2025": "$190B",
                "projected_market_2030": "$800B",
                "ai_startups_funded_2024": 3500,
                "jobs_created_2024": "2.3M",
                "research_papers_2024": 150000,
            },
        },
        "climate": {
            "status": "success",
            "data": {
                "global_temp_increase_c": 1.2,
                "co2_ppm_2025": 425,
                "renewable_energy_share_pct": 35,
                "ev_sales_growth_2024_pct": 45,
                "green_investment_2024_usd": "$1.8T",
            },
        },
    }

    topic_lower = topic.lower()
    for key, data in stats_db.items():
        if key in topic_lower:
            return data

    return {
        "status": "success",
        "data": {
            "note": f"General statistics for '{topic}' are being compiled.",
            "relevance_score": 0.75,
            "data_points_available": 12,
        },
    }


def get_current_datetime() -> dict:
    """Returns the current date and time in UTC.

    Returns:
        dict: A dictionary with 'status' and 'datetime' keys.
    """
    now = datetime.datetime.now(ZoneInfo("UTC"))
    return {
        "status": "success",
        "datetime": now.strftime("%Y-%m-%d %H:%M:%S %Z"),
    }


# ---------------------------------------------------------------------------
# Tools for the Analyst agent
# ---------------------------------------------------------------------------

def evaluate_sources(sources: str) -> dict:
    """Evaluates the credibility and relevance of research sources.

    Args:
        sources: A JSON string or comma-separated list of source names.

    Returns:
        dict: A dictionary with evaluation results.
    """
    trusted_domains = {
        "docs.python.org": {"credibility": "high", "type": "official"},
        "developers.google.com": {"credibility": "high", "type": "official"},
        "ai-research.org": {"credibility": "high", "type": "academic"},
        "climate-science.org": {"credibility": "high", "type": "academic"},
        "techtrends.dev": {"credibility": "medium", "type": "industry"},
        "greentech-review.com": {"credibility": "medium", "type": "industry"},
        "general-knowledge.com": {"credibility": "medium", "type": "general"},
    }

    evaluations = []
    for domain, info in trusted_domains.items():
        if domain in sources.lower():
            evaluations.append({
                "source": domain,
                "credibility": info["credibility"],
                "type": info["type"],
            })

    if not evaluations:
        evaluations.append({
            "source": "unknown",
            "credibility": "unverified",
            "type": "unknown",
            "note": "Sources could not be automatically verified.",
        })

    return {
        "status": "success",
        "evaluations": evaluations,
        "total_sources_checked": len(evaluations),
    }


def check_for_bias(text: str) -> dict:
    """Analyzes text for potential bias indicators.

    Args:
        text: The text to analyze for bias.

    Returns:
        dict: A dictionary with bias analysis results.
    """
    bias_indicators = [
        "always", "never", "everyone", "nobody", "obviously",
        "clearly", "undeniably", "without question",
    ]
    found = [word for word in bias_indicators if word in text.lower()]

    if found:
        bias_level = "high" if len(found) > 3 else "moderate" if len(found) > 1 else "low"
    else:
        bias_level = "none detected"

    return {
        "status": "success",
        "bias_level": bias_level,
        "indicators_found": found,
        "recommendation": (
            "Content appears balanced."
            if bias_level == "none detected"
            else f"Consider revising language around: {', '.join(found)}"
        ),
    }


# ---------------------------------------------------------------------------
# Tools for the Writer agent
# ---------------------------------------------------------------------------

def format_report(title: str, sections: str) -> dict:
    """Formats content into a structured report.

    Args:
        title: The report title.
        sections: A JSON string of sections with 'heading' and 'content' keys,
                  or a plain text description of sections.

    Returns:
        dict: A dictionary with the formatted report.
    """
    try:
        section_list = json.loads(sections)
    except (json.JSONDecodeError, TypeError):
        section_list = [{"heading": "Main Content", "content": str(sections)}]

    report_lines = [
        f"# {title}",
        f"*Generated on {datetime.datetime.now(ZoneInfo('UTC')).strftime('%Y-%m-%d %H:%M UTC')}*",
        "",
        "---",
        "",
    ]

    for section in section_list:
        heading = section.get("heading", "Section")
        content = section.get("content", "")
        report_lines.append(f"## {heading}")
        report_lines.append("")
        report_lines.append(content)
        report_lines.append("")

    report_lines.extend(["---", "", "*Report generated by Multi-Agent Research Assistant*"])

    return {
        "status": "success",
        "formatted_report": "\n".join(report_lines),
        "word_count": sum(len(line.split()) for line in report_lines),
    }


def create_executive_summary(content: str, max_sentences: int = 3) -> dict:
    """Creates a brief executive summary from longer content.

    Args:
        content: The content to summarize.
        max_sentences: Maximum number of sentences in the summary.

    Returns:
        dict: A dictionary with the summary.
    """
    sentences = [s.strip() for s in content.replace("\n", " ").split(".") if s.strip()]
    summary_sentences = sentences[:max_sentences]
    summary = ". ".join(summary_sentences) + "." if summary_sentences else content[:200]

    return {
        "status": "success",
        "executive_summary": summary,
        "original_length": len(content),
        "summary_length": len(summary),
        "compression_ratio": round(len(summary) / max(len(content), 1), 2),
    }


# ---------------------------------------------------------------------------
# Sub-Agents
# ---------------------------------------------------------------------------

researcher_agent = Agent(
    name="researcher",
    model="gemini-2.0-flash",
    description=(
        "Gathers information from web searches and statistical databases. "
        "Use this agent when you need to find facts, data, or background "
        "information on any topic."
    ),
    instruction=(
        "You are a thorough research specialist. Your job is to gather "
        "comprehensive information on the requested topic.\n\n"
        "Steps:\n"
        "1. Use search_web to find relevant articles and information\n"
        "2. Use get_statistics to find quantitative data\n"
        "3. Use get_current_datetime to note when the research was conducted\n"
        "4. Compile all findings into a clear, factual summary\n\n"
        "Always cite your sources and present data accurately."
    ),
    tools=[search_web, get_statistics, get_current_datetime],
    output_key="research_findings",
)

analyst_agent = Agent(
    name="analyst",
    model="gemini-2.0-flash",
    description=(
        "Evaluates research quality, checks sources, and identifies bias. "
        "Use this agent to validate and critique research findings."
    ),
    instruction=(
        "You are a critical analyst. Your job is to evaluate the research "
        "findings stored in {research_findings}.\n\n"
        "Steps:\n"
        "1. Use evaluate_sources to check source credibility\n"
        "2. Use check_for_bias to identify potential bias in the findings\n"
        "3. Provide a critical assessment: What's strong? What's weak? "
        "What needs more evidence?\n"
        "4. Rate the overall quality of the research (high/medium/low)\n\n"
        "Be constructive but rigorous in your analysis."
    ),
    tools=[evaluate_sources, check_for_bias],
    output_key="analysis_results",
)

writer_agent = Agent(
    name="writer",
    model="gemini-2.0-flash",
    description=(
        "Produces polished, well-structured reports from research and analysis. "
        "Use this agent to create the final deliverable."
    ),
    instruction=(
        "You are an expert writer. Using the research from {research_findings} "
        "and the quality analysis from {analysis_results}, create a polished "
        "report.\n\n"
        "Steps:\n"
        "1. Use create_executive_summary to draft a brief overview\n"
        "2. Use format_report to structure the final output\n"
        "3. Incorporate the analyst's feedback to strengthen weak areas\n"
        "4. Ensure the report is clear, well-organized, and actionable\n\n"
        "Write for a professional audience. Be concise but comprehensive."
    ),
    tools=[format_report, create_executive_summary],
    output_key="final_report",
)


# ---------------------------------------------------------------------------
# Parallel analysis pipeline (researcher + analyst work in sequence,
# but multiple research queries could fan out in parallel)
# ---------------------------------------------------------------------------

research_and_analysis_pipeline = SequentialAgent(
    name="research_and_analysis_pipeline",
    description=(
        "Runs the researcher first to gather data, then the analyst "
        "to evaluate the quality of findings."
    ),
    sub_agents=[researcher_agent, analyst_agent],
)


# ---------------------------------------------------------------------------
# Root orchestrator: sequential pipeline of research+analysis -> writing
# ---------------------------------------------------------------------------

root_agent = Agent(
    name="research_coordinator",
    model="gemini-2.0-flash",
    description=(
        "Coordinates a team of specialized agents to produce high-quality "
        "research reports. Routes tasks to the appropriate sub-agents."
    ),
    instruction=(
        "You are the Research Coordinator managing a team of AI specialists.\n\n"
        "When a user asks you to research a topic or write a report:\n"
        "1. Delegate to the research_and_analysis_pipeline to gather and "
        "validate information\n"
        "2. Then delegate to the writer to produce the final report\n\n"
        "When a user asks a simple question, answer directly.\n\n"
        "Always be professional, clear, and helpful. Let the user know "
        "which agents are working on their request."
    ),
    sub_agents=[research_and_analysis_pipeline, writer_agent],
)
