import builtins

def test_books_program(monkeypatch, capsys):
    # Підставимо відповіді, які програма отримає через input()
    inputs = iter([
        "3",             # Кількість книг
        "Книга1", "Автор1", "100",  # 1-а книга
        "Книга2", "Автор2", "200",  # 2-а книга
        "Книга3", "Автор3", "300",  # 3-я книга
    ])

    # Підміняємо input() щоб він повертав наші значення
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    # Імпортуємо твою програму (вона автоматично виконається)
    import books

    # Збираємо увесь вивід програми
    output = capsys.readouterr().out

    # Перевіряємо, що є правильний текст
    assert "Середня кількість сторінок" in output
    assert "Книги з меншою кількістю сторінок" in output
    assert "Книга1" in output
