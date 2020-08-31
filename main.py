from allmodules import *
from time import sleep

name="Your Name"
Fname="Your Full Name"
wakewords=["Jarvis","jarvis","Javed","Java","yaar","Bhavesh","Sarvesh","janwar","jaan","job","Jaan","Javesh","Jalgaon"]

def initialization():
    while True:
        initi=getsound()
        while initi in wakewords:
            data=getaudio()
            if "hi" in data or "hello" in data or "hey" in data or "hay" in data:
                engine.say("Hey,"+name+". what can I do for you?")
                engine.runAndWait()
                pass

            if "how are you" in data:
                engine.say("My systems work great")
                engine.runAndWait()
                break

            if "who are you" in data:
                engine.say("I am JARVIS , Your personal assistant. I will help you in simplifying different tasks at your command")
                engine.runAndWait()
                break

            if "are you there" in data:
                engine.say("Always at your service,sir!")
                engine.runAndWait()
                break

            if data in wakewords:
                engine.say("Yes sir! how may I help you?")
                engine.runAndWait()
                pass

            if "bye" in data:
                engine.say("Bye sir! Have a good day!")
                engine.runAndWait()
                break 

            if "your gender" in data:
                engine.say("I am a machine that simplifies tasks. I am not a biological creature .Therefore, I have no gender.")
                engine.runAndWait()
                break


            if "who is God" in data:
                engine.say("God is the almighty. He is the creator. My creator is my God.")
                engine.runAndWait()
                break

            if "who is your creator" in data:
                engine.say("My creator is Mr.Aakaash Shroff")
                engine.runAndWait()
                break

            if "who is your god" in data:
                engine.say("My god is Mr.Aakaash Shroff")
                engine.runAndWait()
                break

            if "what is the time" in data or "what's the time" in data or "current time" in data or "time" in data:
                while True:
                    now = datetime.now()
                    current_time = now.strftime("%Hhours%Mminutes and")
                    currsec = now.strftime("%S seconds")
                    currtim = currsec.lstrip('0')
                    currtime = current_time+currtim
                    break
                engine.say("The current time is"+currtime)
                engine.runAndWait()
                break

            if "send an email" in data or "send a mail" in data or "send email" in data or "send mail" in data:
                from maile import mail
                mail()
                break
        

            def wolfram1():
                try:
                    if "calculate" in data.lower() or "solve" in data.lower(): 
                        app_id = "W5823V-UU23UR26LY" 
                        client = wf.Client(app_id) 
    
                        indx = data.lower().split().index('calculate') 
                        query = data.split()[indx + 1:] 
                        res = client.query(' '.join(query)) 
                        answer = next(res.results).text 
                        engine.say("sir The answer is " + answer)
                        engine.runAndWait()
                except:
                    engine.say("Sir I am unable to answer that question")
                    engine.runAndWait()
                    return
            wolfram1()


            if "suggest new password" in data:
                from newpass import randpas
                randpas()
                break
initialization()