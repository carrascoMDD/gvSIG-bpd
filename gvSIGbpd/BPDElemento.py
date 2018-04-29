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
from Products.gvSIGbpd.BPDConRegistroActividad import BPDConRegistroActividad
from Products.gvSIGbpd.BPDConTraducciones import BPDConTraducciones
from Products.gvSIGbpd.BPDElemento_Meta import BPDElemento_Meta
from Products.gvSIGbpd.BPDConVersiones import BPDConVersiones
from Products.gvSIGbpd.BPDElemento_ExportConfig import BPDElemento_ExportConfig
from Products.gvSIGbpd.BPDElemento_MappingConfig import BPDElemento_MappingConfig
from Products.gvSIGbpd.BPDElemento_TraversalConfig import BPDElemento_TraversalConfig
from Products.gvSIGbpd.BPDElemento_Credits import BPDElemento_Credits
from Products.gvSIGbpd.BPDElemento_Operaciones import BPDElemento_Operaciones
from Products.ATContentTypes.content.base import ATCTMixin
from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.base import updateAliases
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.CMFCore.utils  import getToolByName
from Acquisition  import aq_inner, aq_parent
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='ownerName',
        widget=ComputedField._properties['widget'](
            label="En",
            label2="In",
            description="El nombre cualificado del elemento que posee este elemento, incluyendo los nombres de  los elementos (paquetes o tipos) que lo poseen, recursivamente, desde la raiz del modelo.",
            description2="The name of the owner of element, including the names of the container packages or type, recusively from the root of the model.",
            label_msgid='gvSIGbpd_BPDElemento_attr_ownerName_label',
            description_msgid='gvSIGbpd_BPDElemento_attr_ownerName_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El nombre cualificado del elemento que posee este elemento, incluyendo los nombres de  los elementos (paquetes o tipos) que lo poseen, recursivamente, desde la raiz del modelo.",
        duplicates="0",
        label2="In",
        ea_localid="299",
        derived="1",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="The name of the owner of element, including the names of the container packages or type, recusively from the root of the model.",
        ea_guid="{F01A2C45-79CF-4e4d-8AFF-073EC965E097}",
        scale="0",
        label="En",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDElemento",
        expression="context.fComposeOwnerName( '::', 'title', theExcludeRoot=True)",
        computed_types="text",
        exclude_from_copyconfig="True",
        exclude_from_exportconfig="True"
    ),

    ComputedField(
        name='qualifiedName',
        widget=ComputedField._properties['widget'](
            label="Nombre completo",
            label2="Qualified name",
            description="El nombre cualificado del elemento, incluyendo los nombres de  los elementos ( paquetes o tipos) que lo poseen, recursivamente, desde la raiz del modelo.",
            description2="The quailified name of the element, including the names of the owner packages and types, recursively from the root of the model.",
            label_msgid='gvSIGbpd_BPDElemento_attr_qualifiedName_label',
            description_msgid='gvSIGbpd_BPDElemento_attr_qualifiedName_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="El nombre cualificado del elemento, incluyendo los nombres de  los elementos ( paquetes o tipos) que lo poseen, recursivamente, desde la raiz del modelo.",
        duplicates="0",
        label2="Qualified name",
        ea_localid="298",
        derived="1",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="The quailified name of the element, including the names of the owner packages and types, recursively from the root of the model.",
        ea_guid="{1D67433F-4F59-4584-A197-E27952AA904E}",
        exclude_from_values_form="True",
        scale="0",
        computed_types="string",
        label="Nombre completo",
        length="0",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDElemento",
        expression="context.fComposeQualifiedName( '::', 'title', theExcludeRoot=True)",
        exclude_from_exportconfig="True",
        exclude_from_copyconfig="True"
    ),

    ComputedField(
        name='pathDelRaiz',
        widget=ComputedField._properties['widget'](
            label="Ruta del Raiz",
            label2="Root's Path",
            description="La ruta completamente cualificada del elemento raiz.",
            description2="Roots element fully qualified path.",
            label_msgid='gvSIGbpd_BPDElemento_attr_pathDelRaiz_label',
            description_msgid='gvSIGbpd_BPDElemento_attr_pathDelRaiz_help',
            i18n_domain='gvSIGbpd',
        ),
        description="La ruta completamente cualificada del elemento raiz.",
        duplicates="0",
        label2="Root's Path",
        ea_localid="253",
        derived="1",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="Roots element fully qualified path.",
        ea_guid="{941F79AF-536C-4d2b-B35B-845573440804}",
        scale="0",
        label="Ruta del Raiz",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDElemento",
        expression="context.fPathDelRaiz()",
        computed_types="string",
        exclude_from_copyconfig="True",
        exclude_from_exportconfig="True"
    ),

    RelationField(
        name='elementosDerivados',
        inverse_relation_label="Elementos Base",
        inverse_relation_description="Elementos a partir de los cuales se ha derivado el actual.",
        description="Elementos que han sido derivados a partir del actual.",
        relationship='BPDElementosDerivados',
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
        inverse_relationship='BPDElementosBase',
        owner_class_name="BPDElemento",
        dependency_supplier=True
    ),

    RelationField(
        name='elementosBase',
        inverse_relation_label="Elementos Derivados",
        containment="Unspecified",
        inverse_relation_description="Elementos que han sido derivados a partir del actual.",
        description="Elementos a partir de los cuales se ha derivado el actual.",
        relationship='BPDElementosBase',
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
        inverse_relationship='BPDElementosDerivados',
        write_permission='Modify portal content'
    ),

    RelationField(
        name='usosDelElemento',
        inverse_relation_label="Elemento Usado",
        inverse_relation_description="El elemento que se reutiliza en esta definicion.",
        description="Donde se usa el elemento como parte de otra definicion.",
        relationship='BPDUsosDelElemento',
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
        inverse_relationship='BPDElementoUsado',
        owner_class_name="BPDElemento",
        dependency_supplier=True
    ),

    RelationField(
        name='elementoUsado',
        inverse_relation_label="Usos del Elemento",
        containment="Unspecified",
        inverse_relation_description="Donde se usa el elemento como parte de otra definicion.",
        description="El elemento que se reutiliza en esta definicion.",
        relationship='BPDElementoUsado',
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
        inverse_relationship='BPDUsosDelElemento',
        write_permission='Modify portal content'
    ),

    RelationField(
        name='elementosCopia',
        inverse_relation_label="Originales",
        inverse_relation_description="Elementos que se copiaron sobre este elemento. Permite recordar de donde se obtuvo la informacion de este elemento.",
        description="Elementos sobre los que se copio la informacion de este elemento. Permite recordar donde se ha utilizado la informacion de este elemento.",
        relationship='BPDElementosCopia',
        label2="Copies",
        widget=ReferenceBrowserWidget(
            label="Copias",
            label2="Copies",
            description="Elementos sobre los que se copio la informacion de este elemento. Permite recordar donde se ha utilizado la informacion de este elemento.",
            description2="Elements onto which information in this elemento was copied onto. Allows to record were has been used the information in this element",
            label_msgid='gvSIGbpd_BPDElemento_rel_elementosCopia_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_elementosCopia_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Elements onto which information in this elemento was copied onto. Allows to record were has been used the information in this element",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Originals",
        dependency_supplier=True,
        inverse_relation_field_name='elementosOriginales',
        inverse_relation_description2="Elementos that were copied onto this element. Allow to record from where was ontained the information in this element.",
        write_permission='Modify portal content',
        label="Copias",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDElementosOriginales'
    ),

    RelationField(
        name='elementosOriginales',
        inverse_relation_label="Copias",
        inverse_relation_description="Elementos sobre los que se copio la informacion de este elemento. Permite recordar donde se ha utilizado la informacion de este elemento.",
        description="Elementos que se copiaron sobre este elemento. Permite recordar de donde se obtuvo la informacion de este elemento.",
        relationship='BPDElementosOriginales',
        label2="Originals",
        widget=ReferenceBrowserWidget(
            label="Originales",
            label2="Originals",
            description="Elementos que se copiaron sobre este elemento. Permite recordar de donde se obtuvo la informacion de este elemento.",
            description2="Elementos that were copied onto this element. Allow to record from where was ontained the information in this element.",
            label_msgid='gvSIGbpd_BPDElemento_rel_elementosOriginales_label',
            description_msgid='gvSIGbpd_BPDElemento_rel_elementosOriginales_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Elementos that were copied onto this element. Allow to record from where was ontained the information in this element.",
        inverse_relation_label2="Copies",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='elementosCopia',
        inverse_relation_description2="Elements onto which information in this elemento was copied onto. Allows to record were has been used the information in this element",
        label="Originales",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDElementosCopia',
        owner_class_name="BPDElemento"
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
        position="5",
        owner_class_name="BPDElemento"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDElemento_schema = getattr(BPDElemento_CopyConfig, 'schema', Schema(())).copy() + \
    getattr(BPDConRegistroActividad, 'schema', Schema(())).copy() + \
    getattr(BPDConTraducciones, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_Meta, 'schema', Schema(())).copy() + \
    getattr(BPDConVersiones, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_ExportConfig, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_MappingConfig, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_TraversalConfig, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_Credits, 'schema', Schema(())).copy() + \
    getattr(BPDElemento_Operaciones, 'schema', Schema(())).copy() + \
    getattr(ATCTMixin, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDElemento(BPDElemento_CopyConfig, BPDConRegistroActividad, BPDConTraducciones, BPDElemento_Meta, BPDConVersiones, BPDElemento_ExportConfig, BPDElemento_MappingConfig, BPDElemento_TraversalConfig, BPDElemento_Credits, BPDElemento_Operaciones, ATCTMixin):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BPDElemento_CopyConfig,'__implements__',()),) + (getattr(BPDConRegistroActividad,'__implements__',()),) + (getattr(BPDConTraducciones,'__implements__',()),) + (getattr(BPDElemento_Meta,'__implements__',()),) + (getattr(BPDConVersiones,'__implements__',()),) + (getattr(BPDElemento_ExportConfig,'__implements__',()),) + (getattr(BPDElemento_MappingConfig,'__implements__',()),) + (getattr(BPDElemento_TraversalConfig,'__implements__',()),) + (getattr(BPDElemento_Credits,'__implements__',()),) + (getattr(BPDElemento_Operaciones,'__implements__',()),) + (getattr(ATCTMixin,'__implements__',()),)



    # Change Audit fields

    creation_date_field = 'fechaCreacion'
    creation_user_field = 'usuarioCreador'
    modification_date_field = 'fechaModificacion'
    modification_user_field = 'usuarioModificador'
    deletion_date_field = 'fechaEliminacion'
    deletion_user_field = 'usuarioEliminador'
    is_inactive_field = 'estaInactivo'
    change_counter_field = 'contadorCambios'
    sources_counters_field = 'contadoresDeFuentes'
    change_log_field = 'registroDeCambios'




    # Versioning and Translation fields

    inter_version_field = 'uidInterVersionesInterno'
    version_field = 'versionInterna'
    version_storage_field = 'versionInternaAlmacenada'
    version_comment_field = 'comentarioVersionInterna'
    version_comment_storage_field = 'comentarioVersionInternaAlmacenada'
    inter_translation_field = 'uidInterTraduccionesInterno'
    language_field = 'codigoIdiomaInterno'
    fields_pending_translation_field = 'camposPendientesTraduccionInterna'
    fields_pending_revision_field = 'camposPendientesRevisionInterna'




    # Traceability links fields

    versioning_link_fields = ['versionesAnteriores', 'versionesSiguientes',]
    translation_link_fields = ['originalDeTraduccion', 'elementosTraducidos',]
    usage_link_fields = ['elementoUsado', 'usosDelElemento',]
    derivation_link_fields = ['elementosBase', 'elementosDerivados',]



    allowed_content_types = ['Image', 'Document', 'File', 'Link', 'News Item'] + list(getattr(BPDElemento_CopyConfig, 'allowed_content_types', [])) + list(getattr(BPDConRegistroActividad, 'allowed_content_types', [])) + list(getattr(BPDConTraducciones, 'allowed_content_types', [])) + list(getattr(BPDElemento_Meta, 'allowed_content_types', [])) + list(getattr(BPDConVersiones, 'allowed_content_types', [])) + list(getattr(BPDElemento_ExportConfig, 'allowed_content_types', [])) + list(getattr(BPDElemento_MappingConfig, 'allowed_content_types', [])) + list(getattr(BPDElemento_TraversalConfig, 'allowed_content_types', [])) + list(getattr(BPDElemento_Credits, 'allowed_content_types', [])) + list(getattr(BPDElemento_Operaciones, 'allowed_content_types', [])) + list(getattr(ATCTMixin, 'allowed_content_types', []))

    aliases = updateAliases( ATDocument, {'placeful_workflow_configuration': 'Tabular', 'select_default_page': 'Textual', 'folder_factories': 'Tabular', 'selectViewTemplate': 'MDDSelectViewTemplate', 'content_status_modify': 'Tabular', 'object_paste': 'MDDPaste', 'object_rename': 'Editar', 'relations_form': 'Tabular', 'delete_confirmation': 'Eliminar', 'content_status_history': 'Tabular'})

    _at_rename_after_creation = True

    schema = BPDElemento_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('displayContentsTab')
    def displayContentsTab(self):
        """
        """
        
        return False

    security.declarePublic('externalEditorEnabled')
    def externalEditorEnabled(self):
        """
        """
        
        return False

    security.declarePublic('cb_isCopyable')
    def cb_isCopyable(self):
        """
        """
        
        return self.fAllowRead()

    security.declarePublic('cb_isMoveable')
    def cb_isMoveable(self):
        """
        """
        
        return self.fAllowWrite()

    security.declarePublic('fAllowExport')
    def fAllowExport(self):
        """
        """
        
        return self.fAllowRead()

    security.declarePublic('fIsCacheable')
    def fIsCacheable(self):
        """
        """
        
        return True

    security.declarePublic('fAllowTranslation')
    def fAllowTranslation(self):
        """
        """
        
        return self.fAllowRead()

    security.declarePublic('fAllowVersion')
    def fAllowVersion(self):
        """
        """
        
        return self.fAllowRead()

    security.declarePublic('fAllowImport')
    def fAllowImport(self):
        """
        """
        
        return self.fAllowWrite()

    security.declarePublic('fAllowEditId')
    def fAllowEditId(self):
        """
        """
        
        return self.fAllowWrite()

    security.declarePublic('fAllowPaste')
    def fAllowPaste(self):
        """
        """
        
        return self.fAlowWrite()

    security.declarePublic('fAllowRead')
    def fAllowRead(self):
        """
        """
        
        return self.getRaiz().fAllowRead()

    security.declarePublic('fAllowWrite')
    def fAllowWrite(self):
        """
        """
        
        return self.fAllowRead() and self.getRaiz().fAllowWrite()

    security.declarePublic('getEsColeccion')
    def getEsColeccion(self):
        """
        """
        
        return False

    security.declarePublic('getNombreProyecto')
    def getNombreProyecto(self):
        """
        """
        
        return "gvSIGbpd"

    security.declarePublic('getAddableTypesInMenu')
    def getAddableTypesInMenu(self,theTypes):
        """
        """
        
        return []

    security.declarePublic('fRelationsNotPropagatingViewInvalidation')
    def fRelationsNotPropagatingViewInvalidation(self):
        """
        """
        
        return ['elementosDerivados','versionAnterior','siguientesVersiones','elementoUsado','elementosTraducidos','originalDeTraduccion','elementosOriginales','elementosCopia','traduccionesDeIdiomaCanonico','idiomaCanonico']

    security.declarePublic('unused_fRelationFieldsNotPropagatingViewInvalidation')
    def unused_fRelationFieldsNotPropagatingViewInvalidation(self):
        """
        """
        
        return ['elementosDerivados','versionAnterior','siguientesVersiones','elementoUsado','elementosTraducidos','originalDeTraduccion','elementosOriginales','elementosCopia','traduccionesDeIdiomaCanonico','idiomaCanonico']
# end of class BPDElemento

##code-section module-footer #fill in your manual code here
##/code-section module-footer



