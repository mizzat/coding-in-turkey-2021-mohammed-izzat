import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW

x=0
while(x<1):
    def validateRecipeWithQuantity():

        fridge = {'tomato': 3, 'banana': 2, 'apple': 0, 'onion': 5, 'cucumber': 1, 'lettuce': 3, 'olives': 1}

        ingredients =input("Type the ingredients with space between each other\n(e.g.: tomato 1 onion 3):\n")
        ingredients=ingredients.lower()
        ingredients =ingredients.split(" ")

        ingredientskeys=list()
        ingredientsvalues=list()

        for n in range(len(ingredients)):
            if n % 2 !=0 :
                ingredientsvalues.append(ingredients[n])

            elif n % 2 == 0:
                ingredientskeys.append(ingredients[n])

        ingredientsvalues = list(map(int, ingredientsvalues))

        ingredientsdict=dict(zip(ingredientskeys,ingredientsvalues))

        Foundcount=len(ingredientsdict)
        for x,y in ingredientsdict.items():
            for i,j in fridge.items():
                if x == i and y <= j:
                    print(x + ": True")
                    Foundcount -= 1


        if Foundcount == 0:
            MessageBox(None, "All found", "Hey Chef", 0)
        else:
            MessageBox(None, "Sorry Chef", "):", 0)


    validateRecipeWithQuantity()
