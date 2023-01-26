major_input = input('Enter your Major: ').lower()
gpa_input = float(input('Enter your GPA: '))
status_input = input('Enter your status: ').lower()


if status_input == 'senior' and major_input == 'computer science' or gpa_input >= 4.0:
    print('You qualify for $10,000 Scholarship')
    
elif status_input == 'sophomore' and gpa_input >= 4.0 or  status_input == 'junior' and gpa_input >= 3.0 and major_input == 'computer science':
    print('You qualify for $5,000 Scholarship')
    
elif status_input == 'junior' and gpa_input > 3.5 or status_input == 'sophomore' and gpa_input >= 3.5 and major_input == 'computer science' or status_input == 'freshman' and gpa_input >= 3.5 or major_input == 'computer science':
    print('You qualify for $1,000 Scholarship')
    
else:
    print('Sorry! You do not qualify for a Scholarship')

