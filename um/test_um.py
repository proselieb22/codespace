from um import count


def test_single_um():
    assert count("um") == 1


def test_question_um():
    assert count("um?") == 1


def test_um_in_sentence():
    assert count("Um, thanks for the album.") == 1


def test_multiple_um():
    assert count("Um, thanks, um...") == 2
