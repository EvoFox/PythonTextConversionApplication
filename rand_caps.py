from random import randint

def rand_caps(string_input):
    processed = ""
    
    designate = randint(1, 100)
    
    for element in string_input:
        designate = randint(1, 100)
        if designate % 2 == 0:
            processed += element
        else:
            processed += element.upper()

    return processed