import re

def filter_chinese_specific_punctuation(sentence: str) -> str:
    """Strips punctuation from an chinese sentence using regex
        # TODO TEST
    Parameters
    ----------
    sentence : String
        The sentence to filter out punctuation from

    Returns
    -------
    String
        The cleaned sentence
    """
    filter = re.findall(u'([\u4e00-\u9fff0-9a-zA-Z]|(?<=[0-9])[^\u4e00-\u9fff0-9a-zA-Z]+(?=[0-9]))', sentence)
    return " ".join(filter)

def filter_general_punctuation(sentence: str) -> str:
    """Filters out more general punctuation, as well as any english punctuation
    # TODO TEST

    Parameters
    ----------
    sentence : str
        The sentence to filter out punctuation from

    Returns
    -------
    str
        the cleaned sentence
    """
    filter = re.findall(u"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", sentence)
    return filter.join('')

def filter_english_text(sentence: str) -> str:
    """Filters out english text from chinese text
        # TODO TEST
    Parameters
    ----------
    sentence : str
        The chinese text which we wish to remove enlish text from

    Returns
    -------
    str
        The fully chinese text
    """
    english = re.findall("[a-z]+", sentence)
    sentence = re.sub("[a-z]+","",sentence)
    return sentence

def filter_all_non_chinese_text(sentence: str) -> str:
    """Filters out ALL non chinese characters
        # TODO TEST
    Parameters
    ----------
    sentence : str
        input sentence as a string

    Returns
    -------
    str
        the filtered string
    """
    try:
        sentence = sentence.decode("utf-8") # convert context from str to unicode
    except:
        sentence = sentence
    filtrate = re.compile(u'[^\u4E00-\u9FA5]') # non-Chinese unicode range
    sentence = filtrate.sub(r'', sentence) # remove all non-Chinese characters
    sentence = sentence.encode("utf-8") # convert unicode back to str
    return sentence

def remove_stop_words(sentence: str, stopwords=[]) -> str:
    """Removes chinese stopwords from chinese text
    # TODO TEST, is this even needed?

    Parameters
    ----------
    sentence : str
        The sentence to clean
    stopwords : list, optional
        The stopwords to remove, by default []

    Returns
    -------
    str
        The stop word removed text
    """
    for i in range(len(stopwords)):
        stopwords[i] = stopwords[i]
    clean = [t for t in sentence if t not in stopwords]
    return clean