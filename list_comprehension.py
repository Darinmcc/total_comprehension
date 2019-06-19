my_numbers = [1, 2, 3, 4, 5, 6, 7]

numbersby100 = []

print("---------------")
print("ORIGINAL LIST:", my_numbers)

print("---------------")
print("TOTAL COMPREHENSION...")


for numbers in my_numbers:
    numbersby100.append(numbers * 100)

print("MAPPED LIST:", numbersby100)

print("---------------")

filtered_list = [numbers for numbers in my_numbers if numbers  > 3]

print("FILTERED LIST W/ MATCHES:", filtered_list)

print("---------------")

unfiltered_list = [numbers for numbers in my_numbers if numbers not in my_numbers]

print("FILTERED LIST W/O MATCHES:", unfiltered_list)

print("---------------")

#mappednfiltered = [nums for nums in numbersby100 if nums > 300]
#print(mappednfiltered)


print("MAPPED AND FILTERED LIST:", mapnfilt)


#Use mapping capabilities to multiply each number by 100 (e.g. [100, 200, 300, 400, 500, 600, 700])
#Use filtering capabilities to return only the numbers greater than three (e.g. [4, 5, 6, 7])
#Use filtering capabilities to return only the numbers greater than eight (e.g. [])
#Use mapping and filtering capabilities to return only the numbers greater than three, each multiplied by 100 (e.g. [400, 500, 600, 700])


#--------------
#ORIGINAL LIST: [1, 2, 3, 4, 5, 6, 7]
#--------------
#TOTAL COMPREHENSION...
#--------------
#MAPPED LIST: [100, 200, 300, 400, 500, 600, 700]
#--------------
#FILTERED LIST W/ MATCHES: [4, 5, 6, 7]
#--------------
#FILTERED LIST W/O MATCHES: []
#--------------
#MAPPED AND FILTERED LIST: [400, 500, 600, 700]