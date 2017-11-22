print ('''
############################################################################################
#                          								   #	
#  __    __                      __              __        __  __  __                      #           
# |  \  |  \                    |  \            |  \      |  \|  \|  \                     #           
# | $$  | $$  ______    _______ | $$____        | $$   __  \$$| $$| $$  ______    ______   #           
# | $$__| $$ |      \  /       \| $$    \       | $$  /  \|  \| $$| $$ /      \  /      \  #           
# | $$    $$  \$$$$$$\|  $$$$$$$| $$$$$$$\      | $$_/  $$| $$| $$| $$|  $$$$$$\|  $$$$$$\ #           
# | $$$$$$$$ /      $$ \$$    \ | $$  | $$      | $$   $$ | $$| $$| $$| $$    $$| $$   \$$ #           
# | $$  | $$|  $$$$$$$ _\$$$$$$\| $$  | $$      | $$$$$$\ | $$| $$| $$| $$$$$$$$| $$       #           
# | $$  | $$ \$$    $$|       $$| $$  | $$      | $$  \$$\| $$| $$| $$ \$$     \| $$       #           
#  \$$   \$$  \$$$$$$$ \$$$$$$$  \$$   \$$       \$$   \$$ \$$ \$$ \$$  \$$$$$$$ \$$       #           
#                                                                                          #          
#                               Coded By: Ismail Al_safadi                                 #          
############################################################################################               
''')


def info():
	print "information"
	print "This tool coded by: Ismael Al-safadi"
	print "to use the tool "
	print "[*] -chr = the possibilities"
	print "[*] -min = the minimum length of password"
	print "[*] -max = the maximum length of password"
	print "[*] -t = the type of the hash"
	print "[*] -hash = the value of the hash"
	print "[+] Example"
	print "python hash-kill.py -chr 1234567890 -min 5 -max 5 -t md5 -hash d3eb9a9233e52948740d7eb8c3062d14"
	
	


import os
import sys
import time
import string
import argparse
import itertools
import winsound
import hashlib


def hashkill(chrs, min_length, max_length, type_type, myhash):

    if min_length > max_length:
        print ("[!] Please `min_length` must smaller or same as with `max_length`")
        sys.exit()
    print ('[i] Starting time: %s' % time.strftime('%H:%M:%S'))
    start = time.time()
    print "[+]Cracking..."
    count = 0
    for n in range(min_length, max_length + 1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)

            g = hashlib.new(str(type_type))
            g.update(chars)
            f = chars.encode("utf-8")
            p = g.hexdigest()
            if p == myhash:
                end = time.time()
                print ('[*]Hash is : ' + chars)
                print "[*]Time: %s seconds" % round((end - start), 2)
                print "[*]Words tried:" + (str(count))
                winsound.Beep(1000, 1000)
                break



            else:
                count += 1
                continue


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description='Python hash killer ')
    parser.add_argument(
        '-chr', '--chars',
        default=None, help='characters to iterate')
    parser.add_argument(
        '-min', '--min_length', type=int,
        default=1, help='minimum length of characters')
    parser.add_argument(
        '-max', '--max_length', type=int,
        default=2, help='maximum length of characters')
    parser.add_argument(
        '-t', '--type_type', type=str,
        default=3, help='the type of the hash')

    parser.add_argument(
        '-hash', '--myhash',type=str,
        default=4, help='the hash value')

    args = parser.parse_args()
    if args.chars is None:
        args.chars = string.printable.replace(' \t\n\r\x0b\x0c', '')
    try:
            hashkill(args.chars, args.min_length, args.max_length, args.type_type,args.myhash)
    except:
            info()
