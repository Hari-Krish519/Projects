email = input("Enter Your Email Address:")
k,j,d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) & (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or j==1 or d==1:
                        print("Email Invalid: Email address does not allow space/uppercase")

            else:
                print("Email Invalid: Please check for missing period '.' in the email address")
        else:
            print("Email Invalid: Please check '@' is missing or '@' is entered more than once")
    else:
        print("Email Invalid: Email starts only with alphabet letters")
else:
    print("Email Invalid: Your Email does not satisfy the Minimum Characters")
    
    
    