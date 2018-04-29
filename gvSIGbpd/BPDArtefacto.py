# -*- coding: utf-8 -*-
#
# File: BPDArtefacto.py
#
# Copyright (c) 2010 by Conselleria de Infraestructuras y Transporte de la
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
        name='caracteristicas',
        widget=ComputedWidget(
            label="Caracteristicas",
            label2="Features",
            description="Elementos de informacion que se especifican para el Artefacto, o que podra contener el Artefacto.",
            description2="Information elements specified for the Artefact, or that may be contained by the Artefact.",
            label_msgid='gvSIGbpd_BPDArtefacto_contents_caracteristicas_label',
            description_msgid='gvSIGbpd_BPDArtefacto_contents_caracteristicas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Features',
        additional_columns=['detallesCaracteristica', 'titulosTiposArtefactos'],
        label='Caracteristicas',
        represents_aggregation=True,
        description2='Information elements specified for the Artefact, or that may be contained by the Artefact.',
        multiValued=1,
        owner_class_name="BPDArtefacto",
        expression="context.objectValues(['BPDCaracteristica'])",
        computed_types=['BPDCaracteristica'],
        non_framework_elements=False,
        description='Elementos de informacion que se especifican para el Artefacto, o que podra contener el Artefacto.'
    ),

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
        contains_collections=True,
        label2='Subordinated Artefacts',
        label='Artefactos subordinados',
        represents_aggregation=True,
        description2='Collections of Lower level Artefacts produced, consumed, consulted, edited, or otherwise object of the Organisation effort, and defined within the context of this Artefact.',
        multiValued=1,
        owner_class_name="BPDArtefacto",
        expression="context.objectValues(['BPDColeccionArtefactos'])",
        computed_types=['BPDColeccionArtefactos'],
        non_framework_elements=False,
        description='Colecciones de Artefactos de orden inferior a este artefacto, que se producen, consumen, consultan, editan, y en general son el objeto del esfuerzo de la Organizacion, definidos en el contexto de este Artefacto.'
    ),

    RelationField(
        name='entradasAProcesosDeNegocio',
        inverse_relation_label="Artefactos de Entrada",
        inverse_relation_description="Artefactos que deben estar disponibles para comenzar el Proceso de Negocio",
        description="Entradas a Procesos de Negocio en que el Artefacto debe estar disponible, para poder comenzar la ejecucion.",
        relationship='BPDEntradasAProcesosDeNegocio',
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
        additional_columns=['codigo',],
        write_permission='Modify portal content',
        label="Entrada a Procesos de Negocio",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDArtefactosDeEntrada'
    ),

    RelationField(
        name='herramientas',
        inverse_relation_label="Artefactos",
        inverse_relation_description="Artefactos que pueden ser manipulados con la Herramienta.",
        description="Herramientas utiles para manejar Artefactos de este tipo.",
        relationship='BPDHerramientas',
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
        additional_columns=['codigo'],
        label="Herramientas",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDArtefactos',
        owner_class_name="BPDArtefacto"
    ),

    RelationField(
        name='salidasDeProcesosDeNegocio',
        inverse_relation_label="Artefactos de Salida",
        inverse_relation_description="Artefactos producidos como Salida al finalizar exitosamente el Proceso de Negocio.",
        description="Procesos de Negocio donde el Artefacto se produce como Salida, tras el final exitoso de la ejecucion.",
        relationship='BPDSalidasDeProcesosDeNegocio',
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
        additional_columns=['codigo',],
        write_permission='Modify portal content',
        label="Salidas de Procesos de Negocio",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDArtefactosDeSalida'
    ),

    RelationField(
        name='reglasDeNegocioDirigentes',
        inverse_relation_label="Artefactos dirigidos",
        containment="Unspecified",
        inverse_relation_description="Artefactos cuya utilizacion esta prescrita o gobernada por la Regla de Negocio.",
        description="Reglas de Negocio que dirigen el uso del Artefacto en la Organizacion.",
        relationship='BPDArtefactosAfectadosPorReglasDeNegocio',
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
        inverse_relationship='BPDArtefactosDirigidos',
        write_permission='Modify portal content',
        additional_columns=['codigo',]
    ),

    RelationField(
        name='pasosQueEnvianElArtefacto',
        inverse_relation_label="Artefactos Enviados",
        additional_columns=['codigo',],
        inverse_relation_description="Artefactos que se envian en este paso a un Participante externo.",
        description="Pasos de Proceso de Negocio que envian un Artefacto de este tipo a un Participante externo.",
        relationship='BPDPasosQueEnvianElArtefacto',
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
        inverse_relationship='BPDArtefactosEnviados',
        dependency_supplier=True
    ),

    RelationField(
        name='procesosGestores',
        inverse_relation_label="Artefactos Gestionados",
        inverse_relation_description="Artefactos que se gestionan ejecutando el Proceso de Negocio.",
        description="Procesos de Negocio con que se gestiona este Artefacto.",
        relationship='BPDProcesosGestoresDeArtefactos',
        label2="Managing Business Processes",
        widget=ReferenceBrowserWidget(
            label="Procesos de Negocio Gestores",
            label2="Managing Business Processes",
            description="Procesos de Negocio con que se gestiona este Artefacto.",
            description2="Business Processes executed to manage this Artefact.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_procesosGestores_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_procesosGestores_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Processes executed to manage this Artefact.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Managed Artefacts",
        dependency_supplier=True,
        inverse_relation_field_name='artefactosGestionados',
        inverse_relation_description2="Artefacts managed by executing this Business Process.",
        additional_columns=['codigo',],
        write_permission='Modify portal content',
        label="Procesos de Negocio Gestores",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDArtefactosGestionadosPorProcesos'
    ),

    RelationField(
        name='politicasDeNegocioGobernantes',
        inverse_relation_label="Artefactos Gobernados",
        containment="Unspecified",
        inverse_relation_description="Artefactos cuya utilizacion esta prescrita o gobernada por la Politica de Negocio.",
        description="Politicas de Negocio que prescriben o gobiernan el uso del Artefacto en la Organizacion.",
        relationship='BPDArtefactoAfectadoPorPoliticasDeNegocio',
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
        inverse_relationship='BPDArtefactosGobernados',
        write_permission='Modify portal content',
        additional_columns=['codigo',]
    ),

    RelationField(
        name='pasosQueRecibenElArtefacto',
        inverse_relation_label="Artefactos Recibidos",
        additional_columns=['codigo',],
        inverse_relation_description="Artefactos que se reciben de un Participante externo en este paso.",
        description="Recepciones pasos de Proceso de Negocio donde se recibe un Artefacto de este tipo de un participante externo.",
        relationship='BPDPasosQueRecibenElArtefacto',
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
        inverse_relationship='BPDArtefactosRecibidos',
        dependency_supplier=True
    ),

    RelationField(
        name='usosDelArtefacto',
        inverse_relation_label="Artefactos Usados",
        inverse_relation_description="Artefactos usados en este Paso del Proceso de Negocio.",
        description="Pasos de Procesos de Negocio donde se usa este Artefacto.",
        relationship='BPDUsosDeArtefactos',
        label2="Artefact Usages",
        widget=ReferenceBrowserWidget(
            label="Usos del Artefacto",
            label2="Artefact Usages",
            description="Pasos de Procesos de Negocio donde se usa este Artefacto.",
            description2="Business Process Steps using this Artefact.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_usosDelArtefacto_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_usosDelArtefacto_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Process Steps using this Artefact.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Artefacts Used",
        dependency_supplier=True,
        inverse_relation_field_name='artefactosUsados',
        inverse_relation_description2="Artefacts used in this Business Process Step.",
        additional_columns=['codigo','estado','nivelDeImposicion',],
        write_permission='Modify portal content',
        label="Usos del Artefacto",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDArtefactosUsados'
    ),

    RelationField(
        name='responsablesDeArtefacto',
        inverse_relation_label="Artefactos a su cargo",
        inverse_relation_description="Artefactos que estan a cargo del Perfil o Unidad Organizacional.",
        description="Perfiles o Unidades Organizacionales a cargo de los Artefactos de este tipo.",
        relationship='BPDResponsablesDeArtefacto',
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
        additional_columns=['abreviatura'],
        label="Responsables",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDArtefactosACargo',
        owner_class_name="BPDArtefacto"
    ),

    RelationField(
        name='caracteristicasDelTipo',
        inverse_relation_label="Tipos de Artefactos",
        inverse_relation_description="Si la Clase de Caracteristica es Referencia o Agregacion, entonces restringe los tipos de Artefactos referenciados o agregados.",
        description="Caracteristicas de Clase Referencia o Agregacion que estan restringidas a Artefactos de este tipo.",
        relationship='BPDCaracteristicasDelTipo',
        label2="Features of the Type",
        widget=ReferenceBrowserWidget(
            label="Caracteristicas del Tipo",
            label2="Features of the Type",
            description="Caracteristicas de Clase Referencia o Agregacion que estan restringidas a Artefactos de este tipo.",
            description2="Features of Reference or Aggregation Class constrained to Artefacts of this type.",
            label_msgid='gvSIGbpd_BPDArtefacto_rel_caracteristicasDelTipo_label',
            description_msgid='gvSIGbpd_BPDArtefacto_rel_caracteristicasDelTipo_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Features of Reference or Aggregation Class constrained to Artefacts of this type.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Artefact Types",
        dependency_supplier=True,
        inverse_relation_field_name='tiposDeArtefactos',
        inverse_relation_description2="If the Feature Class is Reference or Aggregation, then constrains the types of Artefacts that can be referenced or aggregated.",
        additional_columns=['codigo',],
        write_permission='Modify portal content',
        label="Caracteristicas del Tipo",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDTiposDeCaracteristicas'
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
    version_storage_field = 'versionInternaAlmacenada'
    version_comment_field = 'comentarioVersionInterna'
    version_comment_storage_field = 'comentarioVersionInternaAlmacenada'
    inter_translation_field = 'uidInterTraduccionesInterno'
    language_field = 'codigoIdiomaInterno'
    fields_pending_translation_field = 'camposPendientesTraduccionInterna'
    fields_pending_revision_field = 'camposPendientesRevisionInterna'



    allowed_content_types = ['BPDCaracteristica', 'BPDColeccionArtefactos'] + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdartefacto.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Un elemento identificable de information utilizada en el esfuerzo en los procesos de gestion de gvSIG."
    typeDescMsgId                    =  'gvSIGbpd_BPDArtefacto_help'
    archetype_name2                  = 'Artefact'
    typeDescription2                 = '''An identifiable piece of information, i.e. that can be produced, consumed or handled over during the course of Business Processes.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDArtefacto_label'
    factory_methods                  = None
    factory_enablers                 = None
    propagate_delete_impact_to       = None


    actions =  (


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
        'permissions': ("View",),
        'condition': """python:0"""
       },


       {'action': "string:${object_url}/MDDInspectClipboard",
        'category': "object_buttons",
        'id': 'inspectclipboard',
        'name': 'Clipboard',
        'permissions': ("View",),
        'condition': """python:object.fAllowRead()"""
       },


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowWrite()"""
       },


       {'action': "string:${object_url}/MDDOrdenar",
        'category': "object_buttons",
        'id': 'reorder',
        'name': 'Reorder',
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


       {'action': "string:${object_url}/",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDChanges",
        'category': "object_buttons",
        'id': 'mddchanges',
        'name': 'Changes',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDVersions",
        'category': "object_buttons",
        'id': 'mddversions',
        'name': 'Versions',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDCacheStatus/",
        'category': "object_buttons",
        'id': 'mddcachestatus',
        'name': 'Cache',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/TextualRest",
        'category': "object_buttons",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': """python:1"""
       },


    )

    _at_rename_after_creation = True

    schema = BPDArtefacto_schema

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

    security.declarePublic('moveObjectsByDelta')
    def moveObjectsByDelta(self,ids,delta,subset_ids=None):
        """
        """
        
        return self.pHandle_moveObjectsByDelta( ids, delta, subset_ids=subset_ids)

registerType(BPDArtefacto, PROJECTNAME)
# end of class BPDArtefacto

##code-section module-footer #fill in your manual code here
##/code-section module-footer



