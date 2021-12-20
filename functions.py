import psycopg2
from psycopg2 import Error
from passlib.hash import argon2

_dbcredentials = {
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432",
    "database": "postgres"
}


# Sign in function - done
def getLogin(username, password):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        postgreSQL_select_Query = """SELECT u.username,u.password FROM public.user u WHERE u.username=%s;"""
        cursor.execute(postgreSQL_select_Query, (username,))

        login_records = cursor.fetchall()

        for row in login_records:
            #print("Username:", row[0])
            #print("Password:", row[1], "\n")

            if argon2.verify(password, row[1]):
                return True
            else:
                return False

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        connection = None
        cursor = None
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# getLogin("postgres", "postgres")


# Get book records - done
def getBookRows():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        postgreSQL_select_Query = "SELECT b.title, w.first_name, w.surname, t.type FROM public.book b FULL OUTER JOIN " \
                                  "public.bookwriter bw ON b.book_id =bw.book_id FULL OUTER JOIN public.writer w ON " \
                                  "bw.writer_id = w.writer_id FULL OUTER JOIN public.booktype bt ON b.book_id = bt.book_id FULL OUTER JOIN " \
                                  "public.type t ON bt.type_id = t.type_id WHERE title IS NOT NULL"
        cursor.execute(postgreSQL_select_Query)

        # Fetch result
        book_records = cursor.fetchall()
        """
        for row in book_records:
            print("Title:", row[0])
            print("Name:", row[1])
            print("Surname", row[2])
            print("Type:", row[3], "\n")
        """

        return [book for book in book_records]


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        connection = None
        cursor = None
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# getBookRows()

# Get borrow records function - done
def getBorrowRows():
    connection = None
    cursor = None
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        postgreSQL_select_Query = "SELECT bk.title, r.first_name, r.surname, b.borrow_date, b.return_date FROM public.book bk JOIN " \
                                  "public.borrow b ON bk.book_id = b.book_id JOIN " \
                                  "public.reader r ON b.reader_id = r.reader_id"

        cursor.execute(postgreSQL_select_Query)

        # Fetch result
        book_records = cursor.fetchall()
        """for row in book_records:
            print("Title:", row[0])
            print("Name:", row[1])
            print("Surname:", row[2])
            print("Borrow:", row[3])
            print("Return:", row[4], "\n")"""
        return [book for book in book_records]


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# getBorrowRows()


# Get try_me records - done
def getTrymeRows():
    connection = None
    cursor = None
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        postgreSQL_select_Query = "SELECT t.name, t.surname, t.city FROM public.try_me t;"
        cursor.execute(postgreSQL_select_Query)

        # Fetch result
        try_me_records = cursor.fetchall()
        """for row in try_me_records:
            print("Name:", row[0])
            print("Surname:", row[1])
            print("City:", row[2], "\n")"""
        return [book for book in try_me_records]


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


#getTrymeRows()

# Insert New Book - done
def insertNewBook(title, name, surname):
    connection = None
    cursor = None
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        postgres_insert_query1 = """ INSERT INTO public.book (title) VALUES (%s)"""
        record_to_insert1 = (title,)

        postgres_insert_query2 = """ INSERT INTO public.writer (first_name, surname) VALUES (%s, %s)"""
        record_to_insert2 = (name, surname,)

        cursor.execute(postgres_insert_query1, record_to_insert1)
        cursor.execute(postgres_insert_query2, record_to_insert2)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully")


    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# insertNewBook("Everything is fucked", "Mark", "Manson")


# SQL injection - done
def injectionSQL(name, surname, age, city):
    connection = None
    cursor = None
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        postgres_insert_query = "INSERT INTO public.try_me (name, surname, age, city) VALUES ('" + name + "','" + surname + "','" + age + "','" + city + "')"
        cursor.execute(postgres_insert_query)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully")


    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)
    finally:

        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
#injectionSQL("Peter", "Parker", 23, "New York")

# Find Book by title - done
def findBook(myvalue):
    connection = None
    cursor = None
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        postgreSQL_select_Query = "SELECT b.title, w.first_name, w.surname, t.type FROM public.book b JOIN " \
                                  "public.bookwriter bw ON b.book_id =bw.book_id JOIN public.writer w ON " \
                                  "bw.writer_id = w.writer_id JOIN public.booktype bt ON b.book_id = bt.book_id JOIN " \
                                  "public.type t ON bt.type_id = t.type_id WHERE b.title LIKE (%s)"

        search = "%{}%".format(myvalue)
        cursor.execute(postgreSQL_select_Query, (search,))

        # Fetch result
        book_records = cursor.fetchall()
        """for row in book_records:
            print("Title:", row[0])
            print("Name:", row[1])
            print("Surname", row[2])
            print("Type:", row[3], "\n")"""
        return [book for book in book_records]

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# findBook("How")

# Book update query - done
def bookUpdate(new_title, id):
    connection = None
    cursor = None
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        sql_update_query = """UPDATE public.book SET title = %s WHERE book_id = %s"""

        cursor.execute(sql_update_query, (new_title, id,))
        connection.commit()

        row_count = cursor.rowcount
        print(row_count, "Records Updated")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


#bookUpdate("Love is not enough", 51)

# Book delete query
def bookDelete(title):
    connection = None
    cursor = None
    try:
        # Connect to an existing database
        connection = psycopg2.connect(**_dbcredentials)

        # Cursor to perform database operations
        cursor = connection.cursor()
        """
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        """
        # Executing a SQL query
        postgres_delete_Query = "DELETE FROM public.book WHERE title=%s"
        cursor.execute(postgres_delete_Query, (title,))
        connection.commit()
        row_count = cursor.rowcount
        print(row_count, "Record Deleted")


    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

