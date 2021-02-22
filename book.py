class Book:

    def __init__(self, title, author, description):
        self.id = id
        self.title = title
        self.author = author
        self.description = description

    @staticmethod
    def list_book_id_title(cursor):
        # retrive book from database
        query = "select id,title from books;"
        data = cursor.execute(query)
        return data

    @staticmethod
    def book_info(cursor, book_id):
        # retrive specific book from database using id
        query = "select * from books where id={} limit 1;".format(int(book_id))
        data = cursor.execute(query).fetchone()
        return data

    def add_book(self, cursor):
        # get the title,author,description
        query = "insert into books (title, author, description) values ('{}','{}','{}');" \
            .format(self.title, self.author, self.description)
        data = cursor.execute(query)
        return data

    @staticmethod
    def list_all_books(cursor):
        query = "select * from books;"
        data = cursor.execute(query).fetchall()
        return data

    @staticmethod
    def update_book(cursor, id, title, author, description):
        query = "update books set title='{}',author='{}', description='{}' where id={}" \
            .format(title, author, description, int(id))
        data = cursor.execute(query)
        return data


    @staticmethod
    def search_book_by_name(cursor, name):
        query = "select * from books where title like '%{}%';".format(name)
        data = cursor.execute(query).fetchall()
        return data
