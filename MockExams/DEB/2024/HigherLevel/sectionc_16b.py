#
# DEB Exams 2024 Q16B
#

inputVar = input('Please provide the word to check ')
print (inputVar)
print(inputVar[::-1])

if inputVar.lower() == inputVar[::-1].lower():
    print('Yes ', inputVar, ' is a palindrome')
else:
    print('No ', inputVar, ' is not a palindrome')



