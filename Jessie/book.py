class Books:
    pass

if __name__ == "__main__":
    a = Books()
    b = Books()
    a2 = a

    a.name = "Fairy Magic"
    a.genre = "Fantasy"
    a.published = "January 3, 2001"

    b.name = "The Planets"
    b.genre = "Nonfiction"
    b.published = "June 9, 1895"

    print(a.name)
    print(b.genre)
    print(a.published)

    Books.store = "Walmart"
    print(a.store)
    print(b.store)
    print(a2.store)

    print(a.__dict__)
    print(Books.__dict__)