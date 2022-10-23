from letters import LETTERS


while True:

    def stoping(q):
        if q == "yes" or q == "y":
            return True
        else:
            return False

    try:
        choose_translation = int(input("If you want to translate words to morse code, press '1', \n"
                                   "if you want translate morse code to words, press '2': "))
    except:
        print("Entered bad value, try again...")
        continue

    if choose_translation == 1:
        try:
            text = input("Write your word for translation here: ").upper()
            morse = [LETTERS[letter] for letter in text]
            print(" ".join(morse))
            q = input("Do you want to continue, 'YES' or 'NO'? ")
            if stoping(q.lower()):
                continue
            else:
                print("See you next time, Bye")
                break
        except:
            print("Error occured, try again")
            continue

    elif choose_translation == 2:
        try:
            morse_text = input("Write your morse code for translation here: ").split(" ")
            translated_text = []
            for symbol in morse_text:
                for key, value in LETTERS.items():
                    if value == symbol:
                        translated_text.append(key)
            print(" ".join(translated_text))
            q = input("Do you want to continue, 'YES' or 'NO'? ")
            if stoping(q.lower()):
                continue
            else:
                print("See you next time")
                break
        except:
            print("Error occured, try again")
            continue
    else:
        continue


