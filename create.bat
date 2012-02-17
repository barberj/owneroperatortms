@echo off
rem Windows Batch file to build and minimize current javascript files

:: If the debug-extjs directory exists we are in PROD mode
:: Lets set everything up as DEBUG to compile
IF EXIST www\tms\public\js\debug-extjs GOTO MAKEDEBUG

:BUILD
:: http://www.sencha.com/learn/getting-started-with-ext-js-4/
echo using SENCHA SDK Tools for creating build file
call sencha create jsb -a http://localhost:8084 -p www\tms\public\js\app.jsb3
call sencha build -p www\tms\public\js\app.jsb3 -d www\tms\public\js\.

:: After BUILD we want to make PROD
:MAKEPROD
call toggle_env.bat
GOTO END

:MAKEDEBUG
call toggle_env.bat
:: Now that we are in DEBUG we can BUILD
GOTO BUILD

:END
