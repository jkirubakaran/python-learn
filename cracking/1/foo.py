str = 'ra da r2'
str_dict = {}

for c in str:
    if c in str_dict:
        str_dict[c] = str_dict[c] + 1
    else:
        str_dict[c] = 1

num_of_odd_keys = 0 
for key in str_dict:
    if str_dict[key] % 2 == 1:
        num_of_odd_keys += 1

if num_of_odd_keys > 1:
    print("not a palindrome")





