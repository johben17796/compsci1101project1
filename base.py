"""
CSCI1101 Quiz Project
By Ben, Garrett, and Ollie
We're going to do a Jeopardy style quiz, where you answer questions from categories you've selected to earn a total of $(specify amount)
sources used for learning: 
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/library/stdtypes.html
https://www.geeksforgeeks.org/python/switch-case-in-python-replacement/
"""

print("Welcome to Jeopardy! Your goal is to collect $(unspecified) by answering questions correctly! Your categories are")
print("Wonders")
print("Food")
print("Books")
print("Pop Culture")
print("Music")
print("Please type your category exactly. Capitalization matters!")

money: int = 0
# Each entry in the dictionaries corresponds to a dollar amount key with a tuple value for both the question and the answer.
wonders: dict[str, tuple[str, str]] = {
    "100": ("What is the wonder in Egypt?", "Pyramid"),
    "200": ("What is the wonder in Egypt?", "Pyramid"),
    "300": ("What is the wonder in Egypt?", "Pyramid"),
    "400": ("What is the wonder in Egypt?", "Pyramid"),
    "500": ("What is the wonder in Egypt?", "Pyramid")}
food: dict[str, tuple[str, str]] = {
    "100": (),
    "200": (),
    "300": (),
    "400": (),
    "500": ()}
books: dict[str, tuple[str, str]] = {
    "100": (),
    "200": (),
    "300": (),
    "400": (),
    "500": ()}
pop_culture: dict[str, tuple[str, str]] = {
    "100": (),
    "200": (),
    "300": (),
    "400": (),
    "500": ()}
music: dict[str, tuple[str, str]] = {
    "100": (),
    "200": (),
    "300": (),
    "400": (),
    "500": ()}

category: str = input()
if category == "Wonders":
    print("You've selected Wonders!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
elif category == "Food":
    print("You've selected Food!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
elif category == "Books":
    print("You've selected Books!\nPlease choose a $ amount question!\n100\n200\n300\n400\n500")
else:
    print("Please restart and choose a category!")

dollars: str = input()
match category:
    case "Wonders":
        question: tuple[str, str] = wonders.get(dollars)
        answer: str = input(question[0] + " ")
        if answer == question[1]:
            money += int(dollars) # increments the amount if correct
        else: money -= int(dollars) # and decrements if wrong.
            print(f"Correct! You now have {dollars} dollars.")
    # Fill in these other 2 later
    case "Food":
        print("a")
    case "Books":
        print("a")
    case _: 
        print("Please select either Wonders, Food, Books, Pop Culture, or Music!")
