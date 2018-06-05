
nums = [1,2,3,4,5,6,7,8,9]

new_list = []

for num in nums:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)

new_list2 = [n for n in nums if n % 2 == 0]
print(new_list2)