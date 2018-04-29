
attrib .\dvpt -R /S

rmdir /S /Q .\dvpt

mkdir .\dvpt
mkdir .\dvpt\gvSIGbpd
mkdir .\dvpt\gvSIGbpd\model
mkdir .\dvpt\scripts



xcopy ..\sources\additions\*.*           .\dvpt\gvSIGbpd\additions\ /E /Y /I

copy  ..\sources\model\gvSIGbpd.EAP      .\dvpt\gvSIGbpd\model\gvSIGbpd.EAP
copy  ..\sources\model\gvSIGbpd.xmi      .\dvpt\gvSIGbpd\model\gvSIGbpd.xmi

copy  ..\sources\model\gvSIGbpd-HTML.zip .\dvpt\gvSIGbpd\model\gvSIGbpd-HTML.zip 

xcopy .\*.bat   .\dvpt\scripts  /Y /I




copy "D:\Works\MDD\Plone\ArchGenXML152ACV\ArchGenXML152ACV15wksp\distros\ArchGenXML152ACV15b20091202.zip" .\dvpt\
copy "D:\Works\MDD\Plone\gvSIGbpd\TRA0103wk\ThirdParty\distros\CJKSplitter073.zip" .\dvpt\
copy "D:\Works\MDD\Plone\gvSIGbpd\TRA0103wk\ThirdParty\distros\ZopeChinaPak082.zip" .\dvpt\

copy "D:\Works\MDD\Plone\ModelDDvlPlone\DVL0401wk\generation\ModelDDvlPlone.zip" .\dvpt\
copy "D:\Works\MDD\Plone\ModelDDvlPlone\DVL0401wk\generation\ModelDDvlPloneTool.zip" .\dvpt\
copy "D:\Works\MDD\Plone\ModelDDvlPlone\DVL0401wk\generation\ModelDDvlPloneConfiguration.zip" .\dvpt\


attrib .\gvSIGbpd\gvSIGbpd-dvpt.zip -R

del /Q .\gvSIGbpd\gvSIGbpd-dvpt.zip

"C:\Program Files\7-Zip\7z" a -r -y  .\gvSIGbpd\gvSIGbpd-dvpt.zip .\dvpt

attrib .\gvSIGbpd\gvSIGbpd-dvpt.zip +R


REM leave to review. Shall be deleted at the beginning of the next execution of this script rmdir /S /Q .\dvpt