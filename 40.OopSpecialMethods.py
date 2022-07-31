class book():
    def __init__(self,name,writer,page_number,type):
        self.name=name
        self.writer=writer
        self.page_number=page_number
        self.type=type

book1=book("Of Mice and Man","John Steinbeck",107,"fiction")

class book():
    def __init__(self,name,writer,page_number,type):
        self.name=name
        self.writer=writer
        self.page_number=page_number
        self.type=type
    def __str__(self):
        return "Name: {}\n Writer: {}\n Page_number:{}\nType: {}".format(self.name,self.writer,self.page_number,self.type)

book2=book("Of Mice and Man","John Steinbeck",107,"fiction")
print(book2)


class book():
    def __init__(self,name,writer,page_number,type):
        self.name=name
        self.writer=writer
        self.page_number=page_number
        self.type=type
    def __str__(self):
        return "Name: {}\n Writer: {}\n Page_number:{}\nType: {}".format(self.name,self.writer,self.page_number,self.type)
    def __len__(self):
        return self.page_number

book3=book("Of Mice and Man","John Steinbeck",107,"fiction")

print(len(book3))


class book():
    def __init__(self,name,writer,page_number,type):
        self.name=name
        self.writer=writer
        self.page_number=page_number
        self.type=type
    def __str__(self):
        return "Name: {}\n Writer: {}\n Page_number:{}\nType: {}".format(self.name,self.writer,self.page_number,self.type)
    def __len__(self):
        return self.page_number
    def __del__(self):
        print("It was deleted")

book4=book("Of Mice and Man","John Steinbeck",107,"fiction")

del book4
#print(book4)


















