"""
CSCI1101 Quiz Project
By Ben, Garrett, and Ollie
We're going to do a Jeopardy style quiz, where you answer questions from categories you've selected to earn a total of $4500
sources used for learning: 
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/tutorial/controlflow.html
"""

import random
from display_box import DisplayBox
from typing import TextIO
#Each entry in the dictionaries corresponds to a dollar amount key with a tuple value for both the question and the answer. 

wonders: dict[str, tuple[str, str]] = {
    "100": ("The ancient wonder in Egypt:\n", "pyramid"),
    "200": ("The place the hanging gardens were:\n", "babylon"),
    "300": ("It spans 13,000 miles:\n", "wall"),
    "400": ("He's the 8th wonder of the world:\n", "andre"),
    "500": ("The wondrous statue of this god was erected by Phidias:\n", "zeus")}

food: dict[str, tuple[str, str]] = {
    "100": ("A common fried potato product is named for this country:\n", "france"),
    "200": ("The Elvis sandwich usually contains peanut butter and this:\n", "banana"),
    "300": ("Hummus is primarily made from this legume, contrary to its name, it does not contain any poultry:\n", "chickpea"),
    "400": ("This cheese is made backwards:\n", "edam"),
    "500": ("A tangelo is a cross between a tangerine and this ancestor of the grapefruit:\n", "pomelo")}

books: dict[str, tuple[str, str]] = {
    "100": ("With total sales reaching over 5 billion, this book has the most purchases of all time:\n", "bible"),
    "200": ("He asks us to call him \"Ishmael\", but this is what his name actually is:\n", "ahab"),
    "300": ("This graphic novel talks of a Greek army facing insurmountable odds:\n", "300"),
    "400": ("This Dickens novel revolves around an orphan named Pip:\n", "great expectations"),
    "500": ("His book about the things that make people successful is read in many a high school English class:\n", "gladwell")}

pop_culture: dict[str, tuple[str, str]] = {
    "100": ("This Vikings quarterback suffered a concussion in week 1 of the 2026 season:\n", "murray"),
    "200": ("Named for a comic, this Spider-Man movie released July of 2026:\n", "brand new day"),
    "300": ("This legendary country musician with her own theme park passed away in August of 2026:\n", "parton"),
    "400": ("A former Timberwolf, he won the 2026 NBA championship with the New York Knicks. \nand then got married in the summer!:\n", "towns"),
    "500": ("Unironically Dave Strider's creator:\n", "hussie")}

music: dict[str, tuple[str, str]] = {
    "100": ("Not the son of a king, but this musician: \n", "prince"),
    "200": ("Band named for a horror movie that was released in 1963:\n", "black sabbath"),
    "300": ("Both Joan Jett and Thin Lizzy have a bad \"this\",\n Taylor Swift had an era named after it\n", "reputation"),
    "400": ('"Never forget." Not this tragic day, but this other important September date:\n', "21"),
    "500": ("This band released the song Seven Wonders in 1987.\n They likely had more than seven break-ups:\n", "fleetwood mac")}

categories: dict[str, dict[str, tuple[str, str]]] = {
    "wonders": wonders,
    "food": food,
    "books": books,
    "pop culture": pop_culture,
    "music": music}

daily_double = random.randint(0, 24)

money: int = 0

def ask_dollar_amount(dictionary: dict[str, tuple[str, str]]) -> str:
    """
    Called to ask for a dollar amount from the player and handle the input

    Parameters
    ----------
    dictionary : dict[str, tuple[str, str]]
        The dictionary of the category is passed into the function.
    
    Returns
    -------
    str
        The output is the selected dollar reward as a string. 
        Gets fed into the ask_question function.
    """
    numbers: str = "100    |    200    |    300    |    400    |    500"
    # Blank out the dollar amounts for already answered questions
    for i in range(5):
        if f"{(i + 1) * 100}" not in dictionary:
            numbers = numbers.replace(f"{(i + 1) * 100}", "---")
    print(DisplayBox("Now, please choose a $ amount. Your options are:")
    .add_separator()
    .add_text(numbers))
    # Prompt user for the dollar amount, looping back if it is unavailable
    output: str = ""
    while True:
        output = input("> ")
        if output in dictionary:
            break
        print(DisplayBox("Please choose a number shown above"))
    
    return output

