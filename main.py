print("enter the type of bill you want to calculate: ")
print("1. Electricity")
print("2. water")

payment_type = int(input("Enter the type of bill yu want to calculate: "))

if payment_type ==1:
   try:
       meter_amount = int(input("Enter your electric meter readingin kwH: "))
       household = int(input("Enter the number of people in your household- max 20 people: "))
       print('Calculating electricity bill...')
     
       if meter_amount <= 100:
          payment = meter_amount * 5
          per_household = payment/household
          print('Your electricity bill is be $',payment )
          if per_household <= 200:
              print('Your per_household rate is', per_household, 'This is normal')
          elif per_household > 200:
              print('Your per_household rate is', per_household, 'This is above average')
       elif meter_amount > 100 and meter_amount <= 1000:
           payment = meter_amount * 5
           per_household = payment/household
           print('Your Total electricity bill is $',payment )
           if per_household <= 200:
               print('Your per_household rate is', per_household, 'This is normal')
           elif per_household > 200:
               print('Your per_household rate is', per_household, 'This is above average')
       elif meter_amount >1000:
           payment = meter_amount * 5
           per_household = payment/household
           print('Your Total electricity bill is $',payment )
           if per_household <= 200:
              print('Your per_household rate is', per_household, 'This is normal')
           elif per_household > 200:
              print('Your per_household rate is', per_household, 'This is above average')
   except:
         print('Error: Enter a vaid meter reading')

if payment_type == 2:
   try: 
      meter_amount = int(input("Enter your water meter readingin m^3: "))
      household = int(input('Enter the number of people in 6household-max 20 people: '))
      print('Calculating water bill...')
     
      if meter_amount <= 500:
          payment = meter_amount * 50
          per_household = payment/household
          print('Your electricity bill is be $',payment )
          if per_household <= 200:
              print('Your per_household rate is', per_household, 'This is normal')
          elif per_household > 200:
              print('Your per_household rate is', per_household, 'This is above average')
          elif meter_amount > 500 and meter_amount <= 2500:
           payment = meter_amount * 60
           per_household = payment/household
           print('Your Total electricity bill is $',payment )
           if per_household <= 200:
               print('Your per_household rate is', per_household, 'This is normal')
           elif per_household > 200:
               print('Your per_household rate is', per_household, 'This is above average')
          elif meter_amount >2500:
           payment = meter_amount * 70
           per_household = payment/household
           print('Your Total electricity bill is $',payment )
           if per_household <= 200:
              print('Your per_household rate is', per_household, 'This is normal')
           elif per_household > 200:
              print('Your per_household rate is', per_household, 'This is above average')
   except:
         print('Error: Enter a vaid meter reading')
