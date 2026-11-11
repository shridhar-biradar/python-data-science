# Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.

pos_list = [1,2,-2,3,4,5,-1,6,7,8,-9,9,10,11,13,-12]

lst_comp=[i**2 for i in pos_list if i>0 ]
lst_comp=lst_comp[:10]
print('first 10 positive integer square: ', lst_comp)

# Create a new list containing the squares of the first 10 negative integers using a list comprehension. Print the new list.

lst_comp2=[i**2 for i in pos_list if i<0 ]
lst_comp2=lst_comp2[:10]
print('first 10 negeative integer square: ', lst_comp2)


# Create a new list containing the squares of the first 10 even integers using a list comprehension. Print the new list.
even_lst = [x**2 for x in range(1,40) if x%2==0]
print(f'even integer square {even_lst[:10]}')

# Create a new list containing the squares of the first 10 odd integers using a list comprehension. Print the new list.
odd_lst = [y*y for y in range(1,30) if y%2!=0 ]
print(f'odd integer square {odd_lst[:10]}')