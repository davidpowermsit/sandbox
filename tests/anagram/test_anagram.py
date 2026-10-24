from textwrap import dedent

import pytest

from sandbox.anagram.program import main


class TestMain:
    def test_anagrams_displayed_on_screen(
        self, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
    ) -> None:

        words = dedent(
            """\

            op
            ops
            opt
            opts
            os
            post
            pot
            pots
            pst
            so
            sop
            sot
            spot
            stop
            to
            top
            tops
            """
        )
        expected = words + "\nFinal Anagram Phrase: \n\n"
        inputs = iter(["Stop", "tops", "n"])
        monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

        with pytest.raises(SystemExit):
            main()

        output = capsys.readouterr().out
        assert output == expected
