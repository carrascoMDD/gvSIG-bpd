# -*- coding: utf-8 -*-
#
# File: BPDRecepcion.py
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
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.base import ATCTMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

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
            label_msgid='gvSIGbpd_BPDRecepcion_attr_detallesPaso_label',
            description_msgid='gvSIGbpd_BPDRecepcion_attr_detallesPaso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
        duplicates="0",
        label2="Step details",
        ea_localid="275",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the fetarues of the Busienss Process Step",
        ea_guid="{4D4B365C-1A09-4399-8229-6B18165D7EEA}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del Paso",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDRecepcion",
        expression="context.fTFLVs([ 'esInicial', 'tituloRemitente','titulosArtefactosRecibidos','ejecutores'])",
        computed_types="string"
    ),

    RelationField(
        name='artefactosRecibidos',
        inverse_relation_label="Recepciones",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion', 'version', 'fechaAdopcion', 'fechaObsolescencia'],
        inverse_relation_description="Recepciones pasos de Proceso de Negocio donde se recibe un Artefacto de este tipo de un participante externo.",
        description="Artefactos que se reciben de un Participante externo en este paso.",
        relationship='ArtefactosRecibidos',
        inverse_relation_field_name='pasosQueRecibenElArtefacto',
        inverse_relation_label2="Received at Business Process Steps",
        label2="Received Artefacts",
        inverse_relation_description2="Business Process Steps where Artefacts of this type are received from external participants.",
        widget=ReferenceBrowserWidget(
            label="Artefactos Recibidos",
            label2="Received Artefacts",
            description="Artefactos que se reciben de un Participante externo en este paso.",
            description2="Artefacts to be received from an external participant during this step.",
            label_msgid='gvSIGbpd_BPDRecepcion_rel_artefactosRecibidos_label',
            description_msgid='gvSIGbpd_BPDRecepcion_rel_artefactosRecibidos_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Artefactos Recibidos",
        description2="Artefacts to be received from an external participant during this step.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='PasosQueRecibenElArtefacto',
        owner_class_name="BPDRecepcion",
        deststyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;"
    ),

    RelationField(
        name='remitente',
        inverse_relation_label="Remitente de Recepciones",
        additional_columns=['abreviatura', 'responsabilidadesClave'],
        inverse_relation_description="Recepciones originadas en este Perfil o Unidad Organizacional.",
        description="El Perfil o Unidad Organizacional que originan la Recepcion.",
        relationship='Remitente',
        inverse_relation_field_name='remitenteDeRecepciones',
        inverse_relation_label2="Sender of Reception steps",
        label2="Sender",
        inverse_relation_description2="Business Process Reception Steps originated by the participant Profile or Organisational Units.",
        widget=ReferenceBrowserWidget(
            label="Remitente",
            label2="Sender",
            description="El Perfil o Unidad Organizacional que originan la Recepcion.",
            description2="Participant Profiles or Organisational Units originating this Reception.",
            label_msgid='gvSIGbpd_BPDRecepcion_rel_remitente_label',
            description_msgid='gvSIGbpd_BPDRecepcion_rel_remitente_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Remitente",
        description2="Participant Profiles or Organisational Units originating this Reception.",
        multiValued=0,
        containment="Unspecified",
        inverse_relationship='RemitenteDeRecepciones',
        owner_class_name="BPDRecepcion",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;"
    ),

    ComputedField(
        name='tituloRemitente',
        widget=ComputedField._properties['widget'](
            label="Remitente",
            label2="Sender",
            description="El Perfil o Unidad Organizacional que originan la Recepcion.",
            description2="Participant Profiles or Organisational Units originating this Reception.",
            label_msgid='gvSIGbpd_BPDRecepcion_attr_tituloRemitente_label',
            description_msgid='gvSIGbpd_BPDRecepcion_attr_tituloRemitente_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El Perfil o Unidad Organizacional que originan la Recepcion.",
        duplicates="0",
        label2="Sender",
        ea_localid="272",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Participant Profiles or Organisational Units originating this Reception.",
        containment="Not Specified",
        ea_guid="{3A160F44-12E6-4fa6-A441-8AA6D4F93364}",
        position="0",
        owner_class_name="BPDRecepcion",
        label="Remitente",
        expression="context.fFV('remitente')",
        exclude_from_values_form="True"
    ),

    ComputedField(
        name='titulosArtefactosRecibidos',
        widget=ComputedField._properties['widget'](
            label="Artefactos Recibidos",
            label2="Received Artefacts",
            description="Artefactos que se reciben de un Participante externo en este paso.",
            description2="Artefacts to be received from an external participant during this step.",
            label_msgid='gvSIGbpd_BPDRecepcion_attr_titulosArtefactosRecibidos_label',
            description_msgid='gvSIGbpd_BPDRecepcion_attr_titulosArtefactosRecibidos_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Artefactos que se reciben de un Participante externo en este paso.",
        duplicates="0",
        label2="Received Artefacts",
        ea_localid="265",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Artefacts to be received from an external participant during this step.",
        containment="Not Specified",
        ea_guid="{B84AF098-0284-4886-8B03-CAB8DB352F1E}",
        position="1",
        owner_class_name="BPDRecepcion",
        label="Artefactos Recibidos",
        expression="context.fFV('artefactosRecibidos')",
        exclude_from_values_form="True"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDRecepcion_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDPasoGeneral, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDRecepcion(OrderedBaseFolder, BPDPasoGeneral):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDPasoGeneral,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Recepcion'

    meta_type = 'BPDRecepcion'
    portal_type = 'BPDRecepcion'
    allowed_content_types = [] + list(getattr(BPDPasoGeneral, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdrecepcion.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Representa un Paso de Proceso en que se espera y recibe una informacion externa."
    typeDescMsgId =  'gvSIGbpd_BPDRecepcion_help'
    archetype_name2 = 'Receive'
    typeDescription2 = '''Represents a Business Process Step to wait to receive some information from the outside of the boudaries of the Business Process.'''
    archetype_name_msgid = 'gvSIGbpd_BPDRecepcion_label'
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

    schema = BPDRecepcion_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('manage_afterAdd')
    def manage_afterAdd(self,item,container):
        """
        """
        
        return self.pHandle_manage_afterAdd(  item, container)

registerType(BPDRecepcion, PROJECTNAME)
# end of class BPDRecepcion

##code-section module-footer #fill in your manual code here
##/code-section module-footer



