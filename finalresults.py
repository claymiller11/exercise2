import psycopg2
import sys

if len(sys.argv) >2:
	sys.exit("too many arguments. one word only")

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) == 2:
	cur.execute("SELECT word, count from tweetwordcount where word=%s",(sys.argv[1],))
	records = cur.fetchone()
	if records:
		print "Total number of occurences of \"{}\": {}".format(records[0], records[1]) 
	else:
		print "\"{}\" is not in the tweetwordcount table".format(sys.argv[1])


elif len(sys.argv) == 1:
	cur.execute("SELECT word, count FROM tweetwordcount ORDER BY word")
	records = cur.fetchall()
	for rec in records:
		print rec

