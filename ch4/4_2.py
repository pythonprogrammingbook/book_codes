def person_info(first_name, family_name, weight, height, age=25):
    bmi = weight / height**2
    info = "{0:s}.{1:s} is {2:d} years old, bmi:{3:.2f}."\
        .format(first_name, family_name, age, bmi)
    return info

alex_info = person_info(first_name='Alex',
                        family_name='Lee',
                        height=1.82,
                        weight=75)
print(alex_info)

