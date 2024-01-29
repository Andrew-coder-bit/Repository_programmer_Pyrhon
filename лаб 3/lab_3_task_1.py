class Book:
    """ Базовый класс книги. """
    def init(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def init(self, name: str, author: str, pages: int):
        super().init(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц: {self.pages}"



class AudioBook(Book):
    def init(self, name: str, author: str, duration: float):
        super().init(name, author)
        self._duration = duration


    @property
    def duration(self):
        return self._duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность: {self.duration} часов"




