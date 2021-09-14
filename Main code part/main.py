import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import requests
import json
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from pprint import pprint
import subprocess
import winapps
import os
import wolframalpha
import datefinder
import datetime
import winsound


''' My modules'''


'''
for item in winapps.search_installed('Epic Games Launcher'):
    location=item.install_location
    print(location)
    path=location.replace("\","//")
    print(path)
'''



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

what_is_are_question=['what is', 'what are']
where_is_are_question=['where is','where are']
who_is_are_question=['who is','who was']
when_was_did_question=['when was','when did']
which_is_was_question=['which is','which was','which','in which','on which']
open_on_google=['open on','open on google']
weather_questions=['weather at my location','current weather','what is the weather','what is the weather today','what is the current weather','what is the weather at my location',]
temperature_questions=['current temperature','what is the temperature','what is the temperature now','temperature at my location','current temperature at my location','current temperature at my place','current temperature in my area','temperature at my place','temperature in my area','temperature at my area']
temperature_questions2=['what is the current temperature at','current temperature at','temperature in']
read_news=['news','read me the news',"read me today's news","what are today's headlines",'tell me the news','what are the news',"what are today's news"]
notepad=['make a note','remember this','take note','write this','take a note']
file_explorer=['file explorer','this pc','my files','my computer']
gmail=['gmail','show my email','show me my emails','open my emails','open email','new mail for me','check my mail','show me my gmail']
how_are_you_answering_GOOD=['fine','i am doing well','i am fine','i am feeling good','i am doing good','i am alright','going well','perfectly fine','feeling good','doing good']
how_are_you_answering_BAD=['boring','i am not feeling good','not well','not','not feeling','bad','feeling bad','i am not feeling good','awful','really bad','worst']
calculation_questions=['plus','add','subtract','minus','into','multiply','divide','divided by','by','log','antilog','derrivative','integrate']
yes_answering=['yes','yeah','go ahead','proceed','ofcourse','why not','sure','yep']
no_answering=['no','nothing','no nothing','not at all','there is nothing to do','nope','no thank you','no need','not now','not at all','no need of that',"don't need"]

flag=0

def talk(cmd):
    engine.say(cmd)
    engine.runAndWait()

def wolfram(cmmd):
    api_id="4QWQ57-684GP5R98L"
    requester= wolframalpha.Client(api_id)
    requested= requester.query(cmmd)
    answer=next(requested.results).text
    answer=answer[:15]
    print(answer)
    talk("The answer is " + answer)




def note(text):
    date=datetime.datetime.now()
    file_name=str(date).replace(":","-") + "-note.txt"  # removing ":" cause it does not support in file name and also adding the usual text extension
    with open(file_name,"w") as wr: # we use with because it is efficient in exception handling
        wr.write(text)
    subprocess.Popen(["notepad.exe",file_name])

def news_headlines():
    r=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=56bc1062035e4ce5985d673113cb04cc')

    data=json.loads(r.content)
    for i in range(3):
        news_head=data['articles'][i]['title']
        print(news_head)
        talk(i+1)
        talk(news_head)

def news_desc():
    r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=56bc1062035e4ce5985d673113cb04cc')

    data = json.loads(r.content)
    for i in range(3):
        news_head = data['articles'][i]['title']
        news_de=data['articles'][i]['description']
        print(news_head)
        talk(i + 1)
        talk(news_head)
        print(news_de)
        talk(news_de)



def just_temperature():
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')  # To get the ip address of our current location
    ipadd = ip_request.json()['ip']  # json is a text file like file and it will provide output in dictionary format
    print(ipadd)
    url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'  # Here we will be getting our current location based on our current ip address
    geo_request = requests.get(url)
    geo_data = geo_request.json()

    url1 = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2b0f1bd8adfa6d4b6281bb724a268662&units=metric'.format(
        geo_data['city'])
    res = requests.get(url1)
    data = res.json()
    temperature = data['main']['temp']
    print("The current temperature at your location is:",temperature,'°c')
    talk("The current temperature at your location is: "+str(temperature)+'°celcius')

