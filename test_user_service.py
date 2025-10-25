# test_books.py

def test_positive_number():
    # "123" → це число і більше 0 → очікуємо True
    assert "123".isdigit() and int("123") > 0

def test_zero_number():
    # "0" → це число, але не більше 0 → очікуємо False
    assert not ("0".isdigit() and int("0") > 0)

def test_negative_number():
    # "-5" → не проходить .isdigit() → очікуємо False
    assert not ("-5".isdigit() and int("-5") > 0)

def test_not_a_number():
    # "abc" → не число → очікуємо False
    assert not ("abc".isdigit() and int("abc") > 0 if "abc".isdigit() else False)
