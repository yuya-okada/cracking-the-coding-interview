def one_three(url):
	new_url = ""
	
	for l in url:
		if l:
			new_url += l
		else:
			new_url += "%20"
			
	return new_url

	
			
print(one_three("aaa bbb ccc dd"))


