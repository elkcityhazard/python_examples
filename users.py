class User():
    """Define a set of values that make up a user."""
    def __init__(self, first_name, last_name, username, email_address, password):
        """initialize attibutes to describe the user details."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email_address = email_address
        self.password = password

    def describe_user(self):
        """Describe the user."""
        full_name = self.first_name + ' ' + self.last_name
        credentials = self.username + ' - ' + self.email_address + ' - ' + self.password
        return full_name.title() + ' | ' + credentials




    def greet_user(self):
        """print a greeting to the user."""
        full_name = self.first_name + ' ' + self.last_name + '.'
        return "\n\tHello, " + full_name.title() + '!'


user_1 = User('andrew', 'mccall', 'elkcityhazard', 'andrew.m.mccall@punchmyface.com', 'xxxxxxx')
user_2 = User('elizabeth', 'the girlfriend', 'e_bohnhorst', 'elizabethbohnhorst@gkickmyneck.com', 'xxxxxxx')
user_3 = User('omar', 'the dog', 'omar_the_dog', 'omar@wag.com', 'omarlikesbonez')
print(user_1.describe_user())
print(user_1.greet_user())

print('\n' + user_2.describe_user())
print(user_2.greet_user())

print('\n' + user_3.describe_user())
print(user_3.greet_user())
