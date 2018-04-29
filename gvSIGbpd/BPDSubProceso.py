# -*- coding: utf-8 -*-
#
# File: BPDSubProceso.py
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
from Products.gvSIGbpd.BPDPasoGeneral import BPDPasoGeneral
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.ATContentTypes.content.base import ATCTMixin

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='detallesPaso',
        widget=ComputedField._properties['widget'](
            label="Detalles del SubProceso",
            label2="SubProcess Step details",
            description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
            description2="Details about the SubProcess Step, including the title of the used Business Process.",
            label_msgid='gvSIGbpd_BPDSubProceso_attr_detallesPaso_label',
            description_msgid='gvSIGbpd_BPDSubProceso_attr_detallesPaso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
        duplicates="0",
        label2="SubProcess Step details",
        ea_localid="273",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the SubProcess Step, including the title of the used Business Process.",
        ea_guid="{B0D9A6C5-C23B-4725-A085-FAE745CE6C5E}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del SubProceso",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDSubProceso",
        expression="context.fTFLVs([ 'esInicial', 'procesoUsado','ejecutores'])",
        computed_types="string"
    ),

    ComputedField(
        name='tituloProcesoUsado',
        widget=ComputedField._properties['widget'](
            label="Proceso de Negocio usado",
            label2="Used Business Process",
            description="Proceso de Negocio que se ejecuta como parte del Proceso de Negocio actual.",
            description2="Business Process executed as part of the current one.",
            label_msgid='gvSIGbpd_BPDSubProceso_attr_tituloProcesoUsado_label',
            description_msgid='gvSIGbpd_BPDSubProceso_attr_tituloProcesoUsado_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Proceso de Negocio que se ejecuta como parte del Proceso de Negocio actual.",
        duplicates="0",
        label2="Used Business Process",
        ea_localid="264",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Business Process executed as part of the current one.",
        ea_guid="{C08470BC-5A85-49be-9383-630D2A3A0C69}",
        exclude_from_values_form="True",
        scale="0",
        label="Proceso de Negocio usado",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDSubProceso",
        expression="context.fFV('procesoUsado')",
        computed_types="string"
    ),

    RelationField(
        name='procesoUsado',
        inverse_relation_label="Usos como Sub-Proceso de Negocio",
        additional_columns=['proposito', 'responsableMantenimiento', 'detallesProceso', 'estado', 'nivelDeImposicion'],
        inverse_relation_description="Pasos de otros Procesos de Negocio donde este proceso se ejecuta de principio a fin, como un Paso Sub-Proceso.",
        description="Proceso de Negocio que se ejecuta como parte del Proceso de Negocio de mayor alcance.",
        relationship='ProcesoUsado',
        inverse_relation_field_name='usadoComoSubProcesos',
        inverse_relation_label2="Used as Sub-Business Process in",
        label2="Used Business Process",
        inverse_relation_description2="Business Processes where this one is used as a Sub-Process",
        widget=ReferenceBrowserWidget(
            label="Proceso de Negocio usado",
            label2="Used Business Process",
            description="Proceso de Negocio que se ejecuta como parte del Proceso de Negocio de mayor alcance.",
            description2="Business Process executed as part of the current one.",
            label_msgid='gvSIGbpd_BPDSubProceso_rel_procesoUsado_label',
            description_msgid='gvSIGbpd_BPDSubProceso_rel_procesoUsado_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Proceso de Negocio usado",
        description2="Business Process executed as part of the current one.",
        multiValued=0,
        containment="Unspecified",
        inverse_relationship='UsadoComoSubProcesos',
        owner_class_name="BPDSubProceso",
        deststyle="Owned=0;Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDSubProceso_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDPasoGeneral, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDSubProceso(OrderedBaseFolder, BPDPasoGeneral):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDPasoGeneral,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Sub Proceso'

    meta_type = 'BPDSubProceso'
    portal_type = 'BPDSubProceso'
    allowed_content_types = [] + list(getattr(BPDPasoGeneral, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdsubproceso.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Un Proceso de Negocio definido aparte, se ejercita de principio a fin como un paso parte de otro Proceso de Negocio de mayor alcance."
    typeDescMsgId =  'gvSIGbpd_BPDSubProceso_help'
    archetype_name2 = 'Sub Process'
    typeDescription2 = '''A Business Process, specified elsewhere, is executed in its entirety in the context of the current Business Process, as a single step.'''
    archetype_name_msgid = 'gvSIGbpd_BPDSubProceso_label'
    factory_methods = None
    factory_enablers = None


    actions =  (


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
        'permissions': ("View",),
        'condition': 'python:0'
       },


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("Modify portal content",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/MDDExport",
        'category': "object_buttons",
        'id': 'mddexport',
        'name': 'Export',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/MDDImport",
        'category': "object_buttons",
        'id': 'mddimport',
        'name': 'Import',
        'permissions': ("Modify portal content",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("Manage properties",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/TextualRest",
        'category': "object_buttons",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/Textual",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = BPDSubProceso_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('manage_afterAdd')
    def manage_afterAdd(self,item,container):
        """
        """
        
        return self.pHandle_manage_afterAdd(  item, container)

registerType(BPDSubProceso, PROJECTNAME)
# end of class BPDSubProceso

##code-section module-footer #fill in your manual code here
##/code-section module-footer



