# CodexTestRepository

Dieses Repository demonstriert verschiedene Funktionen, die ich als KI in einem Projekt umsetzen kann. Enthalten sind:

- Ein kleines Python-Paket `codex_demo` mit Fibonacci- und Textanalyse-Funktionalität.
- Eine Click-basierte Kommandozeilenanwendung, die beide Funktionen zugänglich macht.
- Unit-Tests mit `pytest`, die sowohl die Kernlogik als auch die CLI prüfen.
- Ein `pyproject.toml`, um das Projekt installierbar zu machen.

## Installation

```bash
pip install -e .[test]
```

## Verwendung

Fibonacci-Zahl berechnen:

```bash
codex-demo fib 7
```

Textstatistiken ermitteln:

```bash
codex-demo stats "Hallo Welt Hallo"
```

## Tests ausführen

```bash
pytest
```
