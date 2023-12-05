import twttr

def test_shorten_no_vowels():
    assert twttr.shorten("hello") == "hll"
    assert twttr.shorten("world") == "wrld"
    assert twttr.shorten("Python") == "Pythn"

def test_shorten_with_vowels():
    assert twttr.shorten("aEiOu") == ""
    assert twttr.shorten("test") == "tst"
    assert twttr.shorten("check") == "chk"
