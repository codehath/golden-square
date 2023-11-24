from lib.Task import *

def test_task_constructor():
    task1 = Task('Go shopping')
    assert task1.task == 'Go shopping'