import sys
from psycopg2 import connect
from psycopg2 import OperationalError, errorcodes, errors
from collections import defaultdict

def get_database_connection(host,port,database,username,password):
    #connect to the db
    con = None
    error = None
    try:
        con = connect(
                    host = host,
                    database = database,
                    user = username,
                    port = port,
                    password = password)
    except OperationalError as err:
        error = err
    return con,error

def calculate_savings(events,context):
    
    result = {}
    try:
        con,err = get_database_connection(events["host"],events["port"],events["database"],events["username"],events["password"])
        if con !=None:
            #cursor
            cur = con.cursor()
            fetch_query = "SELECT T.txn_type,T.txn_amount,C.customer_id,date_part('year',AGE(C.date_of_birth)),date_part('month',AGE(C.date_of_birth)) FROM Transactions T INNER JOIN Customer C ON T.customer_id = C.customer_id WHERE transaction_date = (%s)::date"
            data = (events["date"],)
            try:
                cur.execute(fetch_query,data)
                rows = cur.fetchall()
                
            except Exception as err:
                # pass exception to function
                result["statusCode"] = 400
                result["message"] = err
            finally:
                cur.close()
                con.close()
        else:
            result["statusCode"] = 400
            result["message"] = err
    except Exception as err:
        result["statusCode"] = 400
        result["message"] = err

    return result