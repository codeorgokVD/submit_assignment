#Function definition to check the arguments and to create a list with the needed argument list
def arg_check_func(arg_list):

    welcome_list = []
    script_name = arg_list[0]

    for arg in arg_list:
        #If there is only 1 argument, then add "World" to the list
        if(len(arg_list) == 1):
            welcome_list.append("World")
        #Else check the equality of the script name
        else:
            if (arg == script_name):
                continue
            #If there is more than 1 argument and it is not the script name, then add it to the list
            welcome_list.append(arg)

    #Return the filled list
    return welcome_list



import sys

#Function call
welcome_list = arg_check_func(sys.argv)

#Prints each element of the list
for welcome_names in welcome_list:
    print("Hello ", welcome_names, "!", sep ="")