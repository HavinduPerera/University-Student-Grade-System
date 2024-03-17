#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID : w1953252
#Date : 04/12/2022

results = 'y'

credits_list = [0,20,40,60,80,100,120]      #Used to check if the credits entered are multiples of 20
progress = []                               #List created to store the students who have obtained progress for the module (histogram)
trailer = []                                #List created to store the students who have obtained trailer for the module (histogram)
retriever = []                              #List created to store the students who have obtained retriever for the module (histogram)
excluded = []                               #List created to store the students who have obtained excluded for the module (histogram)
output_list = []                            #List created to store the students results for the list

def histogram():                    #The function created to display the histogram
    print('-----------------------------------------------------------------------------')
    print('Histogram')
    print('Progress', len(progress),'\t: ',end ='')
    for i in progress:
        print('*',end = '')
    print('')

    print('Trailer', len(trailer),'\t: ',end ='')
    for i in trailer:
        print('*',end ='')
    print('')

    print('Retriever', len(retriever),'\t: ',end ='')
    for i in retriever:
        print('*',end ='')
    print('')

    print('Excluded', len(excluded),'\t: ',end ='')
    for i in excluded:
        print('*',end ='')
    print('')

    total = len(progress) + len(trailer) + len(retriever) + len(excluded)

    print(total,'outcomes in total.')
    print('-----------------------------------------------------------------------------')


def textfile():                                 #The function created to open and write in to the textfile
    for x in output_list:
        f = open('output.txt', 'a')
        f.write(x)
        f.write('\n')
        f.close()

print('Are you a student or staff member?')
m = input("Enter 's' for student or enter 'sm' for staff member : ")        #student version or staff version
print('')


while True:
    if m in ['s','sm']:                                 #If the input entered by the user is a student or staff member the loop breaks
        break

    else:
        print('Invalid')                                    #If the input entered by the user is not a student or staff member display that the input is invalid
        print('Are you a student or staff member?')
        m = input("Enter 's' for student or enter 'sm' for staff member : ")
        print('')

if m == 's':                    #Continues if the input entered by the user is student
    while True:
        try:
            pass_credits = input('Please enter your credits at pass : ')        #entering the pass credits
            pass_credits = int(pass_credits)

            while True:
                if pass_credits in credits_list:                 #Checking if the pass credits are in the credits list
                    break

                else:
                    print('Out of range')
                    pass_credits = input('Please enter your credits at pass : ')
                    pass_credits = int(pass_credits)

            defer_credits = input('Please enter your credits at defer : ')          #entering the defer credits
            defer_credits = int(defer_credits)

            while True:
                if defer_credits in credits_list:                #Checking if the defer credits are in the credits list
                    break

                else:
                    print('Out of range')
                    defer_credits = input('Please enter your credits at defer : ')
                    defer_credits = int(defer_credits)

            fail_credits = input('Please enter your credits at fail : ')        #entering the fail credits
            fail_credits = int(fail_credits)

            while True:
                if fail_credits in credits_list:                 #Checking if the fail credits are in the credits list
                    break

                else:
                    print('Out of range')
                    fail_credits = input('Please enter your credits at fail : ')
                    fail_credits = int(fail_credits)


        except ValueError:                              #If the input entered by the user not an integer diplay the following
            print('Integer required')
            continue


        total_credits = pass_credits + defer_credits + fail_credits

        if total_credits != 120:                #if the total credits are not equals to 120 display the following
            print('Total incorrect.')
            continue

        else:                                   #If the total credits are equal to 120 continue
            if pass_credits == 120:
                print('Progress')

            elif pass_credits == 100:
                print('Progress(module trailer)')

            elif pass_credits == 80:
                print('Do not Progress - module retriever')

            elif pass_credits == 60:
                print('Do not Progress - module retriever')

            elif pass_credits == 40:
                if fail_credits == 80:
                    print('Exclude')

                else:
                    print('Do not Progress - module retriever')

            elif pass_credits == 20:
                if fail_credits >= 80:
                    print('Exclude')

                else:
                    print('Do not Progress - module retriever')

            else:
                if fail_credits >= 80:
                    print('Exclude')

                else:
                    print('Do not Progress - module retriever')

        print('')
        break

