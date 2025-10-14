import builtins
import importlib
import sys

def test_books_program(monkeypatch, capsys):
    inputs = iter([
        "3",
        "Книга1", "Автор1", "100",
        "Книга2", "Автор2", "200",
        "Книга3", "Автор3", "300",
    ])

    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    if "books" in sys.modules:
        importlib.reload(sys.modules["books"])
    else:
        import books

    output = capsys.readouterr().out

    assert "Середня кількість сторінок" in output
    assert "Книги з меншою кількістю сторінок" in output
    assert "Книга1" in output
