r"C:\Users\李佳欣\Desktop\1.wav"
"zh-cn"
import speech_recognition as sr
r = sr.Recognizer()
harvard = sr.AudioFile(r"C:\Users\李佳欣\Desktop\1.wav")
with harvard as source:
     audio = r.record(source)
try:
    print("Google thinks you said " + r.recognize_sphinx(audio, language="zh-CN", show_all=True))
except sr.UnknownValueError:
    print("Google could not understand audio")
except sr.RequestError as e:
    print("Google error; {0}".format(e))