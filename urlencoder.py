import sys
import argparse

def url_encoder(plaintext):
    encoded = ""
    for c in plaintext:
        recoded = hex(ord(c)).lstrip('0x')
        if len(recoded) == 1:
            recoded = '0' + recoded
        encoded = encoded + '%' + recoded
    return encoded

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', help="String containing text to be URL encoded")
    parser.add_argument('-f', help="File containing text to be URL encoded")

    arguments = vars(parser.parse_args(sys.argv[1:]))
    
    u_string = arguments['s']
    u_file = arguments['f']

    if u_string is not None:
        print(url_encoder(u_string))
    elif u_file is not None:
        f = open(u_file, 'r')
        lines = f.readlines()

        for line in lines:
            print(url_encoder(line.rstrip('\n')))

        f.close()

