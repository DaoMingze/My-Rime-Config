@ECHO OFF
@REM chcp 65001
CD /d %~dp0
:CHOICE
ECHO.
set /p filename="�汾��: "
ECHO 1  ������һ���ļ�
ECHO 2  ��Android��ͬ�����뷨
ECHO 3  ��Windows��С�Ǻ����뷨
ECHO 4  �˳�
ECHO.
CHOICE /C:1234 /N
IF errorlevel 4 EXIT
IF errorlevel 3 goto THREE
IF errorlevel 2 goto TWO
IF errorlevel 1 goto ONE


:ONE
xcopy .\basic .\release\rime\ /E
xcopy .\schema .\release\rime\ /E
xcopy .\ex_dict .\release\rime\ /E
xcopy .\custom .\release\rime\ /E
7z a "MRC-release-%filename%.7z" .\release
goto end

:TWO
xcopy .\theme\trime .\release\rime\ /E
goto ONE

:THREE
xcopy .\theme\weasel.custom.yaml .\release\rime\ /E
goto  ONE

:end
rd /s .\release
echo ���,�밴������˳�
pause >nul