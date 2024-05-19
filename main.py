
delay = int(input('Whats the delay?    '))
enter = input('Do you need to press enter after inputing password? y = yes      ')
password_length = int(input('How many passwords do you have?     '))
code_file = open('code.txt','w')
password_file = open('passwords.txt','r')


for i in range(0,password_length):
  password = password_file.readline()
  code_file.write(f'Delay {delay} \n')
  code_file.write(f'STRING {password}')
  if enter == 'y' or enter == 'Y':
    code_file.write('enter \n')
    