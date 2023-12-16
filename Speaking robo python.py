from win32com.client import Dispatch
if __name__ == '__main__':
   print("first proper pyhon program speaking robo")
   speak = Dispatch("SAPI.SpVoice").Speak
   x=input("enter required speech text")
   speak(x)
