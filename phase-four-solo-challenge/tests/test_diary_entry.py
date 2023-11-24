from lib.DiaryEntry import *

def test_diary_entry_constructor():
    entry = DiaryEntry('Day 1', 'Contents of Diary')
    assert entry.title == 'Day 1'
    assert entry.content == 'Contents of Diary'