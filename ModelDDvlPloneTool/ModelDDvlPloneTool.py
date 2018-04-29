# -*- coding: utf-8 -*-
#
# File: ModelDDvlPloneTool.py
#
# Copyright (c) 2008 by 2008 Model Driven Development sl and Antonio Carrasco Valero
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
# Model Driven Development sl  Valencia (Spain) www.ModelDD.org 
# Antonio Carrasco Valero                       carrasco@ModelDD.org
#

__author__ = """Model Driven Development sl <gvSIGwhys@ModelDD.org>,
Antonio Carrasco Valero <carrasco@ModelDD.org>"""
__docformat__ = 'plaintext'



# Zope
from OFS import SimpleItem
from OFS.PropertyManager import PropertyManager
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from AccessControl import ClassSecurityInfo


from time import time

from DateTime import DateTime




# cmf
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName, UniqueObject
from Products.CMFCore.ActionProviderBase import ActionProviderBase

from Acquisition  import aq_inner, aq_parent


from ModelDDvlPloneTool_Export      import ModelDDvlPloneTool_Export
from ModelDDvlPloneTool_Retrieval   import ModelDDvlPloneTool_Retrieval
from ModelDDvlPloneTool_Bodies      import ModelDDvlPloneTool_Bodies                
from ModelDDvlPloneTool_Mutators    import ModelDDvlPloneTool_Mutators   





cModelDDvlPloneToolName = 'ModelDDvlPlone_tool'



cModelDDvlPloneToolPermissions = [                                                                                                                                     
    { 'permission': permissions.AddPortalContent,     'acquire': False,  'roles': [              'Authenticated',  ], },  
    { 'permission': permissions.DeleteObjects,        'acquire': False,  'roles': [              'Authenticated',  ], },  
    { 'permission': permissions.ModifyPortalContent,  'acquire': False,  'roles': [              'Authenticated',  ], },  
    { 'permission': permissions.View,                 'acquire': False,  'roles': [ 'Anonymous', 'Authenticated',  ], },  
]


class ModelDDvlPloneTool(UniqueObject, PropertyManager, SimpleItem.SimpleItem, ActionProviderBase):
    
    "The ModelDDvlPloneTool"

    meta_type = 'ModelDDvlPloneTool'

    id = cModelDDvlPloneToolName

    manage_options = PropertyManager.manage_options + \
                     SimpleItem.SimpleItem.manage_options + (
    	{'label': 'View', 'action': 'index_html',},
    )

    _properties = (
        {'id':'title', 'type':'string', 'mode':'w'},
    )

    # Standard security settings
    security = ClassSecurityInfo()


    security.declareProtected('Manage properties', 'index_html')
    index_html = PageTemplateFile('skins/index_html', globals())





# ACV 20090325 Learned from tools generation by ArchGenXML
#    # tool-constructors have no id argument, the id is fixed
#    def __init__(self, id=None):
#        BaseContent.__init__(self,'TRAtool_gvSIGtraducciones')
#        self.setTitle('Catalogo de Traducciones')
#        
#        ##code-section constructor-footer #fill in your manual code here
#        ##/code-section constructor-footer


# ACV 20090325 Learned from tools generation by ArchGenXML
#    # tool should not appear in portal_catalog
#    def at_post_edit_script(self):
#        self.unindexObject()
#        
#        ##code-section post-edit-method-footer #fill in your manual code here
#        ##/code-section post-edit-method-footer




    security.declarePublic('manage_afterAdd')
    def manage_afterAdd(self,item,container):
        """Lazy Initialization.
        
        """        
        self.pSetPermissions()
                
        return self
    


    


    # #############################################################
    # Security configuration utility 
    #     

    
    security.declarePrivate( 'pSetPermissions')
    def pSetPermissions(self):
 
        for unaPermissionSpec in cModelDDvlPloneToolPermissions:
            unaPermission = unaPermissionSpec[ 'permission']
            unAcquire     = unaPermissionSpec[ 'acquire'] 
            unosRoles     = unaPermissionSpec[ 'roles']
            
            if unaPermission:
                self.manage_permission( unaPermission, roles=unosRoles, acquire=unAcquire)
        
        return self
    

 
