import psycopg2

conn = psycopg2.connect(database="oinam", user = "oinam", password = "oinam", host = "127.0.0.1", port = "5432")
print ("Opened database successfully")

cur = conn.cursor()

cur.execute("INSERT INTO MYCOMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Paul', 32, 'California', 20000.00 )");

cur.execute("INSERT INTO MYCOMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Allen', 25, 'Texas', 15000.00 )");

cur.execute("INSERT INTO MYCOMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Teddy', 23, 'Norway', 20000.00 )");

cur.execute("INSERT INTO MYCOMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Mark', 25, 'Rich-Mond', 65000.00 )");

cur.execute("INSERT INTO MYCOMPANY (NAME,AGE,ADDRESS,SALARY) \
      VALUES ('Oinam', 30, 'Bangalore', 25000.00 )");
conn.commit()
print ("Records created successfully");
conn.close()
