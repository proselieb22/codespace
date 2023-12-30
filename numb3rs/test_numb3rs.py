from numb3rs import validate


def test_valid_ipv4_addresses():
    assert validate("127.0.0.1") is True
    assert validate("255.255.255.255") is True
    assert validate("192.168.1.1") is True
    assert validate("10.0.0.1") is True


def test_invalid_ipv4_addresses():
    assert validate("512.512.512.512") is False
    assert validate("1.2.3.1000") is False
    assert validate("cat") is False
    assert validate("256.0.0.0") is False
    assert validate("192.168.1") is False
