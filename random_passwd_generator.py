from random import choice

len_of_passwd = 10

things_tobe_in = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&"

passwd = []

for i in range(len_of_passwd):
    passwd.append(choice(things_tobe_in))
    
main_pass = "".join(passwd)
print(main_pass)

#in single line
# random_pass = "".join(choice(things_tobe_in) for i in range(len_of_passwd))
# print(random_pass)