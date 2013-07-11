#Finding the borders of the string 
def solution(s):
    n = len(s)
	if s[:3] == s[-3:]:
		if s.count(s[:3]) > 2:
			return len(s[:3])
		else:
			return 0
	elif s[:2] == s[-2:]:
		if s.count(s[:2]) > 2:
			return len(s[:2])
		else:
			return 0
	elif s[:1] == s[-1:]:
		if s.count(s[:1]) == 2:
			return 0
		else:
			return 0
	else:
		return 0

print solution(raw_input())
