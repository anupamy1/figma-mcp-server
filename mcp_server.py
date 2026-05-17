from typing import Any, Dict, List

from mcp.server.fastmcp import FastMCP

from figma_service import FigmaService
from code_generator import CodeGenerator


mcp = FastMCP("Figma MCP Server")

figma_service = FigmaService()


IMAGE_NODE_IDS = [
    "1:1495",  # Hero Image
    "1:1499",  # Card image 1
    "1:1504",  # Card image 2
    "1:1509",  # Card image 3
    "1:1513",  # Large right image
    "1:1517",  # Bottom card image 1
    "1:1522",  # Bottom card image 2
    "1:1422",  # Avatar 1
    "1:1429",  # Avatar 2
    "1:1436"   # Avatar 3
]


def build_error_response(message: str, status_code: int, details: Any) -> Dict[str, Any]:
    return {
        "success": False,
        "message": message,
        "status_code": status_code,
        "details": details
    }


@mcp.tool()
def get_figma_file_info() -> Dict[str, Any]:
    """
    Get basic information about the connected Figma file.

    Returns file name, last modified date, version, and document name.
    """
    result, status_code = figma_service.get_file_info()

    if status_code != 200:
        return build_error_response(
            "Failed to get Figma file info",
            status_code,
            result
        )

    return {
        "success": True,
        "data": result
    }


@mcp.tool()
def get_figma_pages() -> Dict[str, Any]:
    """
    Get all pages inside the connected Figma file.

    Use this when the AI needs to understand available pages in the file.
    """
    result, status_code = figma_service.get_pages()

    if status_code != 200:
        return build_error_response(
            "Failed to get Figma pages",
            status_code,
            result
        )

    return {
        "success": True,
        "data": result
    }


@mcp.tool()
def get_figma_frames() -> Dict[str, Any]:
    """
    Get top-level frames from the connected Figma file.

    Use this to identify frames such as Landing page, Shop, About, Product detail page, etc.
    """
    result, status_code = figma_service.get_frames()

    if status_code != 200:
        return build_error_response(
            "Failed to get Figma frames",
            status_code,
            result
        )

    return {
        "success": True,
        "data": result
    }


@mcp.tool()
def get_landing_page_raw_elements() -> Dict[str, Any]:
    """
    Get all raw UI elements from the selected landing page frame.

    This returns detailed node information including id, name, type, x, y, width, height, and text.
    """
    result, status_code = figma_service.get_landing_page_details()

    if status_code != 200:
        return build_error_response(
            "Failed to get landing page raw elements",
            status_code,
            result
        )

    return {
        "success": True,
        "data": result
    }


@mcp.tool()
def get_landing_page_structure() -> Dict[str, Any]:
    """
    Get clean structured UI data from the selected landing page.

    This separates Figma data into headings, paragraphs, buttons, images, sections, and cards.
    This is the main tool the AI should use before generating HTML, React, Next.js, Flutter, or SwiftUI code.
    """
    result, status_code = figma_service.get_clean_landing_page_structure()

    if status_code != 200:
        return build_error_response(
            "Failed to get landing page structure",
            status_code,
            result
        )

    return {
        "success": True,
        "data": result
    }


@mcp.tool()
def get_figma_image_urls() -> Dict[str, Any]:
    """
    Get exported image URLs for important image nodes in the landing page.

    This returns temporary Figma image URLs for hero image, cards, side image, bottom images, and avatars.
    """
    result, status_code = figma_service.get_image_urls(IMAGE_NODE_IDS)

    if status_code != 200:
        return build_error_response(
            "Failed to get Figma image URLs",
            status_code,
            result
        )

    return {
        "success": True,
        "data": result
    }


@mcp.tool()
def generate_html_from_figma() -> Dict[str, Any]:
    """
    Generate an HTML landing page using the connected Figma design.

    This uses current template-based generation and Figma image URLs.
    Later this can be upgraded to AI-based generation.
    """
    result, status_code = figma_service.get_image_urls(IMAGE_NODE_IDS)

    if status_code != 200:
        return build_error_response(
            "Failed to fetch image URLs for HTML generation",
            status_code,
            result
        )

    image_urls = result.get("images", {})
    html_code = CodeGenerator.generate_landing_page_html_v2(image_urls)

    return {
        "success": True,
        "framework": "html",
        "code": html_code
    }


@mcp.tool()
def create_code_generation_prompt(framework: str = "react") -> Dict[str, Any]:
    """
    Create a strong prompt for an AI client to generate code from the Figma landing page.

    Supported framework values:
    - html
    - react
    - nextjs
    - tailwind
    - flutter
    - swiftui

    This does not call GPT/Gemini directly. It prepares clean Figma data and a prompt that Cursor/ChatGPT/Claude can use.
    """
    structure_result, structure_status = figma_service.get_clean_landing_page_structure()

    if structure_status != 200:
        return build_error_response(
            "Failed to fetch landing page structure for prompt generation",
            structure_status,
            structure_result
        )

    image_result, image_status = figma_service.get_image_urls(IMAGE_NODE_IDS)

    if image_status != 200:
        return build_error_response(
            "Failed to fetch image URLs for prompt generation",
            image_status,
            image_result
        )

    clean_framework = framework.strip().lower()

    prompt = f"""
You are an expert frontend developer.

Generate clean, production-quality {clean_framework} code from this Figma landing page structure.

Requirements:
1. Match the Figma layout as closely as possible.
2. Use the provided headings, paragraphs, buttons, cards, sections, and image URLs.
3. Make the layout responsive.
4. Keep code clean and readable.
5. Use semantic structure.
6. Do not use placeholder grey boxes if image URLs are available.
7. Keep buttons clickable.
8. If framework is React/Next.js, create reusable components where useful.
9. If framework is Tailwind, use Tailwind utility classes.
10. Return only the final code.

Figma clean structure:
{structure_result}

Figma image URLs:
{image_result.get("images", {})}
"""

    return {
        "success": True,
        "framework": clean_framework,
        "prompt": prompt
    }


@mcp.tool()
def list_available_tools_summary() -> Dict[str, Any]:
    """
    Show a simple summary of available Figma MCP tools.
    """
    tools: List[Dict[str, str]] = [
        {
            "name": "get_figma_file_info",
            "description": "Returns basic Figma file information."
        },
        {
            "name": "get_figma_pages",
            "description": "Returns pages inside the Figma file."
        },
        {
            "name": "get_figma_frames",
            "description": "Returns top-level frames inside the Figma file."
        },
        {
            "name": "get_landing_page_raw_elements",
            "description": "Returns raw landing page elements."
        },
        {
            "name": "get_landing_page_structure",
            "description": "Returns clean structured UI data."
        },
        {
            "name": "get_figma_image_urls",
            "description": "Returns Figma image URLs."
        },
        {
            "name": "generate_html_from_figma",
            "description": "Returns generated HTML code using Figma data."
        },
        {
            "name": "create_code_generation_prompt",
            "description": "Creates a prompt for React/HTML/Next.js/Tailwind/Flutter/SwiftUI generation."
        }
    ]

    return {
        "success": True,
        "tools": tools
    }


if __name__ == "__main__":
    mcp.run(transport="streamable-http")