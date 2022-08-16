#week5a challenge
def isPalindrome(s):
	return s == s[::-1]
s = "level"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
