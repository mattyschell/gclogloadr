import sys
import os


def main(psqldir
        ,pscript):

    allsqls = [f for f in os.listdir(psqldir) \
               if os.path.isfile(os.path.join(psqldir, f))]

    kount = 0
    with open(pscript, 'w') as f:

        f.write('{0}{1}'.format('drop index geoclientlogmineinputfile;'
                               ,'\n'))
        f.write('{0}{1}'.format('drop index geoclientlogmineip;'
                               ,'\n'))
        f.write('{0}{1}'.format('drop index geoclientlogminegetreq;'
                               ,'\n'))

        for sql in allsqls:
            kount +=1
            f.write('{0}{1}{2}'.format('@'
                                      ,os.path.join(psqldir,sql)
                                      ,'\n'))

        sql = "create bitmap index geoclientlogmineinputfile on geoclientlogmine(inputfile);"
        f.write('{0}{1}'.format(sql
                               ,'\n'))
        sql = "create bitmap index geoclientlogmineip on geoclientlogmine(ip);"
        f.write('{0}{1}'.format(sql
                               ,'\n'))
        sql = "create index geoclientlogminegetreq on geoclientlogmine(getreq);"
        f.write('{0}{1}'.format(sql
                               ,'\n'))

        f.write('{0}{1}'.format('EXIT'
                                ,'\n'))

    return kount


if __name__ == '__main__':

    # writesqlscript.py "D:\temp\gclogs\sqls" "D:\temp\calltomany.sql"

    sqldir = sys.argv[1]
    script = sys.argv[2]

    kount = main(sqldir
                ,script)


    if (kount == 0 or kount is None):
        print("failed")
        retval = 1
    else:
        print('Successfully wrote {0} at signs to {1}'.format(kount
                                                             ,script))
        retval = 0

    exit(kount)
