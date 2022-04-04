import sys
import os
import re


#def find_between(s):
#    try:
#        start = s.index( '/geoclient/v1/' ) + len( '/geoclient/v1/' )
#        end = s.index('app_id=', start )
#        return s[start:end]
#    except ValueError:
#       return ""




def main(pinfile
        ,poutsql):

    rawout = []

    filename = os.path.basename(pinfile)


    with open(pinfile) as fin:
        for logline in fin:
            rawout.append(logline.strip())
        
    with open(poutsql, 'w') as f:

        f.write('set define off{0}'.format('\n'))
        f.write('set feedback off{0}'.format('\n'))

        for rawline in rawout:

            splitline = rawline.split(' ')            

            sql  = "insert into geoclientlogmine (inputfile,ip,gcdate,getreq,httpcode) "
            sql += "values("
            sql += "'{0}'".format(filename)
            sql += ",'{0}'".format(splitline[0])
            sql += ",'{0}'".format(splitline[3].lstrip('[')) 
            sql += ",'{0}'".format(splitline[6].replace("'","''")) #[01/Apr/2021:00:00:28
            sql += ",'{0}'".format(splitline[8]) 
            sql += ");{0}".format('\n') 

            f.write(sql)

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

