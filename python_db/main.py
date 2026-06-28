import sys
import pathlib
from Python_DB import task_handler as th
from Printer_Control import print_task as pt

#th.create_task()
task_json = th.get_all_tasks()
task = task_json[0][1]
print(task)
pt.print_task_by_id(task)
#pt.print_task_by_id("1")
#th.move_task("1")
#th.create_task()
#th.remove_task("2")
#th.move_task_to_completed("3")
#th.move_task_to_todo("3")
