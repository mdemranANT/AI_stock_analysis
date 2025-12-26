def orchestrate_agents(user_request, analyst, researcher, summarizer):
    """
    A simple multi-agent pipeline:
    1. Researcher gathers facts
    2. Analyst interprets them
    3. Summarizer produces the final report
    """

    research = researcher.run(
        f"Collect factual data, metrics, and recent news for: {user_request}"
    )

    analysis = analyst.run(
        f"Using this data:\n\n{research}\n\nProvide a detailed financial analysis."
    )

    summary = summarizer.run(
        f"Summarize this analysis into a clear investor report:\n\n{analysis}"
    )

    return summary