#######################################
# Time methods

   
    
    security.declareProtected( permissions.View, 'fMillisecondsNow')
    def fMillisecondsNow(self):   
        return round( time(), 3)
    
    
    
    security.declareProtected( permissions.View, 'fDateTimeNow')
    def fDateTimeNow(self):   
        return DateTime()
    
    
    
    
        
      


#######################################
# Retrieval methods


    
    
    
    security.declareProtected( permissions.View, 'fRetrieveTypeConfig')
    def fRetrieveTypeConfig(self, 
        theTimeProfilingResults     =None,
        theElement                  =None, 
        theParent                   =None,
        theParentTraversalName      ='',
        theTypeConfig               =None, 
        theAllTypeConfigs           =None, 
        theViewName                 ='', 
        theRetrievalExtents         =None,
        theWritePermissions         =None,
        theFeatureFilters           =None, 
        theInstanceFilters          =None,
        theTranslationsCaches       =None,
        theCheckedPermissionsCache  =None,
        theAdditionalParams         =None):
                
        return ModelDDvlPloneTool_Retrieval().fRetrieveTypeConfig( 
            theTimeProfilingResults     =theTimeProfilingResults,
            theElement                  =theElement, 
            theParent                   =theParent,
            theParentTraversalName      =theParentTraversalName,
            theTypeConfig               =theTypeConfig, 
            theAllTypeConfigs           =theAllTypeConfigs, 
            theViewName                 =theViewName, 
            theRetrievalExtents         =theRetrievalExtents,
            theWritePermissions         =theWritePermissions,
            theFeatureFilters           =theFeatureFilters, 
            theInstanceFilters          =theInstanceFilters,
            theTranslationsCaches       =theTranslationsCaches,
            theCheckedPermissionsCache  =theCheckedPermissionsCache,
            theAdditionalParams         =theAdditionalParams
        )




    security.declareProtected( permissions.View, 'fRetrieveTypeConfigByUID')
    def fRetrieveTypeConfigByUID(self, 
        theTimeProfilingResults     =None,
        theContextualElement        =None, 
        theUID                      =None, 
        theTypeConfig               =None, 
        theAllTypeConfigs           =None, 
        theViewName                 ='', 
        theRetrievalExtents         =None,
        theWritePermissions         =None,
        theFeatureFilters           =None, 
        theInstanceFilters          =None,
        theTranslationsCaches       =None,
        theCheckedPermissionsCache  =None,
        theAdditionalParams         =None):
                
        return ModelDDvlPloneTool_Retrieval().fRetrieveTypeConfigByUID( 
            theTimeProfilingResults     =theTimeProfilingResults,
            theContextualElement        =theContextualElement, 
            theUID                      =theUID, 
            theTypeConfig               =theTypeConfig, 
            theAllTypeConfigs           =theAllTypeConfigs, 
            theViewName                 =theViewName, 
            theRetrievalExtents         =theRetrievalExtents,
            theWritePermissions         =theWritePermissions,
            theFeatureFilters           =theFeatureFilters, 
            theInstanceFilters          =theInstanceFilters,
            theTranslationsCaches       =theTranslationsCaches,
            theCheckedPermissionsCache  =theCheckedPermissionsCache,
            theAdditionalParams         =theAdditionalParams
        )




    security.declareProtected( permissions.View, 'fRetrieveElementoBasicInfoAndTranslations')
    def fRetrieveElementoBasicInfoAndTranslations(self, 
        theTimeProfilingResults     =None,
        theContainerElement         =None, 
        thePloneSubItemsParameters  =None, 
        theRetrievalExtents         =None,
        theWritePermissions         =None,
        theFeatureFilters           =None, 
        theInstanceFilters          =None,
        theTranslationsCaches       =None,
        theCheckedPermissionsCache  =None,
        theAdditionalParams         =None):
        
        return ModelDDvlPloneTool_Retrieval().fRetrieveElementoBasicInfoAndTranslations( 
            theTimeProfilingResults     =theTimeProfilingResults,
            theContainerElement         =theContainerElement, 
            thePloneSubItemsParameters  =thePloneSubItemsParameters, 
            theRetrievalExtents         =theRetrievalExtents,
            theWritePermissions         =theWritePermissions,
            theFeatureFilters           =theFeatureFilters, 
            theInstanceFilters          =theInstanceFilters,
            theTranslationsCaches       =theTranslationsCaches,
            theCheckedPermissionsCache  =theCheckedPermissionsCache,
            theAdditionalParams         =theAdditionalParams
        )




    
    security.declareProtected( permissions.View, 'fRetrievePloneContent')
    def fRetrievePloneContent(self, 
        theTimeProfilingResults     =None,
        theContainerElement         =None, 
        thePloneSubItemsParameters  =None, 
        theRetrievalExtents         =None,
        theWritePermissions         =None,
        theFeatureFilters           =None, 
        theInstanceFilters          =None,
        theTranslationsCaches       =None,
        theCheckedPermissionsCache  =None,
        theAdditionalParams         =None):

        return ModelDDvlPloneTool_Retrieval().fRetrievePloneContent( 
            theTimeProfilingResults     =theTimeProfilingResults,
            theContainerElement         =theContainerElement, 
            thePloneSubItemsParameters  =thePloneSubItemsParameters, 
            theRetrievalExtents         =theRetrievalExtents,
            theWritePermissions         =theWritePermissions,
            theFeatureFilters           =theFeatureFilters, 
            theInstanceFilters          =theInstanceFilters,
            theTranslationsCaches       =theTranslationsCaches,
            theCheckedPermissionsCache  =theCheckedPermissionsCache,
            theAdditionalParams         =theAdditionalParams
        )
    

    
    
    
    security.declareProtected( permissions.View, 'fRetrieveElementsOfType')
    def fRetrieveElementsOfType(self, 
        theTimeProfilingResults     =None,
        theElement                  =None,
        theTypeNames                =None,
        theAllTypeConfigs           =None, 
        theTranslationsCaches       =None, 
        theCheckedPermissionsCache  =None, 
        theWritePermissions         =None, 
        theAdditionalParams         =None):
        
        return ModelDDvlPloneTool_Retrieval().fRetrieveElementsOfType( 
            theTimeProfilingResults     =theTimeProfilingResults,
            theElement                  =theElement,
            theTypeNames                =theTypeNames,
            theAllTypeConfigs           =theAllTypeConfigs, 
            theTranslationsCaches       =theTranslationsCaches, 
            theCheckedPermissionsCache  =theCheckedPermissionsCache, 
            theWritePermissions         =theWritePermissions, 
            theAdditionalParams         =theAdditionalParams
        )
        
        
    
    

    
    
    
    
                                
    security.declareProtected( permissions.View, 'fDefaultPloneSubItemsParameters')
    def fDefaultPloneSubItemsParameters(self):
        return ModelDDvlPloneTool_Retrieval().fDefaultPloneSubItemsParameters()
    
   
   
    
    


    security.declareProtected( permissions.View, 'fDeleteImpactReport')
    def fDeleteImpactReport(self, 
        theTimeProfilingResults =None,
        theElement              =None,
        theAdditionalParams     =None):
        
        return ModelDDvlPloneTool_Retrieval().fDeleteImpactReport( 
            theTimeProfilingResults =theTimeProfilingResults,
            theElement              =theElement,
            theAdditionalParams     =theAdditionalParams 
        )
        
        
        
        
        
        
