#Day 5 30 days of python challenge

lst = list()
lst_ = ['John','Grace','Godwin','Mary','Ann']
print(len(lst_))
print(lst_[0])
print(lst_[2])
print(lst_[-1])

mixed_data_types = ['John', '26', 'Single','Abuja']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM','Oracle','Amazon']
print(mixed_data_types)
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

it_companies.pop()
print(it_companies)
it_companies.append('Salesforce')
it_companies.insert(3, 'Tesla')



>>> it_companies[0]
'Facebook'
>>> it_companies[0].upper()
'FACEBOOK'
>>> it_companies
['Facebook', 'Google', 'Microsoft', 'Tesla', 'Apple', 'IBM', 'Oracle', 'Salesforce']
>>> x = it_companies[0].upper()
>>> it_companies.insert(0,x)
>>> it_companies
['FACEBOOK', 'Facebook', 'Google', 'Microsoft', 'Tesla', 'Apple', 'IBM', 'Oracle', 'Salesforce']
>>> del it_companies[0]
>>> it_companies
['Facebook', 'Google', 'Microsoft', 'Tesla', 'Apple', 'IBM', 'Oracle', 'Salesforce']
>>> '#; 'join.(it_companies)
SyntaxError: invalid syntax
>>> '#; 'join(it_companies)
SyntaxError: invalid syntax
>>> '#; '.join(it_companies)
'Facebook#; Google#; Microsoft#; Tesla#; Apple#; IBM#; Oracle#; Salesforce'
>>> it_companies
['Facebook', 'Google', 'Microsoft', 'Tesla', 'Apple', 'IBM', 'Oracle', 'Salesforce']
>>> 'Facebook' in it_companies
True
>>> it_companies.sort()
>>> it_companies
['Apple', 'Facebook', 'Google', 'IBM', 'Microsoft', 'Oracle', 'Salesforce', 'Tesla']
>>> it_companies.sort(reverse=True)
>>> it_companies
['Tesla', 'Salesforce', 'Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple']
>>> it_companies[:3]
['Tesla', 'Salesforce', 'Oracle']
>>> it_companies[-1:-4]
[]
>>> it_companies
['Tesla', 'Salesforce', 'Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple']
>>> it_companies[-1:]
['Apple']
>>> len(it_companies)
8
>>> it_companies[4:8]
['IBM', 'Google', 'Facebook', 'Apple']
>>> it_companies.pop(4)
'IBM'
>>> it_companies
['Tesla', 'Salesforce', 'Oracle', 'Microsoft', 'Google', 'Facebook', 'Apple']
>>> it_companies['Tesla']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    it_companies['Tesla']
TypeError: list indices must be integers or slices, not str
>>> it_companies.remove['Tesla']
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    it_companies.remove['Tesla']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> it_companies.remove('Tesla')
>>> it_companies
['Salesforce', 'Oracle', 'Microsoft', 'Google', 'Facebook', 'Apple']
>>> it_companies.pop(-1)
'Apple'
>>> it_companies.clear()
>>> it_companies
[]
>>> front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
>>> back_end = ['Node','Express', 'MongoDB']
>>>



 front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
>>> back_end = ['Node','Express', 'MongoDB']
>>> full_stack = front_end.extend(back_end)
>>> full_stack
>>> 
>>> full_stack
>>> print(full_stack)
None
>>> front_end
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
>>> front_end.insert[5, 'Python']
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    front_end.insert[5, 'Python']
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> front_end.insert(5, 'Python')
>>> front_end
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'Node', 'Express', 'MongoDB']
>>> front_end.insert(5, 'SQL')
>>> front_end
['HTML', 'CSS', 'JS', 'React', 'Redux', 'SQL', 'Python', 'Node', 'Express', 'MongoDB']
>>> front_end.remove('SQL')
>>> front_end.insert(6, 'SQL')
>>> front_end
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']
>>> full_stack = front_end
>>> full_stack
['HTML', 'CSS', 'JS', 'React', 'Redux', 'Python', 'SQL', 'Node', 'Express', 'MongoDB']
>>> #The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

>>> ages.sort()
>>> ages
[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
>>> min(ages)
19
>>> max(ages)
26
>>> min(ages) + max(ages)
45
>>> len(ages)
10

>>> ages
[19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
>>> len(ages)
10
>>> median_age = ages[4:6]
>>> median_age
[24, 24]
>>> sum(median_age)
48
>>> new_median_age  = sum(median_age) / len(median_age)
>>> print(new_median_age)
24.0
>>> average_age = sum(ages) / len(ages)
>>> average_age
22.8
>>> range_ages = max(ages) - min(ages)
>>> range_ages
7
>>> abs(min(ages)-average_age) and abs(max(ages) - average_age)
3.1999999999999993
>>> abs(min(ages)-average_age)
3.8000000000000007
>>> abs((min(ages)-average_age) and abs(max(ages) - average_age))
3.1999999999999993
>>> abs((min(ages)-average_age) and (max(ages) - average_age))
3.1999999999999993
>>> (min(ages)-average_age)
-3.8000000000000007
>>> min(ages) - average_age
-3.8000000000000007
>>> max(ages) - average_age
3.1999999999999993
>>> 
