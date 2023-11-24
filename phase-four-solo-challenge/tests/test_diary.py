from lib.Diary import *

def test_diary_constructor():
    diary = Diary()
    assert diary.entries == []
    assert type(diary.contact_list) == ContactList
    assert type(diary.todo_list) == TodoList
