#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary.update({key: value})
    else:
        a_dictionary.setdefault(key, value)
    return a_dictionary


#a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
#new_dict = update_dictionary(a_dictionary, 'language', "Python")
#print(new_dict)
#print("--------")
#print(a_dictionary)
