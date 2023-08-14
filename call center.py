# call center

import time
import random
print (' thank u fo calling AAA')
for numberchosen in range(0,51):
    print (' you can choose from the list ')
    print (' press 1 for (home network)')
    print (' press 2 for (mobile network)')
    print (' press 3 for (customer service)')
    print (' plz select an item form the list above')
    chooselist = int(input ()) # ask for the problem 
    if chooselist == int('1'):
     print ('you chose (home network)')
     print ('if u wanna pay your bill choose (pay) ')
     print ('if their is an other problrm contact the customer service')
     choose = input()
     if choose == 'pay':
        payment =random.randint(500,10000)
        print (payment)
        print ('if u wanna pay press yes!')
        pay = input()
        if pay =='yes':
            print ('transaction is done thank you for joinning AAA')
            break
        elif pay =='no':
            print ('thank u for reaching us BYE')
            break
        else:
            print ('try again')
     else:
        print ('wait unit an agent contact you about your problem')
        break
    elif chooselist == int('2'):
         print ('you chose (mobile network)')
         print ('if u wanna pay your bill choose (pay) ')
         print ('if their is an other problrm contact the customer service')
         choose = input()
         if choose =='pay':
           paymentt = random.randint(100,1000)
           print (paymentt)
           print ('if u wanna pay press yes!')
           pay = input()
           if pay == 'yes':
            print ('transaction is done thank you for joinning AAA')
         elif pay =='no':
          print ('thank u for reaching us BYE')
          break
         else:
             print ('try again')
    elif chooselist == int('3'):
        print ('plz wait until an agent is free')
        time.sleep(5)
        print ('hi my name is Amr i will be helping you today')
        print ('what is your name ?')
        name = input ()
        print ('hi ' + name + ' how can i help you?')
        problem = input ()
        print ('ok i will check now ')
        time.sleep(3)
        print ('Do you sill have the same problem ?')
        answer = input()
        if answer == 'on':
          print ('good happy to help you')
          break
        elif answer =='yes':
             print ('ok we will work on your problem and someone will call you to check if the problem is solved or not !!')
             time.sleep(2)
             print ('any thing else do u want help with ?')
             answer = input()
             if answer =='yes':
                 print ('ok what is it ?')
                 problem = input()
                 print ('ok we will work on it ')
                 time.sleep(1.5)
                 print ('thank u for informing us BYE')
                 break
             else:
                 print ('ok BYE')
                 break
        else:
          print ('try again ')
    else:
        print ('sorry you didnt chose any thing ')
        break