#Building a novice car game
command=""
while True:
    command =input("> ").lower()
    if command == "start":
        print("The car has started..... VROOOM..Vroom...!! ")
    elif command =="stop":
        print("The car has stopped...BRAKEEEEEE.. Screeeecchhhhhhh!!")
    elif command =="help":
        print("""
    > start- starts the car
    > stop - stops the car
    > quit - ends the game
                """)
    elif command =="quit":
        break
    else:
        print("Sorry! I do not understand that! please try something else")
