#I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID : w1953252
#Date : 04/12/2022

results = 'y'

credits_list = [0,20,40,60,80,100,120]    #Used to check if the credits entered are multiples of 20
progress = []                             #List created to store the students who have obtained progress for the module
trailer = []                              #List created to store the students who have obtained trailer for the module
retriever = []                            #List created to store the students who have obtained retriever for the module
excluded = []                             #List created to store the students who have obtained excluded for the module
output_dictionary = {}                    #Dictionary created to store the UOW ID as the key and the credits obtained as values

def histogram():                           #The function created to display the histogram
    print('-----------------------------------------------------------------------------')
    print('Histrogram')
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


while results != 'q' :

    print('')

    while True:
        uow_ID = input('Enter the UOW ID : ')           #Obtains the inputs from the user

        if uow_ID[0] == 'w':                            #Checking that the UOW ID begins with 'w'
            if len(uow_ID) == 8 :                       #Checking if the length of UOW ID has 8 characters
                try:
                    ID = int(uow_ID[1:8])               #Convert the UOW ID into integer from the 2nd position onwards
                    break

                except ValueError:                      #if the UOW ID doesn't have 7 integers display the following
                    print('Wrong UOW ID')

            else:
                print('Wrong UOW ID')

        else:
            print('Wrong UOW ID')


    try:
        pass_credits = input('Please enter your credits at pass : ')            #entering the pass credits
        pass_credits = int(pass_credits)

        while True:
            if pass_credits in credits_list:                        #Checking if the pass credits are in the credits list
                break
        
            else:
                print('Out of range')
                pass_credits = input('Please enter your credits at pass : ')
                pass_credits = int(pass_credits)
    
    
        defer_credits = input('Please enter your credits at defer : ')          #entering the defer credits
        defer_credits = int(defer_credits)

        while True:
            if defer_credits in credits_list:                   #Checking if the defer credits are in the credits list
                break
        
            else:
                print('Out of range')
                defer_credits = input('Please enter your credits at defer : ')
                defer_credits = int(defer_credits)

        fail_credits = input('Please enter your credits at fail : ')           #entering the fail credits
        fail_credits = int(fail_credits)

        while True:
            if fail_credits in credits_list:                    #Checking if the fail credits are in the credits list
                break
        
            else:
                print('Out of range')
                fail_credits = input('Please enter your credits at fail : ')
                fail_credits = int(fail_credits)


    except ValueError:                                          #If the input entered by the user not an integer diplay the following
        print('Integer required')

        continue


    total_credits = pass_credits + defer_credits + fail_credits

    if total_credits != 120:                                #if the total credits are not equals to 120 display the following
        print('Total incorrect.')
        continue

    else:                                                   #If the total credits are equal to 120 continue
        if pass_credits == 120:
            print('Progress')
            progress.append('*')                            #Prints '*' according to the number of students who have obtained progress for the module
            output_dictionary[uow_ID] = ('Progress - '+str(pass_credits)+', '+str(defer_credits)+', '+str(fail_credits))

        elif pass_credits == 100:
            print('Progress(module trailer)')
            trailer.append('*')                             #Prints '*' according to the number of students who have obtained trailer for the module
            output_dictionary[uow_ID] = ('Progress (module trailer) - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

        elif pass_credits == 80:
            print('Do not Progress - module retriever')
            retriever.append('*')                           #Prints '*' according to the number of students who have obtained retriever for the module
            output_dictionary[uow_ID] = ('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

        elif pass_credits == 60:
            print('Do not Progress - module retriever')
            retriever.append('*')                           #Prints '*' according to the number of students who have obtained retriever for the module
            output_dictionary[uow_ID] = ('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

        elif pass_credits == 40:
            if fail_credits == 80:
                print('Exclude')
                excluded.append('*')                        #Prints '*' according to the number of students who have obtained exclude for the module
                output_dictionary[uow_ID] = ('Exclude - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

            else:
                print('Do not Progress - module retriever')
                retriever.append('*')                       #Prints '*' according to the number of students who have obtained retriever for the module
                output_dictionary[uow_ID] = ('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

        elif pass_credits == 20:
            if fail_credits >= 80:
                print('Exclude')
                excluded.append('*')                        #Prints '*' according to the number of students who have obtained exclude for the module
                output_dictionary[uow_ID] = ('Exclude - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

            else:
                print('Do not Progress - module retriever')
                retriever.append('*')                       #Prints '*' according to the number of students who have obtained retriever for the module
                output_dictionary[uow_ID] = ('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

        else:
            if fail_credits >= 80:
                print('Exclude')
                excluded.append('*')                       #Prints '*' according to the number of students who have obtained exclude for the module
                output_dictionary[uow_ID] = ('Exclude - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

            else:
                print('Do not Progress - module retriever')
                retriever.append('*')                       #Prints '*' according to the number of students who have obtained retriever for the module
                output_dictionary[uow_ID] = ('Module retriever - ' + str(pass_credits) + ', ' + str(defer_credits) + ', ' + str(fail_credits))

    print('')

    print('Would you like to enter another set of data?')
    results = input("Enter 'y' for yes or 'q' to quit and view results : ")         #getting an input from the user if we should continue or quit the program and display the histogram

    while True:
        if results in ['y','q']:                              #if the input entered by the user is in the list break the loop and display the histogram
            break

        else:
            print('Invalid')
            print('Would you like to enter another set of data?')
            results = input("Enter 'y' for yes or 'q' to quit and view results : ")


histogram()                         #calling the function that has been defined above to display the histogram

for a,b in output_dictionary.items():               #prints the dictionary with the relavent keys ad values
    print(a,':',b,end=' ')