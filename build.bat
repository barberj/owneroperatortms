@echo off
rem Windows Batch file to build and minimize current javascript files

:BUILD
:: http://www.sencha.com/learn/getting-started-with-ext-js-4/
echo using SENCHA SDK Tools building and minimizing JS
call sencha build -p www\tms\public\js\app.jsb3 -d www\tms\public\js\.

:END
