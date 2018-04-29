# -*- coding: utf-8 -*-
#
# File: BPDArtefacto.py
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
from Products.gvSIGbpd.BPDArquetipoConAdopcion import BPDArquetipoConAdopcion
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='coleccionesArtefactos',
        widget=ComputedWidget(
            label="Artefactos subordinados",
            label2="Subordinated Artefacts",
            description="Colecciones de Artefactos de orden inferior a este artefacto, que se producen, consumen, consultan, editan, y en general son el objeto del esfuerzo de la Organizacion, definidos en el contexto de este Artefacto.",
            description2="Collections of Lower level Artefacts produced, consumed, consulted, edited, or otherwise object of the Organisation effort, and defined within the context of this Artefact.",
            label_msgid='gvSIGbpd_BPDArtefacto_contents_coleccionesArtefactos_label',
            description_msgid='gvSIGbpd_BPDArtefacto_contents_coleccionesArtefactos_help',
            i18n_domain='gvSIGbpd',
        ),
        description='Colecciones de Artefactos de orden inferior a este artefacto, que se producen, consumen, consultan, editan, y en general son el objeto del esfuerzo de la Organizacion, definidos en el contexto de este Artefacto.',
        label2='Subordinated Artefacts',
        label='Artefactos subordinados',
        description2='Collections of Lower level Artefacts produced, consumed, consulted, edited, or otherwise object of the Organisation effort, and defined within the context of this Artefact.',
        multiValued=1,
        owner_class_name="BPDArtefacto",
        expression="context.objectValues(['BPDColeccionArtefactos'])",
        computed_types=['BPDColeccionArtefactos'],
        represents_aggregation=True
    ),

    RelationField(
        name='entradasAProcesosDeNegocio',
        inverse_relation_label="Artefactos de Entrada",
        inverse_relation_description="Artefactos que deben estar disponibles para comenzar el Proceso de Negocio",
        description="Entradas a Procesos de Negocio en que el Artefacto debe estar disponible, para poder comenzar la ejecucion.",
        relationship='EntradasAProcesosDeNegocio',
        label2="Input to Business Processes",
        widget=ReferenceBrowserWidget(
            label="Entrada a Procesos de Negocio",
            label2="Input to Business Processes",
            description="Entradas a Procesos de Negocio en que el Artefacto debe estar disponible, para poder comenzar la ejecucion.",
            description2="Inputs to Business Processes where the Artefact must be made available , in order  to start execution.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_entradasAProcesosDeNegocio_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_entradasAProcesosDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Inputs to Business Processes where the Artefact must be made available , in order  to start execution.",
        sourcestyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        inverse_relation_label2="Input Artefacts",
        dependency_supplier=True,
        inverse_relation_field_name='artefactosDeEntrada',
        inverse_relation_description2="Artefacts required as input to allow the start of the Business Processes.",
        additional_columns=['codigo','estado','nivelDeImposicion',],
        write_permission='Modify portal content',
        label="Entrada a Procesos de Negocio",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ArtefactosDeEntrada'
    ),

    RelationField(
        name='herramientas',
        inverse_relation_label="Artefactos",
        inverse_relation_description="Artefactos que pueden ser manipulados con la Herramienta.",
        description="Herramientas utiles para manejar Artefactos de este tipo.",
        relationship='Herramientas',
        label2="Tools",
        widget=ReferenceBrowserWidget(
            label="Herramientas",
            label2="Tools",
            description="Herramientas utiles para manejar Artefactos de este tipo.",
            description2="Useful tools to handle Artefacts of this type.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_herramientas_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_herramientas_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Useful tools to handle Artefacts of this type.",
        inverse_relation_label2="Artefacts handled with the Tool",
        deststyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        write_permission='Modify portal content',
        inverse_relation_field_name='artefactosDeHerramienta',
        inverse_relation_description2="Artefacts where the tool is applied to visualize, edit or otherwise handle the Artefact content.",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion', 'version', 'fechaAdopcion', 'fechaObsolescencia'],
        label="Herramientas",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='Artefactos',
        owner_class_name="BPDArtefacto"
    ),

    RelationField(
        name='salidasDeProcesosDeNegocio',
        inverse_relation_label="Artefactos de Salida",
        inverse_relation_description="Artefactos producidos como Salida al finalizar exitosamente el Proceso de Negocio.",
        description="Procesos de Negocio donde el Artefacto se produce como Salida, tras el final exitoso de la ejecucion.",
        relationship='SalidasDeProcesosDeNegocio',
        label2="Business Process Outputs",
        widget=ReferenceBrowserWidget(
            label="Salidas de Procesos de Negocio",
            label2="Business Process Outputs",
            description="Procesos de Negocio donde el Artefacto se produce como Salida, tras el final exitoso de la ejecucion.",
            description2="Business Processes where the Artefact is made available as Output, upon successful completion.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_salidasDeProcesosDeNegocio_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_salidasDeProcesosDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Processes where the Artefact is made available as Output, upon successful completion.",
        sourcestyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        inverse_relation_label2="Output Artefacts",
        dependency_supplier=True,
        inverse_relation_field_name='artefactosDeSalida',
        inverse_relation_description2="Artefacts produced as outcomes of successfully completed Business Processes.",
        additional_columns=['codigo','estado','nivelDeImposicion',],
        write_permission='Modify portal content',
        label="Salidas de Procesos de Negocio",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ArtefactosDeSalida'
    ),

    RelationField(
        name='reglasDeNegocioDirigentes',
        inverse_relation_label="Artefactos dirigidos",
        containment="Unspecified",
        inverse_relation_description="Artefactos cuya utilizacion esta prescrita o gobernada por la Regla de Negocio.",
        description="Reglas de Negocio que dirigen el uso del Artefacto en la Organizacion.",
        relationship='ArtefactoAfectadoPorReglasDeNegocio',
        inverse_relation_field_name='artefactosDirigidos',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Affected by Business Rules",
        inverse_relation_description2="Artefacts whose usage is directed by the Business Rule.",
        widget=ReferenceBrowserWidget(
            label="Reglas de Negocio dirigentes",
            label2="Affected by Business Rules",
            description="Reglas de Negocio que dirigen el uso del Artefacto en la Organizacion.",
            description2="Business Rules directing the use of the Artefact",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_reglasDeNegocioDirigentes_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_reglasDeNegocioDirigentes_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Reglas de Negocio dirigentes",
        description2="Business Rules directing the use of the Artefact",
        multiValued=1,
        inverse_relation_label2="Affected Artefacts",
        inverse_relationship='ArtefactosDirigidos',
        write_permission='Modify portal content',
        additional_columns=['codigo','estado','nivelDeImposicion',]
    ),

    RelationField(
        name='pasosQueEnvianElArtefacto',
        inverse_relation_label="Artefactos Enviados",
        additional_columns=['codigo','estado','nivelDeImposicion','version','fechaAdopcion','fechaObsolescencia',],
        inverse_relation_description="Artefactos que se envian en este paso a un Participante externo.",
        description="Pasos de Proceso de Negocio que envian un Artefacto de este tipo a un Participante externo.",
        relationship='PasosQueEnvianElArtefacto',
        inverse_relation_field_name='artefactosEnviados',
        sourcestyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        inverse_relation_label2="Sent Artefacts",
        label2="Sent from Business Process Steps",
        inverse_relation_description2="Artefacts thar shall be sent while in this step to an external participant.",
        widget=ReferenceBrowserWidget(
            label="Enviado desde Pasos de Procesos de Negocio",
            label2="Sent from Business Process Steps",
            description="Pasos de Proceso de Negocio que envian un Artefacto de este tipo a un Participante externo.",
            description2="Business Process Steps sending Artefacts of this type to external participants.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_pasosQueEnvianElArtefacto_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_pasosQueEnvianElArtefacto_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Enviado desde Pasos de Procesos de Negocio",
        description2="Business Process Steps sending Artefacts of this type to external participants.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ArtefactosEnviados',
        dependency_supplier=True
    ),

    RelationField(
        name='politicasDeNegocioGobernantes',
        inverse_relation_label="Artefactos Gobernados",
        containment="Unspecified",
        inverse_relation_description="Artefactos cuya utilizacion esta prescrita o gobernada por la Politica de Negocio.",
        description="Politicas de Negocio que prescriben o gobiernan el uso del Artefacto en la Organizacion.",
        relationship='ArtefactoAfectadoPorPoliticasDeNegocio',
        inverse_relation_field_name='artefactosGobernados',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Geverning Business Policies",
        inverse_relation_description2="Artefacts whose usage is directed by the Business Policy.",
        widget=ReferenceBrowserWidget(
            label="Politicas de Negocio gobernantes",
            label2="Geverning Business Policies",
            description="Politicas de Negocio que prescriben o gobiernan el uso del Artefacto en la Organizacion.",
            description2="Business Policies that prescribe or govern the utilisation of the Artefact in the Organisation",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_politicasDeNegocioGobernantes_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_politicasDeNegocioGobernantes_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Politicas de Negocio gobernantes",
        description2="Business Policies that prescribe or govern the utilisation of the Artefact in the Organisation",
        multiValued=1,
        inverse_relation_label2="Governed Artefacts",
        inverse_relationship='ArtefactosGobernados',
        write_permission='Modify portal content',
        additional_columns=['codigo','estado','nivelDeImposicion',]
    ),

    RelationField(
        name='pasosQueRecibenElArtefacto',
        inverse_relation_label="Artefactos Recibidos",
        additional_columns=['codigo','estado','nivelDeImposicion','version','fechaAdopcion','fechaObsolescencia',],
        inverse_relation_description="Artefactos que se reciben de un Participante externo en este paso.",
        description="Recepciones pasos de Proceso de Negocio donde se recibe un Artefacto de este tipo de un participante externo.",
        relationship='PasosQueRecibenElArtefacto',
        inverse_relation_field_name='artefactosRecibidos',
        sourcestyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        inverse_relation_label2="Received Artefacts",
        label2="Received at Business Process Steps",
        inverse_relation_description2="Artefacts to be received from an external participant during this step.",
        widget=ReferenceBrowserWidget(
            label="Recepciones",
            label2="Received at Business Process Steps",
            description="Recepciones pasos de Proceso de Negocio donde se recibe un Artefacto de este tipo de un participante externo.",
            description2="Business Process Steps where Artefacts of this type are received from external participants.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_pasosQueRecibenElArtefacto_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_pasosQueRecibenElArtefacto_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Recepciones",
        description2="Business Process Steps where Artefacts of this type are received from external participants.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ArtefactosRecibidos',
        dependency_supplier=True
    ),

    RelationField(
        name='responsablesDeArtefacto',
        inverse_relation_label="Artefactos a su cargo",
        inverse_relation_description="Artefactos que estan a cargo del Perfil o Unidad Organizacional.",
        description="Perfiles o Unidades Organizacionales a cargo de los Artefactos de este tipo.",
        relationship='ResponsablesDeArtefacto',
        label2="Responsible Profiles or Organisational Units",
        widget=ReferenceBrowserWidget(
            label="Responsables",
            label2="Responsible Profiles or Organisational Units",
            description="Perfiles o Unidades Organizacionales a cargo de los Artefactos de este tipo.",
            description2="Participant Profiles or Organisational Units generally in charge of Artefacts of this type.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_responsablesDeArtefacto_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_responsablesDeArtefacto_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Participant Profiles or Organisational Units generally in charge of Artefacts of this type.",
        inverse_relation_label2="In charge of Artefacts",
        deststyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        write_permission='Modify portal content',
        inverse_relation_field_name='responsableDeArtefactos',
        inverse_relation_description2="Artefacts for which the the participant Profile or Organisational Unit is generally responsible for.",
        additional_columns=['abreviatura', 'responsabilidadesClave'],
        label="Responsables",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ArtefactosACargo',
        owner_class_name="BPDArtefacto"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDArtefacto_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDArtefacto(OrderedBaseFolder, BPDArquetipoConAdopcion):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Artefacto'

    meta_type = 'BPDArtefacto'
    portal_type = 'BPDArtefacto'
    allowed_content_types = ['BPDColeccionArtefactos'] + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdartefacto.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Un elemento identificable de information utilizada en el esfuerzo en los procesos de gestion de gvSIG."
    typeDescMsgId =  'gvSIGbpd_BPDArtefacto_help'
    archetype_name2 = 'Artefact'
    typeDescription2 = '''An identifiable piece of information, i.e. that can be produced, consumed or handled over during the course of Business Processes.'''
    archetype_name_msgid = 'gvSIGbpd_BPDArtefacto_label'
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

    schema = BPDArtefacto_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(BPDArtefacto, PROJECTNAME)
# end of class BPDArtefacto

##code-section module-footer #fill in your manual code here
##/code-section module-footer



