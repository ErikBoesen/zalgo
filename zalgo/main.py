import random

DIACRITICS_BOTTOM = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ',]
DIACRITICS_TOP = [' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚',]
DIACRITICS_MIDDLE = [' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡',]

def process(text: str, minimum_bottom_diacritics=1, maximum_bottom_diacritics=3, minimum_middle_diacritics=1, maximum_middle_diacritics=2, minimum_top_diacritics=1, maximum_top_diacritics=3, maximum_diacritics_per_letter=3):
    """
    Add zalgo characters to a string.
    """
    # Split string into its constituent characters
    output = ''

    # Add diacritics for each letter
    for letter in text:
        # If character is not alphabetical, skip it
        if not letter.isalpha():
            output += letter
            continue

        num_accents = 0
        num_top_accents = random.randint(minimum_top_diacritics,maximum_top_diacritics)
        num_bottom_accents = random.randint(minimum_bottom_diacritics,maximum_bottom_diacritics)
        num_middle_accents = random.randint(minimum_middle_diacritics,maximum_middle_diacritics)
        # Add diacritics randomly to letter until saturation
        while num_accents < maximum_diacritics_per_letter and num_top_accents + num_middle_accents + num_bottom_accents != 0:
            randint = random.randint(0,2) # randomly choose what accent type to add
            if randint == 0:
                if num_top_accents > 0:
                    letter = combine_with_diacritic(letter, DIACRITICS_TOP)
                    num_accents += 1
                    num_top_accents -= 1
            elif randint == 1:
                if num_bottom_accents > 0:
                    letter = combine_with_diacritic(letter, DIACRITICS_BOTTOM)
                    num_bottom_accents -= 1
                    num_accents += 1
            else:
                if num_middle_accents > 0:
                    letter = combine_with_diacritic(letter, DIACRITICS_MIDDLE)
                    num_middle_accents -= 1
                    num_accents += 1

        #a = a.replace(" ","") #remove any spaces, this also gives it the zalgo text look
        output += letter

    return output

def combine_with_diacritic(letter, diacritic_options):
    """
    Combine letter with a random diacritic.
    """
    return letter.strip() + diacritic_options[random.randrange(0, len(diacritic_options))].strip()
