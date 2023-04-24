# we have str1 = "abcd" , write the code so tha the output is a ab abc abcd b bc bcd c cd d

str1 = "abcd"

def sub_str(str1):
    for i in range(len(str1)):
        for j in range(i+1,len(str1)+1):
            print(str1[i:j],end = " ")

sub_str(str1)

