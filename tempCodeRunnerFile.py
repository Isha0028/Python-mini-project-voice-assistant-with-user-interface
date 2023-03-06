    # def takecommand(self):
    #     r = sr.Recognizer()
    #     with sr.Microphone() as source:
    #         print("listening...")
    #         r.pause_threshold = 1
    #         audio = r.listen(source, timeout=5, phrase_time_limit=10)
    #         # r.pause_threshold = 0.5
    #         # r.adjust_for_ambient_noise(source)
    #         # audio = r.listen(source)
    #         # audio = r.listen(source,timeout=5,phrase_time_limit=8)

    #     try:
    #         print("Recognizing...")
    #         query = r.recognize_google(audio, language='en-in')
    #         print(f"user said: {query}")

    #     except Exception as e:
    #         speak("Say that again please...")
    #         return "none"
    #     # query = query.lower()
    #     return query