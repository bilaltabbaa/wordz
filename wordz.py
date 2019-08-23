import time

def passwd():
    password = input("Password : ")

    def wordz():
        T = 0.6

        i = "\n"

        print("Welcome to...")

        time.sleep(T)

        print("""
    ██╗    ██╗ ██████╗ ██████╗ ██████╗ ███████╗
    ██║    ██║██╔═══██╗██╔══██╗██╔══██╗╚══███╔╝
    ██║ █╗ ██║██║   ██║██████╔╝██║  ██║  ███╔╝ 
    ██║███╗██║██║   ██║██╔══██╗██║  ██║ ███╔╝  
    ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗
     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝
    by @anon_spooky        
    """)
        time.sleep(T)

        print("Where you can create wordlists!\n")

        print("Lets start with the First name...")

        time.sleep(T)

        name = str(input(": "))

        print()

        print("Good")

        print()

        print("Last name?")

        time.sleep(T)

        last = str(input(": "))

        print()

        print("Nice")

        print()

        print("When was he born?")

        print()

        time.sleep(T)

        birth = str(input(": "))

        print()

        print("And where?")

        city = str(input(": "))

        print()

        time.sleep(T)

        def sure():
            print("name: " + name)

            print("last: " + last)

            print("born in: " + birth)

            print("city: " + city)

            print()

            line1 = name + last + i

            line2 = name + birth + i

            line3 = name + city + i

            line4 = last + name + i

            line5 = last + birth + i

            line6 = last + city + i

            line7 = birth + name + i

            line8 = birth + last + i 

            line9 = birth + city + i

            line10 = city + name + i

            line11 = city + last + i

            line12 = city + birth + i

            print("Correct?")

            conf = input("(Y/N) : ")

            if conf == "Y":
                print("ok... good\n")

                print("Please specify a NEW name for the wordlist\n")

                newname = str(input(": "))

                with open(newname + ".lst", "w") as out:
                    
                    out.writelines([line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12])

                print()

                print("Done, you should now see a file called " + newname + ".lst" + " happy hacking!")

                out.close()

            elif conf == "N":
                print("Restarting...\n")

                time.sleep(3)

                wordz()

            else:
                print('Please Enter "Y" or "N"\n')

                sure()
        sure()
    if password == "wordz":
        print("Correct Password!")

        print()

        wordz()
    else:
        print("Incorrect password!")

        print()

        passwd()

passwd()
