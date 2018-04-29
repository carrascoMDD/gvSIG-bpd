# -*- coding: utf-8 -*-
#
# File: BPDArquetipoReferenciable.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    RelationField(
        name='referentes',
        inverse_relation_label="Elementos Referenciados",
        inverse_relation_description="Elementos de la aplicacion referidos desde este elemento.",
        description="Elementos de la aplicacion que refieren al presente elemento.",
        relationship='Referentes',
        label2="Refering elements",
        widget=ReferenceBrowserWidget(
            label="Elementos Referentes",
            label2="Refering elements",
            description="Elementos de la aplicacion que refieren al presente elemento.",
            description2="Application elements referencing this one.",
            label_msgid='gvSIGbpd_BPDArquetipoReferenciable_rel_referentes_label',
            description_msgid='gvSIGbpd_BPDArquetipoReferenciable_rel_referentes_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Application elements referencing this one.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Referenced elements",
        dependency_supplier=True,
        inverse_relation_field_name='referidos',
        inverse_relation_description2="Elements in the application referenced by this element.",
        write_permission='Modify portal content',
        label="Elementos Referentes",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='Referidos'
    ),

    RelationField(
        name='referidos',
        inverse_relation_label="Elementos Referentes",
        inverse_relation_description="Elementos de la aplicacion que refieren al presente elemento.",
        description="Elementos de la aplicacion referidos desde este elemento.",
        relationship='Referidos',
        label2="Referenced elements",
        widget=ReferenceBrowserWidget(
            label="Elementos Referenciados",
            label2="Referenced elements",
            description="Elementos de la aplicacion referidos desde este elemento.",
            description2="Elements in the application referenced by this element.",
            label_msgid='gvSIGbpd_BPDArquetipoReferenciable_rel_referidos_label',
            description_msgid='gvSIGbpd_BPDArquetipoReferenciable_rel_referidos_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Elements in the application referenced by this element.",
        inverse_relation_label2="Refering elements",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='referentes',
        inverse_relation_description2="Application elements referencing this one.",
        label="Elementos Referenciados",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='Referentes',
        owner_class_name="BPDArquetipoReferenciable"
    ),

    ComputedField(
        name='referenciasCualificadas',
        widget=ComputedWidget(
            label="Referencias Cualificadas",
            label2="Qualified References",
            description="Referencias a otros elementos, cualificadas con un titulo y una descripcion.",
            description2="References to other elements, qualified with a title and a description.",
            label_msgid='gvSIGbpd_BPDArquetipoReferenciable_contents_referenciasCualificadas_label',
            description_msgid='gvSIGbpd_BPDArquetipoReferenciable_contents_referenciasCualificadas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Qualified References',
        label='Referencias Cualificadas',
        represents_aggregation=True,
        description2='References to other elements, qualified with a title and a description.',
        multiValued=1,
        owner_class_name="BPDArquetipoReferenciable",
        expression="context.objectValues(['BPDReferenciaCualificada'])",
        computed_types=['BPDReferenciaCualificada'],
        non_framework_elements=False,
        description='Referencias a otros elementos, cualificadas con un titulo y una descripcion.'
    ),

    ComputedField(
        name='todosRelacionados',
        widget=ReferenceBrowserWidget(
            label="All Related Elements",
            label2="Todos los Elementos relacionados",
            description="All Related Elements",
            description2="Todos los Elementos relacionados",
            label_msgid='gvSIGbpd_BPDArquetipoReferenciable_attr_todosRelacionados_label',
            description_msgid='gvSIGbpd_BPDArquetipoReferenciable_attr_todosRelacionados_help',
            i18n_domain='gvSIGbpd',
        ),
        description="All Related Elements",
        relationship="TodosRelacionados",
        duplicates="0",
        label2="Todos los Elementos relacionados",
        ea_localid="179",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Todos los Elementos relacionados",
        ea_guid="{9FCC83A3-8C37-4f7f-B1DD-3BB53D1CBFE7}",
        scale="0",
        expression="context.getReferidos() + context.getReferentes() + context.getRelatedItems() + [ unReferente.getPropietario() for unReferente in context.getReferentesCualificados() ]",
        label="All Related Elements",
        length="0",
        exclude_from_traversalconfig="True",
        multiValued=1,
        containment="Not Specified",
        position="0",
        owner_class_name="BPDArquetipoReferenciable",
        exclude_from_views="[ 'Textual', 'Tabular',  ]",
        computed_types="['ANYTYPE',]",
        non_framework_elements="True"
    ),

    RelationField(
        name='referentesCualificados',
        inverse_relation_label="Elementos cualificadamente Referidos",
        inverse_relation_description="Elementos referidos desde esta Referencia Cualificada.",
        description="Referencias Cualificadas refiriendo a este elemento.",
        relationship='ReferentesCualificados',
        label2="Refering Qualified References",
        widget=ReferenceBrowserWidget(
            label="Referentes Cualificados",
            label2="Refering Qualified References",
            description="Referencias Cualificadas refiriendo a este elemento.",
            description2="Qualified References referencing this element.",
            label_msgid='gvSIGbpd_BPDArquetipoReferenciable_rel_referentesCualificados_label',
            description_msgid='gvSIGbpd_BPDArquetipoReferenciable_rel_referentesCualificados_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Qualified References referencing this element.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Refered Elements",
        dependency_supplier=True,
        inverse_relation_field_name='referidosCualificados',
        inverse_relation_description2="Elements refered to by this qualified Reference.",
        write_permission='Modify portal content',
        label="Referentes Cualificados",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ReferidosCualificados'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDArquetipoReferenciable_schema = getattr(BPDArquetipo, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDArquetipoReferenciable(BPDArquetipo):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BPDArquetipo,'__implements__',()),)

    allowed_content_types = ['BPDReferenciaCualificada'] + list(getattr(BPDArquetipo, 'allowed_content_types', []))

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

    schema = BPDArquetipoReferenciable_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDArquetipoReferenciable

##code-section module-footer #fill in your manual code here
##/code-section module-footer



