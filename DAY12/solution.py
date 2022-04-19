def email(no_mail):

    student = []
    lecturer = []

    email1 = "@student.college.edu"
    email2 = '@lecturer.college.edu'

    count = 0

    while count < int(no_mail):
        email3 = input('Enter the email : ')
        if email1[-21:] in email3:
            student.append(email3)
            count += 1

        elif email2[-21:] in email3:
            lecturer.append(email3)
            count += 1
        
        else:
            print('Not a recognised Email !!')

    print('No of student mail is ', len(student))
    print('No of lecturer email is : ', len(lecturer))


email(input('Enter the no of email : '))