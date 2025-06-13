print("--Instructions--")
print("Exam Type:- Multiple Choice Questions")
print("should answer all questions.")
print("Each carries 1 mark.")
print("No negative marking.")
print()
count=0
print("Q1. Which type of language is python?")
print("a. Statically typed language   " \
"b. Dynamically typed language   " \
"c. Both   " \
"d.None   ")
a1=input("Enter option(a/b/c/d):-  ")
if a1=="b":
    print("correct option .")
    count=count+1
else:
    print("wrong option")
print()
print("Q2.what is the output of string 2 +string 3 ")
print("a.5  "
      "b.23  "
      "c.Error  "
      "d.None ")
a2=input("Enter option(a/b/c/d):-  ")
if a2=="b":
    print("correct option .")
    count=count+1
else:
    print("wrong option")
print()
print("Q3. Which of the following is a valid variable name in Python?")
print("a. 2name  "
      "b. my-name  "
      "c. my_name  "
      "d. class  ")
a3=input("Enter option(a/b/c/d):-  ")
if a3=="c":
    print("correct option .")
    count=count+1
else:
    print("wrong option")
print()
print("Q4. Which of the following is used to define a block of code in Python?")
print("a.parentheses  "
      "b.curly brases  "
      "c.Indentation  "
      "d.Quotation marks")
a4=input("Enter option(a/b/c/d):-  ")
if a4=="c":
    print("correct option .")
    count=count+1
else:
    print("wrong option")
print()
print("Q5. Which keyword is used to define a function in Python?")
print("a.func  "
      "b.define  "
      "c.function  "
      "d.def  ")
a5=input("Enter option(a/b/c/d):-  ")
if a5=="d":
    print("correct option .")
    count=count+1
else:
    print("wrong option")

print("Final Score :- ",count,"/5")