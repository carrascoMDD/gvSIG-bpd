# -*- coding: utf-8 -*-
#
# File: BPDParticipante.py
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

    StringField(
        name='abreviatura',
        widget=StringWidget(
            label="Abreviatura",
            label2="Abbreviation",
            description="Para identificacion rapida de los Perfiles o Unidades Organizacionales mas significativos.",
            description2="For inmediate identification of participant Profiles and Organisational Units.",
            label_msgid='gvSIGbpd_BPDParticipante_attr_abreviatura_label',
            description_msgid='gvSIGbpd_BPDParticipante_attr_abreviatura_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Para identificacion rapida de los Perfiles o Unidades Organizacionales mas significativos.",
        duplicates="0",
        label2="Abbreviation",
        ea_localid="245",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="For inmediate identification of participant Profiles and Organisational Units.",
        ea_guid="{32115567-9FBE-406b-968F-C98308EB0C45}",
        write_permission='Modify portal content',
        scale="0",
        label="Abreviatura",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDParticipante"
    ),

    RelationField(
        name='destinatarioDeEnvios',
        inverse_relation_label="Destinatarios",
        additional_columns=['abreviatura','responsabilidadesClave',],
        inverse_relation_description="Perfiles o Unidades Organizacionales a los que se destina el Envio.",
        description="Envios que se destinan a este Perfil o Unidad Organizacional.",
        relationship='DestinatarioDeEnvios',
        inverse_relation_field_name='destinatarios',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Receivers",
        label2="Receiver of Send steps",
        inverse_relation_description2="Participant Profiles or Organisational Units to whom this is Sent",
        widget=ReferenceBrowserWidget(
            label="Destinatario de Envios",
            label2="Receiver of Send steps",
            description="Envios que se destinan a este Perfil o Unidad Organizacional.",
            description2="Send process steps addressed to this participant Profile or Organisational Unit.",
            label_msgid='gvSIGbpd_BPDParticipante_rel_destinatarioDeEnvios_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_destinatarioDeEnvios_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Destinatario de Envios",
        description2="Send process steps addressed to this participant Profile or Organisational Unit.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='Destinatarios',
        dependency_supplier=True
    ),

    RelationField(
        name='pasosEjecutados',
        inverse_relation_label="Ejecutores",
        inverse_relation_description="Perfiles y Unidades Organizacionales a cargo de ejecutar el Paso.",
        description="Pasos de Negocio que se encarga de ejecutar el Perfil o Unidad Organizacional",
        relationship='PasosEjecutados',
        label2="Performed Business Process Steps",
        widget=ReferenceBrowserWidget(
            label="Pasos Ejecutados",
            label2="Performed Business Process Steps",
            description="Pasos de Negocio que se encarga de ejecutar el Perfil o Unidad Organizacional",
            description2="Business Process Steps performed by the participant Profile or Organisational Unit.",
            label_msgid='gvSIGbpd_BPDParticipante_rel_pasosEjecutados_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_pasosEjecutados_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Process Steps performed by the participant Profile or Organisational Unit.",
        sourcestyle="Owned=0;Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;",
        inverse_relation_label2="Performers",
        dependency_supplier=True,
        inverse_relation_field_name='ejecutores',
        inverse_relation_description2="Participant Profiles and Organisational Units allowed to execute the Step.",
        additional_columns=['abreviatura','responsabilidadesClave',],
        write_permission='Modify portal content',
        label="Pasos Ejecutados",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='EjecutoresDelPaso'
    ),

    RelationField(
        name='procesosEjecutados',
        inverse_relation_label="Ejecutores del Proceso",
        inverse_relation_description="Los Perfiles o Unidades Organizacionales a cargo de ejecutar el Proceso de Negocio.",
        description="Procesos de Negocio que se encarga de ejecutar el Perfil o Unidad Organizacional.",
        relationship='ProcesosEjecutados',
        label2="Performed Business Processes",
        widget=ReferenceBrowserWidget(
            label="Procesos Ejecutados",
            label2="Performed Business Processes",
            description="Procesos de Negocio que se encarga de ejecutar el Perfil o Unidad Organizacional.",
            description2="Business Process that can be executed by the participant Profile or Organisational Unit.",
            label_msgid='gvSIGbpd_BPDParticipante_rel_procesosEjecutados_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_procesosEjecutados_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Process that can be executed by the participant Profile or Organisational Unit.",
        sourcestyle="Owned=0;Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;",
        inverse_relation_label2="Performers",
        dependency_supplier=True,
        inverse_relation_field_name='ejecutores',
        inverse_relation_description2="Participant Profiles and Organisational Units allowed to execute the Business Process.",
        additional_columns=['abreviatura','responsabilidadesClave',],
        write_permission='Modify portal content',
        label="Procesos Ejecutados",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='EjecutoresDelProceso'
    ),

    RelationField(
        name='reglasDeNegocioDirigentes',
        inverse_relation_label="Participantes dirigidos",
        containment="Unspecified",
        inverse_relation_description="Perfiles y Unidades Organizacionales que aplican la Regla de Negocio durante su labor.",
        description="Las Reglas de Negocio que dirigen la labor de el Perfil o Unidad Organizacional.",
        relationship='AfectadoPorReglasDeNegocio',
        inverse_relation_field_name='participantesDirigidos',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Directing Business Rules",
        inverse_relation_description2="Participant Profiles and Organisational Units that apply the Business Rule.",
        widget=ReferenceBrowserWidget(
            label="Reglas de Negocio dirigentes",
            label2="Directing Business Rules",
            description="Las Reglas de Negocio que dirigen la labor de el Perfil o Unidad Organizacional.",
            description2="Business Rule affecting the participant Profile or Organisational Unit",
            label_msgid='gvSIGbpd_BPDParticipante_rel_reglasDeNegocioDirigentes_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_reglasDeNegocioDirigentes_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Reglas de Negocio dirigentes",
        description2="Business Rule affecting the participant Profile or Organisational Unit",
        multiValued=1,
        inverse_relation_label2="Directed Participant Profiles and Organisational Units",
        inverse_relationship='ParticipantesDirigidos',
        write_permission='Modify portal content',
        additional_columns=['abreviatura','responsabilidadesClave',]
    ),

    RelationField(
        name='politicasDeNegocioGobernantes',
        inverse_relation_label="Participantes gobernados",
        containment="Unspecified",
        inverse_relation_description="Perfiles y Unidades Organizacionales que aplican la Politica de Negocio durante su labor.",
        description="Las Politicas de Negocio que afectan a la labor del Perfil o Unidad Organizacional",
        relationship='AfectadoPorPoliticasDeNegocio',
        inverse_relation_field_name='participantesGobernados',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Governing Business Policies",
        inverse_relation_description2="Participant Profiles and Organisational Units that must endeavour to apply the Business Policy.",
        widget=ReferenceBrowserWidget(
            label="Politicas de Negocio gobernantes",
            label2="Governing Business Policies",
            description="Las Politicas de Negocio que afectan a la labor del Perfil o Unidad Organizacional",
            description2="Business Policies governing the participant Profile or Organisational Unit.",
            label_msgid='gvSIGbpd_BPDParticipante_rel_politicasDeNegocioGobernantes_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_politicasDeNegocioGobernantes_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Politicas de Negocio gobernantes",
        description2="Business Policies governing the participant Profile or Organisational Unit.",
        multiValued=1,
        inverse_relation_label2="Governed participant Profiles and Organisational Units",
        inverse_relationship='ParticipantesGobernados',
        write_permission='Modify portal content',
        additional_columns=['abreviatura','responsabilidadesClave',]
    ),

    RelationField(
        name='remitenteDeRecepciones',
        inverse_relation_label="Remitente",
        additional_columns=['abreviatura','responsabilidadesClave',],
        inverse_relation_description="El Perfil o Unidad Organizacional que originan la Recepcion.",
        description="Recepciones originadas en este Perfil o Unidad Organizacional.",
        relationship='RemitenteDeRecepciones',
        inverse_relation_field_name='remitente',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Sender",
        label2="Sender of Reception steps",
        inverse_relation_description2="Participant Profiles or Organisational Units originating this Reception.",
        widget=ReferenceBrowserWidget(
            label="Remitente de Recepciones",
            label2="Sender of Reception steps",
            description="Recepciones originadas en este Perfil o Unidad Organizacional.",
            description2="Business Process Reception Steps originated by the participant Profile or Organisational Units.",
            label_msgid='gvSIGbpd_BPDParticipante_rel_remitenteDeRecepciones_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_remitenteDeRecepciones_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Remitente de Recepciones",
        description2="Business Process Reception Steps originated by the participant Profile or Organisational Units.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='Remitente',
        dependency_supplier=True
    ),

    TextField(
        name='responsabilidadesClave',
        widget=TextAreaWidget(
            label="Responsabilidades Clave",
            label2="Key Responsibilities",
            description="Los Participantes, en general,  se haran cargo principalmente de las responsabilidades especificadas.",
            description2="The participant Profile or Organisational Unit shall be generally responsible of these subject areas.",
            label_msgid='gvSIGbpd_BPDParticipante_attr_responsabilidadesClave_label',
            description_msgid='gvSIGbpd_BPDParticipante_attr_responsabilidadesClave_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Los Participantes, en general,  se haran cargo principalmente de las responsabilidades especificadas.",
        duplicates="0",
        label2="Key Responsibilities",
        ea_localid="246",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="The participant Profile or Organisational Unit shall be generally responsible of these subject areas.",
        ea_guid="{DC8EFEB8-D377-47ff-B13F-A719BDA70D04}",
        write_permission='Modify portal content',
        scale="0",
        label="Responsabilidades Clave",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDParticipante"
    ),

    RelationField(
        name='responsableDeArtefactos',
        inverse_relation_label="Responsables",
        containment="Unspecified",
        inverse_relation_description="Perfiles o Unidades Organizacionales a cargo de los Artefactos de este tipo.",
        description="Artefactos que estan a cargo del Perfil o Unidad Organizacional.",
        relationship='ArtefactosACargo',
        inverse_relation_field_name='responsablesDeArtefacto',
        sourcestyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        label2="In charge of Artefacts",
        inverse_relation_description2="Participant Profiles or Organisational Units generally in charge of Artefacts of this type.",
        widget=ReferenceBrowserWidget(
            label="Artefactos a su cargo",
            label2="In charge of Artefacts",
            description="Artefactos que estan a cargo del Perfil o Unidad Organizacional.",
            description2="Artefacts for which the the participant Profile or Organisational Unit is generally responsible for.",
            label_msgid='gvSIGbpd_BPDParticipante_rel_responsableDeArtefactos_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_responsableDeArtefactos_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Artefactos a su cargo",
        description2="Artefacts for which the the participant Profile or Organisational Unit is generally responsible for.",
        multiValued=1,
        inverse_relation_label2="Responsible Profiles or Organisational Units",
        inverse_relationship='ResponsablesDeArtefacto',
        write_permission='Modify portal content',
        additional_columns=['abreviatura','responsabilidadesClave',]
    ),

    RelationField(
        name='responsableDeHerramientas',
        inverse_relation_label="Responsables",
        containment="Unspecified",
        inverse_relation_description="Perfiles o Unidades Organizacionales a cargo de asistir a la organizacion en su manejo de esta Herramienta.",
        description="Herramientas que estan a cargo de el Perfil o Unidad Organizacional",
        relationship='HerramientasACargo',
        inverse_relation_field_name='responsablesDeHerramienta',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="In charge of Tools",
        inverse_relation_description2="Participant Profiles or Organisational Units generally in charge of handling, administering or assisting the Teams in their usage of the Tool.",
        widget=ReferenceBrowserWidget(
            label="Herramientas a su Cargo",
            label2="In charge of Tools",
            description="Herramientas que estan a cargo de el Perfil o Unidad Organizacional",
            description2="Tools for which the the participant Profile or Organisational Unit is generally responsible for.",
            label_msgid='gvSIGbpd_BPDParticipante_rel_responsableDeHerramientas_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_responsableDeHerramientas_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Herramientas a su Cargo",
        description2="Tools for which the the participant Profile or Organisational Unit is generally responsible for.",
        multiValued=1,
        inverse_relation_label2="Profiles or Organisational Units Responsible for the Tool",
        inverse_relationship='ResponsablesDeHerramienta',
        write_permission='Modify portal content',
        additional_columns=['abreviatura','responsabilidadesClave',]
    ),

    RelationField(
        name='procesosSupervisados',
        inverse_relation_label="Supervisor",
        inverse_relation_description="El Perfil o Unidad Organizacional a cargo de velar por que el cumplimiento del Proceso de Negocio se realize de acuerdo con la regulacion aplicable.",
        description="Procesos de Negocio que se encarga de supervisar el Perfil o Unidad Organizacional.",
        relationship='ProcesosSupervisados',
        label2="Supervised Business Processes",
        widget=ReferenceBrowserWidget(
            label="Procesos Supervisados",
            label2="Supervised Business Processes",
            description="Procesos de Negocio que se encarga de supervisar el Perfil o Unidad Organizacional.",
            description2="Business Process under supervision of the participant Profile or Organisational Unit.",
            label_msgid='gvSIGbpd_BPDParticipante_rel_procesosSupervisados_label',
            description_msgid='gvSIGbpd_BPDParticipante_rel_procesosSupervisados_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Process under supervision of the participant Profile or Organisational Unit.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Supervisor",
        dependency_supplier=True,
        inverse_relation_field_name='supervisor',
        inverse_relation_description2="The participant Profile or Organisational Unit is responsible to ensure the compliance of the Business Process execution with applicable directives.",
        additional_columns=['abreviatura','responsabilidadesClave',],
        write_permission='Modify portal content',
        label="Procesos Supervisados",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='Supervisor'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDParticipante_schema = getattr(BPDArquetipoReferenciable, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDParticipante(OrderedBaseFolder, BPDArquetipoReferenciable):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoReferenciable,'__implements__',()),)

    allowed_content_types = [] + list(getattr(BPDArquetipoReferenciable, 'allowed_content_types', []))

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

    schema = BPDParticipante_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDParticipante

##code-section module-footer #fill in your manual code here
##/code-section module-footer



