from time import *
import random as r



# creating function for counting the number of errors
def mistake(dfault_text,input_text):
    e=0
    for i in range(len(dfault_text)):
        try:
            if dfault_text[i] != input_text[i]:
                e+=1
        except:
            e+=1
    return e

# creating function for speed delay
def speed_time(time_s,time_e,userinput):
    time_delay=(time_e-time_s)
    time_roundOff=round(time_delay,2)
    speed=len(userinput)/time_roundOff
    return round(speed)


if __name__=="__main__":
    while True:
        ck=input("Enter yes/no ")
        if ck=="yes":
            text=['''My name is Bikash ''','''Human skulls had been used as drinking cups for hundred of years.The muscles and flesh were scraped away,the bottom was hacked off
            then they were suitable to hold andy beverage. The first Bowie knife was forged at Washington,Arkansas. All the dirt from foundation to 
            build the World Trade Center in NYC was dumped into the Hudson river to form the community now known as Battery City Park.''',
            '''Being rude to a telephone operator in Prussia was once a crime. In 1908,a respected citizen was reprimanded by the governmet 
            after becoming exasperated with an operator and saying "My dear girl!" ! In Thailand, the left hand is considered unclean, 
            so you should not eat with it. Also pointing with one finger is considered unclean, so you should not eat with it. 
            Also, pointing with one finger is considered  unclean, so you should not eat with it. 
            Also, poiniting with one finger is considered rude and is only done when pointing to objects or animals, never humans.''',
            '''Almonds are a member of the peach family. Dentists have recommended that a toothbrush be kept at least 6 feet away from a toilet
            to avoid airborne particles resulting from the flush. The plastic things on the end of shoelaces are called aglets. Richard 
            Millhouse Nioxn was the first US president whose name contains all the letters from the word 'criminal'. The second was William Jefferson 
            Clinton.''']

            text1=r.choice(text)

            print(text1)
            print("======================================typing speed=============================")
            print("\n")
            time_start=time()
            textinput=input("Enter the text above:")
            time_end=time()
            print("\n")
            print(f"Speed: {speed_time(time_start,time_end,textinput)}word/sec")
            print(f"Total errors: {mistake(text1,textinput)}")
        elif ck=="no":
            print("Thank you ")
            break
        else:
            print("================Wrong Input=======================")