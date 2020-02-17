def is_all_unique(word):
	hash = {}
	for l in word:
		if l in hash:
			return False
		
		hash[l] = True
	
	return True


print(is_all_unique("abcdefg"))
print(is_all_unique("aabcdefg"))
