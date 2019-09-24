def get_plural(word):

    vowels = ["a", "e", "i", "o", "u"]
    
    if word.endswith("ch"):
        word = word + "es"

    elif word.endswith("sh"):
       word = word + "es"

    elif word.endswith("x"):
       word = word + "es"

    elif word.endswith("s"):
       word = word + "es"

    elif word.endswith("z"):
       word = word + "es"

    elif word.endswith("o"):
       word = word + "es"

    elif word.endswith("f"):
       word = word[:-1] + "ves"

    elif word.endswith("fe"):
       word = word[:-2] + "ves"

    elif word.endswith("y") and word[-2] not in vowels:
       word = word[:-1] + "ies"

    else:
       word = word + "s"
       
    return word