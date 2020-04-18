@echo off
%1 %2
ver|find "5.">nul&&goto :Admin
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
:Admin

set venv_switch=on
cd /d %~dp0 && cd /d ..
set work_dir=%cd%
for /d %%i in (%work_dir%\src\*) do (
    set app_name=%%~ni
    goto break_
)
:break_
for /f "delims=" %%i in ('python -c "import sys; print(sys.version_info.major)"') do set major=%%i
for /f "delims=" %%i in ('python -c "import sys; print(sys.version_info.minor)"') do set minor=%%i
if %major%.%minor% neq 3.6 (
    echo python version error, python3.6 is required
    pause
    exit -1
)

if not exist %work_dir%\.already_package (
    echo can not install without packaging
    pause
    exit -1
)

if not exist %work_dir%\lib\*.whl (
    echo install error, mg_app_framework.*whl not exist
    pause
    exit -1
)

if not exist %USERPROFILE%\pip (
    md %USERPROFILE%\pip
    echo [global]> %USERPROFILE%\pip\pip.ini
    echo index-url=https://pypi.tuna.tsinghua.edu.cn/simple>> %USERPROFILE%\pip\pip.ini
    echo trusted-host=pypi.tuna.tsinghua.edu.cn>> %USERPROFILE%\pip\pip.ini
)

if %venv_switch% == on (
    if exist %work_dir%\env (
        rd /s/q %work_dir%\env
    )
    call virtualenv -p python env
    call env\Scripts\activate
)
for %%i in (%work_dir%\lib\*.whl) do (
    python -m pip install %%i
)
if exist %work_dir%\lib\requirements.txt (
    python -m pip install -r %work_dir%\lib\requirements.txt
)
if exist %work_dir%\env\Lib\site-packages\pywin32_system32\pywintypes36.dll (
    xcopy /f /c /y %work_dir%\env\Lib\site-packages\pywin32_system32\pywintypes36.dll  %work_dir%\env\Lib\site-packages\win32\
)
python %work_dir%\src\run_%app_name%.py remove
python %work_dir%\src\run_%app_name%.py --startup auto install
echo finish> %work_dir%\.already_install
echo finish
pause