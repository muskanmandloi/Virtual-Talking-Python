import pyttsx3
friend = pyttsx3.init()
speech = input("Write Something : ")
friend.say(speech)
friend.runAndWait()