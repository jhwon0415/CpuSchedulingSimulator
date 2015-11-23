import sys
import heapq
from src.mod import *


task = Task()

task.start_time = 10
task.end_time = 20
print(task.get_response_time(), file=sys.stdout)