#####################################################
# Rest (ReStructuredText) reporting methods

    
    
    
    security.declarePublic( 'fCookedBodyForElement')
    def fCookedBodyForElement(self, 
        theTimeProfilingResults =None,
        theElement              =None, 
        stx_level               =None, 
        setlevel                =0,
        theAdditionalParams     =None):
        
        return ModelDDvlPloneTool_Bodies().fCookedBodyForElement( 
            theTimeProfilingResults =theTimeProfilingResults,
            theElement              =theElement, 
            stx_level               =stx_level, 
            setlevel                =setlevel,
            theAdditionalParams     =theAdditionalParams)
    

    
    
    
    
    security.declarePublic( 'fEditableBodyForElement')
    def fEditableBodyForElement(self, 
        theTimeProfilingResults =None,
        theElement              =None,
        theAdditionalParams     =None):
        
        return ModelDDvlPloneTool_Bodies().fEditableBodyForElement( 
            theTimeProfilingResults =theTimeProfilingResults,
            theElement              =theElement,
            theAdditionalParams     =theAdditionalParams
        )
    

    

    
    
    
    
    
#####################################################
# Change element methods
            
    
    
    
    security.declareProtected( permissions.AddPortalContent,  'fCrearElementoDeTipo')
    def fCrearElementoDeTipo(self, 
        theTimeProfilingResults =None,
        theContainerElement      =None, 
        theTypeName             ='', 
        theTitle                ='', 
        theDescription          ='',
        theAdditionalParams     =None,
        theAllowFactoryMethods  =False,):           
        
        return ModelDDvlPloneTool_Mutators().fCrearElementoDeTipo( 
            theTimeProfilingResults =theTimeProfilingResults,
            theContainerElement     =theContainerElement, 
            theTypeName             =theTypeName, 
            theTitle                =theTitle, 
            theDescription          =theDescription,
            theAdditionalParams     =theAdditionalParams,
            theAllowFactoryMethods  =theAllowFactoryMethods,
        )
            
        
   
    
    security.declareProtected( permissions.AddPortalContent,  'fCrearElementoDeTipoEspecial')
    def fCrearElementoDeTipoEspecial(self, 
        theTimeProfilingResults =None,
        theContainerElement     =None, 
        theTypeName             ='', 
        theTitle                ='', 
        theDescription          ='',
        theAdditionalParams     =None):           
        
        return ModelDDvlPloneTool_Mutators().fCrearElementoDeTipo( 
            theTimeProfilingResults =theTimeProfilingResults,
            theContainerElement      =theContainerElement, 
            theTypeName             =theTypeName, 
            theTitle                =theTitle, 
            theDescription          =theDescription,
            theAdditionalParams     =theAdditionalParams
        )
            
    
    
        
    security.declareProtected(  permissions.ModifyPortalContent, 'fChangeValues')
    def fChangeValues(self, 
        theTimeProfilingResults =None,
        theElement              =None, 
        theNewValuesDict        =None,
        theAdditionalParams     =None):        
        
        return ModelDDvlPloneTool_Mutators().fChangeValues(  
            theTimeProfilingResults =theTimeProfilingResults,
            theElement              =theElement, 
            theNewValuesDict        =theNewValuesDict,
            theAdditionalParams     =theAdditionalParams
        )
        
        
        
    
    
    security.declareProtected( permissions.ModifyPortalContent, 'pMoveSubObject')
    def pMoveSubObject(self, 
        theTimeProfilingResults =None,
        theContainerElement      =None,  
        theTraversalName        =None, 
        theMovedObjectId        =None, 
        theMoveDirection        =None, 
        theAdditionalParams     =None):        
        
        return ModelDDvlPloneTool_Mutators().pMoveSubObject( 
            theTimeProfilingResults =theTimeProfilingResults,
            theContainerElement      =theContainerElement,  
            theTraversalName        =theTraversalName, 
            theMovedObjectId        =theMovedObjectId, 
            theMoveDirection        =theMoveDirection, 
            theAdditionalParams     =theAdditionalParams
        )
        
        
        
    
           
    security.declareProtected( permissions.ModifyPortalContent, 'pMoveReferencedObject')
    def pMoveReferencedObject(self,
        theTimeProfilingResults =None,
        theSourceElement        =None,  
        theReferenceFieldName   =None, 
        theMovedReferenceUID    =None, 
        theMoveDirection        =None,
        theAdditionalParams     =None):        
        
        return ModelDDvlPloneTool_Mutators().pMoveReferencedObject(
            theTimeProfilingResults =theTimeProfilingResults,
            theSourceElement        =theSourceElement,  
            theReferenceFieldName   =theReferenceFieldName, 
            theMovedReferenceUID    =theMovedReferenceUID, 
            theMoveDirection        =theMoveDirection, 
            theAdditionalParams     =theAdditionalParams
        )

    
    
     
    security.declareProtected(  permissions.ModifyPortalContent, 'fLinkToUIDReferenceFieldNamed')
    def fLinkToUIDReferenceFieldNamed(self, 
        theTimeProfilingResults =None,
        theSourceElement        =None, 
        theReferenceFieldName   =None, 
        theTargetUID            =None,
        theAdditionalParams     =None):        
        
        return ModelDDvlPloneTool_Mutators().fLinkToUIDReferenceFieldNamed( 
            theTimeProfilingResults =theTimeProfilingResults,            
            theSourceElement        =theSourceElement, 
            theReferenceFieldName   =theReferenceFieldName, 
            theTargetUID            =theTargetUID, 
            theAdditionalParams     =theAdditionalParams
        )
        
    
    
        
    
    security.declareProtected(  permissions.ModifyPortalContent, 'fUnlinkFromUIDReferenceFieldNamed')
    def fUnlinkFromUIDReferenceFieldNamed(self, 
        theTimeProfilingResults =None,
        theSourceElement        =None, 
        theReferenceFieldName   =None, 
        theTargetUID            =None,
        theAdditionalParams     =None):        

        return ModelDDvlPloneTool_Mutators().fUnlinkFromUIDReferenceFieldNamed( 
            theTimeProfilingResults =theTimeProfilingResults,            
            theSourceElement        =theSourceElement, 
            theReferenceFieldName   =theReferenceFieldName, 
            theTargetUID            =theTargetUID, 
            theAdditionalParams     =theAdditionalParams
        )
        
        
    
    
    
    security.declareProtected( permissions.DeleteObjects,  'fEliminarElemento')
    def fEliminarElemento(self, 
        theTimeProfilingResults =None,                          
        theElement              =None, 
        theIdToDelete           =None, 
        theUIDToDelete          =None, 
        theRequestSeconds       =None, 
        theAdditionalParams     =None):        

        return ModelDDvlPloneTool_Mutators().fEliminarElemento( 
            theTimeProfilingResults =theTimeProfilingResults,
            theElement              =theElement,            
            theIdToDelete           =theIdToDelete, 
            theUIDToDelete          =theUIDToDelete, 
            theRequestSeconds       =theRequestSeconds, 
            theAdditionalParams     =theAdditionalParams
        )
    
                
    
    
    
    
    
