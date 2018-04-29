# -*- coding: utf-8 -*-
#
# File: BPDExitoFinal.py
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
from Products.gvSIGbpd.BPDPasoGestorExcepciones import BPDPasoGestorExcepciones
from Products.gvSIGbpd.BPDPasoMinimo import BPDPasoMinimo
from Products.gvSIGbpd.BPDPasoConAnteriores import BPDPasoConAnteriores
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.ATContentTypes.content.base import ATCTMixin

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='detallesPaso',
        widget=ComputedField._properties['widget'](
            label="Detalles del Paso",
            label2="Step details",
            description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
            description2="Details about the fetarues of the Busienss Process Step",
            label_msgid='gvSIGbpd_BPDExitoFinal_attr_detallesPaso_label',
            description_msgid='gvSIGbpd_BPDExitoFinal_attr_detallesPaso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
        duplicates="0",
        label2="Step details",
        ea_localid="285",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the fetarues of the Busienss Process Step",
        ea_guid="{6FA7B4A1-D726-41c7-AA1D-570594B06708}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del Paso",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDExitoFinal",
        expression="str()",
        computed_types="string"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDExitoFinal_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDPasoGestorExcepciones, 'schema', Schema(())).copy() + \
    getattr(BPDPasoMinimo, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConAnteriores, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDExitoFinal(OrderedBaseFolder, BPDPasoGestorExcepciones, BPDPasoMinimo, BPDPasoConAnteriores):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDPasoGestorExcepciones,'__implements__',()),) + (getattr(BPDPasoMinimo,'__implements__',()),) + (getattr(BPDPasoConAnteriores,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Exito Final'

    meta_type = 'BPDExitoFinal'
    portal_type = 'BPDExitoFinal'
    allowed_content_types = [] + list(getattr(BPDPasoGestorExcepciones, 'allowed_content_types', [])) + list(getattr(BPDPasoMinimo, 'allowed_content_types', [])) + list(getattr(BPDPasoConAnteriores, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdexitofinal.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Indica el final del Proceso de Negocio con un resultado satisfactorio."
    typeDescMsgId =  'gvSIGbpd_BPDExitoFinal_help'
    archetype_name2 = 'Success'
    typeDescription2 = '''Indicates that the Business Process completes with successful result.'''
    archetype_name_msgid = 'gvSIGbpd_BPDExitoFinal_label'
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

    schema = BPDExitoFinal_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(BPDExitoFinal, PROJECTNAME)
# end of class BPDExitoFinal

##code-section module-footer #fill in your manual code here
##/code-section module-footer



