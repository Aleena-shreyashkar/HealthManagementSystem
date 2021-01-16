#health management system
print("health management system:")
def getdate():
    import datetime
    return datetime.datetime.now()
print("what do you want to do? log or retrieve?\ntype 1 for log or 2 for retrieve")
n = input()
if n == "1":
    print("for whom you wanna log? harry, rohan or hammad?")
    m = input("input 1 for harry,2 for rohan or 3 for hammad")
    if m == "1":
        print("what do you want to log? exercise or diet?\ntype 1 for diet or 2 for exercise")
        o = input()
        if o == "1":
            x = input("type here")
            f = open("harry diet.txt","a")
            f.write(str([str(getdate())])+":" + x)
            print("diet successfully logged")
            f.close()
        elif o == "2":
            x = input("type here")
            f = open("harry exercise.txt","a")
            f.write(str([str(getdate())])+":" + x)
            print("exercise successfully logged")
            f.close()
    if m == "2":
        print("what do you want to log? exercise or diet?\ntype 1 for diet or 2 for exercise")
        o = input()
        if o == "1":
            x = input("type here")
            f = open("rohan diet.txt","a")
            f.write(str([str(getdate())])+":" + x)
            print("diet successfully logged")
            f.close()
        elif o == "2":
            x = input("type here")
            f = open("rohan exercise.txt","a")
            f.write(str([str(getdate())])+":" + x)
            print("exercise successfully logged")
            f.close()
    if m == "3":
        print("what do you want to log? exercise or diet?\ntype 1 for diet or 2 for exercise")
        o = input()
        if o == "1":
            x = input("type here")
            f = open("hammad diet.txt","a")
            f.write(str([str(getdate())])+":" + x)
            print("diet successfully logged")
            f.close()
        elif o == "2":
            x = input("type here")
            f = open("hammad exercise.txt","a")
            f.write(str([str(getdate())])+":" + x)
            print("exercise successfully logged")
            f.close()
elif n == "2":
    m = input("for whom you wanna retrieve? harry, rohan or hammad?\ntype 1 for harry 2 for rohan or 3 for hammad")
    if m == "1":
        o = input("what do you wanna retrieve? diet or exercise?\ntype 1 for diet or 2 for exercise")
        if o == "1":
            f = open("harry diet.txt")
            print(f.readlines())
            f.close()
        else:
            f = open("harry exercise.txt", "r")
            print(f.readlines())
            f.close()

    if m == "2":
        o = input("what do you wanna retrieve? diet or exercise?\ntype 1 for diet or 2 for exercise")
        if o == "1":
            f = open("rohan diet.txt", "r")
            print(f.readlines())
            f.close()
        else:
            f = open("rohan exercise.txt", "r")
            print(f.readlines())
            f.close()
    if m == "3":
        o = input("what do you wanna retrieve? diet or exercise?\n type 1 for diet or 2 for exercise")
        if o == "1":
            f = open("hammad diet.txt", "r")
            print(f.readlines())
            f.close()
        else:
            f = open("hammad exercise.txt", "r")
            print(f.readlines())
            f.close()








