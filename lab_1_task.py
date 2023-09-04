                                                                    #LAB #01 TASK
                                                                    #____________
##Exercise Python input/output Basic operatons:
##_____________________________________________

#(i)Program to take input 4 values and swap them
'''
a=int(input("Enter value: "))
b=int(input("Enter value: "))
c=int(input("Enter value: "))
d=int(input("Enter value: "))
temp_var=a
a=d
d=temp_var
temp_var=b
b=c
c=temp_var
print(a)
print(b)
print(c)
print(d)
'''
#(ii)Program to convert temperature from Celcius to Fahrenheit:
#______________________________________________________________

#From Celcius to Fahrenheit:
#T_cel=float(input("Enter temperature in Celcius: "))
#Fahrenheit= (T_cel*1.8)+32
#print(str(T_cel)+" °C is equal to "+str(Fahrenheit)+" °F")

#From Fahrenheit to Celcius:
#T_fah=float(input("Enter Temperature in Fahrenheit: "))
#Celcius=(T_fah-32)*(5/9)
#print(str(T_fah)+" °F is equal to "+str(Celcius)+" °C")


##Exercise: Lists:
##________________

#(ii)Program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings:
#___________________________________________________________________________________________________________________________________________________

'''
def count_word(words):
    c=0
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            c+=1
    return c
print(count_word(['abc','xyz','aba','1221','faiqa','alexa']))
'''
##Exercise: Dictionaries:
##_______________________

#(ii)Write a Python script to concatenate following dictionaries to create a new one:
#____________________________________________________________________________________

#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#dic4={}
#for d in (dic1, dic2, dic3): dic4.update(d)
#print(dic4)

##Exercise: List Comprehnsion:
##____________________________

#Write a list comprehension which, from a list, generates a lowercased version of each string that has length greater than five: 
#_______________________________________________________________________________________________________________________________

#def list_comp(words):
 #   list=[]
  #  for i in words:
   #     if len(i)>5:
    #        list.append(i.lower())
    #return list     
#print(list_comp(['Hello', 'all', 'How', 'HAPPY', 'BIRTHDAY']))


#PROGRAM TO PRINT A SPECIFIED LIST AFTER REMOVING THE 0th, 4th and 5th ELEMENTS:
#_______________________________________________________________________________

#list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
#list = [x for (i,x) in enumerate(list) if i not in (0,4,5)]
#print(list)


#x = 6
#if (type(x) is int): 
# print ("true") 
#else: 
# print ("false")

#list1=[1,2,3,4,5] 
#list2=[6,7,8,9] 
#for item in list1: 
# if item in list2: 
#  print("overlapping") 
# else: 
#  print("not overlapping")

 
