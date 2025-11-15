# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Overview

DocuMind is an AI-powered multi-agent system for enterprise document understanding. It ingests PDFs, text files, and URLs and turns unstructured text into structured, actionable insights.

The repository is currently in an initial scaffold state:
- High-level design and capabilities are described in `README.md`.
- Core package wiring lives in `src/documind/` with a placeholder entrypoint.
- Planned subpackages (agents, tools, memory, evaluation) are documented but not yet implemented.

When adding significant new modules or subpackages, update this file so future agents understand the architecture and workflows.

## Project layout and architecture

Top-level layout:
- `README.md` — product overview, key capabilities, and planned agents.
- `src/documind/` — main Python package.
  - `__init__.py` — package docstring describing the multi-agent system for ingestion, extraction, analysis, Q&A, memory, and evaluation.
  - `main.py` — temporary entrypoint that will orchestrate DocuMind workflows.

Planned architecture (from `README.md`):
- **Core agents** (expected under `src/documind/agents/`):
  - **Reader Agent** — extracts and chunks content from documents/web pages, applies OCR, preserves page references.
  - **Extractor Agent** — detects and structures tables, numerical values, dates, tasks, and entities.
  - **Analyzer Agent** — produces multi-level summaries and insight reports.
  - **Q&A Agent** — performs retrieval-augmented QA with page-level citations.
  - **Memory Agent** — stores key insights in a Memory Bank with context compaction.
  - **Evaluator Agent** — scores clarity, correctness, completeness, and citation accuracy.
- **Supporting packages** (expected under `src/documind/`):
  - `tools/` — PDF/OCR utilities, table extraction, chunking, and external tool adapters.
  - `memory/` — long-term and session memory management.
  - `evaluation/` — metrics, scoring, and evaluation utilities.

The `main.py` module is intended to become the orchestration layer that:
- Loads input documents (PDFs, text files, URLs).
- Invokes the Reader, Extractor, Analyzer, Q&A, Memory, and Evaluator agents in sequence or in a workflow.
- Exposes a CLI or API surface for enterprise workflows.

As you implement these components, keep cross-agent interfaces and shared data structures (document representations, chunks, citations, and memory records) centralized so they can be reused across agents. Reflect any major architectural decisions here.

## Commands

### Environment assumptions

- Python project using a `src/` layout with the main package at `src/documind/`.
- No explicit packaging, dependency, test, or lint configuration files are defined yet.

Future agents should:
- Prefer running commands from the repository root (`DocuMind/`).
- Set `PYTHONPATH` to include `src` when invoking modules directly, unless the package has been installed.

### Run the current entrypoint

From the project root:

- Unix-like shells (bash/zsh/fish):
  - `PYTHONPATH=src python -m documind.main`
- PowerShell:
  - `$env:PYTHONPATH = "src"; python -m documind.main`

This executes `documind.main:main()`, which currently prints a confirmation message indicating the environment is wired up. As the orchestration logic is implemented, this command should become the primary way to run DocuMind workflows locally.

If the package is later published or installed in editable mode (`pip install -e .`), prefer running via `python -m documind.main` without manually setting `PYTHONPATH`.

### Tests and linting

There is currently no configured test suite or linting/type-checking tooling in this repository (no `tests/` directory, `pyproject.toml`, `requirements.txt`, or similar tooling files have been defined yet).

When tests and tools are added (e.g., `pytest`, `ruff`, `mypy`, `tox`, or equivalent):
- Document the canonical commands here (e.g., `pytest`, how to run a single test file or test case, lint/typecheck commands, coverage runs).
- Note any project-specific flags, environment variables, or entrypoints.

## How future agents should extend the codebase

When evolving DocuMind toward the architecture described in `README.md`:
- Create the planned subpackages (`agents/`, `tools/`, `memory/`, `evaluation/`) under `src/documind/` and keep agent-specific logic in `agents/`.
- Keep document representations, chunking utilities, and citation formats in shared modules so they can be reused by multiple agents.
- Wire orchestration flows in `main.py` (or a dedicated orchestration module) rather than in low-level utilities.

Any time a new high-level workflow (e.g., ingestion pipeline, evaluation job, or API/CLI command) is added, summarize its entrypoint and main components in this file so future Warp agents can navigate and modify it safely.