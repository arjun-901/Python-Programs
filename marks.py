a=eval(input("enter mark out of 300"))
b=a/300*100
print("precentage is ",b,"%")
if(a>300):
    print("you enter a rong marks")
elif b>60:
    print("your div is first")
elif (b>50 and b<53):
    print("third division");
elif(b>33 and b<50):
    print("your didvision is third")
else:
    print("faild!")
