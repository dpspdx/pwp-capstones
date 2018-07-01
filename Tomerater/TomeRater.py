class User(object):
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books ={}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return self.email

    def __repr__(self):
        num_books_read = len(self.books)
        return "User {name}, email: {email} books red:{num_books_read}".format(name=self.name, email = self.email, num_books_read=num_books_read)

    def __eq__(self, other_user):
        if self.email == other_user.email and self.name == other_user.name:
            return True
        else:
            return False

    def read_book(self, book, rating =None):
        self.books[book] = rating
        return self.books

    def get_average_rating(self):
        rating_sum = 0
        rating_count = 0
        for v in self.books.values():
            if v != None:
                rating_count += 1
                rating_sum += v
        if rating_count!= 0:
            average_rating = float(rating_sum) / (rating_count)
            return average_rating
        else:
            return None


class Book:
    def __init__(self, title, isbn):
        self.title=title
        self.isbn=isbn
        self.ratings=[]

    def get_tite(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        print("{title}/'s ISBN has been updated to {isbn}".format(title=self.title, isbn=self.isbn))

    def add_rating(self,rating):
        self.rating = rating
        if self.rating >=0 and self.rating <=4:
            self.ratings.append(self.rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        count_for_aver =0
        sum_for_aver = 0
        for i in self.ratings:
            if i != None:
                count_for_aver +=1
                sum_for_aver +=i
        if count_for_aver != 0:
            average_rating = float(sum_for_aver)/float(count_for_aver)
            return average_rating
        else:
            return None




class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title,isbn)
        self.subject=subject
        self.level=level

    def get_level(self):
        return self.level

    def get_subject(self):
        return self.subject

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title,level=self.level,subject=self.subject)

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.new_book = Book(self.title,self.isbn)
        return self.new_book

    def create_novel(self, title, author, isbn):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.new_novel = Fiction(self.title, self.author, self.isbn)
        return self.new_novel

    def create_non_fiction(self, title, subject, level, isbn):
        self.title = title
        self.isbn = isbn
        self.subject = subject
        self.level = level
        self.new_non_fict = Non_Fiction(self.title, self.subject, self.level,self.isbn,)
        return self.new_non_fict

    def add_book_to_user(self, book, email, rating=None):
        test_for_user = False
        self.book = book
        self.email=email
        self.rating=rating
        if self.email in self.users.keys():
            test_for_user = True
        if test_for_user == False:
            print("No user with email {email}!".format(email=self.email))
        else:
            self.users[self.email].read_book(self.book,self.rating)
            if self.book in self.books.keys():
                v = self.books[self.book]
                v +=1
                self.books[self.book]=v
            else:
                self.books[self.book]=1
            if self.rating != None:
                self.book.add_rating(self.rating)
        return self.books

    def add_user(self, name, email, user_books = None):
        self.email = email
        self.user_books = user_books
        self.name = name
        if self.email in self.users:
            print("The email {email} is already a user.".foramt(email=self.email))
            return
        if self.email[-4:] not in [".com",".edu",".org"]:
            print("We are sorry {email} is not recognized as an acceptable email".format(email=self.email))
            return
        self.new_user = User(self.name, self.email)
        self.users[self.email]=self.new_user
        if self.user_books != None:
            for i in self.user_books:
                self.add_book_to_user(i,self.email, None)

    def print_catalog(self):
        for b in self.books.keys():
            print(b)

    def print_users(self):
        for u in self.users.keys():
            print(u)

    def get_most_read_book(self):
        largest_count = 0
        read_most =''
        for k,v in self.books.items():
            if v > largest_count:
                read_most = k
                largest_count =v
        return read_most

    def highest_rated_book(self):
        high_rate =0
        rated_high =''
        for k in self.books.keys():
            if k.get_average_rating()!= None and k.get_average_rating() > high_rate:
                rated_high =k.title
                high_rate =k.get_average_rating()
        return rated_high

    def most_positive_user(self):
        most_pos=0
        pos_user =''
        for k, v in self.users.items():
            if v.get_average_rating() >most_pos:
                pos_user = v.name
                most_pos = v.get_average_rating()
        return pos_user

    def get_n_most_prolific_readers(self, n):
        prolif_readers = []
        self.n = n
        while len(prolif_readers)<n:
            most_books = 0
            most_prof = ''
            for user in self.users.values():
                if  len(user.books) > most_books and user.name not in prolif_readers:
                    most_prof = user.name
                    most_books = len(user.books)
            prolif_readers.append(most_prof)
        return prolif_readers

    def __repr__(self):
        total_books_read=0
        for v in self.books.values():
            total_books_read+=v
        return """
        We have {reader_count} users. 
        They have read a total {book_count} books""".format(reader_count = len(self.users),book_count=total_books_read)
