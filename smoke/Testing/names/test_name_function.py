from name_function import get_formatted_name as gfn

def test_first_last_name():
    formatted_name = gfn("pRince", "aGyei")
    assert formatted_name == "Prince Agyei"


def test_first_last_name_middle():
    formatted_name = gfn("pRince", "aGyei", "matthew")
    assert formatted_name == "Prince Matthew Agyei"



