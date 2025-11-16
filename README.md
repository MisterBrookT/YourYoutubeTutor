# YourYoutubeTutor 🎧

A small personal project that turns any YouTube video into an interactive English tutor.

The idea is simple:
Use real videos I enjoy, and let an AI tutor guide me through listening and understanding.

## Quickstart

installation:

```bash
uv sync
source .venv/bin/activate
```

fetch a transcript from Youtube:

```bash
tutor fetch <youtube_link> --out transcript.json
```
Run LLM explanation:
```bash
tutor explain transcript.json --out enriched.json
```

## The bigger goal

Make the tutor feel like a real human:

- It plays the original audio segment
- It listens “together" with me (via transcript or audio input)
- It asks whether I understood
- If not, it can repeat, explain, or ask a simple check question
- All actions are triggered through tool-calling
  (e.g., play this segment, explain this part, move to next)


## Current progress

- CLI built with Typer
- Transcript fetching works
- LLM explanation works
- JSON enrichment works

This is the MVP for now.

## Next steps

- Add audio downloading
- Add segment-level audio playback
- Create an interactive learning loop (`tutor learn`)
- Let the tutor decide actions (repeat, explain, next) like a real teacher
