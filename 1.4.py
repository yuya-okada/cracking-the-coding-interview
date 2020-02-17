def one_three(text):
	hash = {}
	
	text = text.lower()
	
	for l in text:
		if l == " ":
			continue
			
		if l in hash:
			if hash[l] >= 3:
				return False
				
			hash[l] += 1
		else:
			hash[l] = 1
			
	
	is_one_exists = False
	
	for i, val in hash.items():
		if val == " ":
			continue
			
		if val == 2:
			continue
			
		elif val == 1:
			if is_one_exists:
				return False
			else:
				is_one_exists = True
				
		else:
			return False
			
			
	return True


print(one_three("Tact Coa"))
print(one_three("tacococ"))
