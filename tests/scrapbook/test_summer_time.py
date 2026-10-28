import pytest

from sandbox.scrapbook.summer_time import main


class TestSummerTime:
    def test_total_value_displayed_after_1000(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:
        expected = "The Total is: 1000\n"
        inputs = iter(["100"] * 10)

        monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

        main()

        output = capsys.readouterr().out

        assert expected == output
