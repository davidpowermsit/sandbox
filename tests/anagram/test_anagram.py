from textwrap import dedent

import pytest

from sandbox.anagram.engine import is_anagram
from sandbox.anagram.program import main


class TestIsAnagram:
    def test_is_case_agnostic(self) -> None:
        given_target = "StOp"
        given_candidate = "pOTS"
        expected = True
        actual = is_anagram(given_target, given_candidate)
        assert expected == actual

    def test_does_not_match_identical_words(self) -> None:
        given_target = "stop"
        given_candidate = "stop"
        expected = False
        actual = is_anagram(given_target, given_candidate)
        assert expected == actual


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
