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
    aiy.voice.tts.say("what is the direct opposite direction. in which the sun rise?") 
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("west")>=0:
        correct()
        aiy.audio.say("Perfect.Answer keep going")
        mark+=10
    else:
        mark-=5
        wrong() 
        aiy.audio.say("You are wrong.hey Come on you can do it in next attempt the answer is east")
    if mark>=100:
       mark=100
    time.sleep(1)
    nothing()
    aiy.audio.say("What is the total number of alphabets in english?"')
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("26")>=0 or text.lower().find("twentysix")>=0:
        mark+=10
        aiy.audio.say("Wow.that's excellent")
        if mark>=100:
           mark=100
        correct()
    else:
        mark-=5
        wrong()
        aiy.audio.say("Sorry you are wrong. good luck for next attempt. the answer is bill gates")
    time.sleep(1)
    nothing()
    if mark>=100:
       mark=100
    aiy.audio.say("Who was the first Prime Minister of India?")
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("nehru")>=0 or text.lower().find("jawaharlal")>=0:
        aiy.audio.say("You are rocking man keep it up")
        mark+=10
        correct()
    else:
        mark-=5
        wrong()
    aiy.audio.say("Think twice before answering.see you are wrong this. time the answer is jawaharlal nehru") 
    time.sleep(1)
    nothing()
    if mark>=100:
       mark=100
    aiy.audio.say("Some months have 31 days.  others have 30 days. How many have 28 days?")
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower()=="call" or text.lower()=="tell" or text.lower().find("twelve")>=0 or text.find("12")>=0:
        mark+=5
        aiy.audio.say("Haha. thats good you made it")
        correct()
    else:
        mark-=10
        wrong()
        aiy.audio.say("So sad.you are wrong")
        aiy.audio.say("All the 12 months have 28 days")
    time.sleep(2)
    nothing()
    aiy.audio.say("You Are Participating In A Race. You Overtake The Second Person.  What Position Do You finish?")
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("second")>=0:
        mark+=5
        aiy.audio.say("You are amazing")
        correct()
    else:
        mark-=10
        wrong() 
        aiy.audio.say("you are wrong. dont worry you can make it at the next attempt")
        aiy.audio.say("If you overtake the second person then you take his second position")
    time.sleep(2)
    nothing()
    aiy.audio.say("How many times can we subtract 10 from 100?")
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower()=="1" or text.lower().find("one")>=0:
        mark+=5
        aiy.audio.say("Keep on rocking. lets head on to the next question")
        correct()
    else:
        mark-=10
        wrong()
        aiy.audio.say("Oops. you are wrong. try hard next time")
        aiy.audio.say("Only one time is the answer. Next time u would be subtracting  10 from 90 ")  
    time.sleep(2)
    nothing()
    aiy.audio.say("What colour symbolises peace?")
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("white")>=0:
        aiy.audio.say("Gooood")
        aiy.audio.say("but i guess it is not a tough question to answer")
        mark+=2
        correct()
    else:
        mark-=15
        wrong()
        aiy.audio.say("Sorry for that.You made it wrong . white is the correct answer")
    time.sleep(2)
    nothing() 
    aiy.audio.say("Which animal. is called the Ship of the Desert?")
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("camel")>=0:
        mark+=2
        aiy.audio.say("You made it")
        correct()
    else:
        mark-=15
        wrong()
        aiy.audio.say("Sorry. You guessed it wrong. camel was the right answer")
    return mark
def main1():
    button = aiy.voicehat.get_button()
    aiy.audio.get_recorder().start()
    text,audio=speechToTextConverter(button,assistant)
    print (text)
    aiy.audio.say("Hello KIDs")
    aiy.audio.say(" its nice to meet you. My name is SMART TEACHER. and By the way how are you")
    text = None
    while(not text):
        text, audio = assistant.recognize()
    aiy.audio.say("Today is going to be a special day for you kids. do u know why?"')
    text = None
    while(not text):
        text, audio = assistant.recognize()
    if(text.lower().find("no")>=0):
        aiy.audio.say("You are going to Learn coding"')
        time.sleep(0.3)
        aiy.audio.say("Believe me it’s going to be lot of fun")
    text = None
    while(not text):
        text= assistant.recognize()
    aiy.audio.say("Learning coding at a very young age will help you kids think creatively, reason systematically, and work collaboratively. ", lang='en-US', speed=100, pitch=159,volume=100, device='default')
    time.sleep(0.3)
    text = None
    while(not text):
        text, audio = assistant.recognize()
    aiy.audio.say("Before getting in to coding. can I ask you couple of questions to understand u kids better.")
    time.sleep(1)
    aiy.audio.say("I request 3 kids to come forward and press my head and introduce yourself")
    count=0
    name=[]
    mark=[]
    while(count<3):
        count+=1
        text,audio=speechToTextConverter(button,assistant)
        name.append(text)
        aiy.audio.say(name[-1]+", I appreciate your boldness to come forward for the question, can I ask an IQ question?")
        mark.append(analyseQuestion(button,assistant))
        aiy.audio.say("You may go thanks "+name[-1]+" You are such a sweet person")
    aiy.audio.say("Let me calculate your scores")
    print("Calculating 2%")
    time.sleep(2)
    print("Calculating 30%")
    time.sleep(2)
    print("Calculating 60%")
    time.sleep(2)
    print("Almost over 90%")
    time.sleep(1)
    aiy.audio.say(name[mark.index(max(mark))]+" is the smartest person i have ever met")
    time.sleep(2)
    aiy.audio.say("Now,let us get into tech toys")
    aiy.audio.say("Do you want to ask questions?")
    text,audio=speechToTextConverter(button,assistant)
    print(text)
    if text.lower().find("yes")>=0 or text.find("yeah")>=0:
        print("Ask Questions")
    aiy.audio.say("Now,you can ask me questions and,i shall try to answer them")
    while(text is not "exit"):
       text, audio=speechToTextConverter(button,assistant)
       print(text)
       if text.find("name")>=0 or text.find("who")>=0 or text.find("who")>=0:
          aiy.audio.say("My name is Smart teacher.i am your artificial intelligence teacher")
       elif text.find("where")>=0 or text.find("come")>=0:
          aiy.audio.say("I am currently available in all smart devices. and for now i am programmed to be an artificial intelligence teacher at this moment", lang='en-US', speed=100, pitch=159,volume=100, device='default')
       elif text.find("like maths")>=0:
          aiy.audio.say("Yeah,maths may seem to be difficult but,it is easier when learnt with fun", lang='en-US', speed=78, pitch=170,volume=120, device='default')
       else:
          aiy.audio.play_audio(audio,100)
main1()
