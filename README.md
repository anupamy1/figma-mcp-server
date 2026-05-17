# Figma MCP Server

A learning prototype that connects the Figma REST API to AI tooling via an MCP server. It extracts structured UI data (pages, frames, headings, buttons, cards, images, etc.) from a Figma file and exposes that information as MCP tools so AI clients (for example VS Code Copilot in Agent/MCP mode) can generate frontend code from actual design context.

> NOTE: This is a learning / build-in-public project. It is not production-ready. Do not commit secrets or API tokens. Use `.env.example` as a guide.

## Why I built this

- To practice integrating design systems (Figma) with programmatic tooling.
- To explore how an MCP server can expose design context to AI-assisted code generation.
- To provide a small reference implementation for generating HTML/React from a Figma landing page.

## What is MCP (simple)

MCP (Model Context Protocol) is a lightweight way to expose structured context and tools to AI clients. In this project the MCP server exposes helper methods ("tools") that return Figma structure and exported image URLs so an AI can use real design data when generating code.

## Architecture / Flow

Figma Design
↓
Figma REST API
↓
Python service (`figma_service.py`) — reads Figma nodes and builds a clean structure
↓
Flask prototype endpoints (`app.py`) for manual testing
↓
MCP server (`mcp_server.py`) — exposes MCP tools to AI clients
↓
VS Code Copilot / AI client — calls MCP tools and generates frontend code
↓
Generated frontend (HTML / React) — preview in `react-preview/`

## Features

- Fetch Figma file metadata (name, last modified)
- List pages and top-level frames
- Select a landing page node and extract a clean structure (headings, paragraphs, buttons, images, sections, cards)
- Request exported image URLs for selected nodes
- Generate simple HTML previews (basic + improved v2 using image URLs)
- Expose MCP tools for AI/agent integration
- Provide a small React preview project under `react-preview/` to preview generated UI

## Folder structure (important files)

- `app.py` — Flask prototype API/routes for quick testing
- `mcp_server.py` — MCP server bindings and tool definitions
- `config.py` — reads `.env` values and validates required variables
- `figma_service.py` — Figma API wrapper and structure extraction logic
- `code_generator.py` — small HTML generator using extracted image URLs
- `requirements.txt` — Python dependencies
- `react-preview/` — Vite + React preview app for generated UI
- `.env.example` — example environment file (do not commit real secrets)

## Tech stack

- Python 3
- Flask (prototype API)
- requests, python-dotenv
- MCP Python SDK (FastMCP wrapper in this repo)
- React + Vite for the preview UI

## Getting started (local)

1. Clone the repo

```bash
git clone https://github.com/anupamy1/figma-mcp-server.git
cd figma-mcp-server
```

2. Create a `.env` file (copy from `.env.example`) and fill values. NEVER commit this file.

3. Create a Python virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate   # or `.venv\\Scripts\\activate` on Windows
pip install -r requirements.txt
```

## Environment variables (example)

Create a `.env` file with these values (do not commit):

```
FIGMA_ACCESS_TOKEN=
FIGMA_FILE_ID=
LANDING_PAGE_NODE_ID=
FLASK_DEBUG=True
```

## How to run the Flask prototype

This is useful for quick manual testing of the Figma integration and to inspect endpoints in a browser.

```bash
python app.py
# open http://127.0.0.1:5000/ in your browser
```

### Prototype routes (examples)

- `GET /figma-file` — file metadata
- `GET /figma-pages` — list pages
- `GET /figma-frames` — list frames
- `GET /figma-landing-page` — raw landing node data
- `GET /figma-clean-landing` — cleaned structure (headings, images, sections, cards)
- `GET /figma-image-urls` — calls Figma images endpoint for a small set of node ids
- `GET /generate-html-v2` — returns generated HTML using image URLs

## How to run the MCP server (for AI clients)

```bash
python mcp_server.py
# MCP server binds tools such as get_figma_image_urls and generate_html_from_figma
```

## Connecting VS Code Copilot (MCP)

If you're using VS Code Copilot Agent mode or other MCP-aware clients, configure a local MCP endpoint. Example: create `.vscode/mcp.json` with:

```json
{
  "servers": {
    "figma-mcp-server": {
      "type": "http",
      "url": "http://127.0.0.1:8000/mcp/"
    }
  }
}
```

## Previewing generated React UI

The `react-preview` folder contains a tiny Vite + React app to preview generated UIs and test local fallbacks.

```bash
cd react-preview
npm install
npm run dev
# open the local vite URL in your browser
```

## Example use cases

- Use the MCP tools to fetch the landing page structure and automatically scaffold a React page.
- Rapidly prototype variations of a landing page by updating text and images from Figma and re-generating HTML.
- Teach or demo how design systems can feed AI-assisted code generation.

## Current limitations

- This is a learning prototype — not production ready.
- Figma rate limits and temporary image URLs can affect flow.
- The generated HTML is intentionally simple and may require manual refinement.
- Security and authentication flows are minimal; treat tokens carefully.

## Future improvements

- Improve the generated React output with component extraction and CSS modules.
- Add tests and CI steps for safety.
- Add pagination and robust node-mapping heuristics for complex files.
- Add optional caching for image exports to avoid rate limits.

## Learning outcomes

- Practical experience calling the Figma REST API and parsing node structures.
- Building an MCP server that exposes useful tooling to AI clients.
- Integrating a simple React preview with generated assets.

## Security notes (important)

- Never commit `.env` or real API tokens. Use `.env.example` in the repo instead.
- If a token is accidentally exposed, revoke it immediately in Figma.
- Figma image URLs are temporary; do not hard-code long-lived URLs without verifying expiration.

## Author

anupamy1 — learning prototype and developer tooling experiments.

## License & contribution

This project is provided as-is for learning and demo purposes. Contributions and issues are welcome. Please open a GitHub issue or PR on the repository.
