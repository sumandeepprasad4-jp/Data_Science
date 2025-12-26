import re
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", numbers)
data = " ".join(str(x) for x in numbers)
all_nums = re.findall(pattern=r"\d+", string=data)
all_nums = [int(x) for x in all_nums]
first_five = all_nums[:5]
print("Extracted first five elements:", first_five)
reversed_first_five = first_five[::-1]
print("Reversed extracted elements:", reversed_first_five)