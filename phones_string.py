number = input('What is your phone number \n')
areacode = number[0:3]
rest = number [3:11]
new_number =input('({}){}'.format(areacode, rest))
print(new_number)
