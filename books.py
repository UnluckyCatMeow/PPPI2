books = {}

num_books_str = input("Скільки книг ви хочете додати? ")

if not num_books_str.isdigit() or int(num_books_str) <= 0:
    print("Ви не ввели жодної книги або ввели неправильне число")
    
else:
    num_books = int(num_books_str)
    for i in range(num_books):
        name = input("Введіть назву книги : ")
        author = input("Введіть автора : ")
        
        while True:
            pages_str = input("Введіть кількість сторінок : ")
            if pages_str.isdigit() and int(pages_str) > 0:
                pages = int(pages_str)
                break
            
            else:
                print("Кількість сторінок має бути додатнім числом. Спробуйте ще раз")
                
        books[name] = (author, pages)

    if len(books) == 0:
        print("Ви не ввели жодної книги")
        
    else:
        total_pages = 0
        for info in books.values():
            total_pages += info[1]
            
        average = total_pages / len(books)
        print("Середня кількість сторінок : ", round(average, 2))
        
        print("Книги з меншою кількістю сторінок, ніж середнє значення : ")
        for book, info in books.items():
            if info[1] < average:
                print("-", book, "(Автор:", info[0] + ", Сторінок:", info[1], ")")