#####################################################
# Change Plone methods
            
                
    
    
    security.declareProtected( permissions.DeleteObjects,  'fEliminarElementoPlone')
    def fEliminarElementoPlone(self, 
        theTimeProfilingResults =None,                          
        theContainerElement     =None, 
        theUIDToDelete          =None, 
        theRequestSeconds       =None, 
        theAdditionalParams     =None):        

        return ModelDDvlPloneTool_Mutators().fEliminarElementoPlone( 
            theTimeProfilingResults =theTimeProfilingResults, 
            theContainerElement     =theContainerElement,
            theUIDToDelete          =theUIDToDelete, 
            theRequestSeconds       =theRequestSeconds, 
            theAdditionalParams     =theAdditionalParams
        )

            
    
    
    
    security.declareProtected( permissions.ModifyPortalContent, 'pMoveSubObjectPlone')
    def pMoveSubObjectPlone(self, 
        theTimeProfilingResults =None,                          
        theContainerElement     =None,  
        theTraversalName        ='', 
        theMovedObjectUID       =None, 
        theMoveDirection        ='', 
        theAdditionalParams     =None):        

        return ModelDDvlPloneTool_Mutators().pMoveSubObjectPlone( 
            theTimeProfilingResults =theTimeProfilingResults,            
            theContainerElement      =theContainerElement,  
            theTraversalName        =theTraversalName, 
            theMovedObjectUID       =theMovedObjectUID, 
            theMoveDirection        =theMoveDirection, 
            theAdditionalParams     =theAdditionalParams
        )
                
    
    
    
    
    
                

