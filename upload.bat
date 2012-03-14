@echo off
rem Upload file for googleappenging
IF EXIST www\tms\public\js\prod-extjs GOTO TOGGLE 

:DEPLOY
echo Deploying 
python C:\PROGRA~2\Google\google_appengine\appcfg.py --email jbarber@owneroperatortms.com update www\
GOTO END

:TOGGLE
echo Making production before dpeloying
call toggle_env.bat
GOTO DEPLOY

:END
echo Making debug again 
call toggle_env.bat