def location():
    r = requests.get("https://get.geojs.io/")  # to check if its connected or not. NOT NEEDED IN OUR PROGRAM

    ip_request = requests.get('https://get.geojs.io/v1/ip.json')  # To get the ip address of our current location
    ipadd = ip_request.json()['ip']  # json is a text file like file and it will provide output in dictionary format
    print(ipadd)
    url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'  # Here we will be getting our current location based on our current ip address
    geo_request = requests.get(url)
    geo_data = geo_request.json()
    print(geo_data['region'])  # it is giving output in dictionary format so we are just taking the detail we need by specifying the key value
    print(geo_data['city'])


def weather():
    r=requests.get("https://get.geojs.io/") #to check if its connected or not. NOT NEEDED IN OUR PROGRAM

    ip_request=requests.get('https://get.geojs.io/v1/ip.json') #To get the ip address of our current location
    ipadd=ip_request.json()['ip'] #json is a text file like file and it will provide output in dictionary format
    print(ipadd)
    url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json' #Here we will be getting our current location based on our current ip address
    geo_request=requests.get(url)
    geo_data=geo_request.json()
    print(geo_data['region']) #it is giving output in dictionary format so we are just taking the detail we need by specifying the key value
    print(geo_data['city'])

    #search="temperature in kerala"
    #url= f"https://www.google.com/search?q={search}"
    #r=requests.get(url)
    #data=BeautifulSoup(r.text,"html.parser")
    #temp=data.find("div",class_="BNeawe").text
    #print(temp)
    #talk(temp)


   # apid = '2b0f1bd8adfa6d4b6281bb724a268662'
    url1 = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2b0f1bd8adfa6d4b6281bb724a268662&units=metric'.format(geo_data['city'])
    res = requests.get(url1)
    data = res.json()
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    day_type = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    print(temperature)
    print(feels_like)
    print(day_type)
    print(wind_speed, 'm/s')
    print('The current temperature at your location is',temperature,'°c .But due to humidity,it feels like',feels_like,'°c and the day will be mostly',day_type,'with a wind speed of',wind_speed,'m/s')
    talk('The current temperature at your location is'+str(temperature)+'°celcius, But due to humidity, it feels like'+str(feels_like)+'°celcius and the day will be mostly '+str(day_type)+',with a vind speed of'+str(wind_speed)+'meter per second')

def alm(cmd):
    dateandtime=datefinder.find_dates(cmd)
    for dandt in dateandtime:
        print(dandt)
    stringtime=str(dandt)
    timealone=stringtime[11:]
    print(timealone)

    hr=timealone[0:2]
    hr=int(hr)

    minu=timealone[3:5]
    minu=int(minu)

    sec=timealone[7:]
    sec=int(sec)
    flag2=0

    print(hr,minu,sec)
    print("Your alarm has been set at " + str(hr) +':'+ str(minu))
    talk("Your alarm has been set at " + str(hr) +':'+ str(minu))
    while True:
        current_hour=datetime.datetime.now().hour
        current_minute=datetime.datetime.now().minute
        if(hr==current_hour):
            if(minu==current_minute):
                if(flag2==0):
                    talk("Your alarm is running")
                    print("Alarm is running")
                    flag2=1
                winsound.PlaySound('F://Projects//Virtual Assistant//alarm sound.mp3',winsound.SND_LOOP)
                #talk("Wake up.... It's time ")
            elif(current_minute>minu):
                talk("Your alarm has been turned off")
                print("Alarm is closing")
                break;


