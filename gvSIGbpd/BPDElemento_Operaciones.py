# -*- coding: utf-8 -*-
#
# File: BPDElemento_Operaciones.py
#
# Copyright (c) 2009 by Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana
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
#

__author__ = """Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana <gvSIGbpd@gvSIG.org>, 
Model Driven Development sl <gvSIGbpd@ModelDD.org>,
Antonio Carrasco Valero <carrasco@ModelDD.org>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.gvSIGbpd.config import *

from Products.Archetypes.utils import shasattr


from Acquisition        import aq_inner, aq_parent



##code-section module-header #fill in your manual code here

       
  

import sys
import traceback
import logging


from Acquisition                    import aq_get

from Products.CMFCore               import permissions
from Products.CMFCore.utils         import getToolByName

from AccessControl.Permissions   import access_contents_information   as perm_AccessContentsInformation

from Products.ModelDDvlPloneTool.ModelDDvlPloneToolLoadConstants import cModelDDvlPloneToolId


#from OFS.CopySupport import CopyError as gCopyErrorExceptionString     
#from OFS.CopySupport import eNoData as gNoDataExceptionDialog     
#from OFS.CopySupport import eInvalid as gInvalidExceptionDialog     
#from OFS.CopySupport import eNotFound as gNotFoundExceptionDialog     

from ZODB.POSException import ConflictError  
from OFS.CopySupport import CopyContainer
from OFS     import Moniker        

from marshal import loads
from urllib  import unquote
from zlib    import decompress



cLogExceptions = True


##/code-section module-header



##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDElemento_Operaciones:
    """
    """
    security = ClassSecurityInfo()

    ##code-section class-header #fill in your manual code here
    
  
    
    
   
    # #############################################################
    # Intercepting modification method for re-ordering an OrderedBaseFolder specialization
    # used in to provide drag&drop functionality directly from Plone.
    # does not hit the ModelDDvlPlone framework presentation layer
    # and therefore the incalidation of cache entries must be triggered by intercepting the method
    #

    security.declareProtected(permissions.ModifyPortalContent, 'pHandle_moveObjectsByDelta')
    def pHandle_moveObjectsByDelta(self, ids, delta, subset_ids=None): 
        
        unResult = OrderedBaseFolder.moveObjectsByDelta( self,  ids, delta, subset_ids=subset_ids)
        
        if not unResult:
            return self
        
        
        unaModelDDvlPloneTool = self.fModelDDvlPloneTool()
        if not unaModelDDvlPloneTool:
            return self
        
        someImpactedUIDs = []
        
        unaOwnUID = self.UID()
        someImpactedUIDs.append( unaOwnUID)
        
        if shasattr( self, 'getContenedor'):
            unContenedor = None
            try:
                unContenedor = self.getContenedor()
            except:
                None
            if not ( unContenedor == None):
                unContenedorUID = ''
                if shasattr( self, 'UID'):
                    unContenedorUID = ''
                    try:
                        unContenedorUID = unContenedor.UID()
                    except:
                        None
                    if unContenedorUID and not ( unContenedorUID in someImpactedUIDs):
                        someImpactedUIDs.append( unContenedorUID)
            
        if shasattr( self, 'getPropietario'):
            unPropietario = None
            try:
                unPropietario = self.getPropietario()
            except:
                None
            if not ( unPropietario == None) and not ( unPropietario == unContenedor):
                unPropietarioUID = ''
                if shasattr( self, 'UID'):
                    unPropietarioUID = ''
                    try:
                        unPropietarioUID = unPropietario.UID()
                    except:
                        None
                if unPropietarioUID and not ( unPropietarioUID in someImpactedUIDs):
                    someImpactedUIDs.append( unPropietarioUID)
            
        someIds = ids
        if not ( someIds.__class__.__name__ in [ 'list', 'tuple', 'set',]):
            someIds = [ someIds,]

        aMovedNewPosition = -1
        someObjectValues = self.objectValues()
        for anObjectIndex in range( len( someObjectValues)):
            
            anObject = someObjectValues[ anObjectIndex]
            
            anObjectId = anObject.getId()
            if ( anObjectId in someIds):
                aMovedNewPosition = anObjectIndex
                
            anObjectUID = anObject.UID()
            if anObjectUID and not ( anObjectUID in someImpactedUIDs):
                someImpactedUIDs.append( anObjectUID)

                
        anElementToReportUpon = None
            
        for anId in someIds:
            for anObject in someObjectValues:
                if anObject.getId() == anId:
                    anElementToReportUpon = anObject
                    break
                
        anElementResult = None
        if not ( anElementToReportUpon == None):
            anElementResult = unaModelDDvlPloneTool.fNewResultForElement( anElementToReportUpon)
            
            
        unaModelDDvlPloneTool.pFlushCachedTemplatesForImpactedElementsUIDs( self, someImpactedUIDs)
        
        aMoveReport = {
            'effect':                  'moved', 
            'new_position':            aMovedNewPosition,
            'delta':                   delta,
            'moved_element':           anElementResult,
            'parent_traversal_name':   '',
            'impacted_objects_UIDs':   someImpactedUIDs,
        } 
        unaModelDDvlPloneTool._pSetAudit_Modification( self, 'Move Sub Object', aMoveReport)
        
        return unResult
            
    
    
    
    
    # #############################################################
    # Portal accessors
    # 


 
    security.declarePrivate('fPortalRoot')
    def fPortalRoot(self):
        aPortalTool = getToolByName( self, 'portal_url')
        unPortal = aPortalTool.getPortalObject()
        return unPortal       
    
    
        
    
    
    
# #############################################################
# Version  accessors (root of application elements network)
# 


    
    security.declareProtected( permissions.View, 'fDerive_VersionInterna')
    def fDerive_VersionInterna(self):
        
        unRaiz = self.getRaiz()
        
        if ( not unRaiz) or ( unRaiz == self):
            return self.getVersionInternaAlmacenada()
        
        return unRaiz.getVersionInterna()
    
            
    

    

    
    security.declareProtected( permissions.View, 'fDerive_ComentarioVersionInterna')
    def fDerive_ComentarioVersionInterna(self):
        
        unRaiz = self.getRaiz()
        
        if ( not unRaiz) or ( unRaiz == self):
            return self.getComentarioVersionInternaAlmacenada()
        
        return unRaiz.getComentarioVersionInterna()
    
            
    
   
    
    
# #############################################################
# Translation  accessors 
# 


    security.declareProtected( permissions.View, 'fDerive_EsTraduccionInterna')
    def fDerive_EsTraduccionInterna(self):
        
        unRaiz = self.getRaiz()
        
        unEsTraduccionInternaAlmacenada = self.getEsTraduccionInternaAlmacenada()
        if unEsTraduccionInternaAlmacenada=='Segun Contenedor':
            if not unRaiz:
                return 'No Traducible'
            
            return unRaiz.getEsTraduccionInterna()
        
        return unEsTraduccionInternaAlmacenada
    

        
    
        

    
# #############################################################
# Owner accessors
# 




 
    security.declarePrivate( 'fComposeOwnerName')
    def fComposeOwnerName( self, theSeparator, theAttributeName, theExcludeRoot=True):

        if not theAttributeName:
            return u''
            
        if self.getEsRaiz():
            if theExcludeRoot:
                return u''
            else:
                return self.fFV( theAttributeName)
            
        unContenedorQualifiedName = u''
        unContenedor = self.getContenedor()
        if unContenedor:
            unContenedorQualifiedName = unContenedor.fComposeQualifiedName( theSeparator, theAttributeName, theExcludeRoot)
 
        return unContenedorQualifiedName
      
     
     
     
     
     
    security.declarePrivate( 'fComposeQualifiedName')
    def fComposeQualifiedName( self, theSeparator, theAttributeName='title', theExcludeRoot=False):

        if not theAttributeName:
            return u''
            
        unSeparator = self.fAsUnicode( theSeparator)
        if not unSeparator:
            unSeparator = u''
                 
        if self.getEsRaiz():
            if theExcludeRoot:
                return u''
            else:
                return self.fFV( theAttributeName)
            
            
        unQualifiedName = u''
        unContenedor = self.getContenedor()
        if unContenedor:
            unContenedorQualifiedName = unContenedor.fComposeQualifiedName( theSeparator, theAttributeName, theExcludeRoot)
            if unContenedorQualifiedName:
                unQualifiedName = unSeparator.join( [ unContenedorQualifiedName, self.fFV( theAttributeName), ] )
            else:
                unQualifiedName = self.fFV( theAttributeName)
            
        return unQualifiedName
      
      
      
      

    
    
    
    
# #############################################################
# Raiz  accessors (root of application elements network)
# 

    


    security.declareProtected( permissions.View, 'getRaiz')
    def getRaiz(self):
        if self.getEsRaiz():
            return self            
        unContenedor =  aq_parent( aq_inner( self))
        
        if not unContenedor:
            return None
        
        return unContenedor.getRaiz()



    # OJO ACV 20091111 
    # Removed from model and coded here for more efficiency
    #
    security.declareProtected( permissions.View, 'getEsRaiz')
    def getEsRaiz(self):
                   
        unContenedor =  aq_parent( aq_inner( self))

        if not unContenedor:
            return True
        
        unMetaTypeContenedor = unContenedor.meta_type 
        
        unasClassNames = self.fParentArchetypeClassNames()
        
        if ( unMetaTypeContenedor in unasClassNames):
            return False
            
        return True



    # OJO ACV 20091111 
    # Removed from model and coded here for more efficiency
    #
    security.declareProtected( permissions.View, 'getContenedor')
    def getContenedor(self):
        return aq_parent( aq_inner( self))





    # OJO ACV 20091111 
    # Removed from model and coded here for more efficiency
    #
    security.declareProtected( permissions.View, 'getContenedorContenedor')
    def getContenedorContenedor(self):
        return aq_parent( aq_parent( aq_inner( self)))





    # OJO ACV 20091111 
    # Removed from model and coded here for more efficiency
    #
    security.declareProtected( permissions.View, 'CookedBody')
    def CookedBody(self, setlevel=0, stx_level=None):
        return getToolByName( self, 'MDDModelDDvlPlone_tool').fCookedBodyForElement( None, self, stx_level, setlevel, None)





    # OJO ACV 20091111 
    # Removed from model and coded here for more efficiency
    #
    security.declareProtected( permissions.View, 'getEditableBody')
    def getEditableBody(self, setlevel=0, stx_level=None):
        return getToolByName( self, 'MDDModelDDvlPlone_tool').fEditableBodyForElement( None, self, None)

















    # OJO ACV 20090609 
    # to use standard plone portal_catalog path index rather than 
    # the application specific getPathDelRaiz
    security.declarePrivate('fPathDelRaiz')
    def fPathDelRaiz(self):
        unRaiz = self.getRaiz()
        if not unRaiz:
            return ''
       
        unPathString = unRaiz.fPhysicalPathString( )
        return unPathString
        
    
    #security.declarePrivate('fPathDelRaiz')
    #def fPathDelRaiz(self):
        #unRaiz = self.getRaiz()
        #if not unRaiz:
            #return ''
       
        #unPathString = self.fPhysicalPathString( unRaiz)
        #return unPathString



    # ACV 20090913 Return the standard path, not the variation we were using before, without the root site name
    # Remove the parameter
    security.declarePrivate('fPhysicalPathString')
    def fPhysicalPathString(self, ):
        unPhysicalPath = self.getPhysicalPath()
        if not unPhysicalPath:
            return ''
     
        #if unPhysicalPath[ 0] == '':
            #unPhysicalPath = unPhysicalPath[1:]
        
        #unFoldersPath = unPhysicalPath[1:]
        #unPathString = '/' + '/'.join( unFoldersPath)
        unPathString = '/'.join( unPhysicalPath)
        return unPathString




    security.declarePrivate('getPropietario')
    def getPropietario(self):
        if self.getEsRaiz():
            return self
            
        unContenedor = aq_parent( aq_inner( self))
        
        if not unContenedor:
            return None
        
        if unContenedor.getEsRaiz():
            return unContenedor
        
        if unContenedor.getEsColeccion():
            return unContenedor.getPropietario()
        
        return unContenedor





    security.declarePrivate('getNumeroOrdenEnPropietario')
    def getNumeroOrdenEnPropietario(self, elNombreTipoColeccion="", elTituloColeccion="", losNombresTiposContenidos=[]):
        unContenedor = self.getContenedor()
        if not unContenedor:
            return -1
        unosContenidos = unContenedor.objectValues()
        
        if self in unosContenidos:
            unIndice = unosContenidos.index( self) + 1
        else:
            unIndice = -1
        return unIndice
            
            
  
  
  
    security.declarePrivate( 'fEsCreacionSimple')
    def fEsCreacionSimple(self, theFieldName, theTypeName):  
        unaFactoryView = self.fFactoryViewForType( theFieldName, theTypeName) 
        if not unaFactoryView:
            return False
        return True
        
        
     


    security.declarePrivate( 'fFactoryViewForType')
    def fFactoryViewForType(self, theFieldName, theTypeName, ):   
        unSchema = self.schema
        if not unSchema.has_key( theFieldName):
            return ''
            
        unField             = unSchema[ theFieldName]
         
        unosFactoryViews = {}
        try:
            unosFactoryViews = unField.factory_views
        except:
            None
            
        if not unosFactoryViews or not unosFactoryViews.has_key( theTypeName):
            return ''
            
        unaFactoryView = unosFactoryViews[ theTypeName]
 
        return unaFactoryView
                



            
            
#   fTFL stands for function for Translated Field Label
#   will be used in the context of expressions of computed archetype schema fields
#   the short name is to use less space
#   in the tagged value edition fields
#   of case tools            
    security.declarePrivate('fTFL')
    def fTFL(self, theFieldName):
        if not theFieldName:
            return ''
            
        aSchema = self.schema
        if not aSchema.has_key( theFieldName):
            return theFieldName
       
        aField = aSchema.get( theFieldName)
        if not aField:
            return theFieldName
            
        aWidget = aField.widget
        if not aWidget:
            return theFieldName
        
        aMsgId = aWidget.label_msgid
        if not aMsgId:
            return theFieldName
        
        anI18NDomain = self.getNombreProyecto()   
        if not anI18NDomain:
            return theFieldName

        aTranslationService = None
        try:
            aTranslationService = self.translation_service
        except:
            None
        if not aTranslationService:
            return theFieldName
            
        aTranslation = aTranslationService.utranslate( anI18NDomain, aMsgId, mapping=None, context=self , target_language= None, default=theFieldName)                       
        if not aTranslation:
            return theFieldName

        return aTranslation
    
 
 
#   fTFLVs stands for function for multiple  Translated Field Label and Value
#   will be used in the context of expressions of computed archetype schema fields
#   the short name is to use less space
#   in the tagged value edition fields
#   of case tools            
    security.declarePrivate('fTFLVs')
    def fTFLVs(self, theFieldNames):
        if not theFieldNames:
            return ''
        
        someFieldLabelsAndValues = []
        for unFieldName in theFieldNames:
            unFieldLabelAndValue = self.fTFLV( unFieldName)
            if unFieldLabelAndValue:
                someFieldLabelsAndValues.append( unFieldLabelAndValue)

        if not someFieldLabelsAndValues:
            return ''
            
        unResultString = '; '.join( someFieldLabelsAndValues)

        return unResultString
            


#   fTFLVsUnless stands for function for multiple  Translated Field Label and Value
#   will be used in the context of expressions of computed archetype schema fields
#   the short name is to use less space
#   in the tagged value edition fields
#   of case tools            
    security.declarePrivate('fTFLVsUnless')
    def fTFLVsUnless(self, theFieldNamesAndExcludeValues):
        if not theFieldNamesAndExcludeValues:
            return ''
        
        someFieldLabelsAndValues = []
        for unFieldName, unExcludeValue in theFieldNamesAndExcludeValues:
            unFieldLabelAndValue = self.fTFLVUnless( unFieldName, unExcludeValue)
            if unFieldLabelAndValue:
                someFieldLabelsAndValues.append( unFieldLabelAndValue)

        if not someFieldLabelsAndValues:
            return ''
            
        unResultString = '; '.join( someFieldLabelsAndValues)

        return unResultString
            
    
    
#   fTFLV stands for function for Translated Field Label and Value
#   will be used in the context of expressions of computed archetype schema fields
#   the short name is to use less space
#   in the tagged value edition fields
#   of case tools            
    security.declarePrivate('fTFLV')
    def fTFLV(self, theFieldName):
        if not theFieldName:
            return ''

        aTranslatedLabel = self.fTFL( theFieldName)
        if not aTranslatedLabel:
            aTranslatedLabel = ''         
    
        unValueString = self.fFV( theFieldName)
        if not unValueString:
            return ''
            
        return aTranslatedLabel + ' ' + unValueString
             

   
#   fTFLVUnless stands for function for Translated Field Label and Value
#   will be used in the context of expressions of computed archetype schema fields
#   the short name is to use less space
#   in the tagged value edition fields
#   of case tools            
    security.declarePrivate('fTFLVUnless')
    def fTFLVUnless(self, theFieldName, theExcludeValue):
        if not theFieldName:
            return ''

        unValueString = self.fFVUnless( theFieldName, theExcludeValue)
        if not unValueString:
            return ''
        
        aTranslatedLabel = self.fTFL( theFieldName)
        if not aTranslatedLabel:
            aTranslatedLabel = ''         
    
        return aTranslatedLabel + ' ' + unValueString
             
        
    
    
#   fFV stands for function for  Field Value
#   will be used in the context of expressions of computed archetype schema fields
#   the short name is to use less space
#   in the tagged value edition fields
#   of case tools            
    security.declarePrivate('fFV')
    def fFV(self, theFieldName):
        if not theFieldName:
            return ''

        unSchema = self.schema
        if not unSchema.has_key( theFieldName):
            return ''
            
        unField  = unSchema[ theFieldName]
        if not unField:
            return ''

        unAccessor = unField.getAccessor( self)
        if not unAccessor:
            return ''

        unValue = unAccessor()
        if ( unValue == None):
            return ''
            
        if unField.__class__.__name__ in ( 'RelationField', 'ReferenceField'):
            unIsMultiValued = unField.multiValued
            if not unIsMultiValued: 
                if not unValue:
                    return ''
                unTitle = unValue.Title()
                if not unTitle:
                    return ''
                return unTitle
            else:
                unosTitulos = []
                if unValue:
                    for unElement in unValue:
                        unTitle = unElement.Title()
                        if unTitle:
                            unosTitulos.append( unTitle)
                if not unosTitulos:
                    return ''
                unosTitulosString = ', '.join( unosTitulos)
                return unosTitulosString
                                             
        
                        
        unElementFieldType      = unField.type
        
        if unElementFieldType == 'computed':
            unElementFieldType = 'string'
                    
        unValueString = ''
                            
        unWidget = unField.widget
        if unWidget and (unWidget.getType() == 'Products.Archetypes.Widget.SelectionWidget') and unField.__dict__.has_key('vocabulary'):    
            unValueString = unValue    
            someVocabularyOptions   = []
            try:
                someVocabularyOptions = unField.vocabulary   
            except:
                None
                
            someVocabularyMsgIds = []
            try:
                someVocabularyMsgIds = unField.vocabulary_msgids   
            except:
                None
                
            aTranslationService = None
            try:
                aTranslationService = self.translation_service
            except:
                None

            anI18NDomain = self.getNombreProyecto()   
                
            if someVocabularyOptions and someVocabularyMsgIds and aTranslationService and anI18NDomain:
                if unValue in someVocabularyOptions:
                    unValueIndex = someVocabularyOptions.index( unValue)
                    if (unValueIndex >= 0) and ( unValueIndex < len( someVocabularyMsgIds)):
                        unValueMsgId = someVocabularyMsgIds[ unValueIndex]
                        aTranslation = aTranslationService.utranslate( anI18NDomain, unValueMsgId, mapping=None, context=self , target_language= None, default=unValueString)                       
                        if aTranslation:
                            unValueString = aTranslation                                               
                   
        elif unElementFieldType in[  'string', 'text']:            
            unValueString = unValue
            
        elif unElementFieldType == 'boolean':
            unValueString = str( unValue)
        
            aTranslationService = None
            try:
                aTranslationService = self.translation_service
            except:
                None

            anI18NDomain = self.getNombreProyecto() 
              
            if aTranslationService and anI18NDomain:
                if unValue:
                    aTranslation = aTranslationService.utranslate( 'ModelDDvlPlone', 'ModelDDvlPlone_True', mapping=None, context=self , target_language= None, default=unValueString)                       
                    if aTranslation:
                        unValueString = aTranslation
                else:
                    aTranslation = aTranslationService.utranslate( 'ModelDDvlPlone', 'ModelDDvlPlone_False', mapping=None, context=self , target_language= None, default=unValueString)                       
                    if aTranslation:
                        unValueString = aTranslation
                        
        elif unElementFieldType == 'integer':
            unValueString  = str( unValue)
            
        elif unElementFieldType == 'float':
            unValueString  = str( unValue)

        elif unElementFieldType == 'fixedpoint':
            unValueString  = str( unValue)

        elif unElementFieldType == 'datetime':
            unValueString  = str( unValue)
        
        else:
            unValueString  = str( unValue)
    
        return unValueString
    
     
    
    
    
    
    

    
#   fFVUnless stands for function for  Field Value
#   will be used in the context of expressions of computed archetype schema fields
#   the short name is to use less space
#   in the tagged value edition fields
#   of case tools            
    security.declarePrivate('fFVUnless')
    def fFVUnless(self, theFieldName, theExcludeValue):
        if not theFieldName:
            return ''

        unSchema = self.schema
        if not unSchema.has_key( theFieldName):
            return ''
            
        unField  = unSchema[ theFieldName]
        if not unField:
            return ''

        unAccessor = unField.getAccessor( self)
        if not unAccessor:
            return ''

        unValue = unAccessor()
        if ( unValue == None):
            return ''
            
        if unValue == theExcludeValue:
            return ''
        
        
        if unField.__class__.__name__ in ( 'RelationField', 'ReferenceField'):
            unIsMultiValued = unField.multiValued
            if not unIsMultiValued: 
                if not unValue:
                    return ''
                unTitle = unValue.Title()
                if not unTitle:
                    return ''
                return unTitle
            else:
                unosTitulos = []
                if unValue:
                    for unElement in unValue:
                        unTitle = unElement.Title()
                        if unTitle:
                            unosTitulos.append( unTitle)
                if not unosTitulos:
                    return ''
                unosTitulosString = ', '.join( unosTitulos)
                return unosTitulosString
                                             
        
                        
        unElementFieldType      = unField.type
        
        if unElementFieldType == 'computed':
            unElementFieldType = 'string'
                    
        unValueString = ''
                            
        unWidget = unField.widget
        if unWidget and (unWidget.getType() == 'Products.Archetypes.Widget.SelectionWidget') and unField.__dict__.has_key('vocabulary'):    
            unValueString = unValue    
            someVocabularyOptions   = []
            try:
                someVocabularyOptions = unField.vocabulary   
            except:
                None
                
            someVocabularyMsgIds = []
            try:
                someVocabularyMsgIds = unField.vocabulary_msgids   
            except:
                None
                
            aTranslationService = None
            try:
                aTranslationService = self.translation_service
            except:
                None

            anI18NDomain = self.getNombreProyecto()   
                
            if someVocabularyOptions and someVocabularyMsgIds and aTranslationService and anI18NDomain:
                if unValue in someVocabularyOptions:
                    unValueIndex = someVocabularyOptions.index( unValue)
                    if (unValueIndex >= 0) and ( unValueIndex < len( someVocabularyMsgIds)):
                        unValueMsgId = someVocabularyMsgIds[ unValueIndex]
                        aTranslation = aTranslationService.utranslate( anI18NDomain, unValueMsgId, mapping=None, context=self , target_language= None, default=unValueString)                       
                        if aTranslation:
                            unValueString = aTranslation                                               
                   
        elif unElementFieldType in[  'string', 'text']:            
            unValueString = unValue
            
        elif unElementFieldType == 'boolean':
            unValueString = str( unValue)
        
            aTranslationService = None
            try:
                aTranslationService = self.translation_service
            except:
                None

            anI18NDomain = self.getNombreProyecto() 
              
            if aTranslationService and anI18NDomain:
                if unValue:
                    aTranslation = aTranslationService.utranslate( 'ModelDDvlPlone', 'ModelDDvlPlone_True', mapping=None, context=self , target_language= None, default=unValueString)                       
                    if aTranslation:
                        unValueString = aTranslation
                else:
                    aTranslation = aTranslationService.utranslate( 'ModelDDvlPlone', 'ModelDDvlPlone_False', mapping=None, context=self , target_language= None, default=unValueString)                       
                    if aTranslation:
                        unValueString = aTranslation
                        
        elif unElementFieldType == 'integer':
            unValueString  = str( unValue)
            
        elif unElementFieldType == 'float':
            unValueString  = str( unValue)

        elif unElementFieldType == 'fixedpoint':
            unValueString  = str( unValue)

        elif unElementFieldType == 'datetime':
            unValueString  = str( unValue)
        
        else:
            unValueString  = str( unValue)
    
        return unValueString
    


    
    security.declarePrivate( 'fBoolFV')
    def fBoolFV( self, theAttributeName, theBoolValueToDisplay=None, theSeparatorBefore='', theSeparatorAfter=''):

        unElementSchema = self.schema        
        if not( unElementSchema.has_key( theAttributeName)):
            return ''
        
        unElementField  = unElementSchema[ theAttributeName]
        if not unElementField:
            return ''
        
        if not ( unElementField.type == 'boolean'):
            return ''
        
        unRawValue = None
        try:
            unRawValue = unElementField.getRaw( self)
        except:
            return ''
                
        unBoolValue = unRawValue == True
        
        if not( theBoolValueToDisplay == None or ( theBoolValueToDisplay == unBoolValue)):
            return ''
                 
        aTranslationService = self.translation_service        
                 
        aTrueTranslation    = aTranslationService.utranslate( 'ModelDDvlPlone',  'ModelDDvlPlone_True' ,                        mapping=None, context=self , target_language= None, default=u'True')                       
        aFalseTranslation   = aTranslationService.utranslate( 'ModelDDvlPlone',  'ModelDDvlPlone_False',                        mapping=None, context=self , target_language= None, default=u'False')                       
        aEsTranslation      = aTranslationService.utranslate( 'ModelDDvlPlone',  'ModelDDvlPlone_prefijoAttributoBoolean_es',   mapping=None, context=self , target_language= None, default=u'Es')                       
        aNoEsTranslation    = aTranslationService.utranslate( 'ModelDDvlPlone',  'ModelDDvlPlone_prefijoAttributoBoolean_noes', mapping=None, context=self , target_language= None, default=u'No es')                       
        

        unTranslatedValue = str( unBoolValue)
                            
        if unBoolValue:
            unTranslatedValue = aTrueTranslation
        else:
            unTranslatedValue = aFalseTranslation

        unI18NDomain = self.getNombreProyecto()
        unaLabelMsgId = ''
        try:
            unaLabelMsgId = unElementField.widget.label_msgid
        except:
            None            

        unTranslatedLabel = ''
        if unaLabelMsgId:     
            unTranslatedLabel = aTranslationService.utranslate( unI18NDomain,  unaLabelMsgId, mapping=None, context=self , target_language= None, default=unaLabelMsgId)                       
 
        if unTranslatedLabel.startswith( aEsTranslation):
            if unBoolValue:
                unTranslatedLabelAndValue = unTranslatedLabel            
            else:
                unBareLabel = unTranslatedLabel[ len( aEsTranslation):].strip()
                unTranslatedLabelAndValue = u'%s %s' % ( aNoEsTranslation, unBareLabel)                        
        else:                                   
            unTranslatedLabelAndValue = u'%s %s' % ( unTranslatedLabel, unTranslatedValue)
                             
        aUnicodeTranslatedLabelAndValue= aTranslationService.asunicodetype( unTranslatedLabelAndValue, errors="ignore")            
                            
        if aUnicodeTranslatedLabelAndValue:
            aUnicodeSeparatorBefore = aTranslationService.asunicodetype( theSeparatorBefore, errors="ignore")            
            aUnicodeSeparatorAfter = aTranslationService.asunicodetype( theSeparatorAfter, errors="ignore")            

            aUnicodeTranslatedLabelAndValue = aUnicodeSeparatorBefore + aUnicodeTranslatedLabelAndValue + aUnicodeSeparatorAfter 
                    
         
        return aUnicodeTranslatedLabelAndValue               
               
        

    
    

     
    security.declarePrivate( 'fTrTFLVs')
    def fTrTFLVs( self, theFieldNamesToTraverse, theFieldNamesToGet):

        if not theFieldNamesToTraverse:
            return self.fTFLVs( theFieldNamesToGet)
        
        unSonMulti = False
        unosElementosPasoAnterior = [ self]
        unosElementosNuevoPaso = [ ]
        for unFieldNameToTraverse in theFieldNamesToTraverse:
            for unElementoAnterior in unosElementosPasoAnterior:
                unSchema = unElementoAnterior.schema
                if unSchema.has_key( unFieldNameToTraverse):
                    unField     = unSchema[ unFieldNameToTraverse]
                    
                    unEsMulti   = unField.multiValued
                    unAccesor   = unField.getAccessor( unElementoAnterior)
                    unValue     = unAccesor( )
                    if unEsMulti:
                        unSonMulti = True
                        if unValue:
                            unosElementosNuevoPaso += unValue
                    else:
                        if unValue:
                            unosElementosNuevoPaso.append( unValue)
                                
            unosElementosPasoAnterior = unosElementosNuevoPaso
        
        if not unosElementosPasoAnterior:
            return []
            
        unResult = ', '.join( [ unElemento.fTFLVs( theFieldNamesToGet) for unElemento in unosElementosPasoAnterior ])
        
        return unResult
    
    
    
    
    

     
# ###########################################
#  Character set methods
#

    security.declarePrivate( 'fAsUnicode')
    def fAsUnicode( self, theString):
        if not theString:
            return u''

        aTranslationService = None
        try:
            aTranslationService = self.translation_service
        except:
            None
            
         
        if not aTranslationService:
            return u'' + theString
        
        aUnicodeString = aTranslationService.asunicodetype( theString, errors="ignore")            
        if not aUnicodeString:
            return theString
        
        return aUnicodeString
    
    
    

   
# ###########################################
#  Internationalisation methods
#


   


    security.declarePublic( 'fTranslateI18NManyIntoDict')
    def fTranslateI18NManyIntoDict( self, 
        theI18NDomainsStringsAndDefaults, 
        theResultDict                   =None):
        """Internationalization: build or update a dictionaty with the translations of all requested strings from the specified domain into the language preferred by the connected user, or return the supplied default.
        
        """
        
        unResultDict = theResultDict
        if ( unResultDict == None):
            unResultDict = { }
                
        if not theI18NDomainsStringsAndDefaults:
            return unResultDict
        
        aTranslationService = getToolByName( self, 'translation_service', None)
        if not aTranslationService:
            return unResultDict
        
        for aDomainStringsAndDefaults in theI18NDomainsStringsAndDefaults:
            aI18NDomain             = aDomainStringsAndDefaults[ 0] or cI18NDomainDefault
            unasStringsAndDefaults  = aDomainStringsAndDefaults[ 1]
            
            for unaStringAndDefault in unasStringsAndDefaults:
                unaString = unaStringAndDefault[ 0]
                unDefault = unaStringAndDefault[ 1]
                if unaString:
                    aTranslation = u''
                    if aTranslationService:
                        aTranslation = aTranslationService.utranslate( aI18NDomain, unaString, mapping=None, context=self , target_language= None, default=unDefault)            
                    if not aTranslation:
                        aTranslation = self.fAsUnicode( unDefault)
                    unResultDict[ unaString] = aTranslation
                        
        return unResultDict
            

    security.declarePrivate( 'fTranslationI18NDomain')
    def fTranslationI18NDomain( self, theI18NDomain):

        aI18NDomain = theI18NDomain
        if not aI18NDomain:
            try:
                aI18NDomain = self.getNombreProyecto()
            except:
                None
            if not aI18NDomain:
                aI18NDomain = 'ModelDDvlPlone'
                
        if not aI18NDomain:
            aI18NDomain = "plone"
            
        return aI18NDomain



    security.declarePrivate( 'fTranslateI18N')
    def fTranslateI18N( self, theI18NDomain, theString, theDefault, theTranslationService=None):
        if not theString:
            return u''

        aI18NDomain = self.fTranslationI18NDomain( theI18NDomain)
        if not aI18NDomain:
            return unicode( theDefault)
        
        
        aTranslationService = theTranslationService
        if not aTranslationService:
            aTranslationService = getToolByName( self, 'translation_service', None)
        
             
        aTranslation = unicode( theDefault)
        
        if aTranslationService:
            aTranslation = aTranslationService.utranslate( aI18NDomain, theString, mapping=None, context=self , target_language= None, default=theDefault)                       
            if not aTranslation:
                aTranslation = unicode( theDefault)

        if not aTranslation:
            aTranslation = unicode( theString)

        return aTranslation

    
    

      
      
    security.declarePrivate( 'getTransBool')
    def getTransBool( self, theFieldName, theValueToShow=None, theSeparatorToAdd=''):

        if not theFieldName:
            return ''
            
        unAttributeMetaAndValue= self.getAttributeMetaAndValue( theFieldName)
        if not unAttributeMetaAndValue:
            return ''
            
        unValue             = unAttributeMetaAndValue[ 1]
        unType              = unAttributeMetaAndValue[ 6]
        unTranslatedLabel   = unAttributeMetaAndValue[ 8]
        if not unType == 'boolean':
            return str( unValue)
           
        unString = ''    
        if (theValueToShow == None) or (theValueToShow == unValue):
            if unValue == True:
                unString = unTranslatedLabel + theSeparatorToAdd
            else:
                unString = self.fTranslateI18N( 'ModelDDvlPlone', 'ModelDDvlPlone_predicado_No', 'No') + ' ' + unTranslatedLabel + theSeparatorToAdd
        
        return unString       
      
 
    
    

         
 
 

    security.declarePrivate( 'fRecurseCollectingReferences')
    def fRecurseCollectingReferences( self, theFieldNameToRecurse, theReferenceFieldNameToGet, theExcludeInitial=True):

        if not theFieldNameToRecurse or not theReferenceFieldNameToGet:
            return [ ]
        
        todosElementosReferenciados = [ ]
        someAlreadyTraversed = [ self]
        
        unosElementosRecurrentes = self.fFOV( theFieldNameToRecurse)
        if unosElementosRecurrentes:
            for unElementoRecurrente in unosElementosRecurrentes:
                unElementoRecurrente.pRecurseCollectingReferencesInto( theFieldNameToRecurse, theReferenceFieldNameToGet, todosElementosReferenciados, someAlreadyTraversed)
        
        if not theExcludeInitial:
            unosElementosReferenciados = self.fFOV( theReferenceFieldNameToGet)
            if unosElementosReferenciados:
                for unElemento in unosElementosReferenciados:
                    if not ( unElemento in todosElementosReferenciados):
                        todosElementosReferenciados.append( unElemento)

        return todosElementosReferenciados





    security.declarePrivate( 'pRecurseCollectingReferencesInto')
    def pRecurseCollectingReferencesInto( self, theFieldNameToRecurse, theReferenceFieldNameToGet, theElementosReferenciados, theAlreadyTraversed):

        if not theFieldNameToRecurse or not theReferenceFieldNameToGet:
            return
            
        if self in theAlreadyTraversed:
            return 
           
        theAlreadyTraversed.append( self)
            
        unosElementosRecurrentes = self.fFOV( theFieldNameToRecurse)
        if unosElementosRecurrentes:
            for unElementoRecurrente in unosElementosRecurrentes:
                unElementoRecurrente.pRecurseCollectingReferencesInto( theFieldNameToRecurse, theReferenceFieldNameToGet, theElementosReferenciados, theAlreadyTraversed)
        
        unosElementosReferenciados = self.fFOV( theReferenceFieldNameToGet)
        if unosElementosReferenciados:
            for unElemento in unosElementosReferenciados:
                if not ( unElemento in theElementosReferenciados):
                    theElementosReferenciados.append( unElemento)
        
        return self






    security.declarePrivate( 'fRecurseCollect')
    def fRecurseCollect( self, theFieldNameToRecurse, theExcludeInitial=True):

        if not theFieldNameToRecurse:
            return [ ]
        
        todosElementos = [ ]

        if not theExcludeInitial:
            todosElementos.append( self)
        
        unosElementosRecurrentes = self.fFOV( theFieldNameToRecurse)
        if unosElementosRecurrentes:
            for unElementoRecurrente in unosElementosRecurrentes:
                unElementoRecurrente.pRecurseCollectInto( theFieldNameToRecurse, todosElementos)
        
        return todosElementos




    security.declarePrivate( 'pRecurseCollectInto')
    def pRecurseCollectInto( self, theFieldNameToRecurse, theElementosReferenciados):
        if not theFieldNameToRecurse:
            return
        
        if self in theElementosReferenciados:
            return
            
        theElementosReferenciados.append( self)
        
        unosElementosRecurrentes = self.fFOV( theFieldNameToRecurse)
        if unosElementosRecurrentes:
            for unElementoRecurrente in unosElementosRecurrentes:
                unElementoRecurrente.pRecurseCollectInto( theFieldNameToRecurse, theElementosReferenciados)
        
        return self

    
    
    

    security.declarePrivate('pHandle_manage_afterAdd')
    def pHandle_manage_afterAdd(self, theItem, theContainer):   
        
        OrderedBaseFolder.manage_afterAdd(  self, theItem, theContainer)
        
        self.fInitializeElement( theItem, theContainer)

        return self
    
    
    
             
    security.declarePrivate(   'pSetElementPermissions')
    def pSetElementPermissions(self, theElement):     
        if ( theElement == None):
            return self

        somePermissionsAndRoles = [ 
            [ [ permissions.View, ],                [ 'Manager', 'Owner', 'Reviewer', ], ],
            [ [ perm_AccessContentsInformation, ],  [ 'Manager', 'Owner', 'Reviewer', ], ],
            [ [ permissions.ListFolderContents, ],  [ 'Manager', 'Owner', 'Reviewer', ], ],
            [ [ permissions.ModifyPortalContent, ], [ 'Manager', 'Owner', ], ],
            [ [ permissions.AddPortalContent, ],    [ 'Manager', 'Owner', ], ],
            [ [ permissions.AddPortalFolders, ],    [ 'Manager', 'Owner', ], ],
            [ [ permissions.DeleteObjects, ],       [ 'Manager', 'Owner', ], ],
            
        ]
        
        for aPermissionsAndRoles in somePermissionsAndRoles:
            somePermissions = aPermissionsAndRoles[ 0]
            for unaPermission in somePermissions:
                if unaPermission:
                    unosRoles = aPermissionsAndRoles[ 1]
                    if unosRoles:
                        theElement.manage_permission( unaPermission, roles=unosRoles, acquire=1)
                    
        return self   
    
    
    
    
    
    security.declarePrivate(   'fInitializeElement')
    def fInitializeElement( self, theItem, theContainer):
        
        if theItem == None:
            return theItem
        
        
        # ACV 20100614 The Title is not empty only at the (third?) invocation by the zope/plone event machinery from events received when creating a new root element from the plone 'add item' action.
        # The Title is never not empty during invocations of this method  when creating elements with ModelDDvlPloneTool.fCrearElementoDeTipo(), which takes the responsibility of setting element permissions and creating aggregated collections.
        # The title is not empty on events delivered after completing (and unwind of ModelDDvlPloneTool.fCrearElementoDeTipo
        
        if not self.Title(): # 'portal_factory' in self.getPhysicalPath(): 
            return theItem
        
        

        self.pSetElementPermissions( self)
        
        unModelDDvlPloneTool = self.fModelDDvlPloneTool()
        if not unModelDDvlPloneTool:
            return theItem
        
            
        unResultadoNuevoElemento = unModelDDvlPloneTool.fRetrieveTypeConfig( 
            theTimeProfilingResults     =None,
            theElement                  =self, 
            theParent                   =None,
            theParentTraversalName      ='',
            theTypeConfig               =None, 
            theAllTypeConfigs           =None, 
            theViewName                 ='', 
            theRetrievalExtents         =[ 'traversals', ],
            theWritePermissions         =[ 'object', 'attrs', 'aggregations', ],
            theFeatureFilters           ={ 'relations': [], }, 
            theInstanceFilters          =None,
            theTranslationsCaches       =None,
            theCheckedPermissionsCache  =None,
            theAdditionalParams         =None,
        )
        if not unResultadoNuevoElemento:
            return theItem     
        
        for unaTraversalResult in unResultadoNuevoElemento.get( 'traversals', []):
            if ( unaTraversalResult[ 'traversal_kind'] == 'aggregation') and  unaTraversalResult[ 'contains_collections']:
                if not unaTraversalResult[ 'elements']:
                    if unaTraversalResult[ 'factories']:
                        unaFactoryAndTranslations = unaTraversalResult[ 'factories'][ 0]
                        if unaFactoryAndTranslations:
                            unTypeName = unaFactoryAndTranslations[ 'meta_type']
                            if unTypeName:
                                unNewTitle = unaFactoryAndTranslations[ 'type_translations'][ 'archetype_name']
                                unNewCollectionCreateResult = unModelDDvlPloneTool.fCrearElementoDeTipo( 
                                    theTimeProfilingResults =None,
                                    theContainerElement     =self, 
                                    theTypeName             =unTypeName, 
                                    theId                   =None,
                                    theTitle                =unNewTitle, 
                                    theDescription          ='',
                                    theAdditionalParams     =None,
                                    theAllowFactoryMethods  = False,
                                )  
                                
                                if ( not unNewCollectionCreateResult) or not ( unNewCollectionCreateResult[ 'effect'] == 'created'):
                                    pass

    
        return theItem
    
    

    
    
    
    
    


   
    security.declarePrivate( 'fModelDDvlPloneTool')
    def fModelDDvlPloneTool( self,):
        """Retrieve the singleton instance of ModelDDvlPloneTool.
        
        """
        try:


            aModelDDvlPloneTool = getToolByName( self, cModelDDvlPloneToolId, None)
            if aModelDDvlPloneTool == None:
                return None
            
            return aModelDDvlPloneTool
        
        
        except:
            unaExceptionInfo = sys.exc_info()
            unaExceptionFormattedTraceback = ''.join(traceback.format_exception( *unaExceptionInfo))
            
            unInformeExcepcion = 'Exception during access operation fModelDDvlPloneTool on element'
            try:
                unInformeExcepcion += 'of type %s\n' % self.meta_type
            except:
                None
            try:
                unInformeExcepcion += 'exception class %s\n' % unaExceptionInfo[1].__class__.__name__ 
            except:
                None
            try:
                unInformeExcepcion += 'exception message %s\n\n' % str( unaExceptionInfo[1].args)
            except:
                None
                
            unInformeExcepcion += unaExceptionFormattedTraceback   
                     
     
            if cLogExceptions:
                logging.getLogger( 'gvSIGbpd').error( unInformeExcepcion)
    
            return None
             

        
        
    security.declarePrivate( 'fVerifyOrInitialize_ModelDDvlPlone')
    def fVerifyOrInitialize_ModelDDvlPlone( self, theAllowInitialization=False, ):
        """Delegate on framework verification or initializacion.
       
        """

        from Products.ModelDDvlPloneTool.ModelDDvlPloneTool_Inicializacion import ModelDDvlPloneTool_Inicializacion

        unInforme = ModelDDvlPloneTool_Inicializacion().fVerifyOrInitialize_ModelDDvlPloneFramework( 
            theContextualElement     =self, 
            theAllowInitialization   =theAllowInitialization,
        )
             
        return unInforme  
                        
        
        
    security.declarePrivate( 'pHandle_manage_pasteObjects')        
    def pHandle_manage_pasteObjects(self, cb_copy_data=None, REQUEST=None):
        """Trap and override behavior of manage_pasteObjects implementation in CopySupport.py 
        
        """
        
        # Get the list of objects to be copied into this (self) container
        # Copied from class CopyContainer in file Zope lib python OFS  CopySupport.py
        if cb_copy_data is not None:
            cp = cb_copy_data
        elif REQUEST is not None and REQUEST.has_key('__cp'):
            cp = REQUEST['__cp']
        else:
            cp = None
        if cp is None:
            return CopyContainer.manage_objectPaste( self, cb_copy_data, REQUEST)
             
        try:
            op, mdatas = loads(decompress(unquote(cp))) # _cb_decode(cp)
        except:
            return CopyContainer.manage_objectPaste( self, cb_copy_data, REQUEST)

    
        oblist = []
        app = self.getPhysicalRoot()
        for mdata in mdatas:
            m = Moniker.loadMoniker(mdata)
            try:
                ob = m.bind(app)
            except:
                return CopyContainer.manage_objectPaste( self, cb_copy_data, REQUEST)
            # Do not verify here
            # self._verifyObjectPaste(ob, validate_src=op+1)
            oblist.append(ob)
        # End of code copied from class CopyContainer
            
        someObjectsToPaste = oblist[:]
        
        if not someObjectsToPaste:
            return CopyContainer.manage_objectPaste( self, cb_copy_data, REQUEST)
        
        someAwareObjects = []
        for anObjectToPaste in someObjectsToPaste:
            anExportConfig = None
            try:
                anExportConfig = anObjectToPaste.exportConfig()
            except:
                None
            if anExportConfig:
                someAwareObjects.append( anObjectToPaste)
                
        # ACV 20090929 Shall paste even standard plone elements (non ModelDDvlPloneTool aware elements)
        #
        #if not someAwareObjects:
            #return CopyContainer.manage_objectPaste( self, cb_copy_data, REQUEST)
        
        
        aRequest = REQUEST
        if not aRequest:
            try:
                aRequest = self.REQUEST
            except:
                None
        if not aRequest:
            """Default to Plone behavior.
            
            """
            return CopyContainer.manage_pasteObjects( self, cb_copy_data, REQUEST)
        
        
        unModelDDvlPloneTool = self.fModelDDvlPloneTool()
        if not unModelDDvlPloneTool:
            return CopyContainer.manage_pasteObjects( self, cb_copy_data, REQUEST)
        
        unIsMoveOperation = op == 1
        
        unPasteResult =  unModelDDvlPloneTool.fPaste( 
            theTimeProfilingResults     =None,
            theContainerObject          =self, 
            theObjectsToPaste           =someObjectsToPaste,
            theIsMoveOperation          =unIsMoveOperation,
            theAdditionalParams         =None,
        )
        
        
        unSuccess = False
        if not unPasteResult:
            unPortalStatusMsg = self.fTranslateI18N( 'ModelDDvlPlone', cError_During_Paste, cError_During_Paste + '-')
        else:
            unSuccess = unPasteResult.get( 'success', False)
            if not unSuccess:
                unPortalStatusMsg = ('%s %s%s %s%s %s%s #Total pasted=%d #MDD pasted=%d #Plone pasted=%d %s%s') % ( 
                    self.fTranslateI18N( 'ModelDDvlPlone', cError_During_Paste, cError_During_Paste + '-'),
                    
                    ( unPasteResult.get( 'status', '') and self.fTranslateI18N( 'ModelDDvlPlone', 'status', 'status-')) or u'',
                    self.fAsUnicode( unPasteResult.get( 'status', '')),
                    
                    ( unPasteResult.get( 'condition', '') and self.fTranslateI18N( 'ModelDDvlPlone', 'condition', 'condition-')) or u'',
                    self.fAsUnicode( unPasteResult.get( 'condition', '')),
                    
                    ( unPasteResult.get( 'exception', '') and self.fTranslateI18N( 'ModelDDvlPlone', 'exception', 'exception-')) or u'',
                    self.fAsUnicode( unPasteResult.get( 'exception', '')),
                    
                    unPasteResult.get( 'num_elements_pasted',       0),
                    unPasteResult.get( 'num_mdd_elements_pasted',   0),
                    unPasteResult.get( 'num_plone_elements_pasted', 0),

                    ( unPasteResult.get( 'error_reports', '') and self.fTranslateI18N( 'ModelDDvlPlone', 'error_reports', 'error_reports-')) or u'',
                    self.fAsUnicode( self.fModelDDvlPloneTool().fPrettyPrint( unPasteResult.get( 'error_reports', []))),
                )
            else:
                unPortalStatusMsg = ('#Total pasted=%d #MDD pasted=%d #Plone pasted=%d %s%s') % ( 
                    unPasteResult.get( 'num_elements_pasted',       0),
                    unPasteResult.get( 'num_mdd_elements_pasted',   0),
                    unPasteResult.get( 'num_plone_elements_pasted', 0),

                    ( unPasteResult.get( 'error_reports', '') and self.fTranslateI18N( 'ModelDDvlPlone', 'error_reports', 'error_reports-')) or u'',
                    self.fAsUnicode( self.fModelDDvlPloneTool().fPrettyPrint( unPasteResult.get( 'error_reports', []))),
                )
                
                
            return REQUEST.RESPONSE.redirect(  '%s/Tabular?portal_status_message=%s' % ( self.absolute_url() + unPortalStatusMsg))
                   

        # return CopyContainer.manage_pasteObjects( self, cb_copy_data, REQUEST)
        # aRequest.response.redirect( '%s/MDDpaste' % self.absolute_url())
        
        
        
       
         
    # From CopySupport.py   
    # class CopyContainer
    #def manage_pasteObjects(self, cb_copy_data=None, REQUEST=None):
        #"""Paste previously copied objects into the current object.

        #If calling manage_pasteObjects from python code, pass the result of a
        #previous call to manage_cutObjects or manage_copyObjects as the first
        #argument.

        #Also sends IObjectCopiedEvent and IObjectClonedEvent
        #or IObjectWillBeMovedEvent and IObjectMovedEvent.
        #"""
        #if cb_copy_data is not None:
            #cp = cb_copy_data
        #elif REQUEST is not None and REQUEST.has_key('__cp'):
            #cp = REQUEST['__cp']
        #else:
            #cp = None
        #if cp is None:
            #raise CopyError, eNoData

        #try:
            #op, mdatas = _cb_decode(cp)
        #except:
            #raise CopyError, eInvalid

        #oblist = []
        #app = self.getPhysicalRoot()
        #for mdata in mdatas:
            #m = Moniker.loadMoniker(mdata)
            #try:
                #ob = m.bind(app)
            #except ConflictError:
                #raise
            #except:
                #raise CopyError, eNotFound
            #self._verifyObjectPaste(ob, validate_src=op+1)
            #oblist.append(ob)

        #result = []
        #if op == 0:
            ## Copy operation
            #for ob in oblist:
                #orig_id = ob.getId()
                #if not ob.cb_isCopyable():
                    #raise CopyError, eNotSupported % escape(orig_id)

                #try:
                    #ob._notifyOfCopyTo(self, op=0)
                #except ConflictError:
                    #raise
                #except:
                    #raise CopyError, MessageDialog(
                        #title="Copy Error",
                        #message=sys.exc_info()[1],
                        #action='manage_main')

                #id = self._get_id(orig_id)
                #result.append({'id': orig_id, 'new_id': id})

                #orig_ob = ob
                #ob = ob._getCopy(self)
                #ob._setId(id)
                #notify(ObjectCopiedEvent(ob, orig_ob))

                #self._setObject(id, ob)
                #ob = self._getOb(id)
                #ob.wl_clearLocks()

                #ob._postCopy(self, op=0)

                #OFS.subscribers.compatibilityCall('manage_afterClone', ob, ob)

                #notify(ObjectClonedEvent(ob))

            #if REQUEST is not None:
                #return self.manage_main(self, REQUEST, update_menu=1,
                                        #cb_dataValid=1)

        #elif op == 1:
            ## Move operation
            #for ob in oblist:
                #orig_id = ob.getId()
                #if not ob.cb_isMoveable():
                    #raise CopyError, eNotSupported % escape(orig_id)

                #try:
                    #ob._notifyOfCopyTo(self, op=1)
                #except ConflictError:
                    #raise
                #except:
                    #raise CopyError, MessageDialog(
                        #title="Move Error",
                        #message=sys.exc_info()[1],
                        #action='manage_main')

                #if not sanity_check(self, ob):
                    #raise CopyError, "This object cannot be pasted into itself"

                #orig_container = aq_parent(aq_inner(ob))
                #if aq_base(orig_container) is aq_base(self):
                    #id = orig_id
                #else:
                    #id = self._get_id(orig_id)
                #result.append({'id': orig_id, 'new_id': id})

                #notify(ObjectWillBeMovedEvent(ob, orig_container, orig_id,
                                              #self, id))

                ## try to make ownership explicit so that it gets carried
                ## along to the new location if needed.
                #ob.manage_changeOwnershipType(explicit=1)

                #try:
                    #orig_container._delObject(orig_id, suppress_events=True)
                #except TypeError:
                    ## BBB: removed in Zope 2.11
                    #orig_container._delObject(orig_id)
                    #warnings.warn(
                        #"%s._delObject without suppress_events is deprecated "
                        #"and will be removed in Zope 2.11." %
                        #orig_container.__class__.__name__, DeprecationWarning)
                #ob = aq_base(ob)
                #ob._setId(id)

                #try:
                    #self._setObject(id, ob, set_owner=0, suppress_events=True)
                #except TypeError:
                    ## BBB: removed in Zope 2.11
                    #self._setObject(id, ob, set_owner=0)
                    #warnings.warn(
                        #"%s._setObject without suppress_events is deprecated "
                        #"and will be removed in Zope 2.11." %
                        #self.__class__.__name__, DeprecationWarning)
                #ob = self._getOb(id)

                #notify(ObjectMovedEvent(ob, orig_container, orig_id, self, id))
                #notifyContainerModified(orig_container)
                #if aq_base(orig_container) is not aq_base(self):
                    #notifyContainerModified(self)

                #ob._postCopy(self, op=1)
                ## try to make ownership implicit if possible
                #ob.manage_changeOwnershipType(explicit=0)

            #if REQUEST is not None:
                #REQUEST['RESPONSE'].setCookie('__cp', 'deleted',
                                    #path='%s' % cookie_path(REQUEST),
                                    #expires='Wed, 31-Dec-97 23:59:59 GMT')
                #REQUEST['__cp'] = None
                #return self.manage_main(self, REQUEST, update_menu=1,
                                        #cb_dataValid=0)

        #return result
             
    
    ##/code-section class-header

    # Methods

# end of class BPDElemento_Operaciones

##code-section module-footer #fill in your manual code here
##/code-section module-footer



