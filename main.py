from difflib import SequenceMatcher

with open("1.txt") as file1, open("2.txt") as file2:
    fill1data = file1.read()
    fill2data = file2.read()
    similarity = SequenceMatcher(None,fill1data,fill2data).ratio()
    print(similarity*100)
