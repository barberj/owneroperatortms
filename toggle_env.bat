@echo off
rem Windows Batch file to toggle environment 

:: If the debug-header.html exists we are in PROD mode
IF EXIST www\tms\templates\debug-header.html GOTO MAKEDEBUG

:MAKEPROD
echo Making Prod
move www\tms\templates\header.html www\tms\templates\debug-header.html
move www\tms\templates\prod-header.html www\tms\templates\header.html

GOTO END

:MAKEDEBUG
echo Making Debug
move www\tms\templates\header.html www\tms\templates\prod-header.html
move www\tms\templates\debug-header.html www\tms\templates\header.html 

:END
