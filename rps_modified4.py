#sudo leapd
# separate terminal python rps_modified3.py
#have www.mp3 in the same folder

# Leap oriented with cable pointing down
# velocity is positive in the x direction when hand is moving down.
# negative x direction is up#


import os, sys, inspect, time, cPickle, numpy as np
from playsound import playsound
from pyfiglet import Figlet
from collections import Counter



sys.path.append('/home/kevin/Desktop/Leap_progs/LeapSDK/lib/x64/')
sys.path.append('/home/kevin/Desktop/Leap_progs/LeapSDK/lib/')
import Leap

class SampleListener(Leap.Listener):
    def on_connect(self, controller):
        print "Connected"
        os.system('clear')

    def count_downward_movement(self, controller):
        frame = controller.frame()
        count = ["up1","ro", "up2", "sham", "up3" ,"bo", "up4", "shoot"]
        while frame.hands[0].is_valid and frame.hands[0].grab_strength == 1: #if a rock gesture is being shown
            frame = controller.frame()
            init_frame = frame
            if frame.hands[0].palm_velocity[0] < -300: #if it is moving up
                stage = count[0]
                while True: # this is based on havng the cable of the leap pointed down
                    #print stage
                    frame = controller.frame() #current position
                    if frame.hands[0].palm_velocity[0] > 200 and stage == "up1": # hand_position[0] is the x co-ordinate
                        stage = count[1] #finished up 1, now on ro
                        os.system('clear')
                        os.system('printf "\n\n\n"')
                        os.system("toilet -w 500 -f pagga -F border ___________ROCK, PAPER, SCISSORS_________")
                        os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                        os.system("toilet -w 500 -f pagga _____________________1______________________")
                    elif frame.hands[0].palm_velocity[0] < -200 and stage == "ro": 
                        stage = count[2] #finished ro, now on up2
                    elif frame.hands[0].palm_velocity[0] > 200 and stage == "up2":
                        stage = count[3] #finished up2, now on sham
                        os.system('clear')
                        os.system('printf "\n\n\n"')
                        os.system("toilet -w 500 -f pagga -F border ___________ROCK, PAPER, SCISSORS_________")
                        os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                        os.system("toilet -w 500 -f pagga _____________________2_____________________")
                    elif frame.hands[0].palm_velocity[0] < -200 and stage == "sham":
                        stage = count[4] #finished sham, now on up3
                    elif frame.hands[0].palm_velocity[0] > 200 and stage == "up3":
                        stage = count[5] #finished up3, now on bo
                        os.system('clear')
                        os.system('printf "\n\n\n"')
                        os.system("toilet -w 500 -f pagga -F border ___________ROCK, PAPER, SCISSORS_________")
                        os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                        os.system("toilet -w 500 -f pagga _____________________3_____________________")
                    elif frame.hands[0].palm_velocity[0] < -200 and stage == "bo":
                        stage = count[6] #finished bo, now on up4
                        os.system('clear')
                        os.system('printf "\n\n\n"')
                        os.system("toilet -w 500 -f pagga -F border ___________ROCK, PAPER, SCISSORS_________")
                        os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                        os.system("toilet -w 500 -f pagga ___________________________________________")
                    elif frame.hands[0].palm_velocity[0] > 200 and stage == "up4":
                        stage = count[7] #finished up4, now on shoot

                    if stage == "shoot":
                        return [stage, init_frame]
        else:
            return [0,0]
                    



  

    def getMove(self, controller, init_frame):
        frame = controller.frame()
        current_pos = frame.hands[0].translation(init_frame)
        move = None
        result_history = []
        while current_pos[0] > -200 and current_pos[0] < 200:
            frame = controller.frame()
            index_finger_extended = frame.hands[0].fingers.finger_type(1).extended()
            middle_finger_extended = frame.hands[0].fingers.finger_type(2).extended()
            ring_finger_extended = frame.hands[0].fingers.finger_type(3).extended()

            if index_finger_extended and not ring_finger_extended:
                move = 's'
            elif index_finger_extended and middle_finger_extended and ring_finger_extended:
                move = 'p'
            elif frame.hands[0].grab_strength > 0.8:
                move = 'r'
            else:
                move = 'fail'
            if frame.hands[0].palm_velocity[0] < 10 or current_pos[0] < -200 and current_pos[0] > 200:
                break
            if move:
                result_history.append(move)
        return result_history

# from pyfiglet import Figlet
# f = Figlet(font='slant')
# print f.renderText('text to render', width=500)
#larry3d
#starwars
#trek
#alligator
#banner3-D
#basic
#computer
#doh
#speed
#ticksslant
#Rounded
#mono12
#Fender
#Eletronic
#Big Money-nw
#pagga _________________Hand Detected__________________
#dotmatrix
#-F gay
#-F metallic


def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    while True:
        frame = controller.frame()
        #f = Figlet(font='pagga', width=500)
        try:
            if frame.hands[0].is_valid:
                # os.system('clear')
                # os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                # os.system("toilet -w 500 -f pagga _________________Hand Detected__________________")
                # time.sleep(0.5)
                os.system('clear')
                os.system('printf "\n\n\n"')
                os.system("toilet -w 500 -f pagga -F border ___________ROCK, PAPER, SCISSORS_________")
                os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                os.system("toilet -w 500 -f pagga ________________Make a fist________________")
                time.sleep(0.5)
                os.system("toilet -w 500 -f pagga __________________Ok, GO!__________________")
                output = listener.count_downward_movement(controller)
                downs = output[0]
                init_frame = output[1]
                if downs == "shoot":
                    result_history = listener.getMove(controller, init_frame) 
                    if result_history:
                        result_history = result_history[-300:]
                        history_dict = Counter(result_history)
                        recognised_gesture = history_dict.most_common(1) # list of tuples (only one tuple)
                    else: 
                        'Random Choice = %s' % np.random.choice(['r','p','s'])
    
                    #os.system("toilet -w 500 -f pagga \U0000270B")
                    gesture, frames = recognised_gesture[0]
                    os.system('clear')
                    os.system('printf "\n\n\n"')
                     os.system("toilet -w 500 -f pagga -F border ___________ROCK, PAPER, SCISSORS_________")
                    os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                    if gesture == 's':
                        os.system("toilet -w 500 -f pagga  __________________ROCK!__________________")
                    elif gesture == 'p':
                        os.system("toilet -w 500 -f pagga  ________________SCISSORS!________________")
                    elif gesture == 'r':
                        os.system("toilet -w 500 -f pagga  __________________PAPER!_________________")
                    elif gesture == 'fail':
                        os.system("toilet -w 500 -f pagga _____________oops, try again_____________")
                        playsound('www.mp3')
                    time.sleep(2)
            if not frame.hands[0].is_valid:
                    os.system('clear')
                    os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                    os.system("toilet -w 500 -f pagga -F border ___________ROCK, PAPER, SCISSORS_________")
                    os.system('printf "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"')
                    os.system("toilet -w 500 -f smmono9 Insert Hand")

                    time.sleep(0.5)
                    os.system('clear')
        except KeyboardInterrupt:
            break

        controller.remove_listener(listener)

if __name__ == "__main__":
    main()
