from part_4 import my_library

### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.


def create_new_book():
    title = input("What is the title of the book you would like to add? - ")
    author = input("Who is the author of the book you would like to add? - ")
    try:
        year = int(input("What year was this book published? - "))
    except:
        year = int(input("Please type a number for the year? - "))
    try:
        rating = float(input("What rating out of 5 would you give this book? - "))
    except:
        rating = float(input("Please type a number [1-5] for the book rating - "))
    try:
        pages = int(input("What is the page count of the book? - "))
    except:
        pages = int(input("Please type a number for the page count - "))
    
    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")
    

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def view_books():

    print("\nHere are all your books...\n")
    
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")
            print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def get_highest_rating():
    with open("library.txt", "r") as f:
        file = f.readlines()
        highest_rating = 0
        best_ranked_book = {}
        for book in file:
            title, author, year, rating, pages = book.split(", ")
            rating = float(rating)
            if rating > highest_rating:
                highest_rating = rating
                best_ranked_book = book  
        print(f"The highest rated book is {best_ranked_book}")


#get_highest_rating()

def sort_by_rank(): 
    with open("library.txt", "r") as f:
        file = f.readlines()
    library = []
    for book in file:
        title, author, year, rating, pages = book.strip().split(", ")
        library.append({'title':title, 'author':author, 'year':year, 'rating':float(rating), 'pages':int(pages)})
    sorted_books = sorted(library, key=lambda x: x['rating'], reverse=True)
    for i, book in enumerate(sorted_books):
        print (f"{i+1}. {book['title']} - {book['rating']}")

#sort_by_rank()

def get_lowest_rating():
    with open("library.txt", "r") as f:
        file = f.readlines()
        lowest_rating = 5
        worst_ranked_book = {}
        for book in file:
            title, author, year, rating, pages = book.split(", ")
            rating = float(rating)
            if rating < lowest_rating:
                lowest_rating = rating
                worst_ranked_book = book  
        print(f"The lowest rated book is {worst_ranked_book}")

#get_lowest_rating()

def main_menu():
    
    menu_opened = True

    while menu_opened is True:
        choice = input("Welcome to the Book Library App! What would you like to do? \n(A)dd new book \n(V)iew all books \n(S)earch for book by title \n(C)ount of Books in Library \n(H)ighest Rated Book \n(W)orst Ranked Book \n(O)rganize By Rank \n(E)xit \nPlease Enter Choice Here:")
        if choice.upper() == "A":
            new_book = create_new_book()
            my_library.append(new_book)
            print("Book added to the library!")
        elif choice.upper() == "V":
            view_books()
        elif choice.upper() == "S":
            title_input = input("What is the title of the book you are looking for? ")
            with open("library.txt", "r") as f:
                file = f.readlines()
                for book in file:
                    title, author, year, rating, pages = book.split(", ")
                    if title == title_input:
                        print(book)
        elif choice.upper() == "C":
            print(f"\nYou have a total of {len(my_library)} books.\n")
        elif choice.upper() == "H":
            get_highest_rating()
        elif choice.upper() == "W":
            get_lowest_rating()
        elif choice.upper() == "O":
            sort_by_rank()
        elif choice.upper() == "E":
            print("Goodbye! Come Back Again Soon!")
            menu_opened = False
        else:
            print("Invalid Option")

if __name__ == "__main__":
    main_menu()





