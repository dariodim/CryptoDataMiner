import psycopg2, sys

class PostgreSQL():

    def ConnectToDB(self, user, password, host, port, database, ToExecute):

        # Connect to Database
        try:
            # Create Connection to DB
            connection = psycopg2.connect(user = user,
                                        password = password,
                                        host = host,
                                        port = port,
                                        database = database)
            # Connect to DB
            cursor = connection.cursor()

            # Log Connection Details
            print("Connected to ",connection.get_dsn_parameters(),"\n")

            # Log Request Pre-Execution
            print("Ready to execute ",ToExecute,"\n")

            # Execute Request
            cursor.executemany(ToExecute)
            
            # Log Request Post-Execution
            print("Executed ",ToExecute,"\n")

            # Get Request Reply
            record = cursor.fetchmany()
            
            # Log Request Reply
            print("Execution Reply ", "\n", record,"\n")

        except (Exception, psycopg2.Error) as error :
            
            # Log Request Post-Execution
            print("Rolling Back - Error with Execution Request ",ToExecute,"\n")

            # Roll-Back Table to DB-state
            if(connection):
                connection.rollback()


        # Disconnect from DB
        if(connection):

            # Log Disconnection Request from DB
            print("Disconnecting from ",connection.get_dsn_parameters(),"\n")

            cursor.close()
            connection.close()
            
            # Log Disconnection from DB Success
            print("Disconnection Successful","\n")