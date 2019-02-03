import random

DIACRITICS_DOWNWARD = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ',]
DIACRITICS_UPWARD = [' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚',]
DIACRITICS_MIDDLE = [' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡',]

def process(self, text: str, downward_diacritics_count=(1, 3), middle_diacritics_count=(1, 2), upward_diacritics_count=(1, 3), maximum_diacritics_per_letter=3):
    """
    Add zalgo characters to a string.
    """
    #get the letters list
    letters = list(text) #['t','e','s','t',' ','t',...]
    #print(letters)
    newWord = ''
    newLetters = []

    #for each letter, add some diacritics of all varieties
    for letter in letters: #'p', etc...
        a = letter #create a dummy letter

        #skip this letter we can't add a diacritic to it
        if not a.isalpha():
            newLetters.append(a)
            continue

        numAccents = 0
        numU = random.randint(upward_diacritics_count[0],upward_diacritics_count[1])
        numD = random.randint(downward_diacritics_count[0],downward_diacritics_count[1])
        numM = random.randint(middle_diacritics_count[0],middle_diacritics_count[1])
        #Try to add accents to the letter, will add an upper, lower, or middle accent randomly until
        #either numAccents == maximum_diacritics_per_letter or we have added the maximum upper, middle and lower accents. Denoted
        #by numU, numD, and numM
        while numAccents < maximum_diacritics_per_letter and numU + numM + numD != 0:
            randint = random.randint(0,2) # randomly choose what accent type to add
            if randint == 0:
                if numU > 0:
                    a = self.combine_with_diacritic(a, DIACRITICS_UPWARD)
                    numAccents += 1
                    numU -= 1
            elif randint == 1:
                if numD > 0:
                    a = self.combine_with_diacritic(a, DIACRITICS_DOWNWARD)
                    numD -= 1
                    numAccents += 1
            else:
                if numM > 0:
                    a = self.combine_with_diacritic(a, DIACRITICS_MIDDLE)
                    numM -= 1
                    numAccents += 1

        #a = a.replace(" ","") #remove any spaces, this also gives it the zalgo text look
        #print('accented a letter: ' + a)
        newLetters.append(a)

    newWord = ''.join(newLetters)
    return newWord

def combine_with_diacritic(self, letter, diacriticList):
    '''
    Combines letter and a random character from diacriticList
    '''
    return letter.strip() + diacriticList[random.randrange(0, len(diacriticList))].strip()
