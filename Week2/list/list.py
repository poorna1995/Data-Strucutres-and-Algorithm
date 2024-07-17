list=[]
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(10)
list.append(12)

print(list)
list.pop()
print(list)
list[1]=44
print(list)

def iteration(list):
    count =0
    for i in range(len(list)):
        count+=1

    return count

   


print (iteration(list))



