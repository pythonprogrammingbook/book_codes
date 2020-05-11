dict1 = {"a":10,"B":20,"C":True,"D":"hello world","e":"PythonBook"}  
dict2 = {key:value for key,value in dict1.items() if key.islower()}  
print(dict2) 
