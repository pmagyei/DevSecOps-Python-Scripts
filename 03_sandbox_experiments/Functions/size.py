def make_tshirt(text="I love Python", size="large"):
    """Prints a sentence summarizing the size of the shirt"""
    print(f"You have ordered a: {size.title()} sized t-shirt with message: {text}")

make_tshirt()
make_tshirt(size="medium")
make_tshirt(size="small", text="Get money")