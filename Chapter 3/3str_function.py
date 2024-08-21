name = 'Jogindar is the world baggest super powered enthusist'

print(len(name))
print(name.endswith("dar"))
print(name.startswith("Jo"))  #This function is case sensitive
print(name.capitalize())  #Capitalize the starting chacater of the word

index = name.find("world")
print(index)

replace_str = name.replace("world", "India")
print(replace_str)
