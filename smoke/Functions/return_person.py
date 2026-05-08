def build_person(first_name, last_name, age=None): #parameters
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age # if age has been assigned value, it inserts a key value entry into the person dictionary
    return person  #return can return any value

musician = build_person('jimi', 'hendrix', age=27) #arguments
print(musician)

