import random


DIACRITICS_TOP = [' ̍',' ̎',' ̄',' ̅',' ̿',' ̑',' ̆',' ̐',' ͒',' ͗',' ͑',' ̇',' ̈',' ̊',' ͂',' ̓',' ̈́',' ͊',' ͋',' ͌',' ̃',' ̂',' ̌',' ͐',' ́',' ̋',' ̏',' ̽',' ̉',' ͣ',' ͤ',' ͥ',' ͦ',' ͧ',' ͨ',' ͩ',' ͪ',' ͫ',' ͬ',' ͭ',' ͮ',' ͯ',' ̾',' ͛',' ͆',' ̚',]
DIACRITICS_MIDDLE = [' ̕',' ̛',' ̀',' ́',' ͘',' ̡',' ̢',' ̧',' ̨',' ̴',' ̵',' ̶',' ͜',' ͝',' ͞',' ͟',' ͠',' ͢',' ̸',' ̷',' ͡',]
DIACRITICS_BOTTOM = ['̖',' ̗',' ̘',' ̙',' ̜',' ̝',' ̞',' ̟',' ̠',' ̤',' ̥',' ̦',' ̩',' ̪',' ̫',' ̬',' ̭',' ̮',' ̯',' ̰',' ̱',' ̲',' ̳',' ̹',' ̺',' ̻',' ̼',' ͅ',' ͇',' ͈',' ͉',' ͍',' ͎',' ͓',' ͔',' ͕',' ͖',' ͙',' ͚',' ',]

def process(text: str, min_top_diacritics=1, max_top_diacritics=3, min_middle_diacritics=1, max_middle_diacritics=2, min_bottom_diacritics=1, max_bottom_diacritics=3, remove_spaces=False):
    """
    Add zalgo characters to a string.
    :param min_top_diacritics: minimum upper diacritic count.
    :param max_top_diacritics: maximum upper diacritic count.
    :param min_middle_diacritics: minimum middle diacritic count.
    :param max_middle_diacritics: maximum middle diacritic count.
    :param min_bottom_diacritics: minimum lower diacritic count.
    :param max_bottom_diacritics: maximum lower diacritic count.
    :param remove_spaces: should spaces be removed from string?
    """
    output = ''

    if remove_spaces:
        output.replace(' ', '')

    # Add diacritics for each character
    for character in text:
        # Skip spaces
        if character == ' ':
            output += character
            continue

        num_top_diacritics = random.randint(min_top_diacritics, max_top_diacritics)
        num_bottom_diacritics = random.randint(min_bottom_diacritics, max_bottom_diacritics)
        num_middle_diacritics = random.randint(min_middle_diacritics, max_middle_diacritics)
        for i in range(num_top_diacritics):
            character = mark(character, DIACRITICS_TOP)
        for i in range(num_middle_diacritics):
            character = mark(character, DIACRITICS_MIDDLE)
        for i in range(num_bottom_diacritics):
            character = mark(character, DIACRITICS_BOTTOM)

        output += character

    return output

def strip(text: str):
    """
    Remove diacritics from text.
    :param str: string from which to strip diacritics.
    """
    for diacritic in DIACRITICS_TOP + DIACRITICS_MIDDLE + DIACRITICS_BOTTOM:
        text = text.replace(diacritic.strip(), '')
    return text

def mark(character, diacritic_options):
    """
    Combine character with a random diacritic.
    """
    return character + random.choice(diacritic_options).strip()
