"""
CSCI1101 Quiz Project
By Ben, Garrett, and Ollie
We're going to do a Jeopardy style quiz, where you answer questions from categories you've selected to earn a total of $(specify amount)
"""

print("Welcome to Jeopardy! Your goal is to collect $(unspecified) by answering questions correctly! Your categories are")
print("Wonders")
print("Food")
print("Books")
print("Please type your category exactly. Capitalization matters!")
cat_select: str = input()
if cat_select == "Wonders":
    print("You've selected Wonders!")
elif cat_select == "Food":
    print("You've selected Food!")
elif cat_select == "Books":
    print("You've selected Books!")
else:
    print("Please choose a category!")