def double_wager(user_money: int) -> str:
    """
    Asks the contestant for a wager, up to either their current amount
    of money, or 1000 dollars if they have less 

    Parameters
    ----------
    user_money : int
        The amount of money the user has already earned.

    Returns
    -------
    str
        returns a string to be used in the ask_question function as the new
        dollars, as opposed to the questions original value.
    """

    if user_money < 1000:
        user_money = 1000
    print(f"How much would you like to wager?\nYou can wager up to ${user_money}")
    while True:
        try:
            wager: str = input()
            if not (0 < int(wager) <= user_money):
                raise IndexError
            break
        except IndexError:
            print(f"You cannot bet that much! Try again.\nYou can wager up to ${user_money}")
        except ValueError:
            print(f"That is not a number, Try again.\nYou can wager up to ${user_money}")
    return wager

def ask_question() -> int:
    """
    Asks the user the question, removing the entry from the category dictionary in the process.
    If the question asked is the daily double, the user is redirected to ``base.double_wager``

    Returns
    -------
    int
        The reward the player received for answering the question. Can be negative.
    """
    dictionary: dict[str, tuple[str, str]] = categories.get(category)
    dollars: str = ask_dollar_amount(dictionary)
    # this guy does double jeopardy
    #             V
    answer_index = (list(categories.keys()).index(category) * 5) + ((int(dollars) - 1) // 100)
    question: tuple[str, str] = dictionary.pop(dollars) #gets rid of category when exhausted
    if (answer_index == daily_double):
        print("You've just hit the daily double!")
        dollars = double_wager(money)
    reward: int = 0
    answer: str = input(question[0])
    reward: int = 0

    # if the answer is in the string, with any capitalization, add money. other, remove money
    if question[1] in answer.lower():
        reward += int(dollars)
        print(f"Correct! You now have {money + reward} dollars.")
    else:
        reward -= int(dollars)
        print(f"Incorrect! You now have {money + reward} dollars.")
    return reward

#this runs the game until someone runs out of questions or earns a total of $4500
first_time: bool = True
while len(categories) > 0 and money < 100:
    welcome: DisplayBox = DisplayBox()
    if first_time:
        welcome.add_text("Welcome to Jeopardy! Collect as much money as possible by")
        welcome.add_text("answering questions correctly! Your categories are:")
        first_time = False
    else:
        welcome.add_text("Welcome back to Jeopardy! Your categories are:")
    welcome.add_separator()
    cat: str = "Wonders | Food | Books | Pop Culture | Music"
    for category_name in categories:
        if len(categories.get(category_name)) == 0:
            cat = cat.replace(category_name.title(), "-" * len(category_name))
    welcome.add_text(cat)
    print(welcome)
    # Prompt user for the category, looping back if it doesn't match a category
    category: str = ""
    while True:
        category = input("> ").lower()
        if category in categories and len(categories.get(category)) > 0:
            break
        print("Please input a valid category as shown above!")
    money += ask_question()
if money >= 4500:
    print(f"Congratulations! You have reached the end of Jeopardy.\nYou finished with a grand total of {money} dollars!")
else:
    #TODO. Allow a player to enter their name.
    print(f"You lose!\nYou ran out of questions and only made {money} dollars.") #NOTE EDIT THIS TO MAKE MORE SENSE!!!
try:
    leaderboard_file: TextIO = open("jeopardy_leaderboard.txt", "x+", encoding="UTF-8")
    lines: list[str] = leaderboard_file.readlines()
    print(lines)
    line: str
    score: dict{str, int} = {}
    for line in lines:
        scores = line.split("|") # pipe as seperator because that is consistent with the way the categories and values are laid out
        print(scores)
        score[scores[0]] = int(scores[1].strip(" $"))

except:
#     print("WEEWOO WEEWOO ERROR")
#     # TODO: Create Default Leaderboard if there is no jeopardy_leaderboard.txt    
    new_file: TextIO = open("jeopardy_leaderboard.txt", "w", encoding="UTF-8")
    default1 = "Garrett | $3700\n"
    default2 = "Ollie | $2500\n"
    default3 = "Ben | $2100\n"
    new_file.write(default1)
    new_file.write(default2)
    new_file.write(default3)

    
        
    



# if __name__ == "__main__":
#     main() # fill this out DO NOT FORGET!!!! make it a main funciton!
