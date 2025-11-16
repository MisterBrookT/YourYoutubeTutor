import json
from pathlib import Path
from typing import Optional

import typer

from src.transcript import YoutubeExtractor
from src.utils.io import read_json
from src.tutor import Tutor
app = typer.Typer(no_args_is_help=True)


@app.command()
def extract(
    url: str = typer.Argument(..., help="YouTube video URL"),
    out: Optional[Path] = typer.Option(
        None,
        "--out",
        "-o",
        help="Output JSON file path (default: transcript.json)",
    ),
):
    """
    Fetch transcript for a YouTube video and save as JSON.
    """
    typer.echo(f"Fetching transcript for: {url}")
    data = YoutubeExtractor.get_transcript(url)

    if out is None:
        out = Path("transcript.json")
    # Save the transcript data as JSON.
    with out.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    typer.echo(f"Saved transcript to {out}")


@app.command()
def explain(
    transcript: Path = typer.Argument(..., help="Transcript JSON file path"),
    out: Optional[Path] = typer.Option(
        None,
        "--out",
        "-o",
        help="Output JSON file path (default: enriched_transcript.json)",
    ),
):
    """
    Explain the transcript using LLM.
    """

    data = read_json(transcript) 
    enriched = Tutor.explain(transcript=data)
    if out is None:
        out = Path("enriched_transcript.json")
    with out.open("w", encoding="utf-8") as f:
        json.dump(enriched, f, ensure_ascii=False, indent=2)
    typer.echo(f"Saved enriched transcript to {out}")



def main():
    app()


if __name__ == "__main__":
    main()