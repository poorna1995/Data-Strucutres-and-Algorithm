#access the values using key


def get_value_by_key(hash_function, hash_table, key):
    hashed_index = hash_function.hash(key)
    if hashed_index in hash_table:
        for k, v in hash_table[hashed_index]:
            if k == key:
                return v
    return None

# Test the access function
test_keys = ['poorna', 'chandana', 'durgaharish', 'Indhu Priya', 'chandran', 'nonexistent']

for key in test_keys:
    value = get_value_by_key(hash_function, hash_table, key)
    print(f"Key: {key}, Retrieved Value: {value}")