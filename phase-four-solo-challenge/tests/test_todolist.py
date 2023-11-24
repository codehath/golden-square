from lib.TodoList import *
from lib.Task import *

def test_todolist_constructor():
    todolist = TodoList()
    assert todolist.taskstodo == []

def test_todolist_add_1():
    todolist = TodoList()
    task_1 = Task('Go shopping')
    todolist.add(task_1)
    actual = todolist.taskstodo
    expected = [task_1]
    assert actual == expected

def test_todolist_add_3():
    todolist = TodoList()
    task_1 = Task('Go shopping')
    task_2 = Task('Go shopping')
    task_3 = Task('Go shopping')
    todolist.add(task_1)
    todolist.add(task_2)
    todolist.add(task_3)
    actual = todolist.taskstodo
    expected = [task_1, task_2, task_3]
    assert actual == expected