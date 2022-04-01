import sys
import os
import re


def find_between(s):
    try:
        start = s.index( '/geoclient/v1/' ) + len( '/geoclient/v1/' )
        end = s.index('app_id=', start )
        return s[start:end]
    except ValueError:
        return ""

def main(pinfile
        ,poutsql):

    rawout = []

    with open(pinfile) as fin:
        for logline in fin:
            rawout.append(logline.strip())
        
    with open(poutsql, 'w') as f:
        for rawline in rawout:

            f.write("insert into geoclientlogmine (inputfile, rawsearch) values('{0}','{1}');{2}".format(os.path.basename(pinfile)
                                                                                                        ,find_between(rawline)
                                                                                                        ,'\n'))
        f.write("commit;")        

if __name__ == '__main__':

    infile = sys.argv[1]
    outsql = sys.argv[2]

    try:
        os.remove(outsql)
    except OSError:
        pass

    main(infile
        ,outsql)

