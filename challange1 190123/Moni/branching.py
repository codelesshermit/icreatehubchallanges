status=input ('Choose your Status (Freshman, Sophomore, Junior or Senior): ')
GPA=input ('Key in your GPA (Between 0 to 4.0): ')
GPA=float(GPA)
major=input ('What is your Major: (Capitalize Each word, for example. Computer Science) ')
if (status=='Freshman' and GPA>=3.5) or (status=='Freshman' and major=='Computer Science'):
    print ('You Qualifies for a $1000 Scholarship')
elif status=='Sophomore' and GPA==4.0:
    print ('You Qualifies for a $5000 Scholarship')
elif (status=='Sophomore' and GPA>=3.0) or (status=='Sophomore' and major=='Computer Science'):
    print ('You Qualifies for a $1000 Scholarship')
elif status=='Junior' and GPA>=3.0 and major=='Computer Science':
    print ('You Qualifies for a $5000 Scholarship')
elif status=='Junior' and GPA>=3.5:
    print ('You Qualifies for a $1000 Scholarship')
elif (status=='Senior' and GPA==4.0) or major=='Computer Science':
    print ('You Qualifies for a $10000 Scholarship')
else:
    print('You Do Not Qualifies for a Scholarship')