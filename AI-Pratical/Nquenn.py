import random

def main():
    print("************* Chat Bot ***************")
    while True:
        print(">>>")
        random.seed()
        z = random.randint(1, 7)
        s = input()

        if s in ["hi", "hii", "hello", "hello there", "hy", "yo", "hey"]:
            response = {
                1: "hi there",
                2: "hello there",
                3: "hi",
                4: "hello",
                5: "hy",
                6: "hey",
                7: "hii"
            }
            print(response[z])
        elif s in ["howdy?", "howdy", "how are you?", "whatsup?", "whats up?", "how do you do?", "how do you do", "how are you"]:
            response = {
                1: "I am fine",
                2: "I am well",
                3: "I am good",
                4: "I am very good",
                5: "fine",
                6: "good",
                7: "well"
            }
            print(response[z])
        elif s in ["who are you?", "who are you", "who", "who?", "who are?", "who are"]:
            response = {
                1: "I am chat bot.",
                2: "I am AI machine.",
                3: "I am not human. I am chat bot machine.",
                4: "chat bot.",
                5: "AI bot",
                6: "Bot",
                7: "I am computer program talking with you."
            }
            print(response[z])
        elif s == "" or s == " " or s == "  ":
            response = {
                1: "why are you so silent?",
                2: "say something.",
                3: "come on, talk",
                4: "Stop sending blank texts",
                5: "are you here to talk or what?",
                6: "blank texts? seriously?",
                7: "Dude, I know a blank text when I see one"
            }
            print(response[z])
        elif s in ["bye", "good bye", "Bye", "exit", "stop"]:
            response = {
                1: "Sorry to see you go...",
                2: "Good Bye!",
                3: "Bye...!",
                4: "See you later. Bye!",
                5: "Thanks for talking. Bye!",
                6: "See you again...",
                7: "Bye Bye"
            }
            print(response[z])
            return
        else:
            print("You entered the wrong input! Try again...")

if __name__ == "__main__":
    main()
