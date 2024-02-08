"""
Create Email class.
Create static variable called inbox and assign empty list to it.
create another static variable called has_been_read and
    provide initial value to False.
"""

import sys


class Email:
    """This class is about Email simulator."""
    inbox = []
    has_been_read = False
    spam = []
    delete = []

# Create consrtructor and provide 3 parameters.

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

# Create instance method mark_as_read and initialise its value to True.
    def mark_as_read(self):
        self.has_been_read = True

# create class method called populate_inbox which will add value to inbox list.
    @classmethod
    def populate_inbox(cls, email_obj):
        cls.inbox.append(email_obj)

# Create class method lists_emails which will provide subject_line with index.

    @classmethod
    def lists_emails(cls):
        for index, obj in enumerate(Email.inbox):
            print(index, obj.subject_line)

# craete class method called read_emails which provide
#   email object(email_address, subject_line, email_content) and
#   provide mark_as_read value to True.

    @classmethod
    def read_email(cls, email_index):
        email_object = Email.inbox[email_index]
        print()
        email_details = f"From: {email_object.email_address}\n"
        email_details += f"Subject: {email_object.subject_line}\n"
        email_details += f"Content: {email_object.email_content}"
        print(email_details)
        print()
        email_object.mark_as_read()
        print("-" * 50)
        print(f"Email from: {email_object.email_address} marked as read.")
        return email_object


email1 = Email("charlietheone@gmail.com", "Greeting", "How are you?")
email2 = Email("john123@yahoo.co.in", "new registration",
               "Welcome to HyperionDev John!!")
email3 = Email("pythondeveloper@microsoft.com", "Learning Python",
               "Functions and OOP")
Email.populate_inbox(email1)
Email.populate_inbox(email2)
Email.populate_inbox(email3)

print()
user_name = input("Please enter your name:")
print()
print(f"Hello {user_name}, welcome to your email inbox.".upper())

"""
create while loop for user menu.
Using if else conditional statement write logic.
"""

while True:
    print()
    user_menu = input("""Please select option from below:
            1. Read an email
            2. View unread emails
            3. Quit application
            : """)

# If user select 1 which is read an email, it should provide list of emails
#    with subject_line to choose from which email user wants to read.
# After reading an email user gets options to whether mark email as spam
#    or delete an email or leave as it is.

    if user_menu == "1":
        print("This is a list of your emails:")
        Email.lists_emails()
        print()
        user_option = "Which email do you want to read? please enter "
        user_option += "number from above or press -1 to go back to main menu:"
        while True:
            try:
                user_email_option = int(input(user_option))
                if user_email_option == -1:
                    print("Taking you to a main menu.")
                    break
                elif user_email_option not in range(len(Email.inbox)):
                    print("Please select valid index")
                else:
                    print()
                    print("Here is your email:".upper())
                    print("-" * 50)
                    current_object = Email.read_email(user_email_option)
                    print("-" * 50)
                    s_d_message = "Do you want to mark this email as spam "
                    s_d_message += "or do you want to delete this email? "
                    s_d_message += "please select (y/n):"
                    while True:
                        spam_delete_option = input(s_d_message).lower()
                        if spam_delete_option == "y":
                            while True:
                                try:
                                    s_d = "Please select option from below:"
                                    s_d += "\n1. spam\n2. delete\n:"
                                    spam_delete = int(input(s_d))
                                    if spam_delete not in [1, 2]:
                                        print("Please enter valid index")
                                    else:
                                        break
                                except Exception:
                                    print("Please enter valid input")

                            if spam_delete == 1:
                                Email.spam.append(current_object)
                                Email.inbox.remove(current_object)
                                print("Email from " +
                                      f"{current_object.email_address} " +
                                      "marked as spam.")

                            elif spam_delete == 2:
                                Email.delete.append(current_object)
                                Email.inbox.remove(current_object)
                                print("Email from " +
                                      f"{current_object.email_address} " +
                                      "deleted.")
                            break
                        elif spam_delete_option == "n":
                            print()
                            print("Taking you to a main menu")
                            break
                        else:
                            print("Please enter (y or n) to continue")
                    break
            except Exception:
                print("Please enter a valid option.")

# If user select 2 it should provide list of unread emails.

    elif user_menu == "2":
        email_statuses = {}
        print("Here is the list of unread email:")
        for index, obj in enumerate(Email.inbox):
            if obj.has_been_read is False:
                print(index, obj.subject_line)
            else:
                email_statuses[index] = obj.has_been_read
        try:
            if (email_statuses[0] is True and email_statuses[1] is True
                    and email_statuses[2] is True):
                print("There are no unread emails in your inbox.")
        except Exception:
            pass

# If user selects 3 the programme shoulde terminate.

    elif user_menu == "3":
        print("Good Bye, Thank you for using Email simulator.")
        sys.exit(0)
    else:
        print("Please enter valid input.")
