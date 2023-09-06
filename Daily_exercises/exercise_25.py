class Book:
    name = "Book"

    def __init__(self, name) -> None:
        self.name = name

bible = Book("Bible")
print("{0} name is {1}".format(Book.name,bible.name))

gita = Book("Gita")
gita.name = "Gita"
print("{0} name is {1}".format(Book.name,gita.name))

class Toy:
    name = "Toy"

    def __init__(self,name) -> None:
        self.name = name

barbie = Toy("Barbie")
print("{0} name is {1}".format(Toy.name,barbie.name))

ken = Toy("Ken")
print("{0} name is {1}".format(Toy.name,ken.name))

