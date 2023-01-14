### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# def book_input():
#     title = input("What's the title of the book?")
#     author = input("Who is the author of the book?")
#     year = input("What year was the book published?")
#     rating = input("What would you rate this book [1-5]?")
#     pages = input("How many pages are in the book?")
#     return (title, author, year, rating, pages)

# print(book_input())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
# def create_new_book():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     year = int(input("What year was this book published? - "))
#     rating = float(input("What rating out of 5 would you give this book? - "))
#     pages = int(input("What is the page count of the book? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

#print(create_new_book())

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
# def create_new_book():
#     title = input("What is the title of the book you would like to add? - ")
#     author = input("Who is the author of the book you would like to add? - ")
#     try:
#         year = int(input("What year was this book published? - "))
#     except:
#         year = int(input("Please type a number for the year? - "))
#     try:
#         rating = float(input("What rating out of 5 would you give this book? - "))
#     except:
#         rating = float(input("Please type a number [1-5] for the book rating - "))
#     try:
#         pages = int(input("What is the page count of the book? - "))
#     except:
#         pages = int(input("Please type a number for the page count - "))
    

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary

#print(create_new_book())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. A. Add new book, B. View All Books, C. Search For Book By Title. Handle their choices with if/elif/else statements.

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

# LIBRARY OF BOOKS #

my_library = [{
"title": "The Hunger Games",
"author": "Suzanne Collins",
"year": 2008,
"rating": 4.32,
"pages": 374
},
{
"title": "Harry Potter and the Sorcerer's Stone",
"author": "J.K. Rowling",
"year": 1997,
"rating": 4.87,
"pages": 309
},
{
"title": "To Kill a Mockingbird",
"author": "Harper Lee",
"year": 1960,
"rating": 4.25,
"pages": 281
}]

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



# def print_all_books(list_of_books):

#     print("\nHere are all your books...\n")

#     for book in list_of_books:
#         title = book["title"]
#         author = book["author"]
#         year = book["year"]
#         rating = book["rating"]
#         pages = book["pages"]

#         print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")


# def view_books_original(book_source):

#     print("\nHere are all your books...\n")
    
#     with open(book_source, "r") as f:
#         file = f.readlines()
        
#         for line in file:
#             title, author, year, rating, pages = line.split(", ")

#             print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

def main_menu():
    
    menu_opened = True

    while menu_opened is True:
        choice = input("Welcome to the Book Library App! What would you like to do? \n(A)dd new book \n(V)iew all books \n(S)earch for book by title \n(C)ount of Books in Library \n(E)Exit \nType Choice Here:")
        if choice.upper() == "A":
            new_book = create_new_book()
            my_library.append(new_book)
            print("Book added to the library!")
        elif choice.upper() == "V":
            print(my_library)
        elif choice.upper() == "S":
            title = input("What is the title of the book you are looking for? ")
            for book in my_library:
                if book["title"] == title:
                    print(book)
                else: 
                    print("book not found.")
        elif choice.upper() == "C":
            print(f"\nYou have a total of {len(my_library)} books.\n")
        elif choice.upper() == "E":
            print("Goodbye! Come Back Again Soon!")
            menu_opened = False
        else:
            print("Invalid Option")


main_menu()









