# -*- coding: utf-8 -*-
#
# File: BPDElemento_Operaciones.py
#
# Copyright (c) 2008 by Conselleria de Infraestructuras y Transporte de la
# Generalidad Valenciana
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

__author__ = """Antonio Carrasco Valero (Model Driven Development sl) <gvSIGbpd@gvSIG.org>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.gvSIGbpd.config import *

from Acquisition        import aq_inner, aq_parent



##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDElemento_Operaciones_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDElemento_Operaciones:
    """
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'BPDElemento_Operaciones'

    meta_type = 'BPDElemento_Operaciones'
    portal_type = 'BPDElemento_Operaciones'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'BPDElemento_Operaciones.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "BPDElemento_Operaciones"
    typeDescMsgId = 'description_edit_bpdelemento_operaciones'
    archetype_name2 = ''
    typeDescription2 = ''''''
    archetype_name_msgid = 'gvSIGbpd_BPDElemento_Operaciones_label'
    typeDescription_msgid = 'gvSIGbpd_BPDElemento_Operaciones_help'

    _at_rename_after_creation = True

    schema = BPDElemento_Operaciones_schema

    ##code-section class-header #fill in your manual code here
    
    
 
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
       
        unPathString = '/'.join( unRaiz.getPhysicalPath( ))
        return unPathString
        
    #security.declarePrivate('fPathDelRaiz')
    #def fPathDelRaiz(self):
        #unRaiz = self.getRaiz()
        #if not unRaiz:
            #return ''
       
        #unPathString = self.fPhysicalPathString( unRaiz)
        #return unPathString




    security.declarePrivate('fPhysicalPathString')
    def fPhysicalPathString(self, theElemento):
        if not theElemento:
            return ''
        
        unPhysicalPath = theElemento.getPhysicalPath()
        if not unPhysicalPath:
            return ''
     
        if unPhysicalPath[ 0] == '':
            unPhysicalPath = unPhysicalPath[1:]
        
        unFoldersPath = unPhysicalPath[1:]
        unPathString = '/' + '/'.join( unFoldersPath)
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
    
     
    
    ##/code-section class-header

    # Methods

# end of class BPDElemento_Operaciones

##code-section module-footer #fill in your manual code here
##/code-section module-footer



