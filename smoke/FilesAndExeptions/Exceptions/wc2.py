from pathlib import Path

def count_words(path):
    """Count approximate number of words"""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
        # print(f"File {path} not found")
    else:
        # words = contents.split()
        print(contents.count("the"))
        print(contents.lower().count("the"))
        #num_words = len(words)
        #print(f"The file {path} has about {num_words} words.")

filenames = ["concrete_construction.txt", "frankestein_prometheus"]

for file in filenames:
    path_to_file = Path(f"../files/{file}")
    count_words(path_to_file)