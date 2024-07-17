# iterative 
#poorna

# reverse the string


# def reverseStringIteration(string):
#     reverse=''
#     # while len(string)-1>0:
#     #     string[]
#     length=len(string)-1

#     while length>=0:
#         reverse=reverse+string[length]
#         length-=1
#     return reverse


# print(reverseString('poorna'))


# recurssion of reverse

def reverseString(string):
    # print(string)
    length=len(string)
    print(string[:-1])
   
    #  base case
    if len(string)==0:
        return ""
    return string[-1]+ reverseString(string[:-1])
        

print(reverseString('hello'))


# #poorna


def iterationReverseString(string):
    reverse = ''
    length=len(string)
    while length>=0:
        reverse=reverse+string[length-1]
        length=length-1
    return reverse


print(iterationReverseString("Poorna Praneesha"))


        

