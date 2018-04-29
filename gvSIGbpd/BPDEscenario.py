# -*- coding: utf-8 -*-
#
# File: BPDEscenario.py
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
from Products.gvSIGbpd.BPDProgramable import BPDProgramable
from Products.gvSIGbpd.BPDArquetipoConAdopcion import BPDArquetipoConAdopcion
from Products.gvSIGbpd.BPDConDatosDePrueba import BPDConDatosDePrueba
from Products.gvSIGbpd.BPDConResolucionesDatos import BPDConResolucionesDatos
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='episodios',
        widget=ComputedWidget(
            label="Episodios",
            label2="Episodes",
            description="La secuencia de pasos en que se desarrolla un escenario, describiendo uno de los posibles flujos de ejecucion del proceso.",
            description2="The sequence of steps in an scenario, describing one of the possible execution flows of the process.",
            label_msgid='gvSIGbpd_BPDEscenario_contents_episodios_label',
            description_msgid='gvSIGbpd_BPDEscenario_contents_episodios_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Episodes',
        additional_columns=['programas', 'sumarioProgramas', 'resolucionesDatos', 'sumarioResolucionesDatos'],
        label='Episodios',
        represents_aggregation=True,
        description2='The sequence of steps in an scenario, describing one of the possible execution flows of the process.',
        multiValued=1,
        owner_class_name="BPDEscenario",
        expression='context.objectValues([])',
        computed_types=[],
        non_framework_elements=False,
        description='La secuencia de pasos en que se desarrolla un escenario, describiendo uno de los posibles flujos de ejecucion del proceso.'
    ),

    RelationField(
        name='casosDePrueba',
        inverse_relation_label="Casos de Prueba",
        containment="Unspecified",
        inverse_relation_description="Casos de Prueba definiendo conjuntos de valores concretos para el Escenario contenedor.",
        description="Escenario para el que se definen los conjuntos de valores.",
        relationship='Escenario_CasosDePrueba',
        inverse_relation_field_name='escenario',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Scenario",
        inverse_relation_description2="Test Cases defining concrete data sets of values for the container Scenario.",
        widget=ReferenceBrowserWidget(
            label="Escenario",
            label2="Scenario",
            description="Escenario para el que se definen los conjuntos de valores.",
            description2="Scenario for which concreate value sets are defined.",
            label_msgid='gvSIGbpd_BPDEscenario_rel_casosDePrueba_label',
            description_msgid='gvSIGbpd_BPDEscenario_rel_casosDePrueba_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Escenario",
        description2="Scenario for which concreate value sets are defined.",
        multiValued=1,
        inverse_relation_label2="Test Cases",
        inverse_relationship='CasosDePrueba_Escenario',
        write_permission='Modify portal content',
        additional_columns=[]
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDEscenario_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDProgramable, 'schema', Schema(())).copy() + \
    getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    getattr(BPDConDatosDePrueba, 'schema', Schema(())).copy() + \
    getattr(BPDConResolucionesDatos, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDEscenario(OrderedBaseFolder, BPDProgramable, BPDArquetipoConAdopcion, BPDConDatosDePrueba, BPDConResolucionesDatos):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDProgramable,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),) + (getattr(BPDConDatosDePrueba,'__implements__',()),) + (getattr(BPDConResolucionesDatos,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Escenario'

    meta_type = 'BPDEscenario'
    portal_type = 'BPDEscenario'


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



    allowed_content_types = [] + list(getattr(BPDProgramable, 'allowed_content_types', [])) + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', [])) + list(getattr(BPDConDatosDePrueba, 'allowed_content_types', [])) + list(getattr(BPDConResolucionesDatos, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdescenario.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Una secuencia de pasos del proceso de negocio, describiendo uno de los posibles flujos de ejecucion del proceso."
    typeDescMsgId                    =  'gvSIGbpd_BPDEscenario_help'
    archetype_name2                  = 'Scenario'
    typeDescription2                 = '''A secuence of steps in the business process, describing one of the possible execution flows of the process.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDEscenario_label'
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

    schema = BPDEscenario_schema

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

registerType(BPDEscenario, PROJECTNAME)
# end of class BPDEscenario

##code-section module-footer #fill in your manual code here
##/code-section module-footer



