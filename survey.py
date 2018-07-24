import json
listofdict=[]
playing=True
while playing == True:
    name1=input ("What is your name? ")
    print("Hello" ,name1, "!")
    bday1=input ("When is your birthday? (MM/DD/YYYY) ")
    age1= input ("How old are you? ")
    feeling1=input("How are you feeling right now? ")
    color1=input("What is your favorite color? ")
    spirit1=input('What is your spirit animal? ')

    dict1={}
    dict1["name"]=name1
    dict1["bday"]=bday1
    dict1["age"]=age1
    dict1["feeling"]=feeling1
    dict1["fav color"]=color1
    dict1["spirit animal"]=spirit1
    listofdict.append(dict1)
    end = input("Would you like to continue? ")
    if end == "no":
        playing = False
print(listofdict)
write(listofdict)
