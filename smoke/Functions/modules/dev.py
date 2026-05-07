def development(os, *specification):
    """Summarizes compute spec requirements"""
    print(f"\nYou have selected {os} "
          f"as the Operating system with the following hardware specifications:")
    for specs in specification:
        print(f" - {specs}")
