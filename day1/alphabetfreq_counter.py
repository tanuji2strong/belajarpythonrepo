def count(sentence):
	output={}
	for i in sentence:
		print(i)
		if i != ' ':
			output[i]=output.get(i,0)+1

	return output
print(count("pepek cok"))
