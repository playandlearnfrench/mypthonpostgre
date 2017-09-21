#!/usr/bin/python
import psycopg2
conn = psycopg2.connect(database="oinam", user = "oinam", password = "oinam", host = "127.0.0.1", port = "5432")
print ("Opened database successfully");
cur = conn.cursor()
cur.execute('SELECT id, name, address, salary FROM mycompany')
rows = cur.fetchall()
for row in rows:
   print("Hi");
   print ("ID = ", row[0]);
   print ("NAME = ", row[1]);
   print ("ADDRESS = ", row[2]);
   print ("SALARY = ", row[3], "\n");
print("Operation done successfully");
conn.close()
