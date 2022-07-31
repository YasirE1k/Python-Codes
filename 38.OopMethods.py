class programmer():
    def __init__(self,name,surname,number,wage,languages):
        self.name=name 
        self.surname=surname
        self.number=number
        self.wage=wage
        self.languages=languages

    def showtheknowledges(self):
        print("""**Programmer Knowledges**
        name={}
        surname={}
        number={}
        wage={}
        languages={}
        """.format(self.name,self.surname,self.number,self.wage,self.languages))
    def increasethewage(self):
        self.wage+=500
    def addthelanguage(self,new_language):
        self.languages.append(new_language)  

programmer1=programmer("John","Wood",1234,3000,["Java","C","Python"])

programmer1.showtheknowledges()
programmer1.increasethewage()
programmer1.showtheknowledges()
programmer1.addthelanguage("C++")
programmer1.showtheknowledges()
