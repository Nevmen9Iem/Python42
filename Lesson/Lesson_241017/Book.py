# Записна книжка
import pickle


class Note:
    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, value):
        if value > 0:
            self._page_count = value
        else:
            raise ValueError('Page count must be greater than zero')

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.page_count = page_count

    def edit(self, new_content):
        self.content = new_content

    def __str__(self):
        return self.content


class Notebook:

    # Create notes
    def __init__(self):
        with open('text.b', 'rb') as file:
            self.notes = pickle.load(file)

    # Create note
    def add_note(self, title, author, content):
        note = Note(title, author, content)
        self.notes.append(note)
        with open('text.b', 'wb') as file:
            pickle.dump(self.notes, file)
    # Read

    def __str__(self):
        result = ''
        for note in self.notes:
            result = result + str(note.content) + '\n'
        return result

    # Delete
    def remove_note(self, title):
        for index in range(len(self.notes)):
            if (self.notes[index]).title == title:
                self.notes.pop(index)
                break
        with open('text.b', 'wb') as file:
            pickle.dump(self.notes, file)
