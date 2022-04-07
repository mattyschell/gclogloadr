import sys
import os


def main(psqldir
        ,pscript):

    allsqls = [f for f in os.listdir(psqldir) \
               if os.path.isfile(os.path.join(psqldir, f))]

    kount = 0
    with open(pscript, 'w') as f:

        for sql in allsqls:
            kount +=1
            f.write('{0}{1}{2}'.format('@'
                                      ,os.path.join(psqldir,sql)
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