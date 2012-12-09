import sys,os, random

#counts = [561,559] #[565,564]
#prefix = ["HP","HW"]
#
#counts = [590,599]   #[595, 605]
#prefix = ["LP","LW"]

#counts = [589,602] #[595, 605]
#prefix = ["RP","RW"]

counts = [999,999,999]
prefix = ["P","S","T"]
passwordLen = 5


login_ids = []
passwords = []

chars = ['3','4','7','9','A','C','D','E','F','H','J','K','M','N','P','Q','R','T','U','V','W','X','Y']
#removed to avoid confusion: 0, O; 1, I, L; 2, Z; 5, S


index = 0
for n in counts:
    c = 1
    while c <= n:
        password = ""
        login_id = prefix[index] + str(c).zfill(3)
        i = 0
        randIndices = []
        while i < passwordLen:
            randIndex = random.randint(0, len(chars)-1)
            if(randIndex in randIndices):
                continue
            password = password + chars[randIndex]
            randIndices.append(randIndex);
            i = i + 1
            
        if password in passwords:
            continue
        passwords.append(password)
        c = c + 1
        print password
    print "-----------"
    index = index + 1

    

