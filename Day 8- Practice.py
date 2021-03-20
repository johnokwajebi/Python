# Day 8 30days of Python- Dictionaries

person = {
    'first_name':'John',
    'last_name':'Okwajebi',
    'age':26,
    'country':'Nigeria',
    'is_marred':False,
    'skills':['Python', 'SQL', 'Excel', 'Tableau'],
    'address':{
        'street':'Bakin Uza',
        'zipcode':'900211'
    }
    }
person['job_title'] = 'Data Entrepreneur'
person['skills'].append('Communication Skills')


dog = {}
dog['Name'] = 'Coco'
dog['Color'] = 'Brown'
dog['Breed'] = 'Caucasian Mix'
dog['Legs'] = 'Long'
dog['age'] = 1

student = dict()
student['first_name'] = 'John'
student['last_name'] = 'Okwajebi'
student['gender'] = 'Male'
student['age'] = 26
student['marital_status'] = 'Single'
student['skills'] = ['Python', 'Excel', 'SQL', 'Tableau']
student['country'] = 'Nigeria'
student['city'] = 'Abuja'
student['address'] = {'Street':'Bakin Uza', 'Zipcode':900211}
print(type(student['skills']))

student['skills'].append('SEO')
print(student.keys())
print(student.values())
print(student.items())
student.pop('marital_status')
