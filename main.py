# var1 ='value'
# print (type(var1))
# print (var1[0])
# print (var1[-1])
# print (var1[1:3])
# print(len(var1))
# var2= 5
# print (type(var2))

# var3 = 3.14
# print (type(var3))

# var4 = True
# print(type(var4))

# var5 = 5+6j
# print (type(var5))
# str1 ='hello'
# str1= 'y'+str1[1:len(str1)]
# print (str1)
# print(str1[0:2]+'mm'+str1[4:len(str1)])

# #elif
# if 1==2:
#     print("1")
# elif 1==1:
#     print("2")
# else:
#     print("unkown")    

# switch :
#    case1:
#      print("1")
#    case2:
#      print("2")
#    default:
#         print("unkown")   

# num=0
# while num<10:
#     print(num)
#     num=num+1
#check an input from the user and if the word is == the value that allready stored in the varible 
#print corect in while loop 
#eles print wron and ask  the user to enter the word again

secretword='python'
# userinput= input('enert your word:')
c=0
cheak =True
while cheak:
    userinput= input("enter your word:")
    c= c+1
    if userinput== secretword:
       print("correct")
       break
    else:
       print ("wrong")
       if c==2:
          check=False
          print("you have recendet")
          break
