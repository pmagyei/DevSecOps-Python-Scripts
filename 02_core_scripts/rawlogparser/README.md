For the RAW log parser the code takes a single long string and chops it up into a list of smaller strings based on a specific character in this case " " space.

I used the .split() function to take a long string and divide by " " spaces into smaller strings. 
Then, since each IP address is at index 0, 0 is used as an index after splitting the lines into substrings

