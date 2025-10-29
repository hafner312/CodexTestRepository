import json

from click.testing import CliRunner

from codex_demo.cli import main


def test_cli_fib():
    runner = CliRunner()
    result = runner.invoke(main, ["fib", "5"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["value"] == 5
    assert data["sequence"][-1] == 5


def test_cli_stats():
    runner = CliRunner()
    result = runner.invoke(main, ["stats", "Hallo", "Welt"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["word_count"] == 2
    assert data["most_common"][0] == "hallo"
