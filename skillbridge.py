import sqlite3 
def run():
    # try:
        sqliteConn = sqlite3.connect('skillbridge.db')
        cursor = sqliteConn.cursor()

        query = '''
            CREATE TABLE user (
            user_id INTEGER private key,
            full_name VARCHAR(30) NOT NULL,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL,
            email VARCHAR(50),
            DOB INTEGER NOT NULL
        );
        '''
        # cursor.execute(query) 


        query = '''
            CREATE TABLE Skills(
            skill_id INTEGER private key,
            skill_name VARCHAR(20) NOT NULL,
            description VARCHAR(200) NOT NULL
        );
        '''
        # cursor.execute(query)


        query = '''
            CREATE TABLE Listing_table(
            listing_id INTEGER private key,
            user_id INTEGER,
            skills_id INTEGER,
            available_slot VARCHAR(30),
            price_per_slot VARCHAR(20)
        );
        '''
        # cursor.execute(query)

        query = '''
            CREATE TABLE Request_table(
            request_id INTEGER private key,
            user_id INTEGER,
            skill_id INTEGER,
            request_date VARCHAR(15) NOT NULL,
            status VARCHAR(15) NOT NULL
        );
        '''
        # cursor.execute(query)

        query = '''
            CREATE TABLE Transaction_table (
            transaction_id INTEGER private key,
            request_id INTEGER,
            transaction_date VARCHAR(20) NOT NULL,
            payment_status VARCHAR(20) NOT NULL
        );
        '''
        # cursor.execute(query)

        query = '''
            CREATE TABLE Rating (
            rating_id INTEGER private key,
            user_id INTEGER,
            skill_id INTEGER,
            rating_value VARCHAR(50),
            review_comment VARCHAR(100) NOT NULL
        );
        '''
        # cursor.execute(query)

        query = """INSERT INTO Rating(rating_id, user_id, skill_id, rating_value, review_comment)
        VALUES("rating1", "user2", 2, "5 star", "absolutly good");
        """
        cursor.execute(query)

        query = """INSERT INTO Rating(rating_id, user_id, skill_id, rating_value, review_comment)
        VALUES("rating2", "user3", 1, "3 star", "good but not up to date");
        """
        cursor.execute(query)

        query = ''' 
        INSERT INTO Skills (skill_id, skill_name, description)
        VALUES (1, "Data Science", "lorem ipsum");
        '''
        # cursor.execute(query)

        query = ''' INSERT INTO Skills (skill_id, skill_name, description)
        VALUES(2, "Web Development", "lorem ipsum");
        '''
        # cursor.execute(query)

        query = ''' INSERT INTO Skills (skill_id, skill_name, description)
        VALUES(3, "UI/UX Design", "lorem ipsum");
        '''
        # cursor.execute(query)

        query = ''' INSERT INTO user(user_id, full_name, username, password, email, DOB)
        VALUES("user1", "Oke Chris", "tife", "okechris1234", "chrisoke@gmail.com", "1999")
        '''
        # cursor.execute(query)

        query = '''INSERT INTO user (user_id, full_name, username, password, email, DOB)
        VALUES("user2", "Ade Master", "Ade-M", "ademaster2002", "ade2@gmail.com", "2002")
        '''
        # cursor.execute(query)

        query = """INSERT INTO Listing_table(listing_id, user_id, skills_id, available_slot, price_per_slot)
        VALUES(1, "user2", 1, "22", "$200");
        """
        # cursor.execute(query)

        query = """INSERT INTO Listing_table(listing_id, user_id, skills_id, available_slot, price_per_slot)
        VALUES(2, "user1", 3, "10", "$1500");
        """
        # cursor.execute(query)

        query = """ INSERT INTO Request_table(request_id, user_id, skill_id, request_date, status)
        VALUES(1, "user3", 2, 24-3, "approved");
        """
        # cursor.execute(query)

        query = """ INSERT INTO Request_table(request_id, user_id, skill_id, request_date, status)
        VALUES(2, "user1", 3, 2-2, "pending");
        """
        # cursor.execute(query)

        query = """INSERT INTO Transaction_table(transaction_id, request_id, transaction_date, payment_status)
        VALUES("trans1", 2, "2023", "paid");
        """
        cursor.execute(query)

        query = """INSERT INTO Transaction_table(transaction_id, request_id, transaction_date, payment_status)
        VALUES("trans2", 1, "2002", "pending");
        """
        cursor.execute(query)

        sqliteConn.commit()
        sqliteConn.close()

    # except Exception as e:
    #     print(f'{e}')

if __name__ == '__main__':
    run()
