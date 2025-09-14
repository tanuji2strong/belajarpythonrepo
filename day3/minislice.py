s = "HelloWorld"
print(s[0:5])   # 'Hello'
print(s[-5:])   # 'World'
print(s[::-1]+'\n')  # 'dlroWolleH'



#s[start:end:step]



def safe_slice(teks,start,end):
    try: 
        return teks[start:end]
    
    except TypeError:
        return ("Error, insert a String.")
print(safe_slice(5,1,5))