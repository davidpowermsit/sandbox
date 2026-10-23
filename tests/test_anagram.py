from textwrap import dedent

import pytest

from sandbox.anagramfinder import is_anagram
from sandbox.anagramprogram import main


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

        expected = dedent(
            """\
        These are the anagrams found for the word Stop
        - opts
        - post
        - pots
        - spot
        - tops
        """
        )
        inputs = iter(["Stop"])
        monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

        main()

        output = capsys.readouterr().out
        assert output == expected
