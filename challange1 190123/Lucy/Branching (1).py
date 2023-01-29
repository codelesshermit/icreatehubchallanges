status = input("Enter your status(freshman,sophomore,junior,senior):")
gpa = float(input("Enter you GPA(0-4.0):"))
major = input("Enter your major:")
if status == "freshman" and (gpa>=3.5 or major =="computer science"):
    print("you qualify for a $1000 scholarship.")
elif status=="sophomore" and gpa>=3.0 and major=="computer science":
    print("you qualify for a $1000 scholarship.") 
elif status=="junior" and gpa>=3.5:
    print("you qualify for  a $1000 scholarship.")  
elif status =="sophomore" and gpa>=4.0:
    print("you qualify for a $5000 scholarship.") 
elif status =="junior" and gpa>=3.0 and major and major=="computer science":
    print("you qualify for a $5000 scholarship.")   
elif status=="senior" and (gpa==4.0 or major=="computer science"):
    print("you qualify for a $10000 scholarship.")
else:
    print("You do not qualify for a scholarship")     
            