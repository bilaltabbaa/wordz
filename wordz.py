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

            line49 = name.title() + last + i

            line50 = name.title() + birth + i

            line51 = name.title() + city + i

            line52 = last.title() + name + i

            line53 = last.title() + birth + i

            line54 = last.title() + city + i

            line55 = birth.title() + name + i

            line56 = birth.title() + last + i 

            line57 = birth.title() + city + i

            line58 = city.title() + name + i

            line59 = city.title() + last + i

            line60 = city.title() + birth + i

            line61 = name.title() + k + last + i

            line62 = name.title() + k + birth + i

            line63 = name.title() + k + city + i

            line64 = last.title() + k + name + i

            line65 = last.title() + k + birth + i

            line66 = last.title() + k + city + i

            line67 = birth.title() + k + name + i

            line68 = birth.title() + k + last + i 

            line69 = birth.title() + k + city + i

            line70 = city.title() + k + name + i

            line71 = city.title() + k + last + i

            line72 = city.title() + k + birth + i

            line73 = name.title() + a + last + i

            line74 = name.title() + a + birth + i

            line74 = name.title() + a + city + i

            line75 = last.title() + a + name + i

            line76 = last.title() + a + birth + i

            line77 = last.title() + a + city + i

            line78 = birth.title() + a + name + i

            line79 = birth.title() + a + last + i 

            line80 = birth.title() + a + city + i

            line81 = city.title() + a + name + i

            line82 = city.title() + a + last + i

            line83 = city.title() + a + birth + i

            line84 = name.title() + d + last + i

            line85 = name.title() + d + birth + i

            line86 = name.title() + d + city + i

            line87 = last.title() + d + name + i

            line88 = last.title() + d + birth + i

            line89 = last.title() + d + city + i

            line90 = birth.title() + d + name + i

            line91 = birth.title() + d + last + i 

            line92 = birth.title() + d + city + i

            line93 = city.title() + d + name + i

            line94 = city.title() + d + last + i

            line95 = city.title() + d + birth + i

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
                      line35, line36, line37, line38, line39, line40, line41, line42, line43, line44, line45, line46, line47, line48,
			            line49, line50, line51, line52, line53, line54, line55, line56, line57, line58, line59 , line60, line61, line62,
			            line63, line64, line65, line66, line67, line68, line69, line70, line71, line72, line73, line74, line75, line76,
			            line77, line78, line79, line80, line81, line82, line83, line84, line85, line86, line87, line88, line89, line90,
                         line91, line92, line93, line94, line95])

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
