from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("CAPSTWITTER") == "CPSTWTTR"
    assert shorten("TWIT SPACE S") == "TWT SPC S"
    assert shorten("Axe124//!.?") == "x124//!.?"

if __name__ == "__main__":
    main()
