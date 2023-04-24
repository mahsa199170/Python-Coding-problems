# if we want to count the number of a specific word in a sentence
# # e.g we want to count the word "world" in a sentence

sentence = "Hello dear World be good to people from all over the world"


# FIRST APPROACH

def count_word(sentence):
    mylist = sentence.lower().split(" ")
    count = 0
    for i in mylist:
        if i == "world":
            count += 1
    return count


print(count_word(sentence))



#-------------------------------------

# SECOND APPROACH

def count_word(sentence):
    mylist = sentence.lower().split(" ")
    dict = {}

    for i in mylist:
        if i in dict:
            dict[i] +=1
        else:
            dict[i] = 1

    for key, value in dict.items():
        print(f"{key} : {value}")


print(count_word(sentence))
