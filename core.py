# Mini-Project : Library management systeme..
"""
create a library class
	method display books
	lend book - (who owns the book if not present) take name
	add book
	return book

HarryLibrary = Library(listofbooks, library name)

dictiionary books - nameofperson
create a main function and run an infinite while loop asking users for their input
"""
#Program:::


infi = 1

class library:
	books = ["Python Proramming","Java Programming","Web designing","English Communication","Polity","History of modern india"]
	users = ["Tejas","Anuj","Sandip"]
	dicttake = {}
	def __init__(self,library_name, *list_of_books):
		self.library_name = library_name
		list(list_of_books)
		for i in list_of_books:
			self.books.append(i)
	def display_books(self):
		print("-"*70)
		print("Displaying the books present in library....")
		print("-"*70)
		num_of_books = len(self.books)
		for i, book in zip(range(1, num_of_books + 1), self.books):
			print(f"{i}. {book}")
	def display_users(self):
		print("-"*70)
		print("Displaying the users of library....")
		print("-"*70)
		num_of_users = len(self.users)
		for i, user in zip(range(1, num_of_users + 1), self.users):
			print(f"{i}. {user}")
	def add_book(self, book_name):
		self.books.append(book_name)
		print("The book donated succesfully....")
	def add_user(self, user_name):
		self.users.append(user_name)
		print("User added successfully....")
	def lend_books(self):
		inte = 1
		while(inte == 1):
			print("1. Add user")
			print("2. lend book")
			print("3. Exit")
			ch = int(input("Enter your choice : "))
			if ch == 1:
				user_add = input("Enter the user's name : ")
				if user_add in self.users:
					print("The user is already exist.....")
				else:
					self.add_user(user_add)
			elif ch == 2:
				check_user = input("Enter your user name : ")
				if check_user in self.users:
					booking = 0
					self.display_books()
					ch_book = int(input("Enter your choice : "))
					for i in self.dicttake.values():
						if self.books[ch_book - 1] == i :
							print("This book is already owned....")
							booking += 1
							break
					if booking != 1 :
						self.dicttake[check_user] = self.books[ch_book-1]
						print("The book is borrowed successfully....")
				else:
					print("The user is not valid...")
					
			elif ch == 3:
				inte += 1
			else : print("Invalid choice...")
	def return_book(self, user, rt_book):
		if user in self.users:
			key1 = str()
			for key, value in self.dicttake.items():
				if rt_book == value:
					key1 = key
			if key1 in self.dicttake:
				del self.dicttake[key1]
				print("Returning book successfully.....")
			else:
				if rt_book not in self.books:
					print("The book is not in library....")
				else:
					print("1. This book is not borrowed....\n2. Check the name of the book....") 
		else : print("No such a user...")
if __name__ == '__main__':				
	name = input("Enter the name of library : ")
	Extra_books_list = list(input("Enter the list of books seperated by comma : ").split(", "))
	a = library(name, *Extra_books_list)
	print("-"*70)
	print(f"Welcome to {name} library system")
	print("-"*70)
	while(infi == 1):
		print("-"*70)
		print("1. Display books")
		print("2. lend books")
		print("3. return books")
		print("4. Donate books")
		print("5. Display users")
		print("6. Exit")
		choi = int(input("Enter your choice : "))
		if choi == 1:
			a.display_books()
		elif choi == 2:
			a.lend_books()
		elif choi == 3:
			user = input("Enter your user name : ")
			book = input("Enter the book name : ")
			a.return_book(user, book)
		elif choi == 4:
			name = input("Enter the book name : ")
			a.add_book(name)
		elif choi == 5:
			a.display_users()
		elif choi == 6:
			break
		else:
			print("Enter the valid choice!!!")


