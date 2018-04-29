call extensions-attrib.bat

xcopy "D:\dvpt\plone251\Data\Products\gvSIGbpd\manualadditions\AsExternalMethodInSiteRoot" .\gvSIGbpd_dep_sec\manualadditions\AsExternalMethodInSiteRoot  /E /Y /I /K

xcopy .\gvSIGbpd\manualadditions\AsExternalMethodInSiteRoot  "D:\dvpt\plone251\Data\Extensions" /E /Y /I /K

del /Q /S /F D:\dvpt\plone251\Data\Products\Extensions\*.bak