from services.library_service import LibraryService

def main():
    library = LibraryService()

    while True:
        print('1. Add Book')
        print('2. Register User')
        print('3. View Book')
        print('4. Issue Book')
        print('5. Return Book')
        print('6. Exit')

        try:
            user_choice = int(input('Enter your choice please: '))

            if user_choice == 1:
                title = input('Enter the title: ')
                author_name = input('Enter the Author name: ')
                library.add_book(title, author_name)
            elif user_choice == 2:
                name = input('Enter your name: ')
                library.register_user(name)
            elif user_choice == 3:
                library.display_books()
            elif user_choice == 4:
                user_id = int(input('Enter your user id: '))
                book_id = int(input('Enter your book id: '))
                library.issue_book(user_id, book_id)
            elif user_choice == 5:
                user_id = int(input('Enter your user id: '))
                book_id = int(input('Enter your book id: '))
                library.return_book(user_id, book_id)
            elif user_choice == 6:
                print('Goodbye! have a nice day.')
                break
        except ValueError:
            print('please enter integer value.')
        except Exception as e:
            print(f'Somethong went wrong: {e}')

if __name__ == '__main__':
    main()