def take_command(flag):
    try:
        with sr.Microphone() as source:
            print("Speak..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if flag==1:
                return command
            elif 'alexa' in command:
                print(command,'first') #for real purpose
                command=command.replace('alexa','')
                if 'hey' in command:
                    command=command.replace('hey','')
                    print(command,'sec') #for debugging
                return command

    except:
        print("Didn't worked")


    #return command    #should add this return command under if 'alexa' condition

def multi_command():
    try:
        with sr.Microphone() as source:
            print("Speak..")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except:
        print("Didn't worked")

'''We used flag here because we need to check two conditions 
if we call the execute assistant from outside the execute assistant function then 
out take command should only detect the command if there is an alexa word in it
Where as when the execute assistant is called from inside the execute assistant itself,
then the value of flag should be 1 because we will not be specifying alexa in out command
we have used it in line number 283,312,324'''

def execute_assistant(flag):

    passing_flag=flag
    command=take_command(passing_flag)


    if 'good morning' in command:
        print('A very Good morning to you')
        talk('A very Good morning to you')

        talk(' ')
        print('How are you feeling today')
        talk('How are you feeling today')
        command=multi_command()


        if(any(i in command for i in how_are_you_answering_BAD)):

            print("I am really sorry to hear that")
            talk("I am really sorry to hear that")
            print("Is there anything I can do to make you feel better")
            talk("Is there anything I can do to make you feel better")
            command=multi_command()
            if(any(i in command for i in no_answering)):
                print("Ok, but I am sure that you will get better")
                talk("Ok, but I am sure that you will get better")
            elif(any(i in command for i in yes_answering)):
                print("What do you want me to do ")
                talk("what do you want me to do")
                flag=1
                execute_assistant(flag)



        elif(any(i in command for i in how_are_you_answering_GOOD)):

            print("Glad to hear that")
            talk("Glad to hear that")
            print("Shall I read the daily morning updates for you ? ")
            talk("Shall I read the daily morning updates for you ?")
            command = multi_command()
            if (any(i in command for i in yes_answering)):
                print('Starting with the weather')
                talk('Starting with the weather   ')

                weather()
                talk('    ')
                print("Moving on to News")
                talk("Moving on to News    ")
                news_desc()
                talk('       ')
                talk("That's all for today          ")
                print(" Is there anything else I have to do for you")
                talk(" Is there anything else I have to do for you")
                command = multi_command()
                if (any(i in command for i in yes_answering)):
                    print("What do I have to do for you")
                    talk("What do I have to do for you")
                    flag=1
                    execute_assistant(flag)
                elif (any(i in command for i in no_answering)):
                    print("Ok, have a nice day :)")
                    talk("Ok, have a nice day")
            elif (any(i in command for i in no_answering)):
                print("Ok, is there anything else I have to do for you")
                talk("Ok, is there anything else I have to do for you")
                command = multi_command()
                if (any(i in command for i in yes_answering)):
                    print("What do I have to do for you")
                    talk("What do I have to do for you")
                    flag=1
                    execute_assistant(flag)
                elif (any(i in command for i in no_answering)):
                    print("Ok, have a nice day :)")
                    talk("Ok, have a nice day")




    elif 'how are you' in command:
        print("I am always good, thank you for asking")
        talk("I am always good, thank you for asking")
        talk(' ')
        print("How are you feeling today")
        talk('How are you feeling today')
        command=multi_command()

        if(any(i in command for i in how_are_you_answering_BAD)):
            print("I am really sorry to hear that")
            talk("I am really sorry to hear that")
            print("Is there anything I can do to make you feel better")
            talk("Is there anything I can do to make you feel better")
            command = multi_command()
            if (any(i in command for i in no_answering)):
                print("Ok, but I am sure that you will get better")
                talk("Ok, but I am sure that you will get better")
            elif(any(i in command for i in yes_answering)):
                print("What do you want me to do ")
                talk("what do you want me to do")
                flag=1
                execute_assistant(flag)

        elif (any(i in command for i in how_are_you_answering_GOOD)):
            print("Glad to hear that")
            talk("Glad to hear that")

   # elif 'joke' or 'jokes' in command:
        #joke=pyjokes.get_joke()
       # print(joke)
       # talk(joke)

    elif 'how to' in command:
        detail=search_wikihow(command,1)
        detail[0].print()
        talk(detail[0].summary)

    elif 'play' in command:
        song=command.replace('play','')
        print(song,'last') #for debugging
        talk('playing' + song)
        print('playing'+ song) #for real purpose
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk("Current time is " + time)
        print("Current time is " + time)
        exit()



    elif 'search on google about' in command:
        print("search on google about")
        detail=command.replace('search on google about','')
        #chromepath = 'C://Users//UK//AppData//Local//Google//Chrome//Application//chrome.exe %s'
        #webbrowser.get(chromepath).open_new_tab(detail+'.com')
        pywhatkit.search(detail)
        talk("This is what i found on the web ")
        print('info in google')
        print(detail)

    elif 'open' in command:
        if 'google' in command:
            print("open on google system")
            detail = command.replace('open','').replace('on google','').replace(' ','')
            chromepath = 'C://Users//UK//AppData//Local//Google//Chrome//Application//chrome.exe %s'
            print(detail+'.com')
            print('opening ' + detail + ' on google')
            talk('opening ' + detail + ' on google')
            webbrowser.get(chromepath).open_new_tab(detail + '.com')

        #Opening windows built in apps

        elif 'notepad' in command:
            subprocess.Popen("notepad.exe")
# the main difference between subprocess.Popen and subprocess.call is that
# subprocess.call will wait while subprocess.Popen will do the job and goes to the
#next line of code
# For eg here when i use subprocess.call it will open notepad and will not go to the
# next lines of code which contain print and talk commands while in subproces.Popen it
# will open and notepad and right after that it will execute the rest of the code lines.
# that's why I used Popen in this code
            print("Opening notepad")
            talk("Opening notepad")

        elif 'calculator' in command:
            subprocess.Popen('calc.exe')
            print("Opening Calculator")
            talk("Opening calculator")

        elif 'command prompt' in command:
            subprocess.Popen('cmd.exe')
            print("Opening Command prompt")
            talk("Opening command prompt")

        elif any(i in command for i in file_explorer):
            subprocess.Popen(['explorer',','])
            print("Opening file explorer")
            talk("Opening file explorer")

        #Opening External apps

        elif 'gmail' in command: #bug : when program stops the google chrome is automatically closing
            mail='gmail'
            chromepath = 'C://Users//UK//AppData//Local//Google//Chrome//Application//chrome.exe %s'
            print('Opening Gmail on google')
            talk('opening gmail on google')
            print("inside if")
            #webbrowser.get(chromepath).open_new_tab(mail + '.com')
            webbrowser.get(chromepath).open(mail + '.com')

        elif 'youtube' in command:
            app = 'Youtube'
            chromepath = 'C://Users//UK//AppData//Local//Google//Chrome//Application//chrome.exe %s'
            print('Opening Youtube on google')
            talk('opening youtube on google')
            webbrowser.get(chromepath).open_new_tab(app + '.com')

        elif 'facebook' in command:
            app="Facebook"
            chromepath = 'C://Users//UK//AppData//Local//Google//Chrome//Application//chrome.exe %s'
            print('Opening Facebook on google')
            talk('opening Facebook on google')
            webbrowser.get(chromepath).open_new_tab(app + '.com')

        elif 'linkedin' in command:
            app = "Linkedin"
            chromepath = 'C://Users//UK//AppData//Local//Google//Chrome//Application//chrome.exe %s'
            print('Opening Linkedin on google')
            talk('opening Linkedin on google')
            webbrowser.get(chromepath).open_new_tab(app + '.com')




    elif any(i in command for i in gmail):
        mail = 'gmail'
        chromepath = 'C://Users//UK//AppData//Local//Google//Chrome//Application//chrome.exe %s'
        print('Opening Gmail on google')
        talk('opening gmail on google')
        webbrowser.get(chromepath).open_new_tab(mail + '.com')
       # webbrowser.get(chromepath).open(mail+'.com')

    elif any(i in command for i in temperature_questions2): #need to solve a bug: when i try to call this elif the above elif is getting executed


        city=command.replace('what is the','').replace('the temperature at','').replace('temperature in','').replace('current temperature','').replace("what's the",'').replace("what is the current temperature at",'').replace('current','').replace('current temperature at','').replace('what is the temperature at','')
        url1 = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2b0f1bd8adfa6d4b6281bb724a268662&units=metric'.format(city)
        res = requests.get(url1)
        data = res.json()
        print(data)
        print(city)
        temperature = data['main']['temp']
        print("The current temperature at"+city+" is:", temperature, '°c')
        talk("The current temperature at"+city+" is" + str(temperature) + '°celcius')


    elif any(i in command for i in temperature_questions):
        just_temperature()
        exit()

    elif any(i in command for i in notepad):
        print("Tell me what do I need to make a note of ")
        talk("Tell me what do I need to make a note of")
        text = multi_command()
        note(text)

        print("I have noted it ")
        talk("I have noted it ")

    elif any(i in command for i in read_news):
        talk("Reading out today's top news")
        news_desc()

    elif 'calculate' in command: #for calculations
        detail=command.replace('calculate','').replace('and','').replace('plus','+').replace('add','+').replace('subtract','-').replace('minus','-').replace('multiply','*').replace('into','*').replace('of','*').replace('divide','').replace('divided by','/').replace('by','/')
        wolfram(detail)

    elif 'convert' in command: # for conversion questions
        pywhatkit.search(command)
        talk("Here is your answer")

    elif 'alarm' in command:
      alm(command)

    if any(i in command for i in weather_questions):
        weather()





    elif any(i in command for i in what_is_are_question) :
        try:
            print("what is wiki")
            detail=command.replace('what is','').replace('what is a','').replace('what are','').replace('what is an','')
            print(detail)
            info=wikipedia.summary(detail,1)
            pywhatkit.search(detail)
            print(info)
            talk(info)
        except:
            print("what is google")
            chromepath='C://Users//UK//AppData//Local//Google//Chrome//Application//chrome.exe %s'
            pywhatkit.search(detail)
            talk("This is what i found for" + detail +"on the web for you ")
            #result=wikipedia.summary(detail,2)
            #talk(result)
            #webbrowser.get(chromepath).open_new_tab('what is ' +detail)
            #print('info in google')

    elif any(i in command for i in where_is_are_question):
        print("where is")
        detail=command.replace('where is','').replace('where are','')
        info=wikipedia.summary(detail,2)
        pywhatkit.search(detail)
        print(info)
        talk(info)

    elif any(i in command for i in who_is_are_question):
        print("who is")
        person=command.replace('who is','').replace('who are','')
        #info=wikipedia.summary(person,1)
        pywhatkit.search(command)
        #print(info)
        #talk(info)

    elif any(i in command for i in when_was_did_question):
        print("when was")
        detail=command.replace('when was','').replace('when did','')
        info=wikipedia.summary(detail,1)
        pywhatkit.search(detail)
        print(info)
        talk(info)

    elif any(i in command for i in which_is_was_question):
        print("which was")
        #detail=command.replace('which was','').replace('which','').replace('which is','')
        #info=wikipedia.summary(detail,1)
        pywhatkit.search(command)
        #print(info)
        #talk(info)
'''
    elif any(i in command for i in notepad):
        print("Tell me what do I need to make a note of ")
        talk("Tell me what do I need to make a note of")
        text = multi_command()
        note(text)

        print("I have noted it ")
        talk("I have noted it ")

    elif any(i in command for i in read_news):
        talk("Reading out today's top news")
        news_desc()

    elif 'calculate' in command: #for calculations
        detail=command.replace('calculate','').replace('and','').replace('plus','+').replace('add','+').replace('subtract','-').replace('minus','-').replace('multiply','*').replace('into','*').replace('of','*').replace('divide','').replace('divided by','/').replace('by','/')
        wolfram(detail)

    elif 'convert' in command: # for conversion questions
        pywhatkit.search(command)
        talk("Here is your answer")

    elif 'alarm' in command:
      alm(command)

    if any(i in command for i in weather_questions):
        weather()
   '''





execute_assistant(flag)