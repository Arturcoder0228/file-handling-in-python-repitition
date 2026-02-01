# with open("pi.text") as file:
#     pi = file.read()

# pi = pi.rstrip()
# pi = pi.replace("\n", "")


# print(pi)


# filename = 'data/talabalar.text'
# # with open(filename) as file:
# #     for line in file:
# #         print(line)


# with open(filename) as file:
#     talabalar = file.readlines()

# print(talabalar)

# for talaba in talabalar:
#     talabalar = talaba.rstrip()
# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)


# filename = 'data/new_file.txt'
# ism = 'Settarov Artur'
# yosh = 2005
# with open(filename, 'w') as filerite:

#     filerite.write(ism+ '\n')
#     filerite.write(str(yosh)+ '\n')
    

filename = 'data/new_file.txt'

with open(filename, 'a') as filerite:

    filerite.write('ali' + '\n')
    filerite.write(str(2004)+ '\n')
    


