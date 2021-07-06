from string import ascii_letters
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
checkList = list(ascii_letters) + numbers


exceptionWord = ["содержит запрещенные символы"]
exceptionOddNumbers = ["содержит четное кол-во цифр"]
exceptionEvenLetters = ["содержит нечетное кол-во букв"]


def checkLetters(word):
    for element in word:
        if element not in checkList:
            return exceptionWord
    return True


def checkNumbers(word):
    count = 0
    for element in word:
        if str(element).isdigit():
            count += 1
    if count % 2 == 0:
        return exceptionOddNumbers
    elif count % 2 > 0:
        return True


def checkWords(word):
    count = 0
    for element in word:
        if str(element) in ascii_letters:
            count += 1
    if count % 2 == 0:
        return True
    elif count % 2 > 0:
        return exceptionEvenLetters


def validate_password(password):
    if checkLetters(password) == exceptionWord:
        return exceptionWord
    elif checkWords(password) != exceptionWord:
        if checkNumbers(password) == exceptionOddNumbers:
            return exceptionOddNumbers
        elif checkNumbers(password) != exceptionOddNumbers:
            if checkWords(password) == exceptionEvenLetters:
                return exceptionEvenLetters
            elif checkWords(password) != exceptionEvenLetters:
                return True


print(validate_password("test228"))
