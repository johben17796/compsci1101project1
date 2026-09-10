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

money: int = 0

cat_select: str = input()
if cat_select == "Wonders":
    print("You've selected Wonders!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
elif cat_select == "Food":
    print("You've selected Food!\nPlease choose a $ amount question!\n100200\n\n300\n400\n500")
elif cat_select == "Books":
    print("You've selected Books!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
else:
    print("Please restart and choose a category!")

dol_select: int = int(input())
if dol_select == 100 and cat_select == "Wonders":
    Won100: str = input("What is the wonder in Egypt? ")
    if Won100 == ("Pyramid"):
        print("Correct!")
        money += 100
        print(money)