#####################################################
# Display view maintenance methods

               
                   

    security.declareProtected( permissions.View,  'pSetDefaultDisplayView')
    def pSetDefaultDisplayView(self, theElement):  
    
        if not ModelDDvlPloneTool_Retrieval().fCheckElementPermission( theElement, [ permissions.ModifyPortalContent ], None):
            return self
            
        unaDefaultView = ''
        try:
            unaDefaultView = theElement.default_view
        except:
            None
        
        if unaDefaultView:
            self.pSetAsDisplayView( theElement, unaDefaultView)
            
        return self
        



    security.declareProtected( permissions.ModifyPortalContent,  'pSetAsDisplayView')
    def pSetAsDisplayView(self, theElement, theViewName):            
                
        unaPortalInterfaceTool = getToolByName( theElement, 'portal_interface')   
        if unaPortalInterfaceTool.objectImplements( theElement, 'Products.CMFPlone.interfaces.BrowserDefault.ISelectableBrowserDefault'):
            if not theElement.getLayout() == theViewName:
                theElement.setLayout( theViewName)                 
        return self
                   
    
    
    
    
    
    
    
    
#######################################
# Internationalisation methods

    
    security.declareProtected( permissions.View,  'fTranslateI18N')
    def fTranslateI18N( self, theContextElement, theI18NDomain, theString, theDefault):
        return ModelDDvlPloneTool_Retrieval().fTranslateI18N( theI18NDomain, theString, theDefault, theContextElement)



    security.declareProtected( permissions.View,  'fAsUnicode')
    def fAsUnicode( self, theContextElement,  theString):
        return ModelDDvlPloneTool_Retrieval().fAsUnicode(theString, theContextElement)

    

    
    
    
    
    
    
