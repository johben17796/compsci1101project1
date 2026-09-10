"""
    CSCI1101 Quiz Project
    By Ben, Garrett, and Ollie
    We're going to do a Jeopardy style quiz, where you answer questions from categories you've selected to earn a total of $(specify amount)
    sources used for learning: 
    https://docs.python.org/3/tutorial/datastructures.html
    https://docs.python.org/3/library/stdtypes.html
    https://www.geeksforgeeks.org/python/switch-case-in-python-replacement/
    https://www.w3schools.com/python/ref_keyword_in.asp 
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
    "100": ("The ancient wonder in Egypt", "pyramid"),
    "200": ("s","s"),
    "300": ("s","s"),
    "400": ("s","s"),
    "500": ("What year were the Hanging Gardens of Babylon Created?", "600 B.C.")}
food: dict[str, tuple[str, str]] = {
    "100": ("s","s"),
    "200": ("The hamburger's country of origin","What is Germany"),
    "300": ("s","s"),
    "400": ("s","s"),
    "500": ("s","s")}
books: dict[str, tuple[str, str]] = {
    "100": ("s","s"),
    "200": ("s","s"),
    "300": ("s","s"),
    "400": ("s","s"),
    "500": ("s","s")}
pop_culture: dict[str, tuple[str, str]] = {
    "100": ("s","s"),
    "200": ("s","s"),
    "300": ("s","s"),
    "400": ("s","s"),
    "500": ("s","s")}
music: dict[str, tuple[str, str]] = {
    "100": ("s","s"),
    "200": ("s","s"),
    "300": ("s","s"),
    "400": ("s","s"),
    "500": ("s","s")}

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
        if question[1] in answer:
            money += int(dollars) # increments the amount if correct
            print(f"Correct! You now have {money} dollars.")
        else: 
            money -= int(dollars)
            print(f"Incorrect! You now have {money} dollars.")
    # Fill in these other 4 later
    case "Food":
        print("a")
    case "Books":
        print("a")
    case _: 
        print("Please select either Wonders, Food, Books, Pop Culture, or Music!")
