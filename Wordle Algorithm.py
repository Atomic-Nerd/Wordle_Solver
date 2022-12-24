from numpy import *

my_file = open("Words", "r")
content = my_file.read()
allowed_words = content.split("\n")
my_file.close()


def split(word):
    return [char for char in word]

def removewords():

    new_allowedwords = []
    if rightanswer != ['#','#','#','#','#']:
        for word in allowed_words:
            valid = True
            for index in range(5):
                if rightanswer[index] != '#' and rightanswer[index] != word[index]:
                    valid = False
            if valid:
                new_allowedwords.append(word)
    else:
        for word in allowed_words:
            new_allowedwords.append(word)

    second_allowedwords = []
    for word in new_allowedwords:
        valid = True
        for letter in inanswer:
            if letter not in word:
                valid = False
        if valid:
            second_allowedwords.append(word)

    third_allowedwords = []
    for word in second_allowedwords:
        valid = True
        for letter in removelist:
            if letter in split(word):
                if letter not in rightanswer:
                    valid = False
        if valid:
            third_allowedwords.append(word)

    final_allowedwords = []
    for word in third_allowedwords:
        valid = True
        for index in range(len(inanswerindex)):
            letterrow = inanswerindex[index]
            for letter in letterrow:
                if word[index] == letter:
                    valid = False
        if valid:
            final_allowedwords.append(word)

    return final_allowedwords

lives = 6
inanswer = []
inanswerindex = [[],[],[],[],[]]
removelist = []
rightanswer = ['#','#','#','#','#']

while lives !=0:
    guess = split(input('Guess: '))
    answer = split(input('(0) - Wrong\n(1) - Correct wrong place\n(2) - Correct right place\nAnswer: '))
    for index in range(len(guess)):
        if answer[index] == '0':
            removelist.append(guess[index])
        elif answer[index] == '1':
            if guess[index] not in inanswer:
                inanswer.append(guess[index])
                if guess[index] not in (inanswerindex[index]):
                    inanswerindex[index].append(guess[index])
        else:
            rightanswer[index] = guess[index]

    allowed_words = removewords()

    if len(allowed_words) == 1:
        print (f'The answer is: {allowed_words[0]}')
        print (f'You completed it with: {lives} lives left')
    else:
        print (f'Your possible words are: {allowed_words}')
        print (f'The number of current posibilites are: {len(allowed_words)}')
        lives -= 1
        print (f'You have: {lives} lives left')
