import psycopg2
from config import host, user, password, db_name


class player:
    def __init__(self):
        self.username = None
        self.userExists = None
        self.userScore = 0

    def getUserName(self, username):
        self.username = username
        try:
            connection = psycopg2.connect(
                host=host, user=user, password=password, database=db_name
            )

            with connection.cursor() as cursor:
                cursor.execute(
                    f"SELECT * FROM players WHERE user_name = '{self.username}'"
                )
                fetchedResults = cursor.fetchone()
                if fetchedResults:
                    self.userExists = True
                    self.userScore = fetchedResults[2]
                    print(self.userScore)

        except Exception as _ex:
            print("[INFO] error", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] PostgreSQL connection closed")

    def addUserName(self):
        if not self.userExists:
            try:
                connection = psycopg2.connect(
                    host=host, user=user, password=password, database=db_name
                )

                with connection.cursor() as cursor:
                    cursor.execute(
                        f"INSERT INTO players (user_name, user_score) VALUES('{self.username}', '0');"
                    )
                    # print(cursor.fetchone())
                    connection.commit()

            except Exception as _ex:
                print("[INFO] error", _ex)
            finally:
                if connection:
                    connection.close()
                    print("[INFO] Succesful added")

    def changeUserScore(self, score):
        try:
            connection = psycopg2.connect(
                host=host, user=user, password=password, database=db_name
            )

            with connection.cursor() as cursor:
                cursor.execute(
                    f"UPDATE players SET user_score = '{score}' WHERE user_name = '{self.username}';"
                )
                connection.commit()

        except Exception as _ex:
            print("[INFO] error", _ex)
        finally:
            if connection:
                connection.close()
                print("[INFO] Succesful added")


# try:
#     connection = psycopg2.connect(
#         host=host, user=user, password=password, database=db_name
#     )

#     with connection.cursor() as cursor:
#         cursor.execute("SELECT * FROM supplier")

#         print(cursor.fetchone())

# except Exception as _ex:
#     print("[INFO] error", _ex)
# finally:
#     if connection:
#         connection.close()
#         print("[INFO] PostgreSQL connection closed")
