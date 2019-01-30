                                                            #Checking the speech properties 


import logging
import aiy.audio
import aiy.cloudspeech 
import aiy.voicehat 
import aiy.assistant.grpc 
import time 
from aiy.leds import Leds 
assistant = aiy.assistant.grpc.get_assistant()
def correct():
    leds = Leds()
    rgb= (0,255,0)
    leds.update(Leds.rgb_pattern(rgb))
def wrong():
    leds = Leds()
    rgb= (255,0,0)
    leds.update(Leds.rgb_pattern(rgb))
def nothing():
    leds = Leds()
    rgb= (0,0,0)
    leds.update(Leds.rgb_pattern(rgb))

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

def speechToTextConverter(button,assistant):
    print('Press the button and speak')
    button.wait_for_press()
    print('Listening...')
    text, audio= assistant.recognize()
    if text is None:
        text, audio=speechToTextConverter(button,assistant)
    return text,audio

def analyseQuestion(button,assistant):
    mark=100
    aiy.voice.tts.say("what is the direct opposite direction. in which the sun rise?", lang='en-US', speed=100, pitch=159,volume=100, device='default') 
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("west")>=0:
        correct()
        aiy.voice.tts.say("Perfect.Answer keep going", lang='en-US', speed=100, pitch=200,volume=90, device='default')
        mark+=10
    else:
        mark-=5
        wrong() 
        aiy.voice.tts.say("You are wrong.hey Come on you can do it in next attempt the answer is east", lang='en-US', speed=76, pitch=100,volume=100, device='default')
    if mark>=100:
       mark=100
    time.sleep(1)
    nothing()
    aiy.voice.tts.say("What is the total number of alphabets in english?", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("26")>=0 or text.lower().find("twentysix")>=0:
        mark+=10
        aiy.voice.tts.say("Wow.that's excellent", lang='en-US', speed=100, pitch=200,volume=100, device='default')
        if mark>=100:
           mark=100
        correct()
    else:
        mark-=5
        wrong()
        aiy.voice.tts.say("Sorry you are wrong. good luck for next attempt. the answer is bill gates", lang='en-US', speed=100, pitch=100,volume=100, device='default')
    time.sleep(1)
    nothing()
    if mark>=100:
       mark=100
    aiy.voice.tts.say("Who was the first Prime Minister of India?", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("nehru")>=0 or text.lower().find("jawaharlal")>=0:
        aiy.voice.tts.say("You are rocking man keep it up", lang='en-US', speed=100, pitch=200,volume=100, device='default')
        mark+=10
        correct()
    else:
        mark-=5
        wrong()
    aiy.voice.tts.say("Think twice before answering.see you are wrong this. time the answer is jawaharlal nehru", lang='en-US', speed=100, pitch=100,volume=100, device='default') 
    time.sleep(1)
    nothing()
    if mark>=100:
       mark=100
    aiy.voice.tts.say("Some months have 31 days.  others have 30 days. How many have 28 days?", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower()=="call" or text.lower()=="tell" or text.lower().find("twelve")>=0 or text.find("12")>=0:
        mark+=5
        aiy.voice.tts.say("Haha. thats good you made it", lang='en-US', speed=100, pitch=200,volume=100, device='default')
        correct()
    else:
        mark-=10
        wrong()
        aiy.voice.tts.say("So sad.you are wrong", lang='en-US', speed=100, pitch=100,volume=100, device='default')
        aiy.voice.tts.say("All the 12 months have 28 days", lang='en-US', speed=100, pitch=100,volume=100, device='default')
    time.sleep(2)
    nothing()
    aiy.voice.tts.say("You Are Participating In A Race. You Overtake The Second Person.  What Position Do You finish?", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("second")>=0:
        mark+=5
        aiy.voice.tts.say("You are amazing", lang='en-US', speed=100, pitch=200,volume=100, device='default')
        correct()
    else:
        mark-=10
        wrong() 
        aiy.voice.tts.say("you are wrong. dont worry you can make it at the next attempt", lang='en-US', speed=100, pitch=100, volume=100, device='default')
        aiy.voice.tts.say("If you overtake the second person then you take his second position", lang='en-US', speed=100, pitch=100,volume=100, device='default')
    time.sleep(2)
    nothing()
    aiy.voice.tts.say("How many times can we subtract 10 from 100?", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower()=="1" or text.lower().find("one")>=0:
        mark+=5
        aiy.voice.tts.say("Keep on rocking. lets head on to the next question", lang='en-US', speed=100, pitch=200,volume=100, device='default')
        correct()
    else:
        mark-=10
        wrong()
        aiy.voice.tts.say("Oops. you are wrong. try hard next time", lang='en-US', speed=100, pitch=150,volume=100, device='default')
        aiy.voice.tts.say("Only one time is the answer. Next time u would be subtracting  10 from 90 ", lang='en-US', speed=100, pitch=100,volume=100, device='default')  
    time.sleep(2)
    nothing()
    aiy.voice.tts.say("What colour symbolises peace?", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("white")>=0:
        aiy.voice.tts.say("Gooood" , lang='en-US', speed=100, pitch=200,volume=100, device='default')
        aiy.voice.tts.say("but i guess it is not a tough question to answer", lang='en-US', speed=100, pitch=179,volume=100, device='default')
        mark+=2
        correct()
    else:
        mark-=15
        wrong()
        aiy.voice.tts.say("Sorry for that.You made it wrong . white is the correct answer", lang='en-US', speed=100, pitch=100,volume=100, device='default')
    time.sleep(2)
    nothing() 
    aiy.voice.tts.say("Which animal. is called the Ship of the Desert?", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("camel")>=0:
        mark+=2
        aiy.voice.tts.say("You made it", lang='en-US', speed=98, pitch=200,volume=100, device='default')
        correct()
    else:
        mark-=15
        wrong()
        aiy.voice.tts.say("Sorry. You guessed it wrong. camel was the right answer", lang='en-US', speed=100, pitch=100,volume=100, device='default')
    return mark
def main1():
    button = aiy.voicehat.get_button()
    aiy.audio.get_recorder().start()
    text,audio=speechToTextConverter(button,assistant)
    print (text)
    aiy.voice.tts.say("Hello KIDs", lang ='en-US',speed =70, pitch= 190, volume = 100, device='default')
    aiy.voice.tts.say(" its nice to meet you. My name is SMART TEACHER. and By the way how are you", lang='en-US', speed=100, pitch=140,volume=90, device='default')
    text = None
    while(not text):
        text, audio = assistant.recognize()
    aiy.voice.tts.say("Today is going to be a special day for you kids. do u know why?", lang='en-US', speed=98, pitch=159,volume=100, device='default')
    text = None
    while(not text):
        text, audio = assistant.recognize()
    if(text.lower().find("no")>=0):
        aiy.voice.tts.say("You are going to Learn coding", lang='en-US', speed=100, pitch=159,volume=100, device='default')
        time.sleep(0.3)
        aiy.voice.tts.say("Believe me it’s going to be lot of fun", lang='en-US', speed=100, pitch=159, volume= 100, device= 'default')
    text = None
    while(not text):
        text= assistant.recognize()
    aiy.voice.tts.say("Learning coding at a very young age will help you kids think creatively, reason systematically, and work collaboratively. ", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    time.sleep(0.3)
    text = None
    while(not text):
        text, audio = assistant.recognize()
    aiy.voice.tts.say("Before getting in to coding. can I ask you couple of questions to understand u kids better.", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    time.sleep(1)
    aiy.voice.tts.say("I request 3 kids to come forward and press my head and introduce yourself", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    count=0
    name=[]
    mark=[]
    while(count<3):
        count+=1
        text,audio=speechToTextConverter(button,assistant)
        name.append(text)
        aiy.voice.tts.say(name[-1]+", I appreciate your boldness to come forward for the question, can I ask an IQ question?", lang='en-US', speed=100, pitch=159,volume=100, device='default')
        mark.append(analyseQuestion(button,assistant))
        aiy.voice.tts.say("You may go thanks "+name[-1]+" You are such a sweet person", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    aiy.voice.tts.say("Let me calculate your scores", lang='en-US', speed=88, pitch=159, volume=100, device='default')
    print("Calculating 2%")
    time.sleep(2)
    print("Calculating 30%")
    time.sleep(2)
    print("Calculating 60%")
    time.sleep(2)
    print("Almost over 90%")
    time.sleep(1)
    aiy.voice.tts.say(name[mark.index(max(mark))]+" is the smartest person i have ever met", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    time.sleep(2)
    aiy.voice.tts.say("Now,let us get into tech toys", lang='en-US', speed=98, pitch=159,volume=100, device='default')
    aiy.voice.tts.say("Do you want to ask questions?", lang='en-US', speed=98, pitch=159,volume=100, device='default')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("yes")>=0 or text.find("yeah")>=0:
        print("Ask Questions")
    aiy.voice.tts.say("Now,you can ask me questions and,i shall try to answer them", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    while(text is not "exit"):
       text, audio=speechToTextConverter(button,assistant)
       print(text)
       if text.find("name")>=0 or text.find("who")>=0 or text.find("who")>=0:
          aiy.voice.tts.say("My name is Smart teacher.i am your artificial intelligence teacher", lang='en-US', speed=100, pitch=159,volume=100, device='default')
       elif text.find("where")>=0 or text.find("come")>=0:
          aiy.voice.tts.say("I am currently available in all smart devices. and for now i am programmed to be an artificial intelligence teacher at this moment", lang='en-US', speed=100, pitch=159,volume=100, device='default')
       elif text.find("like maths")>=0:
          aiy.voice.tts.say("Yeah,maths may seem to be difficult but,it is easier when learnt with fun", lang='en-US', speed=78, pitch=170,volume=120, device='default')
       else:
          aiy.audio.play_audio(audio,100)
main1()