else:

    while results != 'q' :                          #Loops until results is not equal to q
        total_credits = 0

        print('')

        try:
            pass_credits = input('Please enter your credits at pass : ')        #entering the pass credits
            pass_credits = int(pass_credits)

            while True:
                if pass_credits in credits_list:                    #Checking if the pass credits are in the credits list
                    break

                else:
                    print('Out of range')
                    pass_credits = input('Please enter your credits at pass : ')
                    pass_credits = int(pass_credits)


            defer_credits = input('Please enter your credits at defer : ')          #entering the defer credits
            defer_credits = int(defer_credits)

            while True:
                if defer_credits in credits_list:               #Checking if the defer credits are in the credits list
                    break

                else:
                    print('Out of range')
                    defer_credits = input('Please enter your credits at defer : ')
                    defer_credits = int(defer_credits)

            fail_credits = input('Please enter your credits at fail : ')            #entering the fail credits
            fail_credits = int(fail_credits)

            while True:
                if fail_credits in credits_list:            #Checking if the fail credits are in the credits list
                    break

                else:
                    print('Out of range')
                    fail_credits = input('Please enter your credits at fail : ')
                    fail_credits = int(fail_credits)


        except ValueError:                              #If the input entered by the user not an integer diplay the following
            print('Integer required')

            continue


        total_credits = pass_credits + defer_credits + fail_credits

        if total_credits != 120:                        #if the total credits are not equals to 120 display the following
            print('Total incorrect.')
            continue

        else:                                            #If the total credits are equal to 120 continue
            if pass_credits == 120:
                print('Progress')
                progress.append('*')                    #Prints '*' according to the number of students who have obtained progress for the module
                output_list.append('Progress - '+str(pass_credits)+', '+str(defer_credits)+', '+str(fail_credits))

            elif pass_credits == 100:
                print('Progress(module trailer)')
                trailer.append('*')                     #Prints '*' according to the number of students who have obtained trailer for the module
                output_list.append('Progress (module trailer) - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

            elif pass_credits == 80:
                print('Do not Progress - module retriever')
                retriever.append('*')                   #Prints '*' according to the number of students who have obtained retriever for the module
                output_list.append('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

            elif pass_credits == 60:
                print('Do not Progress - module retriever')
                retriever.append('*')                   #Prints '*' according to the number of students who have obtained retriever for the module
                output_list.append('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

            elif pass_credits == 40:
                if fail_credits == 80:
                    print('Exclude')
                    excluded.append('*')                #Prints '*' according to the number of students who have obtained retriever for the module
                    output_list.append('Exclude - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

                else:
                    print('Do not Progress - module retriever')
                    retriever.append('*')               #Prints '*' according to the number of students who have obtained retriever for the module
                    output_list.append('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

            elif pass_credits == 20:
                if fail_credits >= 80:
                    print('Exclude')
                    excluded.append('*')                #Prints '*' according to the number of students who have obtained exclude for the module
                    output_list.append('Exclude - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

                else:
                    print('Do not Progress - module retriever')
                    retriever.append('*')               #Prints '*' according to the number of students who have obtained retriever for the module
                    output_list.append('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

            else:
                if fail_credits >= 80:
                    print('Exclude')
                    excluded.append('*')                #Prints '*' according to the number of students who have obtained exclude for the module
                    output_list.append('Exclude - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

                else:
                    print('Do not Progress - module retriever')
                    retriever.append('*')               #Prints '*' according to the number of students who have obtained retriever for the module
                    output_list.append('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

        print('')

        print('Would you like to enter another set of data?')
        results = input("Enter 'y' for yes or 'q' to quit and view results : ")     #getting an input from the user if we should continue or quit the program and display the histogram

        while True:
            if results in ['y','q']:                #if the input entered by the user is in the list break the loop and display the histogram
                break

            else:
                print('Invalid')
                print('Would you like to enter another set of data?')
                results = input("Enter 'y' for yes or 'q' to quit and view results : ")


    histogram()             #calling the function that has been defined above to display the histogram

    for i in output_list:       #prints the list with the respective progression outcomes and credits obtained
        print(i)

    textfile()              #calling the function that has been defined above to create the text file and insert the respective progression outcomes with the credits obtained
