from sandbox.anagramfinder import is_anagram


def test_anagram_is_case_agnostic():
    given_target = "StOp"
    given_candidate = "pOTS"
    expected = True
    actual = is_anagram(given_target, given_candidate)
    assert expected == actual
