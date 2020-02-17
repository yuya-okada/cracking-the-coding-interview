def one_two(word1, word2):
	hash={}
	for l in word1:
		if l in hash:
			hash[l] += 1
		else:
			hash[l] = 1
				
	for m in word2:
		if m not in hash:
			return False
		elif hash[m] == 0:
			return False
		else:
			hash[m] -= 1
	

	for i, val in hash.items():
		if val != 0:
			return False
			
	return True
	
	
print(one_two("abcde", "acedb"))
print(one_two("abcde", "acedbe"))
print(one_two("abcde", "aced"))
print(one_two("abcde", "acfdb"))
