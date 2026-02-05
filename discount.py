age = int(input("what is your age"))
is_Member = input("are you a member")
is_Resident = input("are you a resident")
def discount():
    if(age <12 or age>= 65) or (is_Member or is_Resident):
        print("discount")
    else:
        print("no discount")
discount()