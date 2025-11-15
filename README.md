# DocuMind – AI Document Intelligence Agent

DocuMind is an AI-powered multi-agent system for enterprise document understanding. It ingests PDFs, reports, policy documents, technical manuals, and web content, and turns unstructured text into structured, actionable insights.

## Key Capabilities
- **Document ingestion**: PDFs, text files, and URLs (with OCR for scanned documents)
- **Structured extraction**: tables, dates, metrics, tasks, and named entities
- **Summarization**: executive, bullet-point, and TL;DR styles
- **Q&A with citations**: retrieval-augmented answers grounded in source pages
- **Memory**: long-term storage of key insights and metrics
- **Evaluation & observability**: logging, metrics, and automated quality checks

## Core Agents
- **Reader Agent** – Extracts and chunks content from documents/web pages, applies OCR, and preserves page references.
- **Extractor Agent** – Identifies and structures tables, numerical values, dates, tasks, and entities.
- **Analyzer Agent** – Generates multi-level summaries and high-level insight reports.
- **Q&A Agent** – Answers questions using retrieval-augmented generation with page-level citations.
- **Memory Agent** – Stores key insights in a Memory Bank with context compaction.
- **Evaluator Agent** – Scores clarity, correctness, completeness, and citation accuracy.

## Project Structure (initial)
- `src/documind/` – Core package
  - `agents/` – Implementations of Reader, Extractor, Analyzer, Q&A, Memory, Evaluator agents
  - `tools/` – PDF/OCR utilities, table extraction, chunking, and external tool adapters
  - `memory/` – Long-term memory and session memory management
  - `evaluation/` – Metrics, scoring, and evaluation utilities

This repository will evolve into a full reference implementation, with example notebooks, evaluation scripts, and deployment guidance for enterprise environments.
