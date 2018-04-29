del archgenxml.log

attrib .\gvSIGbpd\models -R /S
attrib .\gvSIGbpd\models\gvSIGbpd.EAP -R /S
attrib .\gvSIGbpd\models\gvSIGbpd.xmi -R /S
attrib .\gvSIGbpd\models\gvSIGbpd-HTML.zip -R /S


"D:\dvpt\Python24\python.exe" "D:\dvpt\ArchGenXML152ACV15\ArchGenXML.py" ..\sources\model\gvSIGbpd.xmi
del .\gvSIGbpd\i18n\generated.pot

"C:\Program Files\7-Zip\7z" a -r -y  ..\sources\model\gvSIGbpd-HTML.zip ..\sources\model\HTML
