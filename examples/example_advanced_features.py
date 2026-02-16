"""Example usage of advanced features: system instructions and web search grounding."""

import asyncio

from gemini_mcp.tools import GeminiTools


async def main():
    """Demonstrate usage of system instructions and grounding."""
    tools = GeminiTools()

    # Example 1: Using custom system instruction
    print("Example 1: Custom system instruction")
    print("-" * 50)
    result = await tools.call_tool(
        "gemini_prompt",
        {
            "prompt": "Explain Python in simple terms",
            "system_instruction": "You are a teacher explaining concepts to a 10-year-old. Use simple language and fun examples.",
        },
    )
    print(f"Response: {result[:200]}...\n")

    # Example 2: Research with web search grounding (default)
    print("Example 2: Research with web search grounding enabled")
    print("-" * 50)
    result = await tools.call_tool(
        "gemini_research",
        {
            "topic": "Latest developments in AI in 2025",
            # enable_grounding defaults to True for research
        },
    )
    print(f"Research results with web search: {result[:200]}...\n")

    # Example 3: Research without grounding
    print("Example 3: Research without web search grounding")
    print("-" * 50)
    result = await tools.call_tool(
        "gemini_research",
        {
            "topic": "Basic principles of Python programming",
            "enable_grounding": False,  # Disable web search
        },
    )
    print(f"Research results without web search: {result[:200]}...\n")

    # Example 4: Code analysis with custom system instruction
    print("Example 4: Code analysis with custom system instruction")
    print("-" * 50)
    result = await tools.call_tool(
        "gemini_analyze_code",
        {
            "files": ["src/gemini_mcp/tools.py"],
            "analysis_type": "review",
            "system_instruction": "Focus on security best practices and potential vulnerabilities.",
        },
    )
    print(f"Security-focused code review: {result[:200]}...\n")

    # Example 5: Summarize with custom style
    print("Example 5: Summarize with custom style")
    print("-" * 50)
    result = await tools.call_tool(
        "gemini_summarize",
        {
            "content": "The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to LLMs. It enables seamless integration between AI assistants and external tools, allowing them to access files, run commands, and interact with various services. MCP servers expose tools and resources that AI assistants can use to help users with tasks.",
            "summary_type": "bullet_points",
            "system_instruction": "Format the summary in a technical style suitable for developers.",
        },
    )
    print(f"Technical summary: {result}\n")


if __name__ == "__main__":
    asyncio.run(main())
