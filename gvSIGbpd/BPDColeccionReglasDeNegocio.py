# -*- coding: utf-8 -*-
#
# File: BPDColeccionReglasDeNegocio.py
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
        name='reglasDeNegocio',
        widget=ComputedWidget(
            label="Reglas de Negocio",
            label2="Business Rules",
            description="Reglas deNegocio que se derivan de las politicas de Negocio, y dirigen los Procesos de Negocio de la Organizacion.",
            description2="Business Rules derived from Business Policies, and driving the Business Process in the Organisation.",
            label_msgid='gvSIGbpd_BPDColeccionReglasDeNegocio_contents_reglasDeNegocio_label',
            description_msgid='gvSIGbpd_BPDColeccionReglasDeNegocio_contents_reglasDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Business Rules',
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label='Reglas de Negocio',
        description2='Business Rules derived from Business Policies, and driving the Business Process in the Organisation.',
        multiValued=1,
        owner_class_name="BPDColeccionReglasDeNegocio",
        expression="context.objectValues(['BPDReglaDeNegocio'])",
        computed_types=['BPDReglaDeNegocio'],
        represents_aggregation=True,
        description='Reglas deNegocio que se derivan de las politicas de Negocio, y dirigen los Procesos de Negocio de la Organizacion.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDColeccionReglasDeNegocio_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDColeccionArquetipos, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDColeccionReglasDeNegocio(OrderedBaseFolder, BPDColeccionArquetipos):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDColeccionArquetipos,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Coleccion de Reglas de Negocio'

    meta_type = 'BPDColeccionReglasDeNegocio'
    portal_type = 'BPDColeccionReglasDeNegocio'
    allowed_content_types = ['BPDReglaDeNegocio'] + list(getattr(BPDColeccionArquetipos, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'BPDColeccionReglasDeNegocio.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Coleccion de Reglas deNegocio que se derivan de las politicas de Negocio, y dirigen los Procesos de Negocio de la Organizacion."
    typeDescMsgId =  'gvSIGbpd_BPDColeccionReglasDeNegocio_help'
    archetype_name2 = 'Business Rules collection'
    typeDescription2 = '''Collections of Business Rules derived from Business Policies, and driving the Business Process in the Organisation.'''
    archetype_name_msgid = 'gvSIGbpd_BPDColeccionReglasDeNegocio_label'
    factory_methods = None
    factory_enablers = None


    actions =  (


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
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


       {'action': "string:${object_url}/MDDExport",
        'category': "object",
        'id': 'mddexport',
        'name': 'Export',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("ManageProperties",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/TextualRest",
        'category': "object",
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

    schema = BPDColeccionReglasDeNegocio_schema

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

registerType(BPDColeccionReglasDeNegocio, PROJECTNAME)
# end of class BPDColeccionReglasDeNegocio

##code-section module-footer #fill in your manual code here
##/code-section module-footer



