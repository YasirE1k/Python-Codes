def pisagorTriangle():
    
    for x in range(1,101):
        for y in range(1,101):
            c=(x**2+y**2)**(1/2)
            if(c==int(c)):
                print(x,y,int(c))    

pisagorTriangle()








