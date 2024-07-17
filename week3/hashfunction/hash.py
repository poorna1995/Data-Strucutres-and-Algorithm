# import random

# class UniversalHashFunction:
#     def __init__(self, p, m):
#         self.p = p
#         self.m = m
#         self.a = random.randint(1, p - 1)
#         self.b = random.randint(0, p - 1)
    
#     def hash(self,x):
#         return((self.a*x+self.b)%self.p)%self.m
    

# p=10000019
# m=200
# hash_function=UniversalHashFunction(p,m)
# print(f"Chosen values for a: {hash_function.a}, b: {hash_function.b}")


# values=[10,20,30,40,50]

# # Calculate hashed values
# hashed_values = [hash_function.hash(value) for value in values]




# # Display the hashed values
# for value, hashed in zip(values, hashed_values):
#     print(f"Value: {value}, Hashed Value: {hashed}")
    
  


import random

class UniversalHashFunction:
    def __init__(self, p, m):
        self.p=p
        self.m=m
        self.a=random.randint(1,p-1)
        self.b=random.randint(0,p-1)
    
    def hash(self,x):
        x_int = sum(ord(char) for char in x)
        return((((self.a*x_int)+self.b)%self.p)%self.m)




p=10000029
m=200
hash_function=UniversalHashFunction(p,m)

print(f"chosen values a:{hash_function.a} and b:{hash_function.b}")

values=['poorna','chandana','poorn','durgaharish','Indhu Priya','chandran']
hashed_values=[hash_function.hash(value) for value in values]

print(hashed_values)
 

for value,hashed in zip(values,hashed_values):
    print(f"Value: {value} ,Hashed: {hashed}")



print("******************************")

# Example key-value pairs to hash
key_value_pairs = [
    ('poorna', 25),
    ('chandana', 32),
    ('durgaharish', 19),
    ('Indhu Priya', 45),
    ('chandran', 28)
]

# Create a hash table (dictionary) to store values
hash_table = {}

# Hash keys and store values in the hash table
for key, value in key_value_pairs:
    hashed_index = hash_function.hash(key)
    if hashed_index not in hash_table:
        hash_table[hashed_index] = []
    hash_table[hashed_index].append((key, value))

# Display the hash table contents
for index, items in hash_table.items():
    print(f"Hashed Index: {index}")
    for key, value in items:
        print(f"  Key: {key}, Value: {value}")



print("++++++++++++++++++++++++++++++++++++++++++++++++++++")


