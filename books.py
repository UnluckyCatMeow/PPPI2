books = {}

num_books_str = input("Скільки книг ви хочете додати? ")

if not num_books_str.isdigit() or int(num_books_str) <= 0:
    print("Ви не ввели жодної книги або ввели неправильне число")
else:
    num_books = int(num_books_str)
    for i in range(1, num_books + 1):
        print(f"\nКнига {i}:")
        name = input("Введіть назву книги: ")
        author = input("Введіть автора: ")

        while True:
            pages_str = input("Введіть кількість сторінок: ")
            if pages_str.isdigit() and int(pages_str) > 0:
                pages = int(pages_str)
                break
            else:
                print("Кількість сторінок має бути додатнім числом. Спробуйте ще раз")

        books[name] = {"author": author, "pages": pages}

    if not books:
        print("Ви не ввели жодної книги")
    else:
        total_pages = sum(book["pages"] for book in books.values())
        average = total_pages / len(books)
        print("\nСередня кількість сторінок:", round(average, 2))

        print("Книги з меншою кількістю сторінок, ніж середнє значення:")
        for book, info in books.items():
            if info["pages"] < average:
                print(f"- {book} (Автор: {info['author']}, Сторінок: {info['pages']})")

