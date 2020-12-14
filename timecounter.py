import time
        
def countdown(seconds):
    while seconds > 0:
        print(seconds)
        seconds -= 1
        time.sleep(1) #time sleep is time function that waits the amount of seconds set until the while loop continues
    print("BLAST OFF!")

seconds = input("Where would you like the countdown to start? Please enter an interger: ")

while not seconds.isdigit():  #isdigit() is a str class function only
    seconds = input("Please enter an interger: ")
    
seconds = int(seconds)
countdown(seconds)


