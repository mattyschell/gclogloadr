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


class DmlConverter(object):

    def __init__(self
                 ,pinfile
                 ,poutsql
                 ,ptablename = 'geoclientlogmine'):

        self.inlog  = pinfile
        self.outsql = poutsql
        self.tablename = ptablename

        if os.path.isfile(poutsql):
            os.remove(poutsql)

    def convert(self):

        rawout = []
        kount = 0
        filename = os.path.basename(self.inlog)

        # memory management?  Not today angel
        with open(self.inlog) as fin:

            for logline in fin:
                rawout.append(logline.strip())

        with open(self.outsql, 'w') as f:

            f.write('set define off{0}'.format('\n'))
            f.write('set feedback off{0}'.format('\n'))

            for rawline in rawout:

                kount += 1

                splitline = rawline.split(' ')            

                # IndexError: list index out of range
                # is what we will see if totally new format

                sql  = "insert into {0} (inputfile,ip,gcdate,getreq,httpcode) ".format(self.tablename)
                sql += "values("
                sql += "'{0}'".format(filename)

                if splitline[0] == '-':

                    #- 555.666.777.88 - - [01/Aug/2021:01:20:12 -0400] "GET /geoc..._id=yyyy HTTP/1.1" 200 5626

                    try:
                        sql += ",'{0}'".format(splitline[1])
                        sql += ",'{0}'".format(splitline[4].lstrip('[')) 
                        sql += ",'{0}'".format(splitline[7].replace("'","''")) #[01/Apr/2021:00:00:28
                        sql += ",'{0}'".format(splitline[9]) 
                        sql += ");{0}".format('\n') 
                    except:
                        cluephone = 'Failed to parse line {0} in {1}'.format(rawline
                                                                            ,self.inlog)                                   
                        print(cluephone) 
                        #raise ValueError(cluephone)
                    else:
                        f.write(sql)

                elif splitline[0] != '-' \
                and  splitline[2] == '-' \
                and  splitline[3] == '-':

                    #555.666.7.888 99.000.111.22 - - [01/Aug/2021:01:32:52 -0400] "GET /geo....NX HTTP/1.1" 200 1113

                    #same index positions for now
                    try:
                        sql += ",'{0}'".format(splitline[1])
                        sql += ",'{0}'".format(splitline[4].lstrip('[')) 
                        sql += ",'{0}'".format(splitline[7].replace("'","''")) #[01/Apr/2021:00:00:28
                        sql += ",'{0}'".format(splitline[9]) 
                        sql += ");{0}".format('\n') 
                    except:
                        cluephone = 'Failed to parse line {0} in {1}'.format(rawline
                                                                            ,self.inlog)                                   
                        print(cluephone) 
                        #raise ValueError(cluephone)
                    else:
                        f.write(sql)

                else:

                    #11.222.333.444 - - [01/Apr/2021:00:00:28 -0400] "GET /geoc...attan HTTP/1.1" 200 5327

                    try:
                        sql += ",'{0}'".format(splitline[0])
                        sql += ",'{0}'".format(splitline[3].lstrip('[')) 
                        sql += ",'{0}'".format(splitline[6].replace("'","''")) #[01/Apr/2021:00:00:28
                        sql += ",'{0}'".format(splitline[8]) 
                        sql += ");{0}".format('\n') 
                    except:
                        cluephone = 'Failed to parse line {0} in {1}'.format(rawline
                                                                            ,self.inlog)                                   
                        print(cluephone) 
                        #raise ValueError(cluephone)
                    else:
                        f.write(sql)

                if kount > 10000:
                    f.write("commit;{0}".format('\n'))    
                    kount = 0

            f.write("commit;{0}".format('\n'))      


