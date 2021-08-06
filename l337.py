def hacker_speak(string_input):
    """Simple process that replaces a few characters with numbers, I would like to expand this in the future in order to make it closer to actual L3375P34|<"""

    #Replace A's with 4's
    processed = string_input.replace("A", "4")
    processed = processed.replace("a", "4")

    #Replace E's with 3's
    processed = processed.replace("E", "3")
    processed = processed.replace("e", "3")

    #Replace I's with 1's
    processed = processed.replace("I", "1")
    processed = processed.replace("I", "1")

    #Replace O's with 0's
    processed = processed.replace("O", "0")
    processed = processed.replace("o", "0")

    #Replace S's with 5's
    processed = processed.replace("S", "5")
    processed = processed.replace("s", "5")

    #Return Processed string to where it was called from.
    return processed