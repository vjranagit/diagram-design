# Qwen Diagram Design

Qwen Diagram Design is a weak-model wrapper for local LLMs, tuned on qwen3.8-27b. It turns short process topics into technical diagram PNGs using the adjacent `diagram-design` renderer. Created by Usman Mustafa.

## Install

From this directory, run:

```sh
scripts/setup.sh
```

This creates a local Python environment and installs Playwright with its headless Chromium runtime. Python 3 with `venv` and network access for setup are required.

## Use

Prompt pattern: “Use the qwen-diagram-design skill to make a technical diagram about: [topic].”

Copy `templates/content.json`, replace its values, then run:

```sh
scripts/make.sh <content-file> <output-directory>
```

The output directory receives `diagram.html`, `diagram.svg`, and `diagram.png`.

## Tuning results

Best result: attempt 1, overall score 7.2/10. Score history (overall): attempt 1 — 7.2; attempt 2 — 5.4; attempt 3 — 4.8; attempt 4 — 4.2; attempt 5 — 5.3; attempt 6 — 5.0. These scores are an AI critic's assessment, not benchmarks. The included example is the best-scoring attempt's four-stroke engine-cycle diagram.

## License

The upstream `diagram-design` repository is MIT-licensed; its license applies to that renderer. This wrapper is provided alongside it in this fork.

## Example

![Four-stroke engine cycle diagram](examples/four-stroke-engine.png)
