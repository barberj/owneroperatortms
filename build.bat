@echo off
rem Windows Batch file to build and minimize current javascript files

:: If the debug-extjs directory exists we are in PROD mode
:: Lets set everything up as DEBUG to compile
IF EXIST www\tms\public\js\debug-extjs GOTO MAKEDEBUG

:BUILD
:: http://www.sencha.com/learn/getting-started-with-ext-js-4/
echo using SENCHA SDK Tools building and minimizing JS
call sencha create jsb -a http://localhost:8084 -p www\tms\public\js\app.jsb3
call sencha build -p www\tms\public\js\app.jsb3 -d www\tms\public\js\.

:: After BUILD we want to make PROD
:MAKEPROD
echo Make Prod
move www\tms\public\js\extjs www\tms\public\js\debug-extjs
move www\tms\public\js\prod-extjs www\tms\public\js\extjs

move www\tms\templates\header.html www\tms\templates\debug-header.html
move www\tms\templates\prod-header.html www\tms\templates\header.html

GOTO END

:MAKEDEBUG
echo Make Debug
move www\tms\public\js\extjs www\tms\public\js\prod-extjs
move www\tms\public\js\debug-extjs www\tms\public\js\extjs

move www\tms\templates\header.html www\tms\templates\prod-header.html
move www\tms\templates\debug-header.html www\tms\templates\header.html 

:: Now that we are in DEBUG we can BUILD
GOTO BUILD

:END
