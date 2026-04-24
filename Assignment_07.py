class ReadingMaterial:
    def __init__(self, title):
        self.title = title
    
    def display(self):
        print("Title:", self.title)

class Book(ReadingMaterial):
    def __init__(self, title, isbn):
        super().__init__(title)
        self.isbn = isbn

    def display(self):
        super().display()
        print("ISBN:", self.isbn)

class ResearchPaper(ReadingMaterial):
    def __init__(self, title, doi):
        super().__init__(title)
        self.doi = doi

    def display(self):
        super().display()
        print("DOI:", self.doi)

bookname= input("Enter Book Name:")
ISBN = input("Enter ISBN no:")

rname = input("Enter Paper Name:")
doi = input("Enter DOI:")

book1 = Book(bookname, ISBN)
research1 = ResearchPaper(rname, doi)

print("Book deatils:")
book1.display()

print("Paper Details:")
research1.display()
