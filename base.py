"""
CSCI1101 Quiz Project
By Ben, Garrett, and Ollie
We're going to do a Jeopardy style quiz, where you answer questions from categories you've selected to earn a total of $(specify amount)
sources used for learning: 
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/tutorial/controlflow.html
"""

print("Welcome to Jeopardy! Your goal is to collect $(unspecified) by answering questions correctly! Your categories are:")
print("Wonders")
print("Food")
print("Books")
print("Pop Culture")
print("Music")
print("--Please type all inputs for this game in full lowercase and with exact spelling--")

answered_questions: list[str] = []
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
    "100": ("A common fried potato product is named for this country:\n", "france"),
    "200": ("", ""),
    "300": ("Hummus is primarily made from this legume, contrary to its name, it does not contain any poultry\n", "chickpea"),
    "400": ("s", "s"),
    "500": ("s", "s")}

books: dict[str, tuple[str, str]] = {
    "100": ("With total sales reaching over 5 billion, this book has the most purchases of all time:\n", "bible"),
    "200": ("s", "s"),
    "300": ("s", "s"),
    "400": ("This Dickens novel revolves around an orphan named Pip\n", "great expectations"),
    "500": ("s", "s")}

pop_culture: dict[str, tuple[str, str]] = {
    "100": ("This Vikings quarterback suffered a concussion in week 1 of the 2026 season", "murray"),
    "200": ("Named for a comic, this Spider-Man movie released July of 2026:\n", "brand new day"),
    "300": ("This legendary country musician with her own theme park passed away in August of 2026\n", "parton"),
    "400": ("s", "s"),
    "500": ("A former Timberwolf, he won the 2026 NBA championship with the New York Knicks. \nand then got married in the summer! \n", "towns")}

music: dict[str, tuple[str, str]] = {
    "100": ("Not the son of a king, but this musician: \n", "prince"),
    "200": ("Band named for a horror movie that was released in 1963:\n", "black sabbath"),
    "300": ("s", "s"),
    "400": ("", ""),
    "500": ("This band released the song Seven Wonders in 1987.\n They likely had more than seven break-ups\n", "Fleetwood Mac")}


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
if (category + dollars) in answered_questions:
    # TODO: give an error message and send the player back to the start of the loop
    quit()

def ask_question(dictionary: dict):
    question: tuple[str, str] = dictionary.get(dollars)
    answer: str = input(question[0] + " ")
    reward: int = 0
    if question[1] in answer.lower():
        reward += int(dollars)
        print(f"Correct! You now have {money + reward} dollars.")
    else:
        reward -= int(dollars)
        print(f"Incorrect! You now have {money + reward} dollars.")
    answered_questions.append(category + dollars)
    return reward

match category:
    case "Wonders":
        money += ask_question(wonders)
    case "Food":
        money += ask_question(food)
    case "Books":
        money += ask_question(books)
    case "pop culture":
        money += ask_question(pop_culture)
    case "music":
        money += ask_question(music)
    case _:
        print("Please select either Wonders, Food, Books, Pop Culture, or Music!")
