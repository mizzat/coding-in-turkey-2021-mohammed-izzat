import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
x=0
while(x<1):
    def whereIsMyFood():

        item=str(input("What are you looking for to eat?\n"))
        item=item.lower()
        fridge=["apple","orange","banana","lemon","cherry","watermelon"]
        for x in fridge:
            if x == item:
                print(x)
                MessageBox(None,"This is your " + x + "!",x + " finder",0)
                break
            
        if x!=item : print("-1")

    whereIsMyFood()
