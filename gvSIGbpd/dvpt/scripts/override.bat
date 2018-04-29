set buildstring=build%DATE:~6,4%%DATE:~3,2%%DATE:~0,2%%TIME:~0,2%%TIME:~3,2%
REM set buildstring=build%DATE:~0,4%%DATE:~5,2%%DATE:~8,2%%TIME:~0,2%%TIME:~3,2%
copy ..\sources\additions\objects\version_base.txt ..\sources\additions\objects\version.txt
echo %buildstring% >>..\sources\additions\objects\version.txt

xcopy ..\sources\additions\objects\*.*              .\gvSIGbpd /E /Y /I



copy ..\sources\additions\i18n\gvSIGbpd_credits-en.po .\gvSIGbpd\i18n\ /Y 
copy ..\sources\additions\i18n\gvSIGbpd_credits-es.po .\gvSIGbpd\i18n\ /Y 

xcopy ..\sources\additions\skins\icons\*.*          .\gvSIGbpd\skins\gvSIGbpd /E /Y /I
xcopy ..\sources\additions\skins\grids_i18n\*.*     .\gvSIGbpd\skins\gvSIGbpd /E /Y /I
xcopy ..\sources\additions\skins\vistas\*.*         .\gvSIGbpd\skins\gvSIGbpd /E /Y /I
xcopy ..\sources\additions\skins\styles\*.*         .\gvSIGbpd\skins\gvSIGbpd /E /Y /I
xcopy ..\sources\additions\skins\scripts\*.*        .\gvSIGbpd\skins\gvSIGbpd /E /Y /I
xcopy ..\sources\additions\skins\interactions\*.*   .\gvSIGbpd\skins\gvSIGbpd /E /Y /I

xcopy ..\sources\manualadditions\*.*                .\gvSIGbpd\manualadditions /E /Y /I

call sou.bat

del /S /Q .\gvSIGbpd\*.bak

attrib +R /S .\gvSIGbpd\*.*



