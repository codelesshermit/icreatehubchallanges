def check_eligibility(status, gpa, major):
    if status == "freshman":
        if gpa >= 3.5 or major == "computer science":
            return "Eligible for $1000 scholarship"
    elif status == "sophomore":
        if gpa >= 3.0 and major == "computer science":
            return "Eligible for $1000 scholarship"
        elif gpa >= 4.0:
            return "Eligible for $5000 scholarship"
    elif status == "junior":
        if gpa >= 3.5:
            return "Eligible for $1000 scholarship"
        elif gpa >= 3.0 and major == "computer science":
            return "Eligible for $5000 scholarship"
    elif status == "senior":
        if gpa >= 4.0 or major == "computer science":
            return "Eligible for $10000 scholarship"
    else:
        return "Not eligible for a scholarship"

status = input("Enter your status (freshman, sophomore, junior, senior): ")
gpa = float(input("Enter your GPA (0-4.0): "))
major = input("Enter your major: ")

print(check_eligibility(status, gpa, major))
