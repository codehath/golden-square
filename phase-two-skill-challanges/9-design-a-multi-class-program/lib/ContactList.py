class ContactList():
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
    
    def extract(self, diary_entry):
        # numbers always start with a hash(#). Example - #00000000000
        words = diary_entry.split()
        number = [word for word in words if word[0] == "#"]
        if len(number) != 0:
            number = number[0][1:]
            self.add(number)