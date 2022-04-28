from pypinyin import pinyin as to_pinyin
from pypinyin import Style as style

tone_styles = [style.TONE, style.TONE2, style.TONE3]

def char_to_pinyin(char: str, tone_style: int) -> str:
    """Converts a single character to pinyin
    # TODO support heteronyms?

    Parameters
    ----------
    char : String
        A single chinese character
    tone_style : int
        an integeter representing the tone style to use. 0 is "zhong", 1 is "zhōng", 2 is "zho1ng"

    Returns
    -------
    String
        The pinyin representing the single chinese character
    """
    # Is created as a list of lists, so return as just string
    return to_pinyin(char, style=tone_styles[tone_style], heteronyms=False)[0][0]

def chars_to_pinyin(chars: str, tone_style: int, as_list=True) -> [str]:
    """Converts a series characters in a single str into a list of pinyin representing those characters
        
    Parameters
    ----------
    chars : str
        A string representing a series of characters
    tone_style : int
        The tone style to use in the pinyin
    as_list : bool, optional
        If the result should be returned as a list , or as a space separated string

    Returns
    -------
    [str]
        [description]
    """
    chars_list = to_pinyin(chars, style=tone_styles[tone_style])
    chars_list = [char[0] for char in chars_list if char[0] != " "]
    if as_list:
        return chars_list

    # Return as space separated sentence
    return " ".join(chars_list)
