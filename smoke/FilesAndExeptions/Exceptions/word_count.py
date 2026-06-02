from pathlib import Path

def count_words(path):
    """Count approximate number of words"""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
        # print(f"File {path} not found")
    else:
        words = contents.split()#
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ["alice.txt", "love_prejudice.txt", "moby_dick.txt", "romeo_juliet.txt"]

for filename in filenames:
    path_to_file = Path(f"../files/{filename}")
    count_words(path_to_file)
