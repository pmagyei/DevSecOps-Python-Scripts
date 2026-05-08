favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# language = favourite_languages['sarah'].title() #access dictionary value by inserting key in [] right after the dictionary
#
# print(f"Sarah's favourite language is {language}")
#
# language = favourite_languages['sarah'] = 'Bash'
#
# print(f"Sarah's new favourite language is {language}")

for name, language in favourite_languages.items(): #items() returns dictionaries key-value pairs.
    # returners key-value sequence assign key and value to name and language
    print(F"{name.title()}'s favorite language is {language.title()}.")

for name in favourite_languages.keys():  #keys/values pulls the keys out the dictionary and assigns it to the name variable
    print(name.title())

