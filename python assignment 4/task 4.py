def save_returns(books):
    with open("returns.log", "a") as file:
        for book in books:
            file.write(book + "\n")


def process(day_file):
    try:
        with open(day_file, "r") as file:
            books = file.readlines()

        save_returns([book.strip() for book in books])

    except FileNotFoundError:
        with open("error.log", "a") as file:
            file.write("File not found: " + day_file + "\n")


# Create sample files automatically
with open("day1.txt", "w") as file:
    file.write("Book A\nBook B\n")

with open("day2.txt", "w") as file:
    file.write("Book C\nBook D\n")

with open("day3.txt", "w") as file:
    file.write("Book E\n")

process("day1.txt")
process("day2.txt")
process("day3.txt")

with open("returns.log", "r") as file:
    print(file.read())