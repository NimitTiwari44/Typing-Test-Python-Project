from time import *
import random as r

def error(given, userTest):
    error = 0
    for i in range(len(given)):
        try:
            if given[i] != userTest[i]:
                error +=1
        except :
            error +=1
            
def speed_time(time_s, time_e, userInput):
    time_actual =round((time_e - time_s),2)
    speed  =(len(userInput)/time_actual)*60
    return round(speed,2)
                



test = ['''Setting clear, achievable goals is fundamental to academic success.''',''' Goals provide direction, focus, 
        and a sense of purpose, acting as a roadmap for your educational journey.''',''' They can be short-term, 
        like aiming for a high grade on an upcoming exam, or long-term, like earning a degree or pursuing a specific career path.
        The key is to make your goals SMART: specific, measurable, achievable, relevant, and time-bound.''',
        '''This approach ensures that your goals are well-defined, trackable, and realistic, increasing your chances of success.''', 
       ''' By breaking down larger goals into smaller, manageable steps, you can create a clear path towards academic excellence
        and celebrate each milestone along the way''',''' Remember, goals are not set in stone; they can be adjusted and refined 
        as you progress.''']

test1 = r.choice(test)

print("   Typing Test   ")
print(test1)
print()
print()
time_1 = time()
testInput = input("Enter the given text :\n")
time_2 = time()

print("speed : ", speed_time(time_1,time_2,testInput ),"word/min")
print("Error : ", error(test1, testInput))