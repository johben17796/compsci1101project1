"""
CSCI1101 Quiz Project
By Ben, Garrett, and Ollie
We're going to do a Jeopardy style quiz, where you answer questions from categories you've selected to earn a total of $(specify amount)
sources used for learning: 
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/library/stdtypes.html
https://www.geeksforgeeks.org/python/switch-case-in-python-replacement/
"""

print("Welcome to Jeopardy! Your goal is to collect $(unspecified) by answering questions correctly! Your categories are:")
print("Wonders")
print("Food")
print("Books")
print("Pop Culture")
print("Music")
print("--Please type all inputs for this game in full lowercase and with exact spelling--")

money: int = 0
"""
 Each entry in the dictionaries corresponds to a dollar amount key with a tuple value for both the question and the answer. 
"""
wonders: dict[str, tuple[str, str]] = {
    "100": ("The ancient wonder in Egypt:", "pyramid"),
    "200": ("The place the hanging gardens were:", "babylon"),
    "300": ("It spans 13,000 miles:", "wall"),
    "400": ("He's the 8th wonder of the world:", "andre"),
    "500": ("The wondrous statue of this god was erected by Phidias:", "zeus")}
food: dict[str, tuple[str, str]] = {
    "100": ("A common fried potato product is named for this country:", "france"),
    "200": ("", ""),
    "300": ("s", "s"),
    "400": ("s", "s"),
    "500": ("s", "s")}
books: dict[str, tuple[str, str]] = {
    "100": ("With total sales reaching over 5 billion, this book has the most purchases of all time:", "bible"),
    "200": ("s", "s"),
    "300": ("s", "s"),
    "400": ("s", "s"),
    "500": ("s", "s")}
pop_culture: dict[str, tuple[str, str]] = {
    "100": ("s", "s"),
    "200": ("Named for a comic, this Spider-Man movie released July of 2026:", "brand new day"),
    "300": ("s", "s"),
    "400": ("s", "s"),
    "500": ("s", "s")}
music: dict[str, tuple[str, str]] = {
    "100": ("Not the son of a king, but this musician:", "prince"),
    "200": ("Band named for a horror movie that was released in 1963:", "black sabbath"),
    "300": ("s", "s"),
    "400": ("Band named for a horror movie that was released in 1963:", "black sabbath"),
    "500": ("s", "s")}

category: str = input()
if category == "wonders":
    print("You've selected Wonders!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
elif category == "food":
    print("You've selected Food!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
elif category == "books":
    print("You've selected Books!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
elif category == "pop culture":
    print("You've selected Pop Culture!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
elif category == "music":
    print("You've selected Music!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
else:
    print("Please restart and choose a category!")

dollars: str = input()
match category:
    case "wonders":
        question: tuple[str, str] = wonders.get(dollars)
        answer: str = input(question[0] + " ")
        if question[1] in answer:
            money += int(dollars) # increments the amount if correct
            print(f"Correct! You now have {money} dollars.")
        else:
            money -= int(dollars)
            print(f"Incorrect! You now have {money} dollars.")
    # Fill in these other 4 later
    case "food":
        print("a")
    case "books":
        print("a")
    case "pop culture":
        print("a")
    case "music":
        print("a")
    case _:
        print('Please select either "wonders", "food", "books", "pop culture", or "music"!')
