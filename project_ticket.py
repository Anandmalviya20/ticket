#movie_ticket
total_price =0
entries=" "
num =0
status = True
while status :
    age = int(input("Age :"))

    if age >0 and age <= 12:
        price = 5 
        stage ="Children"                                   
    elif age >12 and age<=17:
        price =8
        stage ="Teenagers"
    elif age >17 and age<=64:
        price =12 
        stage =  "Adults" 
    elif age >64 :
        price =7
        stage = "seniors"
    total_price+=price 
    num+=1 
    entries += str(num)+") "+ str(age)+"year" + " - "+ stage +" $" + str(price) +", "
    choose = input("Y/N : ")
    if choose =="Y" :
        status = True
    else :
        status = False  

day = input(" Day (enter in lower case ) : ").lower()
#Age-Based Pricing:
'''Children (ages 0-12) get a ticket for $5.
Teenagers (ages 13-17) get a ticket for $8.
Adults (ages 18-64) get a ticket for $12.
Seniors (ages 65 and above) get a ticket for $7.'''
if age >0 and age <= 12:
    price = 5 
    stage ="Children"                                   
elif age >12 and age<=17:
    price =8
    stage ="Teenagers"
elif age >17 and age<=64:
    price =12 
    stage =  "Adults" 
elif age >64 :
    price =7
    stage = "seniors"   
ticket_price= price
'''Discount Based on Day of the Week:
If the movie is on a weekend (Saturday or Sunday), apply a 10% discount to the ticket price.
If the movie is on a weekday (Monday to Friday), no discount is applied.
'''
if day == "sunday" or day == "saturday" :
    dis =10
else :
    dis = "no discount" 
dis_price= total_price*(1-dis/100) 
print(f"""     
         _________________________________ 
         age = {age} year
         day ={day} 
         members = {entries}
         base price = $ {total_price}
         Discount ={dis} %
         ___________________________
         net price = $ {dis_price}   
        ______________________________
        """)

