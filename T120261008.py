# Given an exam grade and an assistance percentage, gives back "you have failed" "you have passed"
# conditions: exam grade >= 70 and assistance >=80

#get: grade and assistance
# convert grade and assistance to int
class_assistance = int(input("How many classes have you assisted to? "))
grade = int(input("What grade did you get in the exam? "))


message1 = "you have passed this class"
message2 = "you have failed this class"
message3 = "introduce valid values"
message4 = "Your need to attend to more sessions in order to pass this class"
message5 = "Altough you have attended to enough sessions, your exam has not reached the minimun score ir order to pass"
message6= "Both your exam and assistance do not meet the requirements needed to passs"

if class_assistance>40 and grade>100:
    print(message3)

else:
    if  class_assistance>=32 and grade>=70:
        print(message1)
    else:
        if class_assistance<32 and grade>=70:
            print(message4)
        else:
            if class_assistance>=32 and grade<70:
                print(message5)
            else:
                print(message6)


