from colorama import Fore,Style
month=int(input("input the month 1-12   "))
year=int(input("input the year between 1800-2099   "))
mont=('JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER')
day=['SU','MO','TU','WE','TH','FR','SAT']
color=[Fore.RED,Fore.GREEN,Fore.BLUE,Fore.CYAN,Fore.BLACK,Fore.YELLOW,Fore.MAGENTA,Fore.LIGHTGREEN_EX,Fore.RED,Fore.GREEN,Fore.BLUE,Fore.CYAN]
if month<1 or month>12 or year<1800 or year>2099:
    print("wrong input for month or year") 
else:
   
         if (year%4==0) and (not(year%100==0)or(year%400==0)):
               leap_year=True
         else:
               leap_year=False
         if  month in (1,3,5,7,8,10,12):
               num_day=31
         elif month in(4,6,9,11):
               num_day=30
         elif leap_year:
               num_day=29
         else:
               num_day=28
         #calculating starting date of month
         cen_digit=year//100
         year_digit=year%100
         value=year_digit+(year_digit//4)
         if cen_digit==18:
             value=value+2
         elif cen_digit==20:
             value=value+6
         if month==1 and not leap_year:
             value=value+1
         elif month==2:
             if leap_year:
                 value=value+3
             else:
                 value=value+4
         elif  month==3 or month==11:
             value=value+4
         elif month==5:
             value=value+2
         elif month==6:
             value=value+5
         elif month==8:
             value=value+3
         elif month==9 or month==12:
             value=value+6
         elif month==10:
             value=value+1
         day_of_week=(value+1)%7
         print(color[month-1]+mont[month-1]+Style.BRIGHT,year)
         print()
         for i in day:
             print(" ",i,end=" ")
         print()    
         
         if day_of_week==0:
             start_col=7
         else:
             start_col=day_of_week
         curr_col=1
         col_width=4
         blank_char=' '
         blank_col=format(blank_char,str(col_width))
         
         while curr_col<start_col:
             print(blank_col,end=" ")
             curr_col=curr_col+1
         curr_day=1
         while curr_day<=num_day:
             if curr_day<10:
                 
                 print(format(blank_char,'3')+str(curr_day),end=" ")
             else:
                 print(format(blank_char,'2')+str(curr_day),end=" ")
             if curr_col<7:
                 curr_col=curr_col+1
             else:
                 curr_col=1
                 print()
             curr_day=curr_day+1
         print('\n')   
         if leap_year:
               print(year,"year is leap year")
         else:
               print(year,'year is not leap year') 
                
               
   
            
