#python code to demonstrate working of
#alphabets Frequency in String
#using isalphat() + len()
#initializing string
test_str = 'geeksforgeeks!!!$is the best 4 all Geeks 10-0'
#printing original string
print("The original string is: "+str(test_str))
#islaphat() to computation of Alphabets
res = len([ele for ele in test_str if ele.isalpha()])
#printing result
print("Count of Alphabets: "+str(res))