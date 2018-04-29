# -*- coding: utf-8 -*-
#
# File: BPDElemento.py
#
# Copyright (c) 2009 by Conselleria de Infraestructuras y Transporte de la
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

__author__ = """Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana
<gvSIGbpd@gvSIG.org>, Model Driven Development sl <gvSIGbpd@ModelDD.org>,
Antonio Carrasco Valero <carrasco@ModelDD.org>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.gvSIGbpd.BPDElemento_CopyConfig import BPDElemento_CopyConfig
from Products.gvSIGbpd.BPDElemento_Meta import BPDElemento_Meta
from Products.gvSIGbpd.BPDElemento_ExportConfig import BPDElemento_ExportConfig
from Products.gvSIGbpd.BPDElemento_MappingConfig import BPDElemento_MappingConfig
from Products.gvSIGbpd.BPDElemento_TraversalConfig import BPDElemento_TraversalConfig
from Products.gvSIGbpd.BPDElemento_Operaciones import BPDElemento_Operaciones
from Products.ATContentTypes.content.base import ATCTMixin
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.CMFCore.utils  import getToolByName
from Products.CMFCore.utils import getToolByName
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Acquisition  import aq_inner, aq_parent

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    RelationField(
        name='siguientesVersiones',
        inverse_relation_label="Version Anterior",
        inverse_relation_description="Version predecesora a la actual de este elemento",
        description="Versiones posteriores del Elemento",
        relationship='SiguientesVersiones',
        label2="Next Versions",
        widget=ReferenceBrowserWidget(
            label="Siguientes Versiones",
            label2="Next Versions",
            description="Versiones posteriores del Elemento",
            description2="Versions after this element's version.",
            label_msgid='gvSIGbpd_BPDElemento_rel_siguientesVersiones_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_siguientesVersiones_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Versions after this element's version.",
        inverse_relation_label2="Previous Version",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='versionAnterior',
        inverse_relation_description2="Versions before this element's version.",
        label="Siguientes Versiones",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='VersionAnterior',
        owner_class_name="BPDElemento"
    ),

    RelationField(
        name='versionAnterior',
        inverse_relation_label="Siguientes Versiones",
        inverse_relation_description="Versiones posteriores del Elemento",
        description="Version predecesora a la actual de este elemento",
        relationship='VersionAnterior',
        label2="Previous Version",
        widget=ReferenceBrowserWidget(
            label="Version Anterior",
            label2="Previous Version",
            description="Version predecesora a la actual de este elemento",
            description2="Versions before this element's version.",
            label_msgid='gvSIGbpd_BPDElemento_rel_versionAnterior_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_versionAnterior_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Versions before this element's version.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Next Versions",
        dependency_supplier=True,
        inverse_relation_field_name='siguientesVersiones',
        inverse_relation_description2="Versions after this element's version.",
        write_permission='Modify portal content',
        label="Version Anterior",
        multiValued=0,
        containment="Unspecified",
        inverse_relationship='SiguientesVersiones'
    ),

    RelationField(
        name='elementosTraducidos',
        inverse_relation_label="Original de esta Traduccion",
        inverse_relation_description="El elemento original de esta traduccion a otro idioma.",
        description="Traducciones de este elemento a otros idiomas.",
        relationship='ElementosTraducidos',
        inverse_relation_field_name='originalDeTraduccion',
        inverse_relation_label2="Original of this translation",
        label2="Translated Elements",
        inverse_relation_description2="The original element of this translation into a different language.",
        widget=ReferenceBrowserWidget(
            label="Elementos Traducidos",
            label2="Translated Elements",
            description="Traducciones de este elemento a otros idiomas.",
            description2="Translations of this element into other languages.",
            label_msgid='gvSIGbpd_BPDElemento_rel_elementosTraducidos_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_elementosTraducidos_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Elementos Traducidos",
        description2="Translations of this element into other languages.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='OriginalDeTraduccion',
        owner_class_name="BPDElemento",
        dependency_supplier=True
    ),

    RelationField(
        name='originalDeTraduccion',
        inverse_relation_label="Elementos Traducidos",
        containment="Unspecified",
        inverse_relation_description="Traducciones de este elemento a otros idiomas.",
        description="El elemento original de esta traduccion a otro idioma.",
        relationship='OriginalDeTraduccion',
        inverse_relation_field_name='elementosTraducidos',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Original of this translation",
        inverse_relation_description2="Translations of this element into other languages.",
        widget=ReferenceBrowserWidget(
            label="Original de esta Traduccion",
            label2="Original of this translation",
            description="El elemento original de esta traduccion a otro idioma.",
            description2="The original element of this translation into a different language.",
            label_msgid='gvSIGbpd_BPDElemento_rel_originalDeTraduccion_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_originalDeTraduccion_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Original de esta Traduccion",
        description2="The original element of this translation into a different language.",
        multiValued=0,
        inverse_relation_label2="Translated Elements",
        inverse_relationship='ElementosTraducidos',
        write_permission='Modify portal content'
    ),

    RelationField(
        name='elementosDerivados',
        inverse_relation_label="Elementos Base",
        inverse_relation_description="Elementos a partir de los cuales se ha derivado el actual.",
        description="Elementos que han sido derivados a partir del actual.",
        relationship='ElementosDerivados',
        inverse_relation_field_name='elementosBase',
        inverse_relation_label2="Base Elements",
        label2="Derived Elements",
        inverse_relation_description2="Elements from whish this one has been derived.",
        widget=ReferenceBrowserWidget(
            label="Elementos Derivados",
            label2="Derived Elements",
            description="Elementos que han sido derivados a partir del actual.",
            description2="Elements that have been derived from this one.",
            label_msgid='gvSIGbpd_BPDElemento_rel_elementosDerivados_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_elementosDerivados_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Elementos Derivados",
        description2="Elements that have been derived from this one.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='ElementosBase',
        owner_class_name="BPDElemento",
        dependency_supplier=True
    ),

    RelationField(
        name='elementosBase',
        inverse_relation_label="Elementos Derivados",
        containment="Unspecified",
        inverse_relation_description="Elementos que han sido derivados a partir del actual.",
        description="Elementos a partir de los cuales se ha derivado el actual.",
        relationship='ElementosBase',
        inverse_relation_field_name='elementosDerivados',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Base Elements",
        inverse_relation_description2="Elements that have been derived from this one.",
        widget=ReferenceBrowserWidget(
            label="Elementos Base",
            label2="Base Elements",
            description="Elementos a partir de los cuales se ha derivado el actual.",
            description2="Elements from whish this one has been derived.",
            label_msgid='gvSIGbpd_BPDElemento_rel_elementosBase_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_elementosBase_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Elementos Base",
        description2="Elements from whish this one has been derived.",
        multiValued=1,
        inverse_relation_label2="Derived Elements",
        inverse_relationship='ElementosDerivados',
        write_permission='Modify portal content'
    ),

    RelationField(
        name='usosDelElemento',
        inverse_relation_label="Elemento Usado",
        inverse_relation_description="El elemento que se reutiliza en esta definicion.",
        description="Donde se usa el elemento como parte de otra definicion.",
        relationship='UsosDelElemento',
        inverse_relation_field_name='elementoUsado',
        inverse_relation_label2="Used Element",
        label2="Uses of the element",
        inverse_relation_description2="The element reustilised in this specification.",
        widget=ReferenceBrowserWidget(
            label="Usos del Elemento",
            label2="Uses of the element",
            description="Donde se usa el elemento como parte de otra definicion.",
            description2="Which elements use this one as part of their specification.",
            label_msgid='gvSIGbpd_BPDElemento_rel_usosDelElemento_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_usosDelElemento_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Usos del Elemento",
        description2="Which elements use this one as part of their specification.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='ElementoUsado',
        owner_class_name="BPDElemento",
        dependency_supplier=True
    ),

    RelationField(
        name='elementoUsado',
        inverse_relation_label="Usos del Elemento",
        containment="Unspecified",
        inverse_relation_description="Donde se usa el elemento como parte de otra definicion.",
        description="El elemento que se reutiliza en esta definicion.",
        relationship='ElementoUsado',
        inverse_relation_field_name='usosDelElemento',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Used Element",
        inverse_relation_description2="Which elements use this one as part of their specification.",
        widget=ReferenceBrowserWidget(
            label="Elemento Usado",
            label2="Used Element",
            description="El elemento que se reutiliza en esta definicion.",
            description2="The element reustilised in this specification.",
            label_msgid='gvSIGbpd_BPDElemento_rel_elementoUsado_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_elementoUsado_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Elemento Usado",
        description2="The element reustilised in this specification.",
        multiValued=0,
        inverse_relation_label2="Uses of the element",
        inverse_relationship='UsosDelElemento',
        write_permission='Modify portal content'
    ),

    ComputedField(
        name='archivos',
        widget=ComputedWidget(
            label="Ficheros",
            label2="Files",
            description="Elementos Plone convencionales conteniendo un Fichero de contenido arbitrario.",
            description2="Conventional Plone elements containing a File of arbitrary contents.",
            label_msgid='gvSIGbpd_BPDElemento_contents_archivos_label',
            description_msgid='gvSIGbpd_BPDElemento_contents_archivos_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Files',
        label='Ficheros',
        represents_aggregation=True,
        description2='Conventional Plone elements containing a File of arbitrary contents.',
        multiValued=1,
        owner_class_name="BPDElemento",
        expression="context.objectValues(['ATFile'])",
        computed_types=['ATFile'],
        non_framework_elements=True,
        description='Elementos Plone convencionales conteniendo un Fichero de contenido arbitrario.'
    ),

    StringField(
        name='codigoIdioma',
        widget=StringWidget(
            label="Codigo de Idioma",
            label2="Language Code",
            description="Codigo del idioma en que se ha creado el contenido del elemento.",
            description2="Code of the language used to edit the element contents.",
            label_msgid='gvSIGbpd_BPDElemento_attr_codigoIdioma_label',
            description_msgid='gvSIGbpd_BPDElemento_attr_codigoIdioma_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Codigo del idioma en que se ha creado el contenido del elemento.",
        duplicates="0",
        label2="Language Code",
        ea_localid="255",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Code of the language used to edit the element contents.",
        ea_guid="{B7601699-AE23-4127-B9B2-1E2A8D4C064B}",
        write_permission='Modify portal content',
        scale="0",
        label="Codigo de Idioma",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDElemento",
        exclude_from_views="[ 'Textual', 'Tabular',  ]",
        exclude_from_copyconfig="True"
    ),

    ComputedField(
        name='documentos',
        widget=ComputedWidget(
            label="Documentos",
            label2="Documents",
            description="Elementos del tipo documento convencional en Plone.",
            description2="Elements of the Plone Document type.",
            label_msgid='gvSIGbpd_BPDElemento_contents_documentos_label',
            description_msgid='gvSIGbpd_BPDElemento_contents_documentos_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Documents',
        label='Documentos',
        represents_aggregation=True,
        description2='Elements of the Plone Document type.',
        multiValued=1,
        owner_class_name="BPDElemento",
        expression="context.objectValues(['ATDocument'])",
        computed_types=['ATDocument'],
        non_framework_elements=True,
        description='Elementos del tipo documento convencional en Plone.'
    ),

    ComputedField(
        name='enlaces',
        widget=ComputedWidget(
            label="Enlace",
            label2="Link",
            description="Elementos Plone conteniendo una referencia a una pagina Web (URLs como http://www.gvSIG.org)",
            description2="Plone Elements containing a reference to a Web page (URLs like http://www.gvSIG.org)",
            label_msgid='gvSIGbpd_BPDElemento_contents_enlaces_label',
            description_msgid='gvSIGbpd_BPDElemento_contents_enlaces_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Link',
        label='Enlace',
        represents_aggregation=True,
        description2='Plone Elements containing a reference to a Web page (URLs like http://www.gvSIG.org)',
        multiValued=1,
        owner_class_name="BPDElemento",
        expression="context.objectValues(['ATLink'])",
        computed_types=['ATLink'],
        non_framework_elements=True,
        description='Elementos Plone conteniendo una referencia a una pagina Web (URLs como http://www.gvSIG.org)'
    ),

    ComputedField(
        name='imagenes',
        widget=ComputedWidget(
            label="Imagenes",
            label2="Images",
            description="Elementos Plone convencionales conteniendo una Imagen.",
            description2="Conventional Plone elements containing an Image.",
            label_msgid='gvSIGbpd_BPDElemento_contents_imagenes_label',
            description_msgid='gvSIGbpd_BPDElemento_contents_imagenes_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Images',
        label='Imagenes',
        represents_aggregation=True,
        description2='Conventional Plone elements containing an Image.',
        multiValued=1,
        owner_class_name="BPDElemento",
        expression="context.objectValues(['ATImage'])",
        computed_types=['ATImage'],
        non_framework_elements=True,
        description='Elementos Plone convencionales conteniendo una Imagen.'
    ),

    ComputedField(
        name='noticias',
        widget=ComputedWidget(
            label="Noticias",
            label2="News Items",
            description="Elementos de Plone conteniendo una Noticia.",
            description2="Conventional Plone elements containing a news posting.",
            label_msgid='gvSIGbpd_BPDElemento_contents_noticias_label',
            description_msgid='gvSIGbpd_BPDElemento_contents_noticias_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='News Items',
        label='Noticias',
        represents_aggregation=True,
        description2='Conventional Plone elements containing a news posting.',
        multiValued=1,
        owner_class_name="BPDElemento",
        expression="context.objectValues(['ATNewsItem'])",
        computed_types=['ATNewsItem'],
        non_framework_elements=True,
        description='Elementos de Plone conteniendo una Noticia.'
    ),

    ComputedField(
        name='pathDelRaiz',
        widget=ComputedField._properties['widget'](
            label='Pathdelraiz',
            label_msgid='gvSIGbpd_BPDElemento_attr_pathDelRaiz_label',
            i18n_domain='gvSIGbpd',
        ),
        duplicates="0",
        ea_localid="253",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        ea_guid="{941F79AF-536C-4d2b-B35B-845573440804}",
        scale="0",
        expression="context.fPathDelRaiz()",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDElemento",
        exclude_from_views="[ 'Textual', 'Tabular',  ]",
        exclude_from_exportconfig="True",
        exclude_from_copyconfig="True"
    ),

    TextField(
        name='text',
        widget=TextAreaWidget(
            label="Texto",
            label2="text",
            description="Una descripcion textual extensa del elemento.",
            description2="An extended textual description of the element.",
            label_msgid='gvSIGbpd_BPDElemento_attr_text_label',
            description_msgid='gvSIGbpd_BPDElemento_attr_text_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Una descripcion textual extensa del elemento.",
        searchable=1,
        duplicates="0",
        label2="text",
        ea_localid="248",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="An extended textual description of the element.",
        ea_guid="{EEA3C90B-1EF9-4097-9764-5F5C490F47B8}",
        scale="0",
        label="Texto",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDElemento"
    ),

    StringField(
        name='versionInterna',
        widget=StringWidget(
            label="Version Interna",
            label2="Internal Version identifier",
            description="Identificador de version para uso interno de la aplicacion.",
            description2="Version identifier used internally by the application.",
            label_msgid='gvSIGbpd_BPDElemento_attr_versionInterna_label',
            description_msgid='gvSIGbpd_BPDElemento_attr_versionInterna_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Identificador de version para uso interno de la aplicacion.",
        duplicates="0",
        label2="Internal Version identifier",
        ea_localid="254",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Version identifier used internally by the application.",
        ea_guid="{285124FC-4C3A-4c00-9645-4A026E460B11}",
        write_permission='Modify portal content',
        scale="0",
        label="Version Interna",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDElemento",
        exclude_from_views="[ 'Textual', 'Tabular',  ]",
        exclude_from_copyconfig="True"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDElemento_schema = getattr(BPDElemento_CopyConfig, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_Meta, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_ExportConfig, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_MappingConfig, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_TraversalConfig, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_Operaciones, 'schema', Schema(())).copy() + \
    getattr(ATCTMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDElemento(BPDElemento_CopyConfig, BPDElemento_Meta, BPDElemento_ExportConfig, BPDElemento_MappingConfig, BPDElemento_TraversalConfig, BPDElemento_Operaciones, ATCTMixin):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BPDElemento_CopyConfig,'__implements__',()),) + (getattr(BPDElemento_Meta,'__implements__',()),) + (getattr(BPDElemento_ExportConfig,'__implements__',()),) + (getattr(BPDElemento_MappingConfig,'__implements__',()),) + (getattr(BPDElemento_TraversalConfig,'__implements__',()),) + (getattr(BPDElemento_Operaciones,'__implements__',()),) + (getattr(ATCTMixin,'__implements__',()),)

    allowed_content_types = ['Image', 'Document', 'File', 'Link', 'News Item'] + list(getattr(BPDElemento_CopyConfig, 'allowed_content_types', [])) + list(getattr(BPDElemento_Meta, 'allowed_content_types', [])) + list(getattr(BPDElemento_ExportConfig, 'allowed_content_types', [])) + list(getattr(BPDElemento_MappingConfig, 'allowed_content_types', [])) + list(getattr(BPDElemento_TraversalConfig, 'allowed_content_types', [])) + list(getattr(BPDElemento_Operaciones, 'allowed_content_types', [])) + list(getattr(ATCTMixin, 'allowed_content_types', []))
    _at_rename_after_creation = True

    schema = BPDElemento_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('CookedBody')
    def CookedBody(self,setlevel=0,stx_level=None):
        """
        """
        
        return getToolByName( self, 'ModelDDvlPlone_tool').fCookedBodyForElement( None, self, stx_level, setlevel, None)

    security.declarePublic('fAllowImport')
    def fAllowImport(self):
        """
        """
        
        return True

    security.declarePublic('fAllowPaste')
    def fAllowPaste(self):
        """
        """
        
        return True

    security.declarePublic('getContenedor')
    def getContenedor(self):
        """
        """
        
        return aq_parent( aq_inner( self))

    security.declarePublic('getContenedorContenedor')
    def getContenedorContenedor(self):
        """
        """
        
        return aq_parent( aq_parent( aq_inner( self)))

    security.declarePublic('getEditableBody')
    def getEditableBody(self):
        """
        """
        
        return getToolByName( self, 'ModelDDvlPlone_tool').fEditableBodyForElement( None, self, None)

    security.declarePublic('getEsColeccion')
    def getEsColeccion(self):
        """
        """
        
        return False

    security.declarePublic('getEsRaiz')
    def getEsRaiz(self):
        """
        """
        
        return not aq_parent( aq_inner( self)) or ( (self.meta_type == "BPDOrganizacion") and not( aq_parent( aq_inner( self)).meta_type == "BPDColeccionUnidadesOrganizacionales"))

    security.declarePublic('getNombreProyecto')
    def getNombreProyecto(self):
        """
        """
        
        return "gvSIGbpd"
# end of class BPDElemento

##code-section module-footer #fill in your manual code here
##/code-section module-footer



