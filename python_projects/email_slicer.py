#accept the email 
email = input('Enter your email: ').strip()

user = email[:email.index('@')]
domain = email[email.index('@')+1 :]
print(f'username is {user} and domain is {domain}')