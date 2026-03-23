def func5(str) :
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    setstr = set(str)
    return alphabets <= setstr

print("a" , "Is program:" , "Yes" if func5("a") else "No")
str = "The quick brown fox jumps over the lazy dog"
print(str, "Is program:" , "Yes" if func5(str) else "No")
