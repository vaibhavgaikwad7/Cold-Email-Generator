## Document AI Pipeline (Windows‑friendly CommonJS)


It’s designed to be:
- Simple to run (one command),
- Deterministic where possible (authors/date via heuristics),
- LLM-assisted where it helps (summaries),
- Reproducible (Docker included),

What it extracts?
- document_type
- authors
- document_date
- summary
- methods_summary
- findings_summary/conclusions

How it works? 
1) PDF text extraction
Uses pdf-parse to pull raw text, then normalizes whitespace and builds a few “sections.”

2) Header heuristics (authors + date)
- Finds a plausible title line, then slices an “author zone” immediately below it (skipping wrapped title fragments, affiliations, emails, etc.).
- Extracts authors from that zone using robust rules (rejects affiliations/roles/degrees).
- Extracts dates using ranked patterns: prefers “Posted/Published/Accepted/Received” cues and only keeps YYYY-MM for confusing numeric dates.

3) Authority hints
When a DOI appears in the header, we attempt Crossref and only trust it if the title roughly matches the header. This avoids accidentally pulling references.

4) LLM ensemble (2 prompts)
- Two complimentary prompts read the text and produce structured JSON. I used three LLMS: Ollama (Offline), OpenAI (gpt 4o) and Anthropic (Claude 4-5) using API key. Additionally also have a "No AI" option which uses heuristics only. 
- The ensemble merges outputs (e.g., longest reasonable summary, union of author lists after cleaning).

5) Fusion & sanitize
- Heuristic + LLM candidates are fused with simple scoring.
- Dates are sanitized to ISO, preserving day precision only when truly observed in the header.

### Quickstart (PowerShell)
1) `npm install`
2) Set API key for this window: `$env:ANTHROPIC_API_KEY = "YOUR_NEW_CLAUDE_KEY"`
3) Run on one line:
`npx ts-node .\src\cli.ts --pdf ".\reference-docs\<YOUR_FILE>.pdf" --provider anthropic --model claude-4-5-sonnet-20250929 --out .\out.json --debug`

OpenAI: set `$env:OPENAI_API_KEY` and use `--provider openai --model gpt-4o-mini`.
Ollama: run `ollama serve`, pull a model, and use `--provider ollama --model llama3.1:8b`.

Optional structured parsers: start GROBID (port 8070) and add `--grobid-url http://localhost:8070`; or run Unstructured and pass `--unstructured-url`.

Compile: `npm run build` then `node .\dist\cli.js --pdf .\reference-docs\ssrn-5298091.pdf --out .\out.json --debug`.

Docker(PowerShell)
Build
` docker build -t doc-pipeline:latest . `

Run (Anthropic example)

docker run --rm -v ${PWD}:/work `
  -e ANTHROPIC_API_KEY=$env:ANTHROPIC_API_KEY `
  -e PROVIDER=anthropic `
  -e MODEL=claude-sonnet-4-5-20250929 `
  -e PDF_FILE=/work/reference-docs/ssrn-5298091.pdf `
  -e OUT_FILE=/work/out.json `
  doc-pipeline:latest`


Testing
` npm run test `

# Project Structure 



The test suite includes:
- Unit tests for the parser (authors/date extraction, numeric date disambiguation).
- Fusion tests to ensure parser dates beat LLM guesses when both exist.
- A light integration test for pdf-parse on a reference doc. 
