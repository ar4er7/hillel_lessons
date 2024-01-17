original_list = ['first', 'last']

if len(original_list)>1:
    last_symbol = original_list[-1]
    original_list.pop(-1)
    new_list = original_list.insert(0, last_symbol)

print(original_list)



