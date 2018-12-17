import psycopg2, sys

class PostgreSQL:

    def ConnectToDB(self, user, password, host, port, database, ToExecute):

        # Connect to Database
        try:
            connection = psycopg2.connect(user = user,
                                        password = password,
                                        host = host,
                                        port = port,
                                        database = database)
            cursor = connection.cursor()

            # Print PostgreSQL Connection properties
            print ( connection.get_dsn_parameters(),"\n")

            # Pass Request
            cursor.execute(ToExecute)
            record = cursor.fetchmany()
            print("You are connected to - ", record,"\n")

        except (Exception, psycopg2.Error) as error :

            if(connection):
                connection.rollback()


        # Disconnect from DB
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")