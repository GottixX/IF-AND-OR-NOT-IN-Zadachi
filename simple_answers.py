while True:
    text = input("Say what? ")

    if "hello" in text or "Hello" in text:
        print("Hello there, good stranger!")
    elif "how are you?" in text or "How are you" in text:
        print("I am fine, thanks. How are you?")
    elif "feelings" in textor "feeling?" in texxt:
        print("I am a machine. I have no feelings")
    elif "age" in text or "How old are you" in text:
        print("I have no age. Only current timestamp")
    else:
        print("Sorry, I don't understand you. Try hello, feelings or age")
