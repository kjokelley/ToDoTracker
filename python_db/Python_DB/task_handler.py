import psycopg2
#import inquirer


task_table = "tasks"
completed_task_table = "completed_tasks"
#connection = sqlite3.connect("database.db")
def create_connection():
	connection = psycopg2.connect(
		dbname="taskdb",
		user="kyle",
		password="password",
		host="192.168.254.83",
		port="5432"
	)
	return connection

#task_types = [
#    inquirer.List('type',
#                  message="Task Type: ",
#                  choices=['Hygeine', 'Chore', 'Project', 'Religious'],
#                  ),
#]


#def create_connection():
#    return connection



def create_task():
    try:
        connection = create_connection()
        #connection.autocommit = True
        cursor = connection.cursor()

        print("Task: ")
        task = input()
        type = input()
        print("Priority (scale 1-5): ")
        priority = input()
        new_task = (task, type, False, priority)
        #cursor.execute(
        #    "INSERT INTO tasks (name, type, completed, priority) VALUES (%s, %s, %s, %s);", 
        #    (task, type, False, priority)
        #)
        cursor.execute("insert into tasks (name, type, completed, priority) VALUES (%s, %s, %s, %s);",
        new_task )
        #connection.commit()
        #cursor.execute("select * from token_generator.pg_stat_activity;")
        #print(cursor.fetchone())
        #connection.commit()

    except psycopg2.Error as error:
        print(f"Database error occurred: {error}")

    finally:
        # 10. Always close the connection when finished
        connection.commit()
        cursor.close()
        print("End of insertion")
        connection.close()

def remove_task(task_id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "DELETE FROM tasks WHERE id == ?", 
            task_id
        )
        #task = cursor.fetchone()
        #return task
    except psycopg2.Error as error:
        print(f"Database error occured: {error}")
    finally:
        cursor.close()
        print("End of removal")
        connection.close()

def get_task(task_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE id = (%s);", 
            (task_id,)
        )
        task = cursor.fetchone()
        return task
    except psycopg2.Error as error:
        print(f"Database error occured: {error}")
    finally:
        connection.commit()
        cursor.close()
        print("End of retrieval")
        connection.close()

def set_active_task(task_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE tasks SET active = True WHERE id = (%s);", 
            (task_id,)
        )
        task = cursor.fetchone()
        return task
    except psycopg2.Error as error:
        print(f"Database error occured: {error}")
    finally:
        connection.commit()
        cursor.close()
        print("End of retrieval")
        connection.close()

def set_inactive_task(task_id):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE tasks SET active = False WHERE id = (%s);", 
            (task_id,)
        )
        task = cursor.fetchone()
        return task
    except psycopg2.Error as error:
        print(f"Database error occured: {error}")
    finally:
        connection.commit()
        cursor.close()
        print("End of retrieval")
        connection.close()

def get_all_tasks():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM tasks WHERE completed is false;", 
        )
        tasks = cursor.fetchall()
        return tasks
    except psycopg2.Error as error:
        print(f"Database error occured: {error}")
    finally:
        connection.commit()
        cursor.close()
        print("End of retrieval")
        connection.close()

def swap_task_completion(task_id):
	try:
		cursor = connection.cursor()
		cursor.execute(
			"UPDATE tasks SET completed = NOT completed WHERE id == ?",
			task_id
		)
	except psycopg2.Error as error:
		print(f"Database error occured: {error}")
	finally:
		cursor.close()
		print("End of swap")
		connection.close()
 
"""def move_task_to_completed(task_id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE tasks SET completed = NOT completed WHERE id == ?", 
            task_id
        )
        cursor.execute(
            "SELECT * FROM tasks WHERE id == ?", 
            task_id
        )
        task = cursor.fetchone()
        print(task)
        cursor.execute(
            "INSERT INTO completed_tasks (id, name, type, completed, priority) VALUES (?, ?, ?, ?, ?)",
            task

        )
        print("test1")
        cursor.execute(
            "DELETE from tasks WHERE id == ?",
            task_id
        )
        print("test2")
        #task = cursor.fetchone()
        #return task
    except sqlite3.Error as error:
        print(f"Database error occured: {error}")
    finally:
        connection.commit()
        print("End of moving")
        connection.close()"""


"""def move_task_to_todo(task_id):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE completed_tasks SET completed = NOT completed WHERE id == ?", 
            task_id
        )
        cursor.execute(
            "SELECT * FROM completed_tasks WHERE id == ?", 
            task_id
        )
        task = cursor.fetchone()
        print(task)
        cursor.execute(
            "INSERT INTO tasks (id, name, type, completed, priority) VALUES (?, ?, ?, ?, ?)",
            task

        )
        print("test1")
        cursor.execute(
            "DELETE from completed_tasks WHERE id == ?",
            task_id
        )
        print("test2")
        #task = cursor.fetchone()
        #return task
    except sqlite3.Error as error:
        print(f"Database error occured: {error}")
    finally:
        connection.commit()
        print("End of moving")
        connection.close()"""
