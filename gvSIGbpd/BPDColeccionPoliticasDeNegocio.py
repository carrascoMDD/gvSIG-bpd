# -*- coding: utf-8 -*-
#
# File: BPDColeccionPoliticasDeNegocio.py
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
        name='politicasDeNegocio',
        widget=ComputedWidget(
            label="Politicas de Negocio",
            label2="Business Policies",
            description="Politicas de Negocio que gobiernan la Organizacion y sus Procesos de Negocio, y constituyen la base de las Reglas de Negocio.",
            description2="Business Policies  governing the Organisation and its Business Processes, and constitute the basis for the Business Rules.",
            label_msgid='gvSIGbpd_BPDColeccionPoliticasDeNegocio_contents_politicasDeNegocio_label',
            description_msgid='gvSIGbpd_BPDColeccionPoliticasDeNegocio_contents_politicasDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Business Policies',
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label='Politicas de Negocio',
        description2='Business Policies  governing the Organisation and its Business Processes, and constitute the basis for the Business Rules.',
        multiValued=1,
        owner_class_name="BPDColeccionPoliticasDeNegocio",
        expression="context.objectValues(['BPDPoliticaDeNegocio'])",
        computed_types=['BPDPoliticaDeNegocio'],
        represents_aggregation=True,
        description='Politicas de Negocio que gobiernan la Organizacion y sus Procesos de Negocio, y constituyen la base de las Reglas de Negocio.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDColeccionPoliticasDeNegocio_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDColeccionArquetipos, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDColeccionPoliticasDeNegocio(OrderedBaseFolder, BPDColeccionArquetipos):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDColeccionArquetipos,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Coleccion de Politicas de Negocio'

    meta_type = 'BPDColeccionPoliticasDeNegocio'
    portal_type = 'BPDColeccionPoliticasDeNegocio'
    allowed_content_types = ['BPDPoliticaDeNegocio'] + list(getattr(BPDColeccionArquetipos, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'BPDColeccionPoliticasDeNegocio.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Coleccion de Politicas de Negocio que gobiernan la Organizacion y sus Procesos de Negocio, y constituyen la base de las Reglas de Negocio."
    typeDescMsgId =  'gvSIGbpd_BPDColeccionPoliticasDeNegocio_help'
    archetype_name2 = 'Business Policies collection'
    typeDescription2 = '''Collection of Business Policies  governing the Organisation and its Business Processes, and constitute the basis for the Business Rules.'''
    archetype_name_msgid = 'gvSIGbpd_BPDColeccionPoliticasDeNegocio_label'
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

    schema = BPDColeccionPoliticasDeNegocio_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(BPDColeccionPoliticasDeNegocio, PROJECTNAME)
# end of class BPDColeccionPoliticasDeNegocio

##code-section module-footer #fill in your manual code here
##/code-section module-footer



