# -*- coding: utf-8 -*-
#
# File: BPDProcesoDeNegocioSimple.py
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
from Products.gvSIGbpd.BPDProcesoDeNegocio import BPDProcesoDeNegocio
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='coleccionesEntradas',
        widget=ComputedWidget(
            label="Entradas (colecciones)",
            label2="Inputs (collections)",
            description="Colecciones de Informaciones que pueden o deben estar disponibles para poder dar comienzo al Proceso de Negocio.",
            description2="Collections of Informations that must or may be available to start the Business Process.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocioSimple_contents_coleccionesEntradas_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocioSimple_contents_coleccionesEntradas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Inputs (collections)',
        label='Entradas (colecciones)',
        represents_aggregation=True,
        description2='Collections of Informations that must or may be available to start the Business Process.',
        multiValued=1,
        owner_class_name="BPDProcesoDeNegocioSimple",
        expression="context.objectValues(['BPDColeccionEntradas'])",
        computed_types=['BPDColeccionEntradas'],
        non_framework_elements=False,
        description='Colecciones de Informaciones que pueden o deben estar disponibles para poder dar comienzo al Proceso de Negocio.'
    ),

    ComputedField(
        name='coleccionesSalidas',
        widget=ComputedWidget(
            label="Salidas (colecciones)",
            label2="Outputs (collections)",
            description="Colecciones de Informaciones que pueden estar o  estaran disponibles cuando haya concluido exitosamente el Proceso de Negocio.",
            description2="Collections of Informations that may or will be made available upon successful completion of the Business Process.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocioSimple_contents_coleccionesSalidas_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocioSimple_contents_coleccionesSalidas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Outputs (collections)',
        label='Salidas (colecciones)',
        represents_aggregation=True,
        description2='Collections of Informations that may or will be made available upon successful completion of the Business Process.',
        multiValued=1,
        owner_class_name="BPDProcesoDeNegocioSimple",
        expression="context.objectValues(['BPDColeccionSalidas'])",
        computed_types=['BPDColeccionSalidas'],
        non_framework_elements=False,
        description='Colecciones de Informaciones que pueden estar o  estaran disponibles cuando haya concluido exitosamente el Proceso de Negocio.'
    ),

    ComputedField(
        name='coleccionesPasos',
        widget=ComputedWidget(
            label="Pasos (colecciones)",
            label2="Steps (collections)",
            description="Colecciones de Acciones individuales en que transcurre la ejecucion del Proceso de Negocio.",
            description2="Collections of individual actions during the course of the Business Process.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocioSimple_contents_coleccionesPasos_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocioSimple_contents_coleccionesPasos_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Steps (collections)',
        label='Pasos (colecciones)',
        represents_aggregation=True,
        description2='Collections of individual actions during the course of the Business Process.',
        multiValued=1,
        owner_class_name="BPDProcesoDeNegocioSimple",
        expression="context.objectValues(['BPDColeccionPasos'])",
        computed_types=['BPDColeccionPasos'],
        non_framework_elements=False,
        description='Colecciones de Acciones individuales en que transcurre la ejecucion del Proceso de Negocio.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDProcesoDeNegocioSimple_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDProcesoDeNegocio, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDProcesoDeNegocioSimple(OrderedBaseFolder, BPDProcesoDeNegocio):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDProcesoDeNegocio,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Proceso de Negocio'

    meta_type = 'BPDProcesoDeNegocioSimple'
    portal_type = 'BPDProcesoDeNegocioSimple'


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



    allowed_content_types = ['BPDColeccionPasos', 'BPDColeccionSalidas', 'BPDColeccionEntradas'] + list(getattr(BPDProcesoDeNegocio, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdprocesodenegociosimple.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Un Proceso de negocio  describiendo como alcanzar un objetivo concreto, como un conjunto de informacioones de partida, una serie de pasos, y unas informaciones de salida."
    typeDescMsgId                    =  'gvSIGbpd_BPDProcesoDeNegocioSimple_help'
    archetype_name2                  = 'Business Process'
    typeDescription2                 = '''A Business Process describes how to reach specific goals, and can be described as a source information set, a number of steps, and an output information set.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDProcesoDeNegocioSimple_label'
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


       {'action': "string:${object_url}/TextualRest",
        'category': "object_buttons",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
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
        'category': "object",
        'id': 'mddversions',
        'name': 'Versions',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDInspectCache/",
        'category': "object_buttons",
        'id': 'mddinspectcache',
        'name': 'Inspect Cache',
        'permissions': ("View",),
        'condition': """python:1"""
       },


    )

    _at_rename_after_creation = True

    schema = BPDProcesoDeNegocioSimple_schema

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

registerType(BPDProcesoDeNegocioSimple, PROJECTNAME)
# end of class BPDProcesoDeNegocioSimple

##code-section module-footer #fill in your manual code here
##/code-section module-footer



