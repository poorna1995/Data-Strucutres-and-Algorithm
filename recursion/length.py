# count length of the string

# def countString(string):
#     count=0
#     for s in string:

#         count=count+1
#     return count
# print(countString('poorna'))


def recursiveCount(string):
    if len(string)==0:
        return 0
    return 1+ recursiveCount(string[1:])

print(recursiveCount('poorna'))
