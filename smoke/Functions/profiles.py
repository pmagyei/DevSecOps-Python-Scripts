def build_profile(first, last, **user_info):
    """Build a dictionary containing everything about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info



user_profile = build_profile('Prince', 'Agyei',
                             location='Leeds',
                             field='Tech',
                             businesses='Music',
                             languages='English, Italian',
                             age='26')

print(user_profile)