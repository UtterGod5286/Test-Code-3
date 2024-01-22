#Name variable
#name = str(input("What is your name? "))

#Score variable
#score = 0

#Question list
#Q1 = "What is 36 / 3?"
#Q2 = "What is 36 / 9?"
#Q3 = "What is 33 * 3?"
#Q4 = "What is 36 + 3?"
#Q5 = "What is 100^2?"
#Q6 = "What is 16.9 * 30 / 3?"
#Q7 = "What is 654 / 3?"
#Q8 = "What is 675 - 623?"
#Q9 = "What is 4^3?"
#Q10 = "What is 555 - 423?"

#Answer list
#Q1A = "12"
#Q2A = "4"
#Q3A = "99"
#Q4A = "39"
#Q5A = "10000"
#Q6A = "930"
#Q7A = "218"
#Q8A = "187"
#Q9A = "64"
#Q10A = "222"

#Question inputs
#print(Q1)
#Q1I = int(input("What is the answer? "))
#if Q1I == 12:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#print(Q2)
#Q2I = int(input("What is the answer? "))
#if Q2I == 4:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#print(Q3)
#Q3I = int(input("What is the answer? "))
#if Q3I == 99:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#print(Q4)
#Q4I = int(input("What is the answer? "))
#if Q4I == 39:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#print(Q5)
#Q5I = int(input("What is the answer? "))
#if Q5I == 10000:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Zoinks! That's wrong!")
 #score = score - 1

#print(Q6)
#Q6I = int(input("What is the answer? "))
#if Q6I == 930:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#print(Q7)
#Q7I = int(input("What is the answer? "))
#if Q7I == 218:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#print(Q8)
#Q8I = int(input("What is the answer? "))
#if Q8I == 187:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#print(Q9)
#Q9I = int(input("What is the answer? "))
#if Q9I == 64:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#print(Q10)
#Q10I = int(input("What is the answer? "))
#if Q10I == 222:
 #print("Correct Well Done!")
 #score = score + 1

#else:
 #print("Yikes! That's wrong!")
 #score = score - 1

#Results
#print("Well Done", name, "You have completed the quiz!, you have got", score,"/10!")


#Program Challenge
#Num1 = int(input("Enter a number: "))
#Num2 = int(input("Enter another number: "))
#menuoption = str(input("Would you like to add the two inputed numbers? (Y/N): "))
#if menuoption == "Y":
 #answer = Num1 + Num2
 #print(answer)
#elif menuoption == "N":
 #answer = Num1 - Num2
 #print(answer)

#Program Challenge
X = 10
Y = 20
Z = 30

if X == 10:	
  if Y == 20:
    print("End of nested if block")
else:
 print("End of nested if-else block")
if X == 10:
 if Y == 20:
  print("Elif block")
if X == 10:
 print("End of nested if block")
if Y != 20:
 if Z == 30:
  print("End of nested if block")
if Z != 30:
 print("End of nested if-else block")