
def discount(is_Member, age, is_Resident):
    if(age <12 or age>= 65) or (is_Member or is_Resident):
        print("discount")
    else:
        print("no discount")