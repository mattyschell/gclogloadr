import os
import sys

import logconverter

def main(plogdir
        ,psqldir):

    alllogs = [f for f in os.listdir(plogdir) \
               if os.path.isfile(os.path.join(plogdir, f))]
    
    kount = 0
    for log in alllogs:

        #baselogname = os.path.basename(log)
        
        conversionmgr = logconverter.DmlConverter(os.path.join(plogdir
                                                              ,log)
                                                 ,os.path.join(psqldir
                                                              ,'{0}{1}'.format(log
                                                                              ,'.sql')))

        conversionmgr.convert()
        kount +=1

    return kount

if __name__ == '__main__':

    logdir = sys.argv[1]
    sqldir = sys.argv[2]

    kount = main(logdir
                ,sqldir)


    if (kount == 0 or kount is None):
        print("failed")
        retval = 1
    else:
        print('Successfully converted {0} logs to sql in {1}'.format(kount
                                                                    ,sqldir))
        retval = 0

    exit(kount)

