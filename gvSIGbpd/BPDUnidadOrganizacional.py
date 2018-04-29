# -*- coding: utf-8 -*-
#
# File: BPDUnidadOrganizacional.py
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
from Products.gvSIGbpd.BPDParticipante import BPDParticipante
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='coleccionesUnidadesOrganizacionales',
        widget=ComputedWidget(
            label="Unidades Organizacionales (colecciones)",
            label2="Organisational Units (collections)",
            description="Colecciones de UnidadesOrganizacionales mostrando la descomposicion organica en unidades, departamentos, secciones, etc. de orden inferior participantes en los Procesos de Negocio.",
            description2="Collections of Organisational Units corresponding to the Organisation decomposition into units, departments, sections, ... at a lower level, participants in the Business Processes.",
            label_msgid='gvSIGbpd_BPDUnidadOrganizacional_contents_coleccionesUnidadesOrganizacionales_label',
            description_msgid='gvSIGbpd_BPDUnidadOrganizacional_contents_coleccionesUnidadesOrganizacionales_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Organisational Units (collections)',
        label='Unidades Organizacionales (colecciones)',
        represents_aggregation=True,
        description2='Collections of Organisational Units corresponding to the Organisation decomposition into units, departments, sections, ... at a lower level, participants in the Business Processes.',
        multiValued=1,
        owner_class_name="BPDUnidadOrganizacional",
        expression="context.objectValues(['BPDColeccionUnidadesOrganizacionales'])",
        computed_types=['BPDColeccionUnidadesOrganizacionales'],
        non_framework_elements=False,
        description='Colecciones de UnidadesOrganizacionales mostrando la descomposicion organica en unidades, departamentos, secciones, etc. de orden inferior participantes en los Procesos de Negocio.'
    ),

    ComputedField(
        name='coleccionesPerfiles',
        widget=ComputedWidget(
            label="Perfiles (colecciones)",
            label2="Participant Profiles (collections)",
            description="Colecciones de Perfiles tipificando las clases de individuos participantes en los Procesos de Negocio.",
            description2="Collections of Participant Profiles characterising the individual participants in the Business Processes.",
            label_msgid='gvSIGbpd_BPDUnidadOrganizacional_contents_coleccionesPerfiles_label',
            description_msgid='gvSIGbpd_BPDUnidadOrganizacional_contents_coleccionesPerfiles_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Participant Profiles (collections)',
        label='Perfiles (colecciones)',
        represents_aggregation=True,
        description2='Collections of Participant Profiles characterising the individual participants in the Business Processes.',
        multiValued=1,
        owner_class_name="BPDUnidadOrganizacional",
        expression="context.objectValues(['BPDColeccionPerfiles'])",
        computed_types=['BPDColeccionPerfiles'],
        non_framework_elements=False,
        description='Colecciones de Perfiles tipificando las clases de individuos participantes en los Procesos de Negocio.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDUnidadOrganizacional_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDParticipante, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDUnidadOrganizacional(OrderedBaseFolder, BPDParticipante):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDParticipante,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Unidad Organizacional'

    meta_type = 'BPDUnidadOrganizacional'
    portal_type = 'BPDUnidadOrganizacional'


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



    allowed_content_types = ['BPDColeccionUnidadesOrganizacionales', 'BPDColeccionPerfiles'] + list(getattr(BPDParticipante, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdunidadorganizacional.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Parte de la estructura jerarquica de descomposicion de la Organizacion en unidades."
    typeDescMsgId                    =  'gvSIGbpd_BPDUnidadOrganizacional_help'
    archetype_name2                  = 'Organisational Unit'
    typeDescription2                 = '''Part of the organisational decomposition into units.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDUnidadOrganizacional_label'
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

    schema = BPDUnidadOrganizacional_schema

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

registerType(BPDUnidadOrganizacional, PROJECTNAME)
# end of class BPDUnidadOrganizacional

##code-section module-footer #fill in your manual code here
##/code-section module-footer



