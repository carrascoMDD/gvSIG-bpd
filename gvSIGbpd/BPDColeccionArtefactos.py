# -*- coding: utf-8 -*-
#
# File: BPDColeccionArtefactos.py
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
        name='artefactos',
        widget=ComputedWidget(
            label="Artefactos",
            label2="Artefacts",
            description="Artefactos que se producen, consumen, consultan, editan, y en general son el objeto del esfuerzo de la Organizacion.",
            description2="Artefacts produced, consumed, consulted, edited, or otherwise object of the Organisation effort.",
            label_msgid='gvSIGbpd_BPDColeccionArtefactos_contents_artefactos_label',
            description_msgid='gvSIGbpd_BPDColeccionArtefactos_contents_artefactos_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Artefacts',
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label='Artefactos',
        represents_aggregation=True,
        description2='Artefacts produced, consumed, consulted, edited, or otherwise object of the Organisation effort.',
        multiValued=1,
        owner_class_name="BPDColeccionArtefactos",
        expression="context.objectValues(['BPDArtefacto'])",
        computed_types=['BPDArtefacto'],
        non_framework_elements=False,
        description='Artefactos que se producen, consumen, consultan, editan, y en general son el objeto del esfuerzo de la Organizacion.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDColeccionArtefactos_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDColeccionArquetipos, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDColeccionArtefactos(OrderedBaseFolder, BPDColeccionArquetipos):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDColeccionArquetipos,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Coleccion de Artefactos'

    meta_type = 'BPDColeccionArtefactos'
    portal_type = 'BPDColeccionArtefactos'
    allowed_content_types = ['BPDArtefacto'] + list(getattr(BPDColeccionArquetipos, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'BPDColeccionArtefactos.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Coleccion de Artefactos que se producen, consumen, consultan, editan, y en general son el objeto del esfuerzo de la Organizacion."
    typeDescMsgId =  'gvSIGbpd_BPDColeccionArtefactos_help'
    archetype_name2 = 'Artefacts Collection'
    typeDescription2 = '''Collection of Artefacts produced, consumed, consulted, edited, or otherwise object of the Organisation effort.'''
    archetype_name_msgid = 'gvSIGbpd_BPDColeccionArtefactos_label'
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
        'permissions': ("ModifyPortalContent",),
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
        'permissions': ("ManageProperties",),
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

    schema = BPDColeccionArtefactos_schema

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

registerType(BPDColeccionArtefactos, PROJECTNAME)
# end of class BPDColeccionArtefactos

##code-section module-footer #fill in your manual code here
##/code-section module-footer



