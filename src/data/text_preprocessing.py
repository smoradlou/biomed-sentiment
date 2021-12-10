import re
from typing import Set

def remove_stopwords(text:str, stopwords) -> str:

    processed_list = [word for word in text.split() if word not in stopwords]
    return ' '.join(processed_list)


def preprocess(s:str, stopwords:Set) -> str:
    """
    - Lowercase the sentence
    - Change "'t" to "not"
    - Isolate and remove punctuations except "?"
    - Remove other special characters
    - Remove stop words except the modals and not
    - Remove trailing whitespace
    """
    s = s.lower()
    # Change 't to 'not'
    s = re.sub(r"\'t", " not", s)
    # Isolate and remove punctuations except '?'
    s = re.sub(r'([\'\"\.\(\)\!\?\\\/\,])', r' \1 ', s)
    s = re.sub(r'[^\w\s\?]', ' ', s)
    # Remove some special characters
    s = re.sub(r'([\;\:\|•«\n])', ' ', s)
    # Remove stopwords except 'not' and 'can'
    s = remove_stopwords(s, stopwords=stopwords)
    # Remove trailing whitespace
    s = re.sub(r'\s+', ' ', s).strip()
    # Uncomment to lemmatize as well
    #     s = lemmatize(s)

    return s