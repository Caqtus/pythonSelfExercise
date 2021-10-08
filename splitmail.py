



def splitMail():
    email = input(f'enter your email:').strip()
    username = email[:email.index("@")]
    domain = email[email.index("@")+1:]
    print('Your username is {}, and domain name is {}'.format(username, domain))