#######################################
# Pretty print methods

    
    security.declareProtected( permissions.View,  'fPrettyPrintHTML')
    def fPrettyPrintHTML( self, theList, theDictKeysToExclude=None, theDictKeysOrder=None, theFindAlreadyPrinted=False):
        return ModelDDvlPloneTool_Retrieval().fPrettyPrintHTML( theList, theDictKeysToExclude, theDictKeysOrder, theFindAlreadyPrinted)


    security.declareProtected( permissions.View,  'fPrettyPrint')
    def fPrettyPrint( self, theList, theDictKeysToExclude=None, theDictKeysOrder=None, theFindAlreadyPrinted=False):
        return ModelDDvlPloneTool_Retrieval().fPrettyPrint( theList, theDictKeysToExclude, theDictKeysOrder, theFindAlreadyPrinted)


    security.declareProtected( permissions.View,  'fPrettyPrintProfilingResultHTML')
    def fPrettyPrintProfilingResultHTML( self, theProfilingResult):
        return ModelDDvlPloneTool_Retrieval().fPrettyPrintProfilingResultHTML( theProfilingResult)

    security.declareProtected( permissions.View,  'fPrettyPrintProfilingResultHTML')
    def fPrettyPrintProfilingResult( self, theProfilingResult):
        return ModelDDvlPloneTool_Retrieval().fPrettyPrintProfilingResult( theProfilingResult)

    security.declareProtected( permissions.View,  'fPreferredResultDictKeysOrder')
    def fPreferredResultDictKeysOrder( self):
        return ModelDDvlPloneTool_Retrieval().fPreferredResultDictKeysOrder()

    
    
# #############################################################
# Template invocation methods
#


    security.declarePublic('fRenderTemplate')
    def fRenderTemplate(self, theContextualObject, theTemplateName):
        if not theTemplateName:
            return ''
                        
        aViewName = theTemplateName
        if aViewName.find( '%s') >= 0:
            unNombreProyecto = ''
            try:
                unNombreProyecto = theContextualObject.getNombreProyecto()
            except:
                None
            if unNombreProyecto:    
                aViewName = aViewName % unNombreProyecto
            else:
                aViewName = aViewName % ''
            
        if not aViewName:
            return ''
        
        aViewTemplate    = self.unrestrictedTraverse( aViewName)

        aContext                = aq_inner( theContextualObject)               
        aViewTemplateInContext  = aViewTemplate.__of__(aContext)
        
        aRenderedView = aViewTemplateInContext()       
                   
        return aRenderedView
    
    
    



    
    
    
    security.declareProtected( permissions.View, 'fExport')
    def fExport(self, 
        theTimeProfilingResults     =None,
        theObject                   =None, 
        theOutputEncoding           =None,
        theAdditionalParams         =None):
        
        someAllExportTypeConfigs =  ModelDDvlPloneTool_Retrieval().getAllTypeExportConfigs( theObject)        
                
        return ModelDDvlPloneTool_Export().fExport( 
            theTimeProfilingResults     =theTimeProfilingResults,
            theObject                   =theObject, 
            theAllExportTypeConfigs     =someAllExportTypeConfigs, 
            theOutputEncoding           =theOutputEncoding,
            theAdditionalParams         =theAdditionalParams
        )

    
    
    

#####################################################
# Constructor methods, only used when adding class
# to objectManager

def manage_addAction(self, REQUEST=None):
    "Add tool instance to parent ObjectManager"
    id = ModelDDvlPloneTool.id
    self._setObject(id, ModelDDvlPloneTool())
    if REQUEST is not None:
        return self.manage_main(self, REQUEST)

constructors = (manage_addAction,)



