my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def get_dict(dict):
    print(dict)

get_dict(my_book)

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def get_title(dict):
    print(dict["title"])

get_title(my_book)

def get_auth(dict):
    print(dict["author"])

get_auth(my_book)

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below