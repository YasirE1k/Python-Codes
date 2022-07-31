import random

class command():
    def __init__(self,tv_situation="Closed",tv_sound=0,channel_list=["TRT"],channel="Trt"):
        self.tv_situation=tv_situation
        self.tv_sound=tv_sound
        self.channel_list=channel_list
        self.channel=channel

    def openTv(self):
        self.tv_situation="Opened"
    def closeTv(self):
        self.tv_situation="Closed"
    def sound_settings(self):
        while True:
            print("exit to q")
            choosing=input("+ or -")
            if(choosing=="q"):
                break
            elif(choosing=="+"):
                if(self.tv_sound!=31):
                    self.tv_sound+=1
            elif(choosing=="-"):
                if(self.tv_sound!=0):
                    self.tv_sound-=1
            else:
                print("Invalid Process") 
    def add_channel(self,data):
        self.channel_list.append(data)
    def __len__(self):
        return len(self.channel_list) 
    def random_Channel(self):
        randomm=random.randint(0,len(self.channel_list)-1)
        self.channel=self.channel_list[randomm]
        print("Channel is {} right now".format(self.channel))
    def __str__(self):
        return "Tv situation:{}\nTv sound:{}\nChannel list:{}\nChannel:{}".format(self.tv_situation,self.tv_sound,self.channel_list,self.channel)

command1=command()

print("""1-Open Tv\n2-Close Tv\n3-SoundSettings\n4-AddChannel\n5-LearnChannelNumber\n6-PassRandomChannel
7-TvKnowledges\nPress q to exit
""")

while True:
    process=input("Select the process")
    if(process=="q"):
        break
    elif(process=="1"):
        command1.openTv()
    elif(process=="2"):
        command1.closeTv()
    elif(process=="3"):
        command1.sound_settings()
    elif(process=="4"):
        channel_names=input("Enter the channels with the comma")
        for i in channel_names.split(","):
            command1.add_channel(i)
    elif(process=="5"):
        print(len(command1))
    elif(process=="6"):
        command1.random_Channel()
    elif(process=="7"):
        print(command1)
    else:
        print("Invalid Process")
