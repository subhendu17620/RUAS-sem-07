class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

human_obj = Human("Virat", "Kohli")

print(isinstance(human_obj, Human))# Output: True

# As object is the base class for all the class hence
# isinstance(human_obj, object) is True
print(isinstance(human_obj, object))# Output: True
