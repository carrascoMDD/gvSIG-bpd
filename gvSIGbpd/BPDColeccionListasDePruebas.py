# -*- coding: utf-8 -*-
#
# File: BPDColeccionListasDePruebas.py
#
# Copyright (c) 2011 by Conselleria de Infraestructuras y Transporte de la
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
from Products.gvSIGbpd.BPDColeccionArquetipos import BPDColeccionArquetipos
from Products.gvSIGbpd.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='listasDePruebas',
        widget=ComputedWidget(
            label="Listas de Pruebas",
            label2="Test Suites",
            description="Listas de Pruebas ensamblando secuencias de Casos de Prueba para ser ejecutados en secuencia.",
            description2="Test Suites assembling sequences of Test Cases to be executed.",
            label_msgid='gvSIGbpd_BPDColeccionListasDePruebas_contents_listasDePruebas_label',
            description_msgid='gvSIGbpd_BPDColeccionListasDePruebas_contents_listasDePruebas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Test Suites',
        label='Listas de Pruebas',
        represents_aggregation=True,
        description2='Test Suites assembling sequences of Test Cases to be executed.',
        multiValued=1,
        owner_class_name="BPDColeccionListasDePruebas",
        expression="context.objectValues(['BPDListaDePruebas'])",
        computed_types=['BPDListaDePruebas'],
        non_framework_elements=False,
        description='Listas de Pruebas ensamblando secuencias de Casos de Prueba para ser ejecutados en secuencia.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDColeccionListasDePruebas_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDColeccionArquetipos, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDColeccionListasDePruebas(OrderedBaseFolder, BPDColeccionArquetipos):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDColeccionArquetipos,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Coleccion de Listas de Pruebas'

    meta_type = 'BPDColeccionListasDePruebas'
    portal_type = 'BPDColeccionListasDePruebas'


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



    allowed_content_types = ['BPDListaDePruebas'] + list(getattr(BPDColeccionArquetipos, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdcoleccion_listasdepruebas.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Coleccion de Listas de Pruebas ensamblando secuencias de Casos de Prueba para ser ejecutados en secuencia."
    typeDescMsgId                    =  'gvSIGbpd_BPDColeccionListasDePruebas_help'
    archetype_name2                  = 'Test Suites collection'
    typeDescription2                 = '''Collection of Test Suites assembling sequences of Test Cases to be executed.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDColeccionListasDePruebas_label'
    factory_methods                  = None
    factory_enablers                 = None
    propagate_delete_impact_to       = None


    actions =  (


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("ManageProperties",),
        'condition': """python:1"""
       },


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
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDImport",
        'category': "object_buttons",
        'id': 'mddimport',
        'name': 'Import',
        'permissions': ("Modify portal content",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/",
        'category': "object",
        'id': 'view',
        'name': 'View',
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


       {'action': "string:${object_url}/MDDChanges",
        'category': "object_buttons",
        'id': 'mddchanges',
        'name': 'Changes',
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


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("ModifyPortalContent",),
        'condition': """python:object.fAllowWrite()"""
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

    schema = BPDColeccionListasDePruebas_schema

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

registerType(BPDColeccionListasDePruebas, PROJECTNAME)
# end of class BPDColeccionListasDePruebas

##code-section module-footer #fill in your manual code here
##/code-section module-footer



