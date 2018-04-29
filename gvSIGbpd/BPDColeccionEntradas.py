# -*- coding: utf-8 -*-
#
# File: BPDColeccionEntradas.py
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
from Products.gvSIGbpd.BPDColeccionArquetipos import BPDColeccionArquetipos
from Products.gvSIGbpd.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='entradas',
        widget=ComputedWidget(
            label="Entradas",
            label2="Inputs",
            description="Informaciones que pueden o deben estar disponibles para poder dar comienzo al Proceso de Negocio.",
            description2="Informations that must or may be available to start the Business Process.",
            label_msgid='gvSIGbpd_BPDColeccionEntradas_contents_entradas_label',
            description_msgid='gvSIGbpd_BPDColeccionEntradas_contents_entradas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Inputs',
        additional_columns=['esRequerido', 'fuenteDeInformacion', 'valorDefecto', 'titulosArtefactosDeEntrada'],
        label='Entradas',
        description2='Informations that must or may be available to start the Business Process.',
        multiValued=1,
        owner_class_name="BPDColeccionEntradas",
        expression="context.objectValues(['BPDEntrada'])",
        computed_types=['BPDEntrada'],
        represents_aggregation=True,
        description='Informaciones que pueden o deben estar disponibles para poder dar comienzo al Proceso de Negocio.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDColeccionEntradas_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDColeccionArquetipos, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDColeccionEntradas(OrderedBaseFolder, BPDColeccionArquetipos):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDColeccionArquetipos,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Coleccion de Entradas'

    meta_type = 'BPDColeccionEntradas'
    portal_type = 'BPDColeccionEntradas'
    allowed_content_types = ['BPDEntrada'] + list(getattr(BPDColeccionArquetipos, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'BPDColeccionEntradas.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', 'Anexos',  'General', )
    typeDescription = "Coleccion de Informaciones que pueden o deben estar disponibles para poder dar comienzo al Proceso de Negocio."
    typeDescMsgId =  'gvSIGbpd_BPDColeccionEntradas_help'
    archetype_name2 = 'Inputs collection'
    typeDescription2 = '''Collection of Informations that must or may be available to start the Business Process.'''
    archetype_name_msgid = 'gvSIGbpd_BPDColeccionEntradas_label'
    factory_methods = None


    actions =  (


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("ManageProperties",),
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


       {'action': "string:${object_url}/TextualRest",
        'category': "object",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("ModifyPortalContent",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = BPDColeccionEntradas_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(BPDColeccionEntradas, PROJECTNAME)
# end of class BPDColeccionEntradas

##code-section module-footer #fill in your manual code here
##/code-section module-footer



