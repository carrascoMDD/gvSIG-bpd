# -*- coding: utf-8 -*-
#
# File: BPDDecision.py
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
from Products.gvSIGbpd.BPDPasoGeneral import BPDPasoGeneral
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.base import ATCTMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='condicionSiguientePaso',
        widget=TextAreaWidget(
            label="Condicion",
            label2="Condition",
            description="Condicion que se evalua para determinar el siguiente Paso por el que continua el Proceso de Negocio.",
            description2="Criteria for selection of the next Step to execute when the Decision completes.",
            label_msgid='gvSIGbpd_BPDDecision_attr_condicionSiguientePaso_label',
            description_msgid='gvSIGbpd_BPDDecision_attr_condicionSiguientePaso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Condicion que se evalua para determinar el siguiente Paso por el que continua el Proceso de Negocio.",
        duplicates="0",
        label2="Condition",
        ea_localid="218",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Criteria for selection of the next Step to execute when the Decision completes.",
        ea_guid="{F3C63933-CCBA-4ceb-BB89-4D31D31DE0FB}",
        write_permission='Modify portal content',
        scale="0",
        label="Condicion",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDDecision"
    ),

    ComputedField(
        name='detallesPaso',
        widget=ComputedField._properties['widget'](
            label="Detalles del Paso",
            label2="Step details",
            description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
            description2="Details about the fetarues of the Busienss Process Step",
            label_msgid='gvSIGbpd_BPDDecision_attr_detallesPaso_label',
            description_msgid='gvSIGbpd_BPDDecision_attr_detallesPaso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
        duplicates="0",
        label2="Step details",
        ea_localid="281",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the fetarues of the Busienss Process Step",
        ea_guid="{42E93CA4-2C92-43c9-B67B-12BB221B6299}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del Paso",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDDecision",
        expression="context.fTFLVs([ 'esInicial','condicionSiguientePaso','ejecutores'])",
        computed_types="string"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDDecision_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDPasoGeneral, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDDecision(OrderedBaseFolder, BPDPasoGeneral):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDPasoGeneral,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Decision'

    meta_type = 'BPDDecision'
    portal_type = 'BPDDecision'
    allowed_content_types = [] + list(getattr(BPDPasoGeneral, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpddecision.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Decision"
    typeDescMsgId =  'gvSIGbpd_BPDDecision_help'
    archetype_name2 = 'Decision'
    typeDescription2 = '''A Decision to take to select the next Business Process Step, from the ones composing the Business Process.'''
    archetype_name_msgid = 'gvSIGbpd_BPDDecision_label'
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
        'permissions': ("Modify portal content",),
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
        'permissions': ("Manage properties",),
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

    schema = BPDDecision_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('manage_afterAdd')
    def manage_afterAdd(self,item,container):
        """
        """
        
        return self.pHandle_manage_afterAdd(  item, container)

registerType(BPDDecision, PROJECTNAME)
# end of class BPDDecision

##code-section module-footer #fill in your manual code here
##/code-section module-footer



