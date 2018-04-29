# -*- coding: utf-8 -*-
#
# File: BPDColeccionSalidas.py
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
        name='salidas',
        widget=ComputedWidget(
            label="Salidas",
            label2="Outputs",
            description="Informaciones que pueden estar o  estaran disponibles cuando haya concluido exitosamente el Proceso de Negocio.",
            description2="Informations that may or will be made available upon successful completion of the Business Process.",
            label_msgid='gvSIGbpd_BPDColeccionSalidas_contents_salidas_label',
            description_msgid='gvSIGbpd_BPDColeccionSalidas_contents_salidas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Outputs',
        additional_columns=['esRequerido', 'titulosArtefactosDeSalida'],
        label='Salidas',
        description2='Informations that may or will be made available upon successful completion of the Business Process.',
        multiValued=1,
        owner_class_name="BPDColeccionSalidas",
        expression="context.objectValues(['BPDSalida'])",
        computed_types=['BPDSalida'],
        represents_aggregation=True,
        description='Informaciones que pueden estar o  estaran disponibles cuando haya concluido exitosamente el Proceso de Negocio.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDColeccionSalidas_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDColeccionArquetipos, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDColeccionSalidas(OrderedBaseFolder, BPDColeccionArquetipos):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDColeccionArquetipos,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Coleccion de Salidas'

    meta_type = 'BPDColeccionSalidas'
    portal_type = 'BPDColeccionSalidas'
    allowed_content_types = ['BPDSalida'] + list(getattr(BPDColeccionArquetipos, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    #content_icon = 'BPDColeccionSalidas.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Coleccion de Informaciones que pueden estar o  estaran disponibles cuando haya concluido exitosamente el Proceso de Negocio."
    typeDescMsgId =  'gvSIGbpd_BPDColeccionSalidas_help'
    archetype_name2 = 'Outputs collection'
    typeDescription2 = '''Collection of Informations that may or will be made available upon successful completion of the Business Process.'''
    archetype_name_msgid = 'gvSIGbpd_BPDColeccionSalidas_label'
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

    schema = BPDColeccionSalidas_schema

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

registerType(BPDColeccionSalidas, PROJECTNAME)
# end of class BPDColeccionSalidas

##code-section module-footer #fill in your manual code here
##/code-section module-footer



