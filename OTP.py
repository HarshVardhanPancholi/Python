#Program on generating otp
import random
import time as t
while(1):
    a="qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+-="
    b=list(a)          
    e=random.choice(b)
    f=random.choice(b)
    g=random.choice(b)
    h=random.choice(b)
    print('Your OTP is ',e,f,g,h)
    t.sleep(5)
    
