my_list = [56, 89, 21, 56, 85, 236, 559, 58, 47, 251, 5895, 569]
new_list = [j for i, j in enumerate(my_list) if my_list[i]) > my_list[i - 1] and i != 0]
print(new_list)