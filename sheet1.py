#Q2
print("="*10,"Q2","="*10)
a = 20
a+=30
a%=3
print(5**9,3//2,7//3,7/3,6 == 6,f"a = 20, a+=30, a%=3 then print = {a}",True * False,True & False,True and False,((6>3) and (7<4) or (18==3)) and (9>3),True is False,((True == False) or (False > True)) and (False <= True),sep = "\n")

#False in "False"
#This will give the following error
#TypeError: 'in <string>' requires string as left operand, not bool


#Q3
print("\n","="*10,"Q3","="*10)
s1 = "Nice to have it"
s2 = "here"
print(s1+" "+s2)


#Q4
print("\n","="*10,"Q4","="*10)
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])


#Q5
print("\n","="*10,"Q5","="*10)
s1 = "Nice to have it"
s2 = "here"
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
l = [s1,s2]
t = []

print("This is using the extend method on a list containing s1 and s2")
t.extend(l)
t.extend(a)
t.extend(l)
print(t)

print("using addition and updation of (a)")
a = l + a + l
print(a)


#Q6
print("\n","="*10,"Q6","="*10)
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
for i in numbers:
    if i == 237:
        break
    else:
        if i % 2 == 0:
            print(i,end = " ")


#Q7
print("\n","="*10,"Q7","="*10)
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))


#Q8
print("\n","="*10,"Q8","="*10)
s = input("Enter the string to be checked for Pangram: ")
l = list(range(65,91))           #storing ascii values of A to Z
for i in s.upper():              #changing string to upper
    if ord(i) in l:              #if ordinate of a character is found in the list l
        l.remove(ord(i))         #remove that element

if len(l) == 0:                  #then if l is empty then all A-Z exist
    print(f"{s} is a Pangram.")
else:                            #if l is not empty then some in A-Z were not used
    print(f"{s} is not a Pangram.")


#Q9
print("\n","="*10,"Q9","="*10)
n = input("Enter a number: ")
ans = int(n) + int(n*2) + int(n*3)
print(ans)


#Q10
print("\n","="*10,"Q10","="*10)
l = input("Enter the pattern: ").split("#")               #splitting array on the # ==== l gets 2 elements
x = l[0].split(" ")                                       #assigning 1st element to x
y = l[1].split(" ")                                       #assigning 2nd element to y
x = [int(i) for i in x]                                   #using string comprehension to convert all elements of x to int
y = [int(i) for i in y]                                   #using string comprehension to convert all elements of y to int
print(f"l = {l}",f"x = {x}",f"y = {y}",sep = "\n")


#Q11
print("\n","="*10,"Q11","="*10)
a = input("Enter the sequence of words: ").split(",")
a.sort()
print(a)

#ALTERNATE METHOD NOT DONE YET

#ordinates = [ord(i[0]) for i in a]
#n = len(ordinates)
#print(ordinates)
#for i in range(n):
#    ch = n-i-1
#    for j in range(ch):
#        if ordinates[j] > ordinates[j+1]:
#            temp = ordinates[j]
#            ordinates[j] = ordinates[j+1]
#            ordinates[j+1] = temp
#i = 0 
#j = 0
#while i < n:
#   if ord(a[i][0]) == ordinates[j]:



#Q12
print("\n","="*10,"Q12","="*10)
d = {"Student": ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]} 
ma = max(d['Marks'])
i = d['Marks'].index(ma)
print(d['Student'][i])


#Q13
print("\n","="*10,"Q13","="*10)
s = input("Enter the String: ")
l = 0
d = 0
for i in s:
    if i.isalpha():
        l+=1
    elif i.isnumeric():
        d+=1
print(l,d)


#Q14
print("\n","="*10,"Q14","="*10)
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'], 'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'], 'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
sub = input("Enter the subect: ")
newData = {"Name" : [], "Subject" : [], "Ratings" : []}
for i in range(len(d['Name'])):
    s = d["Subject"][i] 
    if s == "Python":
        newData["Name"].append(d["Name"][i])
        newData["Subject"].append(d["Subject"][i])
        newData["Ratings"].append(d["Ratings"][i])
print(newData)


#Q16
print("\n","="*10,"Q16","="*10)
ini = (0,0)
up = int(input("Enter the number of Steps for UP: "))
down = int(input("Enter the number of Steps for DOWN: "))
left = int(input("Enter the number of Steps for LEFT: "))
right = int(input("Enter the number of Steps for RIGHT: "))
y = abs(up - down)
x = abs(right - left)
fin = (x,y)
d = int(((ini[0] - fin[0])**2 + (ini[1] - fin[1])**2)**0.5)
print(d)
