"""

Start

Ask participants how much time they have taken to complete swimming
    and store them in a variable.
Ask participants how much time they have taken to complete cyclig and
    store them in a variable.
Ask participants how much time they have taken to complete running and
    store them in a variable.
Create a variable, add swimming, cycling and running time and store its value
     and then print added value.
Use if, elif conditional statement, and decide award for each participants.
Qualifying time for award is 100 minutes.
so, If total time is in range of 0-100 minutes, print "You have won
    Provincial Colours Award".
If total time is in range of 101-105 minutes, print "You have won
     Provincial Half Colours Award".
If total time is in range of 106-110 minutes, print "You have won
     Provincial Scroll Award".
If total time is greater or equal to 111 minutes, print
    "Sorry, you are not qualify for Award."

End

"""

swimming_time_in_minutes = \
    int(input("How many minutes have you taken to complete swimming?"))

cycling_time_in_minutes = \
    int(input("How many minutes have you taken to complete cycling?"))

running_time_in_minutes = \
    int(input("How many minutes have you taken to complete running?"))

triathlon_total_time = swimming_time_in_minutes + cycling_time_in_minutes
+ running_time_in_minutes
print("You have taken total {} minutes to complete triathlon."
    .format(triathlon_total_time))


if triathlon_total_time in range(0, 101):
    print("You have won Provincial Colours Award.")
elif triathlon_total_time in range(101, 106):
    print("You have won Provincial Half Colours Award.")
elif triathlon_total_time in range(106, 111):
    print("You have won Provincial Scroll Award.")
elif triathlon_total_time >= 111:
    print("Sorry, you are not qualify for Award.")
