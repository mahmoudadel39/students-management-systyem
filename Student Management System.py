import json
try:
    with open("students.json","r")as file:
     students= json.load(file)
except:
     students=[]

def main_menu(students):
     
     while True:
          try:
               print("\n1. Display All Students\n2. Add New Student\n3. Show Top Students\n4. Search Student\n5. Exit\n")
               choose = input("choose an option: ")
               if choose == "1":
                    display_students(students)
               elif choose== "2":
                    add_student(students)
               elif choose== "3":
                    get_top_students(students)
               elif choose=="4":
                    search_student(students)
               elif choose== "5":
                    break
               else:
                    print("\nEnter Valid Value\n")
          except ValueError :
               print("\nEnter Valid Value\n")
                    
def save_students(students):
     with open("students.json","w")as file:
          json.dump(students,file,indent=4)
                    

def calculate_average(student):
     return round(sum(student["grades"])/len(student["grades"]),2)
   
def search_student(students):
     found=False
     try:
          name = input("enter student Name : ").strip().lower()
          for i in students:
               if i["name"].lower()==name:
                    found=True
                    print(i["name"],i["age"],calculate_average(i))
                    break
          if found ==False:
               print("student not founded")
     except ValueError:
          print("enter valid Name")
     
          

def get_top_students(students):
     top = list(filter(
          lambda student:calculate_average(student) >80
          ,students))
     print("\n\n========== Top Students ==========\n")
     for student in top:
          print(f"Name: {student['name']}\nAge: {student['age']}\nGrades: {student['grades']}\nAverage: {calculate_average(student) }\n\n-----------------------------------\n")
     
        
def display_students(students):
     print("\n\n\n========== Students List ==========")
     for student in students:
          print(f"Name: {student['name']}\nAge: {student['age']}\nGrades: {student['grades']}\nAverage: {calculate_average(student) }\n\n-----------------------------------\n")
          
def add_student(students):
     name= input("Enter Student Name : ")
     while True:
          try: 
               age = int(input("Enter Student Age : "))
               break
          except ValueError:
               print("Enter vaild Numbers")
     while True:
          try: 
               sgrades = input("Enter Student Grades : ").split()
               grades = list(map(int,sgrades))
               if len(grades)==3:
                     students.append({
                         "name":name,
                         "age":age,
                         "grades":grades

                         })
                     break
               else:
                    print("enter valid numbers")
                          
          except ValueError:
               print ("enter valid numbers")
     save_students(students)
      
print("\n\n========== Student Management System ==========\n")  

main_menu(students)


   

