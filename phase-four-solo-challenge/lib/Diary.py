from lib.DiaryEntry import *
from lib.ContactList import *
from lib.Task import *
from lib.TodoList import *

class Diary():
    def __init__(self):
        self.entries = []
        self.todo_list = TodoList()
        self.contact_list = []

    def add_entry(self, entry):
        self.entries.append(entry)
        self.contact_list.extract(entry.content)
    
    def past_entries(self):
        past_entries = []
        for entry in self.entries:
            past_entries.append(f"{entry.title}: {entry.content}")
            print(past_entries[-1])
        return past_entries
    
    def display_numbers(self):
        for number in self.contact_list.numbers:
            print(number)
        return self.contact_list.numbers

    def entries_to_read(self, time, wpm):
        max_words = time*wpm
        return_entries = []        
        all_entries = {len(entry.content.split()): entry for entry in self.entries}

        while len(all_entries) > 0 and max_words >= min(all_entries.keys()):
            all_entries = {words: entry for words, entry in all_entries.items() if words <= max_words}
            longest_length = max(all_entries.keys())
            return_entries.append(all_entries.pop(longest_length))
            max_words -= longest_length

        return return_entries
