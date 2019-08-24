import time
def app():
    
    start = input("Press Enter : ")
    print()

    def wordz():
        
        T = 0.6

        k = "_"

        i = "\n"

        a = "@"

        d = "-"

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

        if name == "":
            print("Please enter a name...")
            time.sleep(2)
            print()
            wordz()

        print()

        print("Last name?")

        time.sleep(T)

        last = str(input(": "))

        print()

        if last == "":
            print("Please enter a surname...")
            print()
            time.sleep(2)
            wordz()

        print()

        print("Date of birth?")

        print()

        time.sleep(T)

        birth = str(input(": "))

        print()

        print("City of birth?")

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

            line13 = name + k + last + i

            line14 = name + k + birth + i

            line15 = name + k + city + i

            line16 = last + k + name + i

            line17 = last + k + birth + i

            line18 = last + k + city + i

            line19 = birth + k + name + i

            line20 = birth + k + last + i 

            line21 = birth + k + city + i

            line22 = city + k + name + i

            line23 = city + k + last + i

            line24 = city + k + birth + i

            line25 = name + a + last + i

            line26 = name + a + birth + i

            line27 = name + a + city + i

            line28 = last + a + name + i

            line29 = last + a + birth + i

            line30 = last + a + city + i

            line31 = birth + a + name + i

            line32 = birth + a + last + i 

            line33 = birth + a + city + i

            line34 = city + a + name + i

            line35 = city + a + last + i

            line36 = city + a + birth + i

            line37 = name + d + last + i

            line38 = name + d + birth + i

            line39 = name + d + city + i

            line40 = last + d + name + i

            line41 = last + d + birth + i

            line42 = last + d + city + i

            line43 = birth + d + name + i

            line44 = birth + d + last + i 

            line45 = birth + d + city + i

            line46 = city + d + name + i

            line47 = city + d + last + i

            line48 = city + d + birth + i

            print("Correct?")

            conf = input("(Y/N) : ")

            print()

            if conf == "Y":

                print("ok... good\n")

                print("Please specify a NEW name for the wordlist\n")

                newname = str(input(": "))

                with open(newname + ".txt", "w") as out:
                    
                    out.writelines([line1, line2, line3, line4, line5, line6, line7, line8,line9, line10,
                     line11, line12, line13, line14, line15, line16, line17, line18,line19, line20, line21, line22, line23, line24,
                     line25, line26, line27,line28, line29, line30, line31, line32, line33, line34,
                      line35, line36, line37, line38, line39, line40, line41, line42, line43, line44, line45, line46, line47, line48])

                print()

                print("[+] Generating file... ")

                time.sleep(2)

                print("[+] File saved as " + newname + ".txt")

                time.sleep(1)

                print("[+] Done!\n")

                time.sleep(4)

                print("you should now see a file called " '"'+ newname + '.txt"' + " I suggest you combine it with another wordlist for higher chances, happy hacking!")

                print()

                out.close()

            elif conf == "N":

                print("Restarting...\n")

                time.sleep(2)

                wordz()

            else:

                print('Please Enter "Y" or "N"\n')

                sure()
        sure()

    if start == "":

        print("Hi!")

        print()

        wordz()

    else:
        wordz()

app()
