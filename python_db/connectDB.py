import psycopg2

try:
	connection = psycopg2.connect(
	dbname="taskdb",
	user="kyle",
	password="password",
	host="192.168.254.83",
	port="5432"
	)

	cursor = connection.cursor()

	cursor.execute("select * from tasks;")
	output = cursor.fetchall()
	print(output)
except psycopg2.Error as error:
	print("error: ", error)
finally:
	if connection:
		cursor.close()
		connection.close()
		print("psql connection closed...")
