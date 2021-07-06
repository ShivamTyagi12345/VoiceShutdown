
import os
import pyttsx3
import speech_recognition as sr
class CODE:
      
    def takeCommands(self):
          
          r = sr.Recognizer()
          with sr.Microphone() as source:
              print('Listening')
  
              r.pause_threshold = 0.7 
              audio = r.listen(source)

              try:

                  print("Recognizing")
                  Query = r.recognize_google(audio, language='en-in')
  
                 
                  print("the query is printed='", Query, "'")
  
              except Exception as e:
  
                  
                  print(e)  
                  
                  print("Say that again!!")
                  return "None"
          return Query
  
    def Speak(self, audio):

          engine = pyttsx3.init('sapi5')
          voices = engine.getProperty('voices')
          engine.setProperty('voice', voices[1].id)
          engine.say(audio)
          engine.runAndWait()
  
    def quitSelf(self):
        self.Speak("do u want to switch off the computer ")
  
        choice =  self.takeCommands()

        if choice == 'yes':
  
            print("Shutting down the computer")
            self.Speak("Shutting the computer")
            os.system("shutdown /s /t 30")
        if choice == 'no':
  
            print("Thank u sir")
            self.Speak("Thank u sir")
  
              
  
if __name__ == '__main__':
    Maam = CODE()
    Maam.quitSelf()