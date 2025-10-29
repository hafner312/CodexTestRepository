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

## Änderungen auf GitHub hochladen

Innerhalb dieser Umgebung wird kein Remote-Repository konfiguriert und es findet kein automatisches Pushen statt. Wenn du den Code nach GitHub übertragen möchtest, melde dich zunächst mit `git remote add origin <URL>` bei deinem eigenen Repository an und führe anschließend `git push origin <branch>` aus.
