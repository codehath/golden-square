from lib.ContactList import *

def test_contact_list_constructor():
    contacts = ContactList()
    assert contacts.numbers == []

def test_contact_list_add_1():
    contacts = ContactList()
    contacts.add("07972876521")

    actual = contacts.numbers
    expected = ["07972876521"]
    assert actual == expected

def test_contact_list_add_3():
    contacts = ContactList()
    contacts.add("07972876521")
    contacts.add("07972876522")
    contacts.add("07972876523")

    actual = contacts.numbers
    expected = ["07972876521", "07972876522", "07972876523"]
    assert actual == expected

def test_contact_list_extract():
    contacts = ContactList()
    diary_entry = "Today i called the bank #07972876521"
    contacts.extract(diary_entry)

    actual = contacts.numbers
    expected = ["07972876521"]
    assert actual == expected

def test_contact_list_extract_no_number_entry():
    contacts = ContactList()
    diary_entry = "Today i called the bank"
    contacts.extract(diary_entry)

    actual = contacts.numbers
    expected = []
    assert actual == expected

def test_contact_list_extract_some_entries_have_numbers():
    contacts = ContactList()
    diary_entry_1 = "Today i called the bank"
    diary_entry_2= "Today i called the bank #07972876521"
    diary_entry_3 = "Today i called the dentist"
    diary_entry_4= "Today i called the library #07972876156"
    contacts.extract(diary_entry_1)
    contacts.extract(diary_entry_2)
    contacts.extract(diary_entry_3)
    contacts.extract(diary_entry_4)

    actual = contacts.numbers
    expected = ["07972876521", "07972876156"]
    assert actual == expected