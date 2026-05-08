favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favourite_languages.values()): #set identifies duplicates, only set of only unique values is built
    print(language.title())  #values from dictionary are assigned to the variable language and printed

# languages = {'python', 'rust', 'python', 'c'} braces with no key-value pairs = a set