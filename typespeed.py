while True:
    try:
        import datetime
        import time
        import random as r

        print("""\nThis app will generate your typing speed and accuracy!\n""")

        sen = ["The king died so everyone wants to be royalty.",
               "John's kid loves to munch on potato waffers.",
               "Charles had Covid-19, but now he has recovered."]


        def get_sent_for_typing():
            choic = r.choice(sen)
            return choic


        sentence = get_sent_for_typing()
        count = int(0)
        length = int(len(sentence))
        le = int(length - 1)
        le_n = int(length - 1)
        qwerty = True
        print("Start typing in....")
        time.sleep(1)
        print("3....")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1....")
        time.sleep(1)
        print(f"start typing--\n   {sentence}")
        beginning = datetime.datetime.now()
        sd = input("Type here::")
        end = datetime.datetime.now()
        while qwerty is True:
            if sd[le] == sentence[le]:
                count = int(count + 1)
            le = int(le - 1)
            if le == 0:
                break
        accuracy = ((count / le_n) * 100)
        accuracy=int(accuracy)
        ss = sd.split()
        so = int(len(ss))
        x = (end - beginning).total_seconds()
        # .total_seconds() is used to return the total number of seconds contained in the duration
        print(f"Time taken to type the sentence is- {x} seconds.")
        spo = float(x)
        poes = ((so / spo) * 60)
        poes=int(poes)
        print(f"""Your typing speed is {poes} words per minute(or wpm) 
        and your accuracy is {accuracy}%.""")
        break
    except IndexError:
        print("Please type till the same sentence length or else this message will be shown again!\n\n")
