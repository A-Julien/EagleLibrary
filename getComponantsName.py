from bs4 import BeautifulSoup
import sys

inputfile = sys.argv[1]
Outfile = sys.argv[2]


try:
    in_file = open(inputfile, 'r')
    out_file = open(Outfile, 'a')

    parser = BeautifulSoup(in_file)
       
    for index in enumerate(in_file):
        print(parser.findAll("package")[index]["name"])

        #out_file.write("- "+cName+'\n') #if you want to use commas to seperate the files, else use something like \n to write a new line.
finally:
    in_file.close()
    out_file.close()