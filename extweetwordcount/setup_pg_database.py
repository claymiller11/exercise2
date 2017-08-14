import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(database="postgres", user="postgres",
password = "pass", host = "localhost", port="5432")

try:
	conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cur=conn.cursor()
	cur.execute("CREATE DATABASE tcount")
	cur.close()
	conn.close()
except:
	print "Could not create tcount"

conn = psycopg2.connect(database="tcount", user="postgres",
password = "pass", host = "localhost", port="5432")

#Createa a Table
cur = conn.cursor()
cur.execute('''CREATE TABLE tweetwordcount (word TEXT PRIMARY KEY     NOT NULL, count INT     NOT NULL);''')
conn.commit()


