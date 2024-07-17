# string="poorna Praneesha "

# def removeTandS(string):
#     result=''
#     for s in string:

#         if s!= ' ' and s!='\t':
#             result = result+s
#     return result
            

# print(removeTandS('poorna P\traneesha'))




def removeTadSRecur(s):
    if len(s)==0:
        return ''
    if s[0] !=' ' and s[0] !='\t':
        return s[0]+ removeTadSRecur(s[1:])
    else:
        return removeTadSRecur(s[1:])


print(removeTadSRecur(' Poorna Pran sae\t '))

