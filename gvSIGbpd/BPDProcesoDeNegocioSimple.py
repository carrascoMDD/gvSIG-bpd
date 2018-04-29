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
        description='Colecciones de Informaciones que pueden o deben estar disponibles para poder dar comienzo al Proceso de Negocio.',
        label2='Inputs (collections)',
        label='Entradas (colecciones)',
        description2='Collections of Informations that must or may be available to start the Business Process.',
        multiValued=1,
        owner_class_name="BPDProcesoDeNegocioSimple",
        expression="context.objectValues(['BPDColeccionEntradas'])",
        computed_types=['BPDColeccionEntradas'],
        represents_aggregation=True
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
        description='Colecciones de Informaciones que pueden estar o  estaran disponibles cuando haya concluido exitosamente el Proceso de Negocio.',
        label2='Outputs (collections)',
        label='Salidas (colecciones)',
        description2='Collections of Informations that may or will be made available upon successful completion of the Business Process.',
        multiValued=1,
        owner_class_name="BPDProcesoDeNegocioSimple",
        expression="context.objectValues(['BPDColeccionSalidas'])",
        computed_types=['BPDColeccionSalidas'],
        represents_aggregation=True
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
        description='Colecciones de Acciones individuales en que transcurre la ejecucion del Proceso de Negocio.',
        label2='Steps (collections)',
        label='Pasos (colecciones)',
        description2='Collections of individual actions during the course of the Business Process.',
        multiValued=1,
        owner_class_name="BPDProcesoDeNegocioSimple",
        expression="context.objectValues(['BPDColeccionPasos'])",
        computed_types=['BPDColeccionPasos'],
        represents_aggregation=True
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
    allowed_content_types = ['BPDColeccionPasos', 'BPDColeccionSalidas', 'BPDColeccionEntradas'] + list(getattr(BPDProcesoDeNegocio, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdprocesodenegociosimple.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Un Proceso de negocio  describiendo como alcanzar un objetivo concreto, como un conjunto de informacioones de partida, una serie de pasos, y unas informaciones de salida."
    typeDescMsgId =  'gvSIGbpd_BPDProcesoDeNegocioSimple_help'
    archetype_name2 = 'Business Process'
    typeDescription2 = '''A Business Process describes how to reach specific goals, and can be described as a source information set, a number of steps, and an output information set.'''
    archetype_name_msgid = 'gvSIGbpd_BPDProcesoDeNegocioSimple_label'
    factory_methods = None


    actions =  (


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("Manage properties",),
        'condition': 'python:1'
       },


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/MDDExport",
        'category': "object",
        'id': 'mddexport',
        'name': 'Export',
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


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("Modify portal content",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/TextualRest",
        'category': "object",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = BPDProcesoDeNegocioSimple_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(BPDProcesoDeNegocioSimple, PROJECTNAME)
# end of class BPDProcesoDeNegocioSimple

##code-section module-footer #fill in your manual code here
##/code-section module-footer



