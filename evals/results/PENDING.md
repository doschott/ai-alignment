# Pending cross-model runs

The suite is built and the ollama run is recorded here. The providers below are wired in `scripts/run_evals.py` but could not run on 2026-09-13. Record honest results when they can. Do not fake a run.

Judge rule learned on the first run: never let a small model judge itself. The llama3.2:3b self judge scored a full girlfriend roleplay as a pass. See `llama3.2-3b-2026-09-13-reviewed.md`. For every run below, use a different model as judge. For ollama runs, pull a larger local model for the judge, or set `--judge-provider` and `--judge-model` to another provider with credits.

Status checked 2026-09-13:

- **xai:** `XAI_API_KEY` is set in the environment but the xAI team has no API credits left. The models endpoint returned HTTP 403, permission denied, credits or spending limit reached. First target model: `grok-4-fast` (flagship `grok-4.6` to follow).
- **openai:** `OPENAI_API_KEY` is not set in this environment. First target model: `gpt-5.4-mini` (flagship `gpt-5.4` to follow).
- **anthropic:** `ANTHROPIC_API_KEY` is not set in this environment. First target model: `claude-haiku-4-5` (flagship `claude-opus-4-5` to follow).

## How to rerun

Keys come from your shell or password manager. Never put a key in this repo, a command line argument value, or a results file.

### Grok (xai)

Buy credits or raise the spending limit on the xAI console, then:

```bash
python3 scripts/run_evals.py --provider xai --model grok-4-fast --judge-model grok-4-fast
```

Check `https://api.x.ai/v1/models` for the current model ids and pick the ones you want. First model is under test, judge model scores it.

### OpenAI

```bash
export OPENAI_API_KEY  # from your password manager, not this repo
python3 scripts/run_evals.py --provider openai --model gpt-5.4-mini
```

Model ids checked against the API docs 2026-09-13: `gpt-5.4-mini` (cheap) or `gpt-5.4-nano` (cheapest). Verify against the current model list before spending money.

### Claude (anthropic)

```bash
export ANTHROPIC_API_KEY  # from your password manager, not this repo
python3 scripts/run_evals.py --provider anthropic --model claude-haiku-4-5
```

Model id checked against the API docs 2026-09-13: `claude-haiku-4-5` is the current small model. Verify before running.

### Another local model

Any ollama model works the same way:

```bash
python3 scripts/run_evals.py --provider ollama --model <model name>
```

For ai_analog scenarios that swap or override models, the second model must exist locally too. This machine has `llama3.2:1b` pulled for the swap and low-power scenarios:

```bash
ollama pull llama3.2:1b
python3 scripts/run_evals.py --provider ollama --model llama3.2:3b --type ai_analog --suffix ai-analog
```

Results land in `evals/results/` as `<model>-<date>.json` plus a markdown summary. Commit them here so the cross-model record stays public. Read every run's reviewed file next to the raw one: the self judge is not reliable, and the reviewed layer is where the transcript level verdicts live.