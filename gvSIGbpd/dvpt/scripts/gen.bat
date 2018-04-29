attrib .\gvSIGbpd\*.* -R /S

del /Q /S /F .\gvSIGbpd\*.*

call genonly.bat

call override.bat
