# -*- coding: utf-8 -*-
#
# File: BPDSalida.py
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
from Products.gvSIGbpd.BPDArquetipoReferenciable import BPDArquetipoReferenciable
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.ATContentTypes.content.base import ATCTMixin

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    BooleanField(
        name='esRequerido',
        widget=BooleanField._properties['widget'](
            label="Es Requerida",
            label2="Is Required",
            description="Indica que la Salida se producira siempre que concluya exitosamente la ejecucion del Proceso.",
            description2="Whether the Output shall be always produced when the Business Process completes successfully.",
            label_msgid='gvSIGbpd_BPDSalida_attr_esRequerido_label',
            description_msgid='gvSIGbpd_BPDSalida_attr_esRequerido_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica que la Salida se producira siempre que concluya exitosamente la ejecucion del Proceso.",
        duplicates="0",
        label2="Is Required",
        ea_localid="207",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Whether the Output shall be always produced when the Business Process completes successfully.",
        ea_guid="{9F00AC88-2BF9-4b83-B010-B3511669553D}",
        write_permission='Modify portal content',
        scale="0",
        default="1",
        label="Es Requerida",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDSalida"
    ),

    RelationField(
        name='artefactosDeSalida',
        inverse_relation_label="Salidas de Procesos de Negocio",
        inverse_relation_description="Procesos de Negocio donde el Artefacto se produce como Salida, tras el final exitoso de la ejecucion.",
        description="Artefactos producidos como Salida al finalizar exitosamente el Proceso de Negocio.",
        relationship='ArtefactosDeSalida',
        label2="Output Artefacts",
        widget=ReferenceBrowserWidget(
            label="Artefactos de Salida",
            label2="Output Artefacts",
            description="Artefactos producidos como Salida al finalizar exitosamente el Proceso de Negocio.",
            description2="Artefacts produced as outcomes of successfully completed Business Processes.",
            label_msgid='gvSIGbpd_BPDSalida_rel_artefactosDeSalida_label',
            description_msgid='gvSIGbpd_BPDSalida_rel_artefactosDeSalida_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Artefacts produced as outcomes of successfully completed Business Processes.",
        inverse_relation_label2="Business Process Outputs",
        deststyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        write_permission='Modify portal content',
        inverse_relation_field_name='salidasDeProcesosDeNegocio',
        inverse_relation_description2="Business Processes where the Artefact is made available as Output, upon successful completion.",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label="Artefactos de Salida",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='SalidasDeProcesosDeNegocio',
        owner_class_name="BPDSalida"
    ),

    ComputedField(
        name='tituloProcesoDeNegocio',
        widget=ComputedField._properties['widget'](
            label="Proceso de Negocio",
            label2="Business Process",
            description="El titulo del Proceso de Negocio que contiene la Salida.",
            description2="Title of the Business Process containing the Output.",
            label_msgid='gvSIGbpd_BPDSalida_attr_tituloProcesoDeNegocio_label',
            description_msgid='gvSIGbpd_BPDSalida_attr_tituloProcesoDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El titulo del Proceso de Negocio que contiene la Salida.",
        duplicates="0",
        label2="Business Process",
        ea_localid="206",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Title of the Business Process containing the Output.",
        ea_guid="{4288DB0F-52A4-45c6-92FA-8C0AE537B78B}",
        exclude_from_values_form="True",
        scale="0",
        label="Proceso de Negocio",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDSalida",
        expression="context.getPropietario().Title()",
        computed_types="string"
    ),

    ComputedField(
        name='titulosArtefactosDeSalida',
        widget=ComputedField._properties['widget'](
            label="Artefactos de Salida",
            label2="Output Artefacts",
            description="Artefactos producidos como Salida al finalizar exitosamente el Proceso de Negocio.",
            description2="Artefacts produced as outcomes of successfully completed Business Processes.",
            label_msgid='gvSIGbpd_BPDSalida_attr_titulosArtefactosDeSalida_label',
            description_msgid='gvSIGbpd_BPDSalida_attr_titulosArtefactosDeSalida_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Artefactos producidos como Salida al finalizar exitosamente el Proceso de Negocio.",
        duplicates="0",
        label2="Output Artefacts",
        ea_localid="259",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Artefacts produced as outcomes of successfully completed Business Processes.",
        containment="Not Specified",
        ea_guid="{8DFB0E16-2B44-4e1b-8037-12BD9AA79BFC}",
        position="2",
        owner_class_name="BPDSalida",
        label="Artefactos de Salida",
        expression="', '.join( [a.Title() for a in context.getArtefactosDeSalida()])",
        exclude_from_values_form="True"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDSalida_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoReferenciable, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDSalida(OrderedBaseFolder, BPDArquetipoReferenciable):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoReferenciable,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Salida de Proceso de Negocio'

    meta_type = 'BPDSalida'
    portal_type = 'BPDSalida'
    allowed_content_types = [] + list(getattr(BPDArquetipoReferenciable, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdsalida.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Informaciones que puede o debe producir el esfuerzo realizado en el Proceso de Negocio."
    typeDescMsgId =  'gvSIGbpd_BPDSalida_help'
    archetype_name2 = 'business process Output'
    typeDescription2 = '''Information that may be produced during the Business Process execution and delivered at its end.'''
    archetype_name_msgid = 'gvSIGbpd_BPDSalida_label'
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

    schema = BPDSalida_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(BPDSalida, PROJECTNAME)
# end of class BPDSalida

##code-section module-footer #fill in your manual code here
##/code-section module-footer



