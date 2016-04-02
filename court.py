__author__ = 'Courtenay'

your_task = """
ask for a name, print out their phone number
>> addresses = {
      "josh" : "110 stewart",
      "matt" : "220 concession"
      }
   print addresses['josh']
   >>> 110 stewart
"""
response = raw_input("whose number")

numbers = {
    "josh" : 8639587,
    "courtenay" : 82394860
}
while response not in numbers:
    print "name not found?"
    response = raw_input("whose number")

print numbers[response]




# my_variable = True
#
# while my_variable:
#     print "ASDAD"
#     my_variable = False













