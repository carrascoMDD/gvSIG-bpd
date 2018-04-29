xcopy ..\sources\manualadditions\*.*                .\gvSIGbpd\manualadditions /E /Y /I
del /S /Q .\gvSIGbpd\manualadditions\*.bak
attrib +R /S .\gvSIGbpd\manualadditions\*.*



