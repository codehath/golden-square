# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

```
See miro board
```
``
```python

class Diary:

    def __init__(self):
        # my_special_diary
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Side-effects:
        #   Adds the entry to the diary property of the self object
        pass # No code here yet

class DiaryEntry:

    def __init__(self, title, content):
        # Parameters:
        #   title: string
        #   content: string
        # Side-effects:
        #   Sets the title and content properties
        pass # No code here yet

class CalculateEntry:

    def __init__(self, wpm, speed):
        # Parameters:
        #   wpm: integer
        #   speed: integer
        # Side-effects:
        #   None, but searches entries via diary
        # Returns:
        #   Most appropriate diary entry based on wpm and speed
        pass # No code here yet

class NumbersList:

    def __init__(self):
        # Parameters:
        #   None
        # Side-effects:
        #   None, but searches entries via diary
        # Returns:
        #   List of phone numbers and contacts assuming format of 'number: name'
        pass # No code here yet

class TodoList:

    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   task: an instance of Task
        # Side-effects:
        #   Adds the task to the todo_list property of the self object
        pass # No code here yet

class Task:

    def __init__(self, job):
        # Parameters:
        #   task: string
        # Side-effects:
        #   Sets the task properties
        pass # No code here yet


```
## 3. Create Examples as Integration Tests

```python
"""
Description
"""
"""
1 Given a diary
When we add a diary entry
And see that entry in the diary
"""
diary = Diary()
entry = DiaryEntry('Date 1', 'Dear diary 1')
diary.add(entry)
assert diary.my_special_diary == entry
"""
2 Given a diary
When we add some diary entries
Return best diary entry for wpm and minutes
"""
diary = Diary()
calc = CalculateEntry()
# find diary generator from working with Troy
diary.add(all entries generated)
result = calc(wpm, speed)
assert result == entry

"""
3 Given a diary
When we add some diary entries
Return list of phone numbers and contacts
"""
diary = Diary()
lst = NumbersList()
# find diary generator from working with Troy
diary.add(all entries generated)
result = lst()
assert result == [lst of entries]
"""
Given a task
When we can add it to the todo list
Return list of all tasks
"""
todolist = TodoList()
todolist.add('Task')
assert todolist.history = ['Task']

```
## 4. Create Examples as Unit Tests
```python

"""
Given a class
We can see that it initialises
"""
actual = Class()
assert isinstance(actual, Class)
"""
Given a diary entry
We can see its title and contents
"""
entry = DiaryEntry('Day 1', 'Content 1')
entry.title # => 'Day 1'
entry.content # => 'Content 1'

"""
Given a task
We can see its body
"""
task = Task('Do a thing')
task.job # => 'Do a thing'
```


## 5. Implement the Behaviour

```python

```