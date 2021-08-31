import threading
import test
def load(fps):
    print("Loading...")
    test.fps = fps
    test.main()
def main():
    opt = input(">>>")
    if opt == "start":
        try:
            print("New FPS?")
            newfps = int(input(">>>"))
            print("New FPS: "+str(newfps))
            print("New iteration number?")            
            newiter = int(input(">>>"))
            print("New iteration number: "+str(newiter))
            test.loopc = True
            test.itern = newiter
            threading.Thread(target=lambda:load(newfps)).run()
            test.loopc = False
            main()
        except Exception as error:
            print("Failed, try again.")
            main()
    else:
        main()
if __name__ == "__main__":
    print("pgtest")
    print("use the command 'start' please")
    main()
