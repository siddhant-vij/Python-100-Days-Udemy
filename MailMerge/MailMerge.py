import os


RESOURCE_FILE = "./MailMerge/Input/Resources/NameFieldYear.txt"
STARTING_LETTER = "./MailMerge/Input/Letters/StartingLetter.txt"
OUTPUT_FOLDER = "./MailMerge/Output"


def getNameFieldAndYearFromFile():
    listOfWinners = []
    with open(RESOURCE_FILE, "r") as file:
        for line in file:
            name, field, year = line.strip().split(",")
            listOfWinners.append((name, field, year))
    return listOfWinners


def getStartingLetterFromFile():
    with open(STARTING_LETTER, "r") as file:
        return file.read()


def writeLetterToEachWinner(listOfWinners: list[tuple[str, str, str]]):
    for winner in listOfWinners:
        winnerFile = os.path.join(OUTPUT_FOLDER,
                                  f"LetterTo{winner[0].replace(' ', '')}.txt")
        with open(winnerFile, "w") as file:
            file.write(getStartingLetterFromFile().replace("[Name]", winner[0]).
                       replace("[Field]", winner[1]).replace("[Year]", winner[2]))


if __name__ == "__main__":
    writeLetterToEachWinner(getNameFieldAndYearFromFile())
