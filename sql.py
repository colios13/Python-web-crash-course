# Python crash course
# https://www.youtube.com/watch?v=WNvxR8RFzBg&list=WL&index=58

# SQL part

import sqlite3

connect = sqlite3.connect('data.db')

connect.execute("DROP TABLE IF EXISTS CUSTOMER")
connect.execute('''CREATE TABLE CUSTOMER
                     (ID INT PRIMARY KEY NOT NULL,
                      NAME TEXT NOT NULL,
                      AGE INT NOT NULL);''')

connect.execute("INSERT INTO CUSTOMER (ID, NAME, AGE) VALUES (1, 'John',15)")
connect.execute("INSERT INTO CUSTOMER (ID, NAME, AGE) VALUES (2, 'Eva',16)")

customer_row = connect.execute("SELECT * FROM CUSTOMER")

for customer in customer_row:
    print(customer)

connect.close()

