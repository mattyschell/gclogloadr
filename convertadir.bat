REM INGEOCLIENTLOGDIR: input directory with geoclient logs
REM OUTSQLLOGDIR: an existing directory where we drop one sql per log 
REM SQLCALLERSCRIPT: we will create this script to call all SQLs
set INGEOCLIENTLOGDIR="D:\temp\gclogs"
set OUTSQLLOGDIR="D:\temp\gclogs\sqls"
set SQLCALLERSCRIPT="D:\temp\calltomany.sql"
set PYTHONPATH=src\py;%PYTHONPATH%
echo converting %INGEOCLIENTLOGDIR% to %OUTSQLLOGDIR% on %date% at %time%
python convertadir.py %INGEOCLIENTLOGDIR% %OUTSQLLOGDIR%
python writesqlscript.py %OUTSQLLOGDIR% %SQLCALLERSCRIPT%
echo lets say done