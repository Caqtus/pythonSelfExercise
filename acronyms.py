def acronym():
    user_input = str(input('input text: '))
    text = user_input.split()
    a = ''

    for i in text:
        a = a + str(i[0]).upper()
    print(f'-= {a} =-')
