from Book import *

flag = True
book = Notebook()

while flag:
    command = str(input('Enter command: [r], [c], [e], [d]: '))
    if command.lower() == 'c':
        title = str(input('Enter title: '))
        author = str(input('Enter author: '))
        content = str(input('Enter content: '))

        book.add_note(title, author, content)
    elif command.lower() == 'r':
        print(book)

    elif command.lower() == 'e':
        flag = str(input("Enter [any key] + [enter] to continue OR enter [enter] to exit: "))

    elif command.lower() == 'd':
        title = str(input('Enter title: '))
        book.remove_note(title)

