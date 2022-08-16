#week5b challenge
string = input("Enter the String: ").lower()
word_list = string.split()
word_list.sort()

print(" -----------Sorted words of String are:--------------")
for i in word_list:
    print(i)