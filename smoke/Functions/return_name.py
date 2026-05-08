def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title() #Return value requires a variable that it can be assigned to

musician = get_formatted_name('john', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hendrix', 'lee')
print(musician) #the return value is assigned to the musician variable and printed