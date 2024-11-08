 
months_dict = {1:31 , 2:28 , 3:31 , 4:30 , 5:31 , 6:30                  
                , 7:31 , 8:31 , 9:30 , 10:31 , 11:30 , 12:31}
selected_month = int(input("Enter the number of the month (1-12): "))   

if selected_month < 1 or selected_month > 12:                          
    print("Incorrect! Enter a number between 1-12")
elif selected_month == 2:                                                
    leap_year_input = 2
    leap_year_input = input("It's a leap year? Answer [yes/no]: ")          

    if leap_year_input == "yes":                                    
        months_dict[2] = 29
        days_in_selected_month = months_dict[selected_month]
else:
    leap_year_input = "no"
days_in_selected_month = months_dict[selected_month]

print(f"The {selected_month} has {days_in_selected_month} days.")




        

