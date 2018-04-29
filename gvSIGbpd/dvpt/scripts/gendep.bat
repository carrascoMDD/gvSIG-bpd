attrib .\gvSIGbpd\*.* -R /S
attrib .\gvSIGbpd_dep_sec -R /S
del /Q /S /F .\gvSIGbpd\*.*
call genonly.bat
call override.bat
call dep.bat
Time /T