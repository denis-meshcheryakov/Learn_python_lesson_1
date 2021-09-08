dict1 = {"city": "Москва", "temperature": "20"}
print(dict1['city'])
dict1['temperature'] = int(dict1['temperature']) - 5
print(dict1)
if 'country' not in dict1:
    print('country is not in keys')
print(dict1.get('country', 'Россия'))
dict1['date'] = '27.05.2019'
print(len(dict1))
print(dict1)
