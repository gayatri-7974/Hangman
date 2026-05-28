import random
options=["mango", "watermelon", "orange"]
tobe_word=random.choice(options)
guesses=len(tobe_word) + 2
dash= ["_"] * len(tobe_word)
man= {0: (" o "),
       1: (" o ",
           " | ",),
       2: (" o ",
           "/|"),
       3: (" o ",
           "/|\\"),
       4: (" o ",
           "/|\\",
           "/"),
       5: (" o ",
           "/|\\",
           "/\\")
       }
j=0
while guesses!=0:
    read=input("enter your guess:")
    if read in tobe_word:
        for i in range(len(tobe_word)):
            if tobe_word[i]==read:
                dash[i]=read
        print(dash)
        if "".join(dash)==tobe_word:
            print("Ayooo u wonnnn!!!")
            break
    else:
        guesses-=1
        for k in man[j]:
            print(k)
        j = j + 1
        if j==6:
            print("Bruh u lost:)")
            break
