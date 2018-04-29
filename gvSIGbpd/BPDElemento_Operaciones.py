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

from Acquisition        import aq_inner, aq_parent



##code-section module-header #fill in your manual code here

       
  

import sys
import traceback
import logging


from Acquisition                    import aq_get

from Products.CMFCore               import permissions
from Products.CMFCore.utils         import getToolByName


from Products.ModelDDvlPloneTool.ModelDDvlPloneTool import cModelDDvlPloneToolName, ModelDDvlPloneTool


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

cLazyCreateModelDDvlPloneTool = True

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
    
    
 
    security.declarePrivate('fPortalRoot')
    def fPortalRoot(self):
        aPortalTool = getToolByName( self, 'portal_url')
        unPortal = aPortalTool.getPortalObject()
        return unPortal       
    
    
        
        

    
# #############################################################
# Owner accessors
# 



    security.declarePrivate('getRaiz')
    def getRaiz(self):
        if self.getEsRaiz():
            return self            
        unContenedor =  aq_parent( aq_inner( self))
        
        if not unContenedor:
            return None
        
        return unContenedor.getRaiz()





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
    
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    security.declarePrivate('pHandle_manage_afterAdd')
    def pHandle_manage_afterAdd(self, theItem, theContainer):   
        
        OrderedBaseFolder.manage_afterAdd(  self, theItem, theContainer)
        
        self.fLazyCrear( theItem, theContainer)

        return self
    
             
    security.declarePrivate(   'pSetElementPermissions')
    def pSetElementPermissions(self, theElement):     
        if not theElement:
            return self

        somePermissionsAndRoles = [ 
            [ [ permissions.View, ],                [ 'Manager', 'Owner', 'Reviewer', ], ],
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
    
    
    security.declarePrivate(   'fLazyCrear')
    def fLazyCrear( self, theItem, theContainer):
        
        if not theItem:
            return None
        
        
        if not self.Title(): # 'portal_factory' in self.getPhysicalPath(): 
            return None
        
        self.pSetElementPermissions( self)
        
        unModelDDvlPloneTool = self.fModelDDvlPloneTool( True)
        if not unModelDDvlPloneTool:
            return None
        
            
        unResultadoNuevoElemento = unModelDDvlPloneTool.fRetrieveTypeConfig( 
            theTimeProfilingResults     =None,
            theElement                  =theItem, 
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
            return None     
        
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
                                    theContainerElement     =theItem, 
                                    theTypeName             =unTypeName, 
                                    theTitle                =unNewTitle, 
                                    theDescription          ='',
                                    theAdditionalParams     =None,
                                    theAllowFactoryMethods  = False,
                                )  
                                
                                if (not unNewCollectionCreateResult) or not ( unNewCollectionCreateResult[ 'effect'] == 'created'):
                                    None

    
        return theItem
    
    

    
    
    
    
    


   
    security.declarePrivate( 'fModelDDvlPloneTool')
    def fModelDDvlPloneTool( self, theAllowCreation=False):
        """Retrieve or create an instance of ModelDDvlPloneTool.
        
        """
        try:
    
            unPortalRoot = self.fPortalRoot()
            if not unPortalRoot:
                return None
            
            aModelDDvlPloneTool = None
            try:
                aModelDDvlPloneTool = aq_get( unPortalRoot, cModelDDvlPloneToolName, None, 1)
            except:
                None  
            if aModelDDvlPloneTool:
                return aModelDDvlPloneTool
            
            if not ( theAllowCreation and cLazyCreateModelDDvlPloneTool):
                return None
     
            
            unaNuevaTool = ModelDDvlPloneTool( ) 
            unPortalRoot._setObject( cModelDDvlPloneToolName,  unaNuevaTool)
            aModelDDvlPloneTool = None
            try:
                aModelDDvlPloneTool = aq_get( unPortalRoot, cModelDDvlPloneToolName, None, 1)
            except:
                None  
            if not aModelDDvlPloneTool:
                return None
                        
            return aModelDDvlPloneTool
        
        except:
            unaExceptionInfo = sys.exc_info()
            unaExceptionFormattedTraceback = ''.join(traceback.format_exception( *unaExceptionInfo))
            
            unInformeExcepcion = 'Exception during Lazy Initialization operation fModelDDvlPloneTool\n' 
            unInformeExcepcion += 'exception class %s\n' % unaExceptionInfo[1].__class__.__name__ 
            unInformeExcepcion += 'exception message %s\n\n' % str( unaExceptionInfo[1].args)
            unInformeExcepcion += unaExceptionFormattedTraceback   
                     
     
            if cLogExceptions:
                logging.getLogger( 'gvSIGbpd').error( unInformeExcepcion)
    
            return None
             

        
        
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
                
        if not someAwareObjects:
            return CopyContainer.manage_objectPaste( self, cb_copy_data, REQUEST)
        
        
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
        
        
        unModelDDvlPloneTool = self.fModelDDvlPloneTool( True)
        if not unModelDDvlPloneTool:
            return CopyContainer.manage_pasteObjects( self, cb_copy_data, REQUEST)
        
        return unModelDDvlPloneTool.fPaste( 
            theTimeProfilingResults     =None,
            theContainerObject          =self, 
            theObjectsToPaste           =someObjectsToPaste,
            theAdditionalParams         =None,
        )
    
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



