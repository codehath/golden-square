# Food Ordering System Design Recipe

## 1. Describe the Problem

> As a customer  
> So that I can check if I want to order something  
> I would like to see a list of dishes with prices.
> 
> As a customer  
> So that I can order the meal I want  
> I would like to be able to select some number of several available dishes.
> 
> As a customer  
> So that I can verify that my order is correct  
> I would like to see an itemised receipt with a grand total.

Use the `twilio-python` package to implement this next one. You will need to use
mocks too.

> As a customer  
> So that I am reassured that my order will be delivered on time  
> I would like to receive a text such as "Thank you! Your order was placed and
> will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

```python
class OrderSystem:

    def __init__(self):
        pass

    def take_order(self):
        # Side-effects:
        #   Receive order from customer
        pass
    
    def place_order(self, order):
        # Parameters:
        #   order: a 
        # Side-effects:
        #   Place the order
        pass

class Order:

    def __init__(self, title, content):
        # Side-effects:
        #   Sets dishes_ordered and order_placed class attributes
        pass

    def receipt(self):
        # Returns:
        #   Itemised Receipt
        pass
    
    def order_placed_text():
        # Returns:
        #   Boolean for whether order was placed successfully
        #Side-effects:
        #   Sends text to customer
        pass


class Dish:

    def __init__(self, name, price):
        # Parameters:
        #   name: string
        #   price: float
        # Side-effects:
        #   Sets class attributes
        pass

class Menu:

    def display_menu(self):
        # Returns
        #   A list of strings in format "Dish Name - Price"

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