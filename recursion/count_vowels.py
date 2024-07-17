
# count vowels in a string

# string="poorna"
# vowels='aeiou'
# count =0


# def CountVowels(string):
#     count=0
#     vowels='aeiou'
#     string=string.lower()
#     print(string)
#     for s in range(len(string)):
#         if string[s] in vowels:
#             print(string[s])
#             count = count+1
#     return count


# print(CountVowels("poorna"))



def RecurCountVowels(string):
    vowels='aeiou'
    if len(string)==0:
        return 0
    if string[0] in vowels:
        return 1+ RecurCountVowels(string[1:])
    else:
        return  RecurCountVowels(string[1:])

    
print(RecurCountVowels('poorna'))
    
   