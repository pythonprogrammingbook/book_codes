def person_info(first_name, family_name, age, weight, height):
    bmi = weight / height**2
    info = "{0:s}.{1:s} is {2:d} years old, bmi:{3:.2f}."\
        .format(first_name, family_name, age, bmi)
    return info

#参数传递方式：位置参数
michael_info = person_info('Michael', 'Jackson', 17, 70.4, 1.75)
print(michael_info)


#参数传递方式：关键字参数
alex_info = person_info(first_name='Alex', family_name='Lee',
                        height = 1.82, weight = 75, age = 25)
print(alex_info)


