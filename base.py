"""
CSCI1101 Quiz Project
By Ben, Garrett, and Ollie
We're going to do a Jeopardy style quiz, where you answer questions from categories you've selected to earn a total of $(specify amount)
sources used for learning: 
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/tutorial/controlflow.html
"""

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


categories: dict[str, dict] = {
    "wonders": wonders,
    "food": food,
    "books": books,
    "pop culture": pop_culture,
    "music": music}
money: int = 0

def ask_dollar_amount(dictionary: dict):
    numbers: str = "|      100    |    200    |    300    |    400    |    500       |"
    # Blank out the dollar amounts for already answered questions
    for i in range(5):
        if f"{(i + 1) * 100}" not in dictionary:
            numbers = numbers.replace(f"{(i + 1) * 100}", "---")
    print("+----------------------------------------------------------------+")
    print("|   Now, please choose a $ amount question. Your options are:    |")
    print("+-------------+-----------+-----------+-----------+--------------+")
    print(numbers)
    print("+-------------+-----------+-----------+-----------+--------------+")
    output: str = ""
    while True:
        output = input("> ")
        if output in dictionary:
            break
        print("Please choose a number shown above!")
    return output

def ask_question(dictionary: dict):
    dollars: str = ask_dollar_amount(dictionary)
    question: tuple[str, str] = dictionary.pop(dollars)
    answer: str = input(question[0] + " ")
    reward: int = 0

    if question[1] in answer.lower():
        reward += int(dollars)
        print(f"Correct! You now have {money + reward} dollars.")
    else:
        reward -= int(dollars)
        print(f"Incorrect! You now have {money + reward} dollars.")
    if len(dictionary) == 0:
        categories.pop(dictionary)
    return reward

first_time: bool = True
while True:
    if first_time:
        print("+----------------------------------------------------------------+")
        print("|   Welcome to Jeopardy! Collect as much money as possible by    |")
        print("|     answering questions correctly! Your categories are:        |")
        first_time = False
    else:
        print("+----------------------------------------------------------------+")
        print("|         Welcome back to Jeopardy! Your categories are:         |")
    print("+------------------+------+-------+-------------+----------------+")
    print("|          Wonders | Food | Books | Pop Culture | Music          |")
    print("+------------------+------+-------+-------------+----------------+")

    category: str = ""
    while True:
        category = input("> ").lower()
        if category in categories:
            break
        print("Please select either Wonders, Food, Books, Pop Culture, or Music!")
    money += ask_question(categories.get(category))
print(f"Congratulations! You have reached the end of Jeopardy. You finished with a grand total of {money} dollars!")
