def thing(*items):
    """print different items"""
    for item in items:
        print(f"the following item has been ordered:")
        print(f"{item}\n")

thing('watch')
thing('phone', 'airpods', 'socks', 'glasses')
thing('computer', 'monitor')