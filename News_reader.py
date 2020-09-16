# Read news paper for me

import requests
import pyttsx3
import pyautogui as pag
import json


def Speak(text,r,v):
    # global r,voc
    engine = pyttsx3.init() # object creation
    # try:
    # except Exception as e:
    #     print("Python Module pyttsx3 problem")
        # input("Press Enter Key")
        # exit()
    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', int(r))     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[int(v)].id)   #changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def writefile(L):
    for i in range(len(L)):
        L[i] = L[i] + "\n" 
    with open("set.txt","w") as f:
        f.writelines(L)


def start():
    while 1:
        with open("set.txt") as f:
            L = f.readlines()
        for i in range(len(L)):
            L[i] = L[i].replace("\n","")
        print(L)
        r , v = L[0] , L[1]
        while 1:
            Choose  = pag.confirm(text='Please Select Any One', title='Text to Speech Conveter', buttons=['Set Speak Rate', 'Change Voice' ,"Read News","Exit"])
            if  Choose == 'Set Speak Rate':
                while 1:
                    r = pag.prompt("Enter the Rate of the Speech bewwten 0 to 300","Speech RATE")
                    if r.isdigit():
                        L[0] = r
                        break
                    else:
                        pag.alert(text = "Entered wrong input try again", title = "Wrong input")
                        continue
                break

            
            if Choose == 'Change Voice':
                voc = pag.confirm(text="Select the Voice.", title="Voice", buttons = ['MALE','FEMALE'])
                if voc == 'MALE':
                    L[1] = "0"
                    print(L)
                if voc == 'FEMALE':
                    L[1] = "1"
                    print(L)
                break

            if Choose == "Read News":
                check_conn(r,v)
                break

            if Choose == "Exit":
                exit()
        writefile(L)
        continue

def check_conn(r,v):
    url = ('http://newsapi.org/v2/top-headlines?'
            'country=in&'
            'apiKey=GET_YOUR_OWN_API_KEY_FROM_NEWSAPI.COM')
    try:        
        news_json = requests.get(url).text
        readnews(news_json,r,v)
    except:
        pag.alert(text = "Check Your Internet Conectivity" , title = "!!Error")
        exit()

def readnews(news_json,r,v):  
    news_dict = json.loads(news_json)
    arts = news_dict["articles"]
    Choose  = pag.confirm(text='READ ONLY.......?', title='Read News', buttons=['Headlines', "Headlines & description" ,"Exit"])
    if Choose == "Headlines":
        Speak("Reading HeadLines",r,v)
        for articles in arts:
            print(articles["title"])
            Speak(articles["title"],r,v)
            Speak("moving to next Headline.. ",r,v)
        Speak("That's All For Todays News......",r,v)

    if Choose == "Headlines & description":
        Speak("Reading HeadLines & description",r,v)
        for articles in arts:
            Speak("Headline...",r,v)
            print(articles["title"])
            Speak(articles["title"],r,v)
            Speak("description....",r,v)
            print(articles["description"])
            Speak(articles["description"],r,v)
            Speak("moving to next News... ",r,v)
        Speak("That's All For Todays News......",r,v)
        

def main():
    start()

if __name__ == "__main__":
    try:
        with open("set.txt","w") as f:
            f.write("200\n1")
    except:
        pass
    main()