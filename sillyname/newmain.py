import random
print("Welcome to the 'Psych Namepicker'\n")

first = ('huge','small','tiny','smelly','lovely','chinese','france','indo','lion','hippo','black','niggaone','niggadope','smallpp','pussy','cock','white','blackman','yellowdicks')

last=('dickens','pussies','deeznuts','lovelypants','washerum','burgers','bazaars','donalddicks','hugecocks','ppsmallie','sweetmans')


while(True):
    firstName = random.choice(first)
    #middleName = random.choice(middle)
    lastName = random.choice(last)

    print(firstName ,lastName )

    inputn = input("\nPress enter to generate new names or n to exit\n")

    if (inputn =="n"):
        break





