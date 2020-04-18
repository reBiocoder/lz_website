@echo off
%1 %2
ver|find "5.">nul&&goto :Admin
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
:Admin

set debug_switch=off
set venv_switch=on
cd /d %~dp0 && cd /d ..
set work_dir=%cd%

for /d %%i in (%work_dir%\src\*) do (
    set app_name=%%~ni
    goto break_
)
:break_

echo #############################��ѡ��Ҫִ�еĲ���############################
echo ----------------------1����������1�����س�����������----------------------
echo ----------------------2����������2�����س�,  �رշ���----------------------
echo ----------------------3����������3�����س�����������----------------------
echo ----------------------4�������κ������ַ���  �˳�����----------------------
echo.
echo ��ѡ��Ҫִ�еĲ���
set /p num=
if "1"=="%num%" (
    cls
    env\Scripts\activate
    python %work_dir%\src\run_%app_name%.py start
    pause
)

if "2"=="%num%" (
    cls
    env\Scripts\activate
    python %work_dir%\src\run_%app_name%.py stop
    pause
)

if "3"=="%num%" (
    cls
    env\Scripts\activate
    python %work_dir%\src\run_%app_name%.py restart
    pause
)