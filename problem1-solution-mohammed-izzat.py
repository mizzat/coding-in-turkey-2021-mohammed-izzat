import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
x=0
while(x<1):
    found=0
    notfound=0
    def validateRecipe():
        fridge = ['tomato', 'banana', 'apple', 'onion', 'cucumber', 'lettuce', 'olives']
        ingredients =input("Type the ingredients with space between each other:\n")
        ingredients=ingredients.lower()
        ingredients =ingredients.split(" ")
        global found
        global notfound
        for i in ingredients:
            for f in fridge:
                if i == f:
                    print(i + " : True")
                    found+=1
                    break
            if i != f:
                print(i + " : False")
                notfound=notfound+1
        found=str(found)
        notfound=str(notfound)
        MessageBox(None,"Found: " + found + "\nNotfound: "+ notfound , "Final result", 0)
    validateRecipe()
