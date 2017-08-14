import psycopg2
import sys

if len(sys.argv) >3 or len(sys.argv) <2:
	sys.exit("wrong number of arguments. Requires two command line arguments")
try:
	arg1 = int(sys.argv[1])
	arg2 = int(sys.argv[2])
except:
	sys.exit("cannot convert one or more integers")


conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute("SELECT word, count from tweetwordcount where count>=%s and count<=%s",(sys.argv[1],sys.argv[2]))
records = cur.fetchall()
if records:
	for rec in records:
		print "{}: {}".format(rec[0],rec[1])
