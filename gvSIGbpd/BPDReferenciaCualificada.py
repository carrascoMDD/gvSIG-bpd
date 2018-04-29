# -*- coding: utf-8 -*-
#
# File: BPDReferenciaCualificada.py
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
from Products.gvSIGbpd.BPDArquetipo import BPDArquetipo
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    RelationField(
        name='referidosCualificados',
        inverse_relation_label="Referentes Cualificados",
        inverse_relation_description="Referencias Cualificadas refiriendo a este elemento.",
        description="Elementos referidos desde esta Referencia Cualificada.",
        relationship='ReferidosCualificados',
        label2="Refered Elements",
        widget=ReferenceBrowserWidget(
            label="Elementos cualificadamente Referidos",
            label2="Refered Elements",
            description="Elementos referidos desde esta Referencia Cualificada.",
            description2="Elements refered to by this qualified Reference.",
            label_msgid='gvSIGbpd_BPDReferenciaCualificada_rel_referidosCualificados_label',
            description_msgid='gvSIGbpd_BPDReferenciaCualificada_rel_referidosCualificados_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Elements refered to by this qualified Reference.",
        inverse_relation_label2="Refering Qualified References",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='referentesCualificados',
        inverse_relation_description2="Qualified References referencing this element.",
        label="Elementos cualificadamente Referidos",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ReferentesCualificados',
        owner_class_name="BPDReferenciaCualificada"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDReferenciaCualificada_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipo, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDReferenciaCualificada(OrderedBaseFolder, BPDArquetipo):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipo,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Referencia Cualificada'

    meta_type = 'BPDReferenciaCualificada'
    portal_type = 'BPDReferenciaCualificada'
    allowed_content_types = [] + list(getattr(BPDArquetipo, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdreferenciacualificada.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Permite referir a otros elementos de la aplicacion, incluyendo ademas un texto cualificando la referencia."
    typeDescMsgId =  'gvSIGbpd_BPDReferenciaCualificada_help'
    archetype_name2 = 'Qualified Reference'
    typeDescription2 = '''Allows to reference other application elements, including an additional title and description that qualifies the reference.'''
    archetype_name_msgid = 'gvSIGbpd_BPDReferenciaCualificada_label'
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

    schema = BPDReferenciaCualificada_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(BPDReferenciaCualificada, PROJECTNAME)
# end of class BPDReferenciaCualificada

##code-section module-footer #fill in your manual code here
##/code-section module-footer



