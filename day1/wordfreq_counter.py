x = "Budi Doremi adalah anak ganteng"
y={}
z=x.split()
print(z)
for i in z:
	if i in y:
		y[i]+=1
	else:
		y[i]=1
#lol
print(y)
