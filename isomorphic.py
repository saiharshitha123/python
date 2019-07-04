def strn(a,b):
    if(len(a)==len(b)):
        return ("yes")
    else:
        return ("no")
a,b=map(strn,input().split()) 
print(strn(a,b))