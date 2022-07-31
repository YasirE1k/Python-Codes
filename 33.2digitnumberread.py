def read(nmbr):
    onesdigit=["","one","two","three","four","five","six","seven","eight","nine"]
    tensdigit=["","ten","twenty","thirty","fourty","fivety","sixty","seventy","eighty","ninety"]

    print(tensdigit[nmbr//10],onesdigit[nmbr%10])
    
a=int(input("Enter 2 digit number"))

read(a)
