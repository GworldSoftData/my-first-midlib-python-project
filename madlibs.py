# string concatenation ( aka how to put strings together)
# suppose we want to create a string that says "subscribe to _______"
#youtuber = " Godspower Uyanga " # some string varaiable


# a few ways to do this
#print ("subscribe to " + youtuber )
#print ("subscribe to {}".format(youtuber) )
#print (f"subscribe to {youtuber}")
adj = input ("Adjective : ")
verb1 = input ("Verb: ")
verb2 = input ("Verb: ")
famous_person= input("Famous person : ")
madlib= f"Computer Programming is so {adj}! it makes me excited all the time because \
i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
