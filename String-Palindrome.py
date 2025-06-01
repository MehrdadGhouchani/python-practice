string = input('Enter a name: ').replace(' ', '').lower()
print(len(string))
print(string[::-1])
if string == string[::-1]:
    print('Yes')
else:
    print('No')
