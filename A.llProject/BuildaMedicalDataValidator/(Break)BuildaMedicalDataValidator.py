#Medical Data Validator
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------

import re


medical_records=[
    {
        'patient_id':"p12333",
        'age': 34,
        'gender': 'female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

#---------------------------------------------------------------------
#Question 2 :Learning this new way to Validate the Values of 
#Given Data;

#1. Syntax of regular express function
#2. Use it again



def fine_invalid_record(patient_id,age,gender,
        diagnosis,medications,last_visit_id):
    
    Constraints={
        'patient_id': isinstance(patient_id,str)
        and re.fullmatch('p\\d+',patient_id,re.IGNORECASE),

        'age':isinstance(age,int)and(age>=18),

        'gender':re.fullmatch(r'female|male',gender,re.IGNORECASE),

        'diagnosis':isinstance(diagnosis,str),

#---------------------------------------------------------------------
#Question 4: how to use the isinstance inside of list's str
#such as : 'medications' : [("dwdwdw",'qwdwdw')]
#use  #Iterable comprehensive #

        'medications':isinstance(medications,list)
        and all([isinstance(i,str) for i in medications]),
        #for example:Here the medications= ['Metformin', 'Insulin']

#---------------------------------------------------------------------

        'last_visit_id':isinstance(last_visit_id,str)and
        re.fullmatch('v\\d+',last_visit_id,re.IGNORECASE)
    }


#---------------------------------------------------------------------
#Warning 5:when you iterate over a dictionary 
#without calling .items(), Python only gives you the keys

    return [key for key,value in Constraints.items()  if not value]

#---------------------------------------------------------------------------



def validate(data):
    is_sequence=isinstance(data,(list,tuple))

    if not is_sequence:
        print('Invalid format: expected a list or tuple.')#lack of warning information
        return False
    
    is_invalid=False

    key_set=set(
        ['patient_id','age','gender','diagnosis',
        'medications','last_visit_id']
        )#Use set function to build a set contain all the key

    for index,dictionary in enumerate(data):
        if not isinstance(dictionary,dict):
            is_invalid=True
            continue

#----------------------------------------------------------------
#Question1: how to use key_set in if ?


            # key_set=set(
            #         ['patient_id','age','gender','diagnosis',
            #         'medications','last_visit_id'])
            #    Way to build a set

        if set(dictionary.keys())!=key_set:
            print(
                f'Invalid format:{dictionary}at position {index} \
                has missing and/or invalid keys'
            )
            is_invalid=True
            continue
 #------------------------------------------------------------------       
 #------------------------------------------------------------------       
#Warning3:how to use the **dictionary to get the value from 
#dict that make code more clearer

        invalid_records=fine_invalid_record(**dictionary)
        for key in invalid_records:
            val=dictionary[key]
            print(f"The '{key}:{val}' in the dictionary at position {index}")
            is_invalid=True
 #------------------------------------------------------------------       

    if is_invalid:
        return False
    
    print("Value Format")
    return True


validate(medical_records)
