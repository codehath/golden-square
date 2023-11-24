from lib.Diary import *
from lib.DiaryEntry import *
from lib.ContactList import *
from lib.Task import *
from lib.TodoList import *

def test_diary_constructor():
    diary = Diary()
    assert diary.entries == []
    assert type(diary.contact_list) == ContactList
    assert type(diary.todo_list) == TodoList

def test_diary_add_1_entry_no_number():
    diary = Diary()
    entry = DiaryEntry('Date 1', 'Dear diary 1')
    diary.add_entry(entry)
    actual = diary.entries
    expected = [entry]
    assert actual == expected
    assert diary.contact_list.numbers == []

def test_diary_add_1_entry_extract_number():
    diary = Diary()
    entry = DiaryEntry('Date 1', 'Today i called the bank #07972876521')
    diary.add_entry(entry)
    actual = diary.entries
    expected = [entry]
    assert actual == expected
    assert diary.contact_list.numbers == ['07972876521']

def test_diary_add_4_entries():
    diary = Diary()
    test_entries = []
    for i in range(4):
        entry = DiaryEntry(f'Title {i + 1}', f'Contents {i + 1} ' * (i + 1))
        diary.add_entry(entry)
        test_entries.append(entry)
    actual = diary.entries
    expected = test_entries
    assert actual == expected
    assert diary.contact_list.numbers == []

def test_diary_add_4_entries_extract_2_numbers():
    diary = Diary()
    diary_entry_1 = DiaryEntry('Title', "Today i called the bank")
    diary_entry_2= DiaryEntry('Title', "Today i called the bank #07972876521")
    diary_entry_3 = DiaryEntry('Title', "Today i called the dentist")
    diary_entry_4= DiaryEntry('Title', "Today i called the library #07972876156")
    diary.add_entry(diary_entry_1)
    diary.add_entry(diary_entry_2)
    diary.add_entry(diary_entry_3)
    diary.add_entry(diary_entry_4)
    actual = diary.entries
    expected = [diary_entry_1, diary_entry_2, diary_entry_3, diary_entry_4]
    assert actual == expected
    assert diary.contact_list.numbers == ['07972876521', '07972876156']

def test_diary_past_entries():
    diary = Diary()
    test_entries = []
    for i in range(2):
        entry = DiaryEntry(f'Title {i + 1}', f'Contents {i + 1} ' * (i + 1))
        diary.add_entry(entry)
        test_entries.append(f'Title {i + 1}: ' + f'Contents {i + 1} ' * (i + 1))
    actual = diary.past_entries()
    expected = test_entries
    assert actual == expected

# def test_diary_return_best_entry_for_wpm_and_minutes():
#     diary = Diary()
#     calc = CalculateEntry()
#     for i in range(8):
#         diary.add(DiaryEntry(f'Title {i + 1}', f'Contents {i + 1} ' * (i + 1)))
#     result = calc.extract(2,2)
#     actual = result
#     expected = ['Contents 4 Contents 4 Contents 4 Contents 4 ']
#     assert actual == expected


def test_display_numbers():
    diary = Diary()
    diary_entry_1 = DiaryEntry('Title', "Today i called the bank")
    diary_entry_2= DiaryEntry('Title', "Today i called the bank #07972876521")
    diary_entry_3 = DiaryEntry('Title', "Today i called the dentist")
    diary_entry_4= DiaryEntry('Title', "Today i called the library #07972876156")
    diary.add_entry(diary_entry_1)
    diary.add_entry(diary_entry_2)
    diary.add_entry(diary_entry_3)
    diary.add_entry(diary_entry_4)

    actual = diary.entries
    expected = [diary_entry_1, diary_entry_2, diary_entry_3, diary_entry_4]
    assert actual == expected
    assert diary.display_numbers() == ['07972876521', '07972876156']


def test_entries_to_read_return_one_entry():
    diary = Diary()
    for entry in range(1, 4):
        diary.add_entry(DiaryEntry(f'Title {entry}', "Content " * entry))
        if entry == 2:
            expected = [diary.entries[-1]]

    actual = diary.entries_to_read(1, 2)
    assert actual == expected

def test_entries_to_read_return_two_entries():
    diary = Diary()
    expected = []
    for entry in range(1, 4):
        diary.add_entry(DiaryEntry(f'Title {entry}', "Content " * entry))
        if entry == 2:
            expected.append(diary.entries[-1])
        if entry == 3:
            expected.insert(0, diary.entries[-1])

    actual = diary.entries_to_read(1, 5)
    assert actual == expected

def test_entries_to_read_return_three_entries():
    diary = Diary()
    expected = []
    diary_entry_1 = DiaryEntry('Title 5', "Today I called the bank")
    diary_entry_2= DiaryEntry('Title 14', "Today I brushed my teeth and then ate bread, I was a bad boy.")
    diary_entry_3 = DiaryEntry('Title 11', "Dear Diary i called the dentist today i called the dentist")
    diary_entry_4= DiaryEntry('Title 17', "Today i called the library #07972876156 Today i called the library #07972876156Today i called the library #07972876156")
    diary.add_entry(diary_entry_1)
    diary.add_entry(diary_entry_2)
    diary.add_entry(diary_entry_3)
    diary.add_entry(diary_entry_4)

    expected = [diary_entry_4, diary_entry_2, diary_entry_1] 
    actual = diary.entries_to_read(6, 6)
    assert actual == expected