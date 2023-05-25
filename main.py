from functions import *


def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
<<<<<<< HEAD
    print("3. Add quotes")
    print("4. Exit")
=======
    print("3. Exit")
>>>>>>> origin/main


def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

<<<<<<< HEAD
        choice = input("Choose your an action (1-4): ")
=======
        choice = input("Choose your an action (1-3): ")
>>>>>>> origin/main

        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2":
            view_quotes(quotes)
        elif choice == "3":
<<<<<<< HEAD
            add_quote(quotes, "quotes.txt")
        elif choice == "4" :
=======
>>>>>>> origin/main
            print("Good bye...")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()