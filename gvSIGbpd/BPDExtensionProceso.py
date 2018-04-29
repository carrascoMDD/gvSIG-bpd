# -*- coding: utf-8 -*-
#
# File: BPDExtensionProceso.py
#
# Copyright (c) 2010 by Conselleria de Infraestructuras y Transporte de la
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
from Products.gvSIGbpd.BPDArquetipoReferenciable import BPDArquetipoReferenciable
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.base import ATCTMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='condicion',
        widget=TextAreaWidget(
            label="Condicion",
            label2="Condition",
            description="Criterio para determinar si el Proceso de Negocio puede realmente extender el Proceso de Negocio extendido.",
            description2="Criteria to determine whether this Business Process can actually extend the extended Business Process.",
            label_msgid='gvSIGbpd_BPDExtensionProceso_attr_condicion_label',
            description_msgid='gvSIGbpd_BPDExtensionProceso_attr_condicion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Criterio para determinar si el Proceso de Negocio puede realmente extender el Proceso de Negocio extendido.",
        searchable=1,
        duplicates="0",
        label2="Condition",
        ea_localid="403",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Criteria to determine whether this Business Process can actually extend the extended Business Process.",
        ea_guid="{6F7752F4-B5E9-45f5-B92B-710C993C3E8B}",
        write_permission='Modify portal content',
        scale="0",
        label="Condicion",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDExtensionProceso"
    ),

    RelationField(
        name='puntosExtension',
        inverse_relation_label="Extensiones Procesos",
        additional_columns=['tituloProcesoDeNegocio'],
        inverse_relation_description="Extensiones de Procesos de Negocio insertando comportamiento en este Punto de Extension.",
        description="El Punto de Extension en el Proceso de Negocio que se extiende insertando el comportamiento de este Proceso de Negocio.",
        relationship='BPDPuntosExtension',
        inverse_relation_field_name='extensionesProcesos',
        inverse_relation_label2="Process Extensions",
        label2="Extension Points",
        inverse_relation_description2="Business Process Extensions inserting behavior in this Extension Point.",
        widget=ReferenceBrowserWidget(
            label="Puntos de Extension",
            label2="Extension Points",
            description="El Punto de Extension en el Proceso de Negocio que se extiende insertando el comportamiento de este Proceso de Negocio.",
            description2="The Extension Point in the Business Process that is being extended by inserting the behavior of this Business Process.",
            label_msgid='gvSIGbpd_BPDExtensionProceso_rel_puntosExtension_label',
            description_msgid='gvSIGbpd_BPDExtensionProceso_rel_puntosExtension_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Puntos de Extension",
        description2="The Extension Point in the Business Process that is being extended by inserting the behavior of this Business Process.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDExtensionesProcesos',
        owner_class_name="BPDExtensionProceso",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;"
    ),

    ComputedField(
        name='tituloProcesoDeNegocio',
        widget=ComputedField._properties['widget'](
            label="Proceso de Negocio",
            label2="Business Process",
            description="El titulo del Proceso de Negocio que contiene la Extension",
            description2="Title of the Business Process containing the Extension.",
            label_msgid='gvSIGbpd_BPDExtensionProceso_attr_tituloProcesoDeNegocio_label',
            description_msgid='gvSIGbpd_BPDExtensionProceso_attr_tituloProcesoDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="El titulo del Proceso de Negocio que contiene la Extension",
        duplicates="0",
        label2="Business Process",
        ea_localid="404",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Title of the Business Process containing the Extension.",
        ea_guid="{784912F0-DB7E-4844-A432-5E052C297C4A}",
        exclude_from_values_form="True",
        scale="0",
        label="Proceso de Negocio",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDExtensionProceso",
        expression="context.getContenedor().Title()",
        computed_types="string"
    ),

    ComputedField(
        name='titulosProcesosExtendidos',
        widget=ComputedField._properties['widget'](
            label="Procesos de Negocio Extendidos",
            label2="Extended Business Processes",
            description="Los titulos de los Procesos de Negocio que son Extendidos por este Proceso de Negocio.",
            description2="Titles of the Business Processes extended by this Business process.",
            label_msgid='gvSIGbpd_BPDExtensionProceso_attr_titulosProcesosExtendidos_label',
            description_msgid='gvSIGbpd_BPDExtensionProceso_attr_titulosProcesosExtendidos_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Los titulos de los Procesos de Negocio que son Extendidos por este Proceso de Negocio.",
        duplicates="0",
        label2="Extended Business Processes",
        ea_localid="402",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Titles of the Business Processes extended by this Business process.",
        ea_guid="{6A32C528-B937-4134-944F-C559614A2AC3}",
        exclude_from_values_form="True",
        scale="0",
        label="Procesos de Negocio Extendidos",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDExtensionProceso",
        expression="context.fTrTFLVs([ 'puntosExtension'], [ 'title',  'tituloProcesoDeNegocio',])",
        computed_types="string"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDExtensionProceso_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoReferenciable, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDExtensionProceso(OrderedBaseFolder, BPDArquetipoReferenciable):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoReferenciable,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Extension de Proceso de Negocio'

    meta_type = 'BPDExtensionProceso'
    portal_type = 'BPDExtensionProceso'


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



    allowed_content_types = [] + list(getattr(BPDArquetipoReferenciable, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdextensionproceso.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Indica que el Proceso de Negocio aporta comportamiento adicional a uno o mas Procesos de Negocio"
    typeDescMsgId                    =  'gvSIGbpd_BPDExtensionProceso_help'
    archetype_name2                  = 'Extend Business Process'
    typeDescription2                 = '''Indicates the the Business Process introduces additional behavior to other Business Process(es).'''
    archetype_name_msgid             = 'gvSIGbpd_BPDExtensionProceso_label'
    factory_methods                  = None
    factory_enablers                 = None
    propagate_delete_impact_to       = None


    actions =  (


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
        'permissions': ("View",),
        'condition': """python:0"""
       },


       {'action': "string:${object_url}/MDDInspectClipboard",
        'category': "object_buttons",
        'id': 'inspectclipboard',
        'name': 'Clipboard',
        'permissions': ("View",),
        'condition': """python:object.fAllowRead()"""
       },


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowWrite()"""
       },


       {'action': "string:${object_url}/MDDOrdenar",
        'category': "object_buttons",
        'id': 'reorder',
        'name': 'Reorder',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowWrite()"""
       },


       {'action': "string:${object_url}/MDDExport",
        'category': "object_buttons",
        'id': 'mddexport',
        'name': 'Export',
        'permissions': ("View",),
        'condition': """python:object.fAllowExport()"""
       },


       {'action': "string:${object_url}/MDDImport",
        'category': "object_buttons",
        'id': 'mddimport',
        'name': 'Import',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowImport()"""
       },


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("Manage properties",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDChanges",
        'category': "object_buttons",
        'id': 'mddchanges',
        'name': 'Changes',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDVersions",
        'category': "object_buttons",
        'id': 'mddversions',
        'name': 'Versions',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDCacheStatus/",
        'category': "object_buttons",
        'id': 'mddcachestatus',
        'name': 'Cache',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/TextualRest",
        'category': "object_buttons",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': """python:1"""
       },


    )

    _at_rename_after_creation = True

    schema = BPDExtensionProceso_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('manage_afterAdd')
    def manage_afterAdd(self,item,container):
        """
        """
        
        return self.pHandle_manage_afterAdd(  item, container)

    security.declarePublic('manage_pasteObjects')
    def manage_pasteObjects(self,cb_copy_data=None,REQUEST=None):
        """
        """
        
        return self.pHandle_manage_pasteObjects( cb_copy_data, REQUEST)

    security.declarePublic('moveObjectsByDelta')
    def moveObjectsByDelta(self,ids,delta,subset_ids=None):
        """
        """
        
        return self.pHandle_moveObjectsByDelta( ids, delta, subset_ids=subset_ids)

registerType(BPDExtensionProceso, PROJECTNAME)
# end of class BPDExtensionProceso

##code-section module-footer #fill in your manual code here
##/code-section module-footer



