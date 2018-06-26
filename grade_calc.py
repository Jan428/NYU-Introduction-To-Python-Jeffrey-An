grade = input('What is your grade? \n')
final_grade = int(grade)

if 90 <= final_grade:
    print('You got an A')
elif 80 <= final_grade:
    print('You got a B')
elif 70 <= final_grade:
    print('You got a C')
elif 60 <= final_grade:
    print('You got a D')
elif 60 > final_grade:
    print('You failed!!!')
