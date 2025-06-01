#  String Practice
#  1. Take a string from the User
#  2. Calculate its length
#  3. Reverse the string
#  4. Check if it is a palindrome

string = input('Enter a name: ').replace(' ', '').lower()
print(len(string))
print(string[::-1])
if string == string[::-1]:
    print('Yes')
else:
    print('No')
