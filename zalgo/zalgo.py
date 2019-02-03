import random

DIACRITICS_BOTTOM = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ',]
DIACRITICS_TOP = [' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚',]
DIACRITICS_MIDDLE = [' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡',]

def process(text: str, bottom_diacritics_count=(1, 3), middle_diacritics_count=(1, 2), top_diacritics_count=(1, 3), maximum_diacritics_per_letter=3):
    """
    Add zalgo characters to a string.
    """
    # Split string into its constituent characters
    letters = list(text)
    new_word = ''
    new_letters = []

    # Add diacritics of each type for each letter
    for letter in letters:
        a = letter #create a dummy letter

        #skip this letter we can't add a diacritic to it
        if not a.isalpha():
            new_letters.append(a)
            continue

        num_accents = 0
        numU = random.randint(top_diacritics_count[0],top_diacritics_count[1])
        numD = random.randint(bottom_diacritics_count[0],bottom_diacritics_count[1])
        numM = random.randint(middle_diacritics_count[0],middle_diacritics_count[1])
        #Try to add accents to the letter, will add an upper, lower, or middle accent randomly until
        #either num_accents == maximum_diacritics_per_letter or we have added the maximum upper, middle and lower accents. Denoted
        #by numU, numD, and numM
        while num_accents < maximum_diacritics_per_letter and numU + numM + numD != 0:
            randint = random.randint(0,2) # randomly choose what accent type to add
            if randint == 0:
                if numU > 0:
                    a = self.combine_with_diacritic(a, DIACRITICS_TOP)
                    num_accents += 1
                    numU -= 1
            elif randint == 1:
                if numD > 0:
                    a = self.combine_with_diacritic(a, DIACRITICS_BOTTOM)
                    numD -= 1
                    num_accents += 1
            else:
                if numM > 0:
                    a = self.combine_with_diacritic(a, DIACRITICS_MIDDLE)
                    numM -= 1
                    num_accents += 1

        #a = a.replace(" ","") #remove any spaces, this also gives it the zalgo text look
        #print('accented a letter: ' + a)
        new_letters.append(a)

    new_word = ''.join(new_letters)
    return new_word

def combine_with_diacritic(letter, diacritic_options):
    """
    Combine letter with a random diacritic.
    """
    return letter.strip() + diacritic_options[random.randrange(0, len(diacritic_options))].strip()
