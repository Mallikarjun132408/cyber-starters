pwd = input("Enter a password to check: ").strip()
score = 0
if len(pwd) >= 8: score += 1
if any(c.islower() for c in pwd): score += 1
if any(c.isupper() for c in pwd): score += 1
if any(c.isdigit() for c in pwd): score += 1
if any(not c.isalnum() for c in pwd): score += 1

labels = {5:"Very strong",4:"Strong",3:"Okay",2:"Weak",1:"Very weak",0:"Terrible"}
print("Score:", score, "-", labels.get(score))