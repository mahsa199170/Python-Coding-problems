sentence = "There is A Greate Chocate Store Over There"

def check_capital(sentence):
    count = 0
    new_s = sentence.replace(" ","")
    for letter in new_s:
        if letter == letter.upper():
            count +=1
    return count


print(check_capital(sentence))


# -------------------------------------------------

def check_capital1(sentence):
    count = 0
    new_s = sentence.replace(" ","")
    for letter in new_s:
        if letter.isupper():
            count +=1
    return count


print(check_capital1(sentence))