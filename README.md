# gclogloadr

Given some geoclient logs, mine them for the good stuff.


## Parse Logs and Load to a Database

#### Generate SQL  

Replace the variables at the top of the batch file.

```shell
C:\abc\gclogloadr>convertadir.bat
```

#### Load SQL 

```shell
C:\abc>cd C:\Temp
C:\Temp>sqlplus gis/iluvoracle247@devdb
> ...
SQL> @calltomany.sql
```

## Regression Test Any New Log Parsing Shenanigans

```shell
> regressiontest.bat
```

