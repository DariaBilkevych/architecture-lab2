from app.models import db_session, Book

def seed_data():
    books = [
        Book(title="The Pragmatic Programmer", author="Andy Hunt"),
        Book(title="Clean Code", author="Robert C. Martin"),
        Book(title="Python Crash Course", author="Eric Matthes"),
        Book(title="Fluent Python", author="Luciano Ramalho"),
        Book(title="Automate the Boring Stuff with Python", author="Al Sweigart"),
        Book(title="Introduction to Algorithms", author="Thomas H. Cormen"),
        Book(title="You Don’t Know JS", author="Kyle Simpson"),
        Book(title="Refactoring", author="Martin Fowler"),
        Book(title="Design Patterns", author="Erich Gamma"),
        Book(title="Code Complete", author="Steve McConnell"),
        Book(title="The Mythical Man-Month", author="Fred Brooks"),
        Book(title="Structure and Interpretation of Computer Programs", author="Harold Abelson"),
        Book(title="Grokking Algorithms", author="Aditya Bhargava"),
        Book(title="The Art of Computer Programming", author="Donald Knuth"),
        Book(title="Head First Design Patterns", author="Eric Freeman"),
        Book(title="Working Effectively with Legacy Code", author="Michael Feathers"),
        Book(title="Domain-Driven Design", author="Eric Evans"),
        Book(title="Test-Driven Development", author="Kent Beck"),
        Book(title="Continuous Delivery", author="Jez Humble"),
        Book(title="Soft Skills: The software developer's life manual", author="John Sonmez")
    ]
    db_session.add_all(books)
    db_session.commit()
    print("Seed data inserted.")

if __name__ == "__main__":
    seed_data()
