import random

DIACRITICS_TOP = [' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚',]
DIACRITICS_MIDDLE = [' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡',]
DIACRITICS_BOTTOM = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ',]

def process(text: str, min_top_diacritics=1, max_top_diacritics=3, min_middle_diacritics=1, max_middle_diacritics=2, min_bottom_diacritics=1, max_bottom_diacritics=3, max_diacritics_per_character=3, remove_spaces=False):
    """
    Add zalgo characters to a string.
    """
    output = ''

    # Add diacritics for each character
    for character in text:
        # If character is not alphabetical, skip it
        if not character.isalpha():
            output += character
            continue

        diacritics_added = 0
        num_top_diacritics = random.randint(min_top_diacritics,max_top_diacritics)
        num_bottom_diacritics = random.randint(min_bottom_diacritics,max_bottom_diacritics)
        num_middle_diacritics = random.randint(min_middle_diacritics,max_middle_diacritics)
        # Add diacritics randomly to character until saturation
        while diacritics_added < max_diacritics_per_character and num_top_diacritics + num_middle_diacritics + num_bottom_diacritics != 0:
            randint = random.randint(0,2) # randomly choose what accent type to add
            if randint == 0:
                if num_top_diacritics > 0:
                    character = combine_with_diacritic(character, DIACRITICS_TOP)
                    diacritics_added += 1
                    num_top_diacritics -= 1
            elif randint == 1:
                if num_middle_diacritics > 0:
                    character = combine_with_diacritic(character, DIACRITICS_MIDDLE)
                    num_middle_diacritics -= 1
                    diacritics_added += 1
            else:
                if num_bottom_diacritics > 0:
                    character = combine_with_diacritic(character, DIACRITICS_BOTTOM)
                    num_bottom_diacritics -= 1
                    diacritics_added += 1

        output += character

    if remove_spaces:
        output.replace(' ', '')

    return output

def combine_with_diacritic(character, diacritic_options):
    """
    Combine character with a random diacritic.
    """
    return character + diacritic_options[random.randrange(0, len(diacritic_options))]
