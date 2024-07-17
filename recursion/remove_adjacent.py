#  remove ADJACENT

# def removeAdjacent(string):
#     result=''
#     for i in range(len(string)-1):
#         if string[i] == string[i+1]:
#             result=result+string[i]
#     return result

# print(removeAdjacent('abbcceezz'))




def removeAdjacent(string):
    if not string:
        return ""
    
    result = string[0]
    
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            result += string[i]
    
    return result

print(removeAdjacent('abbcceezz'))




def removeAdjacentRecur(string):
    if len(string) == 0:
        return 0
    if len(string)==1:
        return string
    if string[0] == string[1]:
        return removeAdjacentRecur(string[1:])
    else:
        return string[0] + removeAdjacentRecur(string[1:])


print(removeAdjacentRecur('abbcceezz'))