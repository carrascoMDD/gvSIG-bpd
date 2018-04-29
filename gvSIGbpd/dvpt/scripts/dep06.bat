attrib -R /S \\ACVP06\dvpt\Plone251\Data\Products\gvSIGbpd\*.*
del /S /Q \\ACVP06\dvpt\Plone251\Data\Products\gvSIGbpd\*.*
rmdir /Q /S \\ACVP06\dvpt\Plone251\Data\Products\gvSIGbpd
xcopy .\gvSIGbpd  \\ACVP06\dvpt\Plone251\Data\Products\gvSIGbpd /E /Y /I
attrib \\ACVP06\dvpt\Plone251\Data\Products\gvSIGbpd\*.* +R /S
TIME /T