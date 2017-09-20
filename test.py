import psycopg2
import sys

con = None
con = psycopg2.connect("dbname='postgres' user='postgres'")
cur = con.cursor()
cur.execute("INSERT INTO Packages VALUE(1, 'adfa', 'asdf', 123, 126345)")
con.commit()
 
