from termcolor import colored

origins = []

def pushOrigin(name):
    origins.append(name)

def popOrigin():
    origins.pop()

def printLogNormal(text):
    print("[",''.join(origins[0]),"]",text)

def printLogWarning(text):
    print("[",colored(origins[len(origins)-1], "yellow"),"]",text)

def printLogError(text):
    print("[",colored(origins[len(origins)-1], "red"),"]",text)


#from termcolor import colored
#origins = []
#def pushOrigin(name):
#	origins.append(name)

#def popOrigin():
#	origins.pop()

#def printLogNormal(text):
#	print("[",''.join(origins[0]),"]",text)


#use whole above code or use only commented code as you wish both works fine