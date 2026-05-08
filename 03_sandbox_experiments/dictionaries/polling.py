favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'philip': 'python',
    'dante': 'bash',
    'prince': 'python'
}

lan_poll = ['jen', 'prince', 'dante', 'sarah']

for name in favourite_languages:
    if name in lan_poll:
        print(f"Thanks for taking the poll {name.title()}")
    else:
        print(f"Hi {name.title()}, please take the language poll as soon as possible.")