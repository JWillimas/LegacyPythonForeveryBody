def sum(a,b):
    return (a+b)



# medical_records=[
#     {
#         'patient_id':"p12333",
#         'age': 34,
#         'gender': 'female',
#         'diagnosis': 'Hypertension',
#         'medications': ['Lisinopril'],
#         'last_visit_id': 'V2301',
#     },
#     {
#         'patient_id': 'p1002',
#         'age': 47,
#         'gender': 'male',
#         'diagnosis': 'Type 2 Diabetes',
#         'medications': ['Metformin', 'Insulin'],
#         'last_visit_id': 'v2302',
#     },
#     {
#         'patient_id': 'P1003',
#         'age': 29,
#         'gender': 'female',
#         'diagnosis': 'Asthma',
#         'medications': ['Albuterol'],
#         'last_visit_id': 'v2303',
#     },
#     {
#         'patient_id': 'p1004',
#         'age': 56,
#         'gender': 'Male',
#         'diagnosis': 'Chronic Back Pain',
#         'medications': ['Ibuprofen', 'Physical Therapy'],
#         'last_visit_id': 'V2304',
#     }
# ]

# [print(key,value) for key,value in medical_records[0] ]

# print(medical_records[0],'\n')

# print(medical_records[0].items(),'\n')

# print(type(medical_records[0].items()),'\n')

# import re
# print(re.fullmatch('female'or'male','male',re.IGNORECASE))

# key_set=set(
#         ['patient_id','age','gender','diagnosis',
#         'medications','last_visit_id']
#         )

# dictionary={'patient_id': 'p1004',
#         'age': 56,
#         'gender': 'Male',
#         'diagnosis': 'Chronic Back Pain',
#         'medications': ['Ibuprofen', 'Physical Therapy'],
#         'last_visit_id': 'V2304'}


# print(type(key_set))
# print(type(dictionary.keys()))
# print(type(set(dictionary.keys())))
# print(dictionary.keys())



# pizza = dict([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250), ('toppings', ['mozzarella', 'basil'])])
# print(pizza)
# print(type(pizza))
# print(type(pizza.items()))

# pizza=('name', 'Margherita Pizza')

# print('name' in pizza )

#8.What is a view object?
#Which of the following built-in modules is used for generating random numbers?

settings={
     "theme": "light",
     "the": "lig"
}

del settings["the"]
print(settings)


settings={
     "theme": "light",
     "the": "lig"
}

settings.remove("the")
print(settings)
