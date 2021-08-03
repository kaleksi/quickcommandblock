#paste command block code into commandblock.txt
#when you recieve an error in game (ex: a syntax error at character 347)
#input the location of the error into the index

f = open("commandblock.txt", "r")

command_block = f.read()

print(command_block[347:400)
#in the square brackets, input the range of characterss you would like to pull to locate your error
#you can ctrl+f in text editor to search the line and correct it

f.close()
