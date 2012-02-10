@echo off
rem Windows Batch file to toggle environment 

IF EXIST www\tms\public\js\debug-extjs GOTO MAKEDEBUG

:MAKEPROD
echo Making Prod
move www\tms\public\js\extjs www\tms\public\js\debug-extjs
move www\tms\public\js\prod-extjs www\tms\public\js\extjs

move www\tms\templates\header.html www\tms\templates\debug-header.html
move www\tms\templates\prod-header.html www\tms\templates\header.html

GOTO END

:MAKEDEBUG
echo Making Debug
move www\tms\public\js\extjs www\tms\public\js\prod-extjs
move www\tms\public\js\debug-extjs www\tms\public\js\extjs

move www\tms\templates\header.html www\tms\templates\prod-header.html
move www\tms\templates\debug-header.html www\tms\templates\header.html 

:END
