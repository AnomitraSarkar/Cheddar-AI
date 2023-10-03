import algorithm as algo
import file_checkers as fc


net_state = False

if __name__ == "__main__":
    fc.display_cheddar_image()
    speak_mode = "Enabled"  # default parameter for greeter and creators
    fc.create_default_preloader()
    fc.understand_preloader(fc.preload_file)
    profiles_file = f"{fc.vars_dir['data_directory']}\profiles.csv"
    fc.checkfordirectory()
    fc.template_profile(profiles_file)
    pswdcheck = False
    while not pswdcheck:
        pswdcheck = fc.profile_setter(algo.password_inlet(), profiles_file)
    call = fc.phrase_call(fc.person_call_list)
    algo.speakCommand(speak_mode, f"Hello {call}")
    net_state = algo.networkCheck(speak_mode)

    algo.perpare_laptop(speak_mode, "ASSEST\prepare1.bat",
                        "ASSEST\prepare2.bat", call)
    algo.speakCommand(speak_mode, f"{call} the laptop is ready")
    # taking query in offline mode <state to be changed>
    # trial input <state to be changed>
    algo.clearConsole("disabled")
    algo.speakCommand(
        speak_mode, f"{call} Enter any command in offline mode: ")
    print("\n(------------------------------------CHEDDAR AI < KIRA VER >------------------------------------)\n")
    while True:
        query = input("COMMAND FOR CHEDDAR |)> ")
        query = query.lower()
        query = " " + query + " "
        if "exit" in query or "quit" in query or "bye" in query or "close" in query:
            algo.commands(speak_mode, call)
        elif "clear" in query:
            algo.commands(speak_mode, call, 1)
        elif "play" in query and "music" in query:
            algo.commands(speak_mode, call, 2)
        elif "direct" in query and "shutdown" in query:
            algo.commands(speak_mode, call, 3)
        elif "direct" in query and "restart" in query:
            algo.commands(speak_mode, call, 4)
        elif "prepare" in query and ("laptop" in query or "pc" in query or "computer" in query):
            algo.commands(speak_mode, call, 5)
        elif "cmd" in query and "new" in query:
            algo.commands(speak_mode, call, 6)
        elif ("list" in query or "available") and ("wifi" in query or "wi fi" in query or "wi-fi" in query):
            algo.commands(speak_mode, call, 7)
        elif ("vsc" in query or "visual studio code" in query or "vs code" in query) and ("new" in query and "folder" in query):
            algo.commands(speak_mode, call, 10)
        elif ("vsc" in query or "visual studio code" in query or "vs code" in query) and "new" in query:
            algo.commands(speak_mode, call, 9)
        elif "vsc" in query or "visual studio code" in query or "vs code" in query:
            try:
                algo.commands(speak_mode, call, 8)
            except:
                algo.commands(speak_mode, call, 11)
        elif "spotify" in query:
            algo.commands(speak_mode, call, 15)
        elif "whatsapp" in query or "whatapp" in query:
            algo.commands(speak_mode, call, 16)
        elif "yt" in query or "youtube" in query:
            if "chrome" in query:
                algo.commands(speak_mode, call, 25, algo.ytprocessor(query))
            else:
                algo.commands(speak_mode, call, 24, algo.ytprocessor(query))
        elif "chrome" in query:
            if "incognito" in query:
                algo.commands(speak_mode, call, 13, algo.webproc(query))
            elif " previous " in query or " restore " in query or " last " in query:
                algo.commands(speak_mode, call, 14, algo.webproc(query))
            else:
                algo.commands(speak_mode, call, 12, algo.webproc(query))

        elif "brave" in query:
            if "incognito" in query:
                algo.commands(speak_mode, call, 18, algo.webproc(query))
            elif " previous " in query or " restore " in query or " last " in query:
                algo.commands(speak_mode, call, 19, algo.webproc(query))
            else:
                algo.commands(speak_mode, call, 17, algo.webproc(query))
        elif "edge" in query:
            if "incognito" in query:
                algo.commands(speak_mode, call, 21, algo.webproc(query))
            elif " previous " in query or " restore " in query or " last " in query:
                algo.commands(speak_mode, call, 22, algo.webproc(query))
            else:
                algo.commands(speak_mode, call, 20, algo.webproc(query))
        elif "fake" in query:
            algo.commands(speak_mode, call, 26)
        elif "notepad" in query or "note" in query or "parakeet" in query:
            algo.commands(speak_mode, call, 27)
        else:
            algo.speakCommand(speak_mode, f"I did not understand the {call}")
