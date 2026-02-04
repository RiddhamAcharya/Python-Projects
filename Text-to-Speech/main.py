import pyttsx3

text_speech = pyttsx3.init()

answer = input("Enter the message you want to listen to: \n")
text_speech.say(answer)
text_speech.runAndWait()
