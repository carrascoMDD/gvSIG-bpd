# -*- coding: utf-8 -*-
#
# File: BPDEntrada.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    RelationField(
        name='artefactosDeEntrada',
        inverse_relation_label="Entrada a Procesos de Negocio",
        inverse_relation_description="Entradas a Procesos de Negocio en que el Artefacto debe estar disponible, para poder comenzar la ejecucion.",
        description="Artefactos que deben estar disponibles para comenzar el Proceso de Negocio",
        relationship='BPDArtefactosDeEntrada',
        label2="Input Artefacts",
        widget=ReferenceBrowserWidget(
            label="Artefactos de Entrada",
            label2="Input Artefacts",
            description="Artefactos que deben estar disponibles para comenzar el Proceso de Negocio",
            description2="Artefacts required as input to allow the start of the Business Processes.",
            label_msgid='gvSIGbpd_BPDEntrada_rel_artefactosDeEntrada_label',
            description_msgid='gvSIGbpd_BPDEntrada_rel_artefactosDeEntrada_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Artefacts required as input to allow the start of the Business Processes.",
        inverse_relation_label2="Input to Business Processes",
        deststyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        write_permission='Modify portal content',
        inverse_relation_field_name='entradasAProcesosDeNegocio',
        inverse_relation_description2="Inputs to Business Processes where the Artefact must be made available , in order  to start execution.",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label="Artefactos de Entrada",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDEntradasAProcesosDeNegocio',
        owner_class_name="BPDEntrada"
    ),

    BooleanField(
        name='esRequerida',
        widget=BooleanField._properties['widget'](
            label="Es Requerida",
            label2="Is Required",
            description="Indica si la Entrada es absolutamente necesaria para la ejecucion del Proceso.",
            description2="Whether the Input is absolutely needed in order to start the Business Process.",
            label_msgid='gvSIGbpd_BPDEntrada_attr_esRequerida_label',
            description_msgid='gvSIGbpd_BPDEntrada_attr_esRequerida_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica si la Entrada es absolutamente necesaria para la ejecucion del Proceso.",
        duplicates="0",
        label2="Is Required",
        ea_localid="209",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Whether the Input is absolutely needed in order to start the Business Process.",
        ea_guid="{7031C4F3-C2D3-4413-8CFB-E034B8BB337C}",
        write_permission='Modify portal content',
        scale="0",
        default="1",
        label="Es Requerida",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDEntrada"
    ),

    TextField(
        name='fuenteDeInformacion',
        widget=TextAreaWidget(
            label="Fuente de Informacion",
            label2="Sources of Information",
            description="Identifica de donde se debe obtener la informacion de Entrada.",
            description2="Identifies where to obtain the input information.",
            label_msgid='gvSIGbpd_BPDEntrada_attr_fuenteDeInformacion_label',
            description_msgid='gvSIGbpd_BPDEntrada_attr_fuenteDeInformacion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Identifica de donde se debe obtener la informacion de Entrada.",
        duplicates="0",
        label2="Sources of Information",
        ea_localid="210",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Identifies where to obtain the input information.",
        ea_guid="{1520DE18-1E53-4705-9D10-E8991D747C47}",
        write_permission='Modify portal content',
        scale="0",
        label="Fuente de Informacion",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDEntrada"
    ),

    ComputedField(
        name='tituloProcesoDeNegocio',
        widget=ComputedField._properties['widget'](
            label="Proceso de Negocio",
            label2="Business Process",
            description="El titulo del Proceso de Negocio que contiene la Entrada",
            description2="Title of the Business Process containing the Input.",
            label_msgid='gvSIGbpd_BPDEntrada_attr_tituloProcesoDeNegocio_label',
            description_msgid='gvSIGbpd_BPDEntrada_attr_tituloProcesoDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El titulo del Proceso de Negocio que contiene la Entrada",
        duplicates="0",
        label2="Business Process",
        ea_localid="208",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Title of the Business Process containing the Input.",
        ea_guid="{B6D6085C-B18E-4b26-B8E1-45ED0329A7DA}",
        exclude_from_values_form="True",
        scale="0",
        label="Proceso de Negocio",
        length="0",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDEntrada",
        expression="context.getPropietario().Title()",
        computed_types="string"
    ),

    ComputedField(
        name='titulosArtefactosDeEntrada',
        widget=ComputedField._properties['widget'](
            label="Artefactos de Entrada",
            label2="Input Artefacts",
            description="Artefactos que deben estar disponibles para comenzar el Proceso de Negocio",
            description2="Artefacts required as input to allow the start of the Business Processes.",
            label_msgid='gvSIGbpd_BPDEntrada_attr_titulosArtefactosDeEntrada_label',
            description_msgid='gvSIGbpd_BPDEntrada_attr_titulosArtefactosDeEntrada_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Artefactos que deben estar disponibles para comenzar el Proceso de Negocio",
        duplicates="0",
        label2="Input Artefacts",
        ea_localid="260",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Artefacts required as input to allow the start of the Business Processes.",
        containment="Not Specified",
        ea_guid="{D6D11F45-DE22-463d-A8FC-1299E58E21B6}",
        position="4",
        owner_class_name="BPDEntrada",
        label="Artefactos de Entrada",
        expression="', '.join( [a.Title() for a in context.getArtefactosDeEntrada()])",
        exclude_from_values_form="True"
    ),

    TextField(
        name='valorDefecto',
        widget=TextAreaWidget(
            label="Valor por Defecto",
            label2="Default Value",
            description="El valor que se toma por defecto para la informacion de entrada, cuando no se suministra un valor de entrada.",
            description2="The Input's default value, if none is explicitely supplied.",
            label_msgid='gvSIGbpd_BPDEntrada_attr_valorDefecto_label',
            description_msgid='gvSIGbpd_BPDEntrada_attr_valorDefecto_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El valor que se toma por defecto para la informacion de entrada, cuando no se suministra un valor de entrada.",
        duplicates="0",
        label2="Default Value",
        ea_localid="211",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="The Input's default value, if none is explicitely supplied.",
        ea_guid="{B4741C35-A7EE-4563-B8EA-03EF64AC7606}",
        write_permission='Modify portal content',
        scale="0",
        label="Valor por Defecto",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDEntrada"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDEntrada_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoReferenciable, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDEntrada(OrderedBaseFolder, BPDArquetipoReferenciable):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoReferenciable,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Entrada'

    meta_type = 'BPDEntrada'
    portal_type = 'BPDEntrada'


    # Change Audit fields

    creation_date_field = 'fechaCreacion'
    creation_user_field = 'usuarioCreador'
    modification_date_field = 'fechaModificacion'
    modification_user_field = 'usuarioModificador'
    deletion_date_field = 'fechaEliminacion'
    deletion_user_field = 'usuarioEliminador'
    is_inactive_field = 'estaInactivo'
    change_counter_field = 'contadorCambios'
    sources_counters_field = 'contadoresDeFuentes'
    change_log_field = 'registroDeCambios'




    # Versioning and Translation fields

    inter_version_field = 'uidInterVersionesInterno'
    version_field = 'versionInterna'
    version_comment_field = 'comentarioVersionInterna'
    language_field = 'codigoIdiomaInterno'
    fields_pending_translation_field = 'camposPendientesTraduccionInterna'
    fields_pending_revision_field = 'camposPendientesRevisionInterna'



    allowed_content_types = [] + list(getattr(BPDArquetipoReferenciable, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdentrada.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Informacion de Entrada que se debe o puede aportar para ejecutar un Proceso de Negocio."
    typeDescMsgId =  'gvSIGbpd_BPDEntrada_help'
    archetype_name2 = 'Input'
    typeDescription2 = '''nformation that may or must be made available at the start of the Business Process.'''
    archetype_name_msgid = 'gvSIGbpd_BPDEntrada_label'
    factory_methods = None
    factory_enablers = None


    actions =  (


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
        'permissions': ("View",),
        'condition': """python:0"""
       },


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowWrite()"""
       },


       {'action': "string:${object_url}/MDDExport",
        'category': "object_buttons",
        'id': 'mddexport',
        'name': 'Export',
        'permissions': ("View",),
        'condition': """python:object.fAllowExport()"""
       },


       {'action': "string:${object_url}/MDDImport",
        'category': "object_buttons",
        'id': 'mddimport',
        'name': 'Import',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowImport()"""
       },


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("Manage properties",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/TextualRest",
        'category': "object_buttons",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/Textual",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDNewVersion",
        'category': "object_buttons",
        'id': 'mddnewversion',
        'name': 'New Version',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowVersion() and object.getEsRaiz()"""
       },


       {'action': "string:${object_url}/MDDNewTranslation",
        'category': "object_buttons",
        'id': 'mddnewtranslation',
        'name': 'New Translation',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowTranslation() and object.getEsRaiz()"""
       },


    )

    _at_rename_after_creation = True

    schema = BPDEntrada_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('manage_afterAdd')
    def manage_afterAdd(self,item,container):
        """
        """
        
        return self.pHandle_manage_afterAdd(  item, container)

registerType(BPDEntrada, PROJECTNAME)
# end of class BPDEntrada

##code-section module-footer #fill in your manual code here
##/code-section module-footer



