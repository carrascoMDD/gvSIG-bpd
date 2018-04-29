# -*- coding: utf-8 -*-
#
# File: BPDElemento_Credits.py
#
# Copyright (c) 2008, 2009 by Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
# Authors: 
# Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana (Spain) <gvSIGbpd@gvSIG.org>  
# Model Driven Development sl  Valencia (Spain) <http://www.ModelDD.org> 
# Antonio Carrasco Valero                       <carrasco@ModelDD.org>
#
#
__author__ = """Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana <gvSIGbpd@gvSIG.org>, 
Model Driven Development sl <gvSIGbpd@ModelDD.org>, 
Antonio Carrasco Valero <carrasco@ModelDD.org>"""
__docformat__ = 'plaintext'



from AccessControl              import ClassSecurityInfo

from Products.CMFCore.utils     import getToolByName


cMustLocalizeSentinel = object()



gBPDCredits_Constant = {
    'gvSIGbpd_credits_AuthorCITAbbreviated_PropertyValue': u"GVA/CIT",
    'gvSIGbpd_credits_ProjectTitle_PropertyValue': u"gvSIG-business process definition (gvSIG-bpd)",
    'gvSIGbpd_credits_Copyright_PropertyValue': u"(C) 2008, 2009 Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana",
    'gvSIGbpd_credits_License_PropertyValue': u"GNU General Public License (GPL)",
    'gvSIGbpd_credits_License_URL_PropertyValue': u"www.fsf.org/licensing/licenses/gpl.html",
    'gvSIGbpd_credits_License_FreeSoftwareFoundation_URL_PropertyValue': u"Free Software Foundation, Inc.",
    'gvSIGbpd_credits_License_FreeSoftwareFoundation_PropertyValue': u"Free Software Foundation, Inc.",
    'gvSIGbpd_credits_License_FreeSoftwareFoundation_URL_PropertyValue': u"www.fsf.org",
    'gvSIGbpd_credits_Author_Conselleria_Institucion_PropertyValue': u"Regional Ministry at Comunidad Valenciana in Spain, Europe",
    'gvSIGbpd_credits_Author_Conselleria_PropertyValue': u"Conselleria de Infraestructuras y Transporte de la Generalitat Valenciana",
    'gvSIGbpd_credits_Author_Conselleria_URL_PropertyValue': u"www.cit.gva.es",
    'gvSIGbpd_credits_Author_Conselleria_Logo_PropertyValue': u"CIT.gif",
    'gvSIGbpd_credits_Author_ModelDrivenDevelopmentSL_PropertyValue': u"Model Driven Development, sl",
    'gvSIGbpd_credits_Author_ModelDrivenDevelopmentSL_URL_PropertyValue': u"www.ModelDD.org",
    'gvSIGbpd_credits_Author_ModelDrivenDevelopmentSL_Logo_PropertyValue': u"ModelDrivenDevelopmenSL.gif",
    'gvSIGbpd_credits_Author_AntonioCarrascoValero_PropertyValue': u"Antonio Carrasco Valero",
    'gvSIGbpd_credits_Author_AntonioCarrascoValero_URL_PropertyValue': u"gvsig.org/web/author/tcarrasco",
    'gvSIGbpd_credits_Author_AntonioCarrascoValero_Photo_PropertyValue': u"ACV.jpg",
    'gvSIGbpd_credits_SponsorProjectTitle_PropertyValue': u"gvSIG project by Conselleria de Infraestructuras y Transporte de la Generalitat Valenciana",
    'gvSIGbpd_credits_SponsorProjectTitle_URL_PropertyValue': u"gvSIG.org",
    'gvSIGbpd_credits_SponsorProjectTitle_Logo_PropertyValue': u"gvSIG.gif",
    'gvSIGbpd_credits_Standards_MDA_PropertyValue': u"Model Driven Architecture (MDA)",    
    'gvSIGbpd_credits_Standards_MDA_URL_PropertyValue': u"www.omg.org/mda",    
    'gvSIGbpd_credits_Standards_OMG_PropertyValue': u"Object Management Group, inc",    
    'gvSIGbpd_credits_Standards_OMG_URL_PropertyValue': u"www.omg.org",    
    'gvSIGbpd_credits_RequirementsCoordination_Business_Name1':u"Juanjo Ripolles",
    'gvSIGbpd_credits_RequirementsCoordination_Business_URL1':u"gvsig.org/web/author/jripolles",
    'gvSIGbpd_credits_RequirementsCoordination_Business_Name2':u"Victoria Agazzi",
    'gvSIGbpd_credits_RequirementsCoordination_Business_URL2':u"gvsig.org/web/author/vagazzi",
    'gvSIGbpd_credits_RequirementsCoordination_Organization_Name':u"Manuel Madrid",
    'gvSIGbpd_credits_RequirementsCoordination_Organization_URL':u"gvsig.org/web/author/mmadrid",
    'gvSIGbpd_credits_RequirementsCoordination_Platform_Name':u"Joaquin del Cerro",
    'gvSIGbpd_credits_RequirementsCoordination_Platform_URL':u"gvsig.org/web/author/jjdelcerro",
    'gvSIGbpd_credits_RequirementsCoordination_Administration_Name':u"Victor Acevedo",
    'gvSIGbpd_credits_RequirementsCoordination_Administration_URL':u"gvsig.org/web/author/vacevedo",
    'gvSIGbpd_credits_SponsorProjectTitle_Jefe_Name':u"Martin Garcia",
    'gvSIGbpd_credits_SponsorProjectTitle_CoordinadorGeneral_Name':u"Gabriel Carrion",
    'gvSIGbpd_credits_SponsorProjectTitle_CoordinadorTecnico_Name':u"Luis W. Sevilla",
    'gvSIGbpd_credits_Standards_UML_PropertyValue': u"Unified Modeling Language (UML)",   
    'gvSIGbpd_credits_Standards_UML_URL_PropertyValue':u"www.omg.org/technology/documents/modeling_spec_catalog.htm#UML",
    'gvSIGbpd_credits_Standards_MOF_PropertyValue': u"Meta Object Facility (MOF)",    
    'gvSIGbpd_credits_Standards_MOF_URL_PropertyValue':u"www.omg.org/technology/documents/modeling_spec_catalog.htm#MOF",
    'gvSIGbpd_credits_Standards_XMI_PropertyValue': u"XML Metadata Interchange (XMI)",    
    'gvSIGbpd_credits_Standards_XMI_URL_PropertyValue':u"www.omg.org/technology/documents/modeling_spec_catalog.htm#XMI",
    'gvSIGbpd_credits_Platform_Zope_PropertyValue': u"Zope v2.9",
    'gvSIGbpd_credits_Platform_Zope_URL_PropertyValue': u"www.zope.org",
    'gvSIGbpd_credits_Platform_Plone_PropertyValue': u"Plone v2.5",
    'gvSIGbpd_credits_Platform_Plone_URL_PropertyValue': u"www.plone.org",
    'gvSIGbpd_credits_Platform_Python_PropertyValue': u"Python v2.4",
    'gvSIGbpd_credits_Platform_Python_URL_PropertyValue': u"www.python.org",
    'gvSIGbpd_credits_Standards_GNUgettextPO_PropertyValue': u"GNU gettext PO",
    'gvSIGbpd_credits_Standards_GNUgettextPO_URL_PropertyValue': u"www.gnu.org/software/gettext/",
    'gvSIGbpd_credits_Standards_JavaProperties_PropertyValue': u"Java .properties",
    'gvSIGbpd_credits_Standards_JavaProperties_URL_PropertyValue': u"www.javasoft.com",
    'gvSIGbpd_credits_Standards_BusinessSpecification_Intro_URL': u"www.omg.org/technology/documents/br_pm_spec_catalog.htm",
    'gvSIGbpd_credits_Standards_BMM_URL': u"www.omg.org/technology/documents/br_pm_spec_catalog.htm#BMM",
    'gvSIGbpd_credits_Standards_BPDM_URL': u"www.omg.org/technology/documents/br_pm_spec_catalog.htm#BPDM",
    'gvSIGbpd_credits_Standards_BPMN_URL': u"www.omg.org/technology/documents/br_pm_spec_catalog.htm#BPMN",
    
}


