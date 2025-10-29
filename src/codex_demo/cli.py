"""CLI für das Codex Demo Paket."""
from __future__ import annotations

import json
from dataclasses import asdict

import click

from .fibonacci import fibonacci
from .text import word_statistics


@click.group()
def main() -> None:
    """Codex Demo Kommandozeile."""


@main.command()
@click.argument("n", type=int)
def fib(n: int) -> None:
    """Berechnet die n-te Fibonacci Zahl."""
    result = fibonacci(n)
    click.echo(json.dumps(asdict(result), ensure_ascii=False, indent=2))


@main.command()
@click.argument("text", nargs=-1)
def stats(text: tuple[str, ...]) -> None:
    """Zeigt Wortstatistiken für den gegebenen Text."""
    result = word_statistics(" ".join(text))
    click.echo(json.dumps(asdict(result), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
