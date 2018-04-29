attrib D:\dvpt\plone251\Data\Products\gvSIGbpd\*.* -R /S


call extensions-attrib.bat

xcopy "D:\dvpt\plone251\Data\Products\gvSIGbpd" .\gvSIGbpd_dep_sec  /E /Y /I /K

xcopy .\gvSIGbpd  "D:\dvpt\plone251\Data\Products\gvSIGbpd" /E /Y /I /K
xcopy .\gvSIGbpd\manualadditions\AsExternalMethodInSiteRoot  "D:\dvpt\plone251\Data\Extensions" /E /Y /I /K


del /Q /S /F D:\dvpt\plone251\Data\Products\gvSIGbpd\i18n\gvSIGbpd-es_justgen.po
del /Q /S /F D:\dvpt\plone251\Data\Products\gvSIGbpd\i18n\gvSIGbpd-en_justgen.po

del /Q /S /F D:\dvpt\plone251\Data\Products\gvSIGbpd\*.bak
del /Q /S /F D:\dvpt\plone251\Data\Products\Extensions\*.bak