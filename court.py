__author__ = 'Courtenay'

your_task = """
create a list of days in the week
>> my_list_of_animals = ['cats', 'dogs']

for each day of the week print out a different thing you're going to do,
like on monday you'll walk the dog, on tuesday you'll go to the gym etc
>> for animal in my_list_of_animals:
     if animal == "dogs":
       print dogs are cute

once you've got that going, you'll make it so it asks you what you want to do
on monday, and then print that along with the preprogrammed stuff

then you'll make it so it asks you the day you want to edit instead of only monday

then you'll make it so it saves it so the next time you start the app, it'll persist what you saved
"""
response_day = raw_input("What day do you want to edit?\n")
response_day = response_day.title()
response_task = raw_input("what do you want to do on %s?" % response_day)

mapped_days = {
    "Monday" : "Go to work",
    "Tuesday" : "walk the dog"
}

days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days_of_the_week:
    print day + ":",

    print mapped_days.get(day, "party hard on %s" % day),

    if day == response_day:
        print response_task
    else:
        print