gBPDCredits_I18N = {
    'gvSIGbpd_credits_por': 'by-',
    'gvSIGbpd_credits_Title': u"Credits-",
    'gvSIGbpd_credits_ProjectTitle_PropertyName': "Project-",
    'gvSIGbpd_credits_ProjectTitle_Description_PropertyValue': "Collaborative application for the specification and publication of organizational structures,  business process definitions, business policies, business rules, artefacts and tools.-",
    'gvSIGbpd_credits_Copyright_PropertyName': u"Copyright-",
    'gvSIGbpd_credits_License_PropertyName': u"License-",
    'gvSIGbpd_credits_Autores_PropertyName': u"Authors-",
    'gvSIGbpd_credits_Author_ModelDrivenDevelopmentSL_Empresa_PropertyValue': u"company-",
    'gvSIGbpd_credits_Author_AntonioCarrascoValero_Desarrollador_PropertyValue': u"developer-",
    'gvSIGbpd_credits_SponsorProjectTitle_PropertyName': u"Sponsor and Director-",
    'gvSIGbpd_credits_SponsorProjectTitle_Description_PropertyValue': u"gvSIG is a software application for the management of geospatial information. Released as Free Libre Open Source Software (FLOSS). Developed as a dektop application programmed in the Java language. Available in the free libre open source software operating system GNU/Linux, and the proprietary Apple Macintosh(R) and Microsoft Windows(R). Localized to many languages and countries. gvSIG now facilitates the availability for even more languages and countries, with this gvSIGtraducciones application for collaborative translations of user interface strings.-",
    'gvSIGbpd_credits_Standards_PropertyName': u"Standards-",
    'gvSIGbpd_credits_Warranty_PropertyName': u"Warranty-",
    'gvSIGbpd_credits_Warranty_PropertyValue':u"This program is distributed in the hope that it will be useful, but without any warraty; without even the implied warranty of merchantability or fitness for a particular purpose. See the GNU General Public License (GPL) for more details.-",
    'gvSIGbpd_credits_Standards_Intro_PropertyName':u"Developed following the recommendations in the-",
    'gvSIGbpd_credits_RequirementsCoordination_PropertyName':u"Requirements Coordination-",
    'gvSIGbpd_credits_RequirementsCoordination_Business_Title':u"Business Domain Requirements-",
    'gvSIGbpd_credits_RequirementsCoordination_Organization_Title':u"Organization Requirements-",
    'gvSIGbpd_credits_RequirementsCoordination_Platform_Title':u"Platform Requirements-",
    'gvSIGbpd_credits_RequirementsCoordination_Administration_Title':u"Administration Requirements-",
    'gvSIGbpd_credits_SponsorProjectTitle_Jefe_Title':u"Chief Organization and Information Officer at CIT-",
    'gvSIGbpd_credits_SponsorProjectTitle_CoordinadorGeneral_Title':"gvSIG General Coordinator-",
    'gvSIGbpd_credits_SponsorProjectTitle_CoordinadorTecnico_Title': u"gvSIG Technical Coordinator-",
    'gvSIGbpd_credits_DevelopedBy_PropertyName': u"Developed by-",
    'gvSIGbpd_credits_PorLa': u"by the-",
    'gvSIGbpd_credits_por':   u"by-",
    'gvSIGbpd_credits_Platform_PropertyName': u"Platform-",
    'gvSIGbpd_credits_Standards_BusinessSpecification_Intro': u"Adopted standard specifications for Business Strategy, Business Rules and Business Processes-",
    'gvSIGbpd_credits_Components_PropertyName': u"Components-",
    'gvSIGbpd_credits_Components_ThirdParty_PropertyName': u"Third party-",
    'gvSIGbpd_credits_Components_DevelopedBy_PropertyName': u"Developed by-",
    'gvSIGbpd_credits_Components_Installed_PropertyName': u"Installed-",
    'gvSIGbpd_credits_Components_NotInstalled_PropertyName': u"Not Installed-",
    'gvSIGbpd_credits_Components_Missing_PropertyName': u"Missing-",
    'gvSIGbpd_credits_Components_Error_PropertyName':  u"Failed-",
    'gvSIGbpd_credits_Components_Optional_PropertyName': u"Optional-",
    'gvSIGbpd_credits_Platform_Intro_PropertyName': u"Application Server, Content Management System and Programming Language",
    'gvSIGbpd_credits_Standards_BMM': u"Business Motivation Model (BMM) adopted standard specification",
    'gvSIGbpd_credits_Standards_BPDM': u"Business Process Definition Metamodel (BPDM) adopted standard specification",
    'gvSIGbpd_credits_Standards_BPMN': u"Business Process Modeling Notation (BPMN) adopted standard specification",
}


class BPDElemento_Credits:
    """
    """
    security = ClassSecurityInfo()

    

    security.declarePublic( 'fCredits')
    def fCredits( self):
        
        aCreditsDict = gBPDCredits_I18N.copy()
        
        aTranslationService = getToolByName( self, 'translation_service', None)   
        if not aTranslationService:
            aCreditsDict.update( gBPDCredits_Constant)
            return aCreditsDict
        
        someKeys = aCreditsDict.keys()
        for aKey in someKeys:
            aValue = aCreditsDict.get( aKey, u'')
            aTranslatedValue = self.fTranslateI18N( 'gvSIGbpd_credits', aKey, aValue, aTranslationService)
            aCreditsDict[ aKey] = aTranslatedValue
        
        aCreditsDict.update( gBPDCredits_Constant)
        return aCreditsDict




