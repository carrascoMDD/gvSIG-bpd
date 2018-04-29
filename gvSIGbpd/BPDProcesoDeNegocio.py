# -*- coding: utf-8 -*-
#
# File: BPDProcesoDeNegocio.py
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
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import  ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='proposito',
        widget=TextAreaWidget(
            label="Proposito",
            label2="Purpose",
            description="Perseguido por el Proceso",
            description2="Pursued by the Business Process.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_proposito_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_proposito_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Perseguido por el Proceso",
        duplicates="0",
        label2="Purpose",
        ea_localid="231",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Pursued by the Business Process.",
        ea_guid="{91E6E831-690D-49dc-9CBD-AED7809684B2}",
        write_permission='Modify portal content',
        scale="0",
        label="Proposito",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDProcesoDeNegocio"
    ),

    TextField(
        name='preCondicion',
        widget=TextAreaWidget(
            label="Pre Condicion",
            label2="Pre Condition",
            description="La condicion que debera cumplirse para que pueda comenzar el Proceso",
            description2="The conditioni that is required to be true, to allow the start of the Business Process execution.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_preCondicion_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_preCondicion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="La condicion que debera cumplirse para que pueda comenzar el Proceso",
        duplicates="0",
        label2="Pre Condition",
        ea_localid="236",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="The conditioni that is required to be true, to allow the start of the Business Process execution.",
        ea_guid="{30ADBBDD-941A-4c1a-B6F7-0E033B19BF46}",
        write_permission='Modify portal content',
        scale="0",
        label="Pre Condicion",
        length="0",
        containment="Not Specified",
        position="5",
        owner_class_name="BPDProcesoDeNegocio"
    ),

    TextField(
        name='postCondicion',
        widget=TextAreaWidget(
            label="Post Condicion",
            label2="Post Condition",
            description="La condicion que se cumplira cuando el Proceso concluya con exito.",
            description2="The condition that is guaranteed to be met, whent he Business Process completes successfully.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_postCondicion_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_postCondicion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="La condicion que se cumplira cuando el Proceso concluya con exito.",
        duplicates="0",
        label2="Post Condition",
        ea_localid="237",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="The condition that is guaranteed to be met, whent he Business Process completes successfully.",
        ea_guid="{ADE0B368-5B74-4162-A5CE-F94276D53067}",
        write_permission='Modify portal content',
        scale="0",
        label="Post Condicion",
        length="0",
        containment="Not Specified",
        position="6",
        owner_class_name="BPDProcesoDeNegocio"
    ),

    StringField(
        name='responsableMantenimiento',
        widget=StringWidget(
            label="Responsable del Mantenimiento",
            label2="Responsible for Maintenance",
            description="Responsable de Mantenimiento",
            description2="Person in charge of the maintenance of the specification.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_responsableMantenimiento_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_responsableMantenimiento_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Responsable de Mantenimiento",
        duplicates="0",
        label2="Responsible for Maintenance",
        ea_localid="232",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Person in charge of the maintenance of the specification.",
        ea_guid="{928DD89F-31AE-42be-8D23-9C475ED711B5}",
        write_permission='Modify portal content',
        scale="0",
        label="Responsable del Mantenimiento",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDProcesoDeNegocio"
    ),

    TextField(
        name='seleccionDePersonal',
        widget=TextAreaWidget(
            label="Seleccion de Personal",
            label2="Human Resources Selection",
            description="Criterios para seleccionar el personal de los Perfiles ejecutores de este proceso de negocio especifico.",
            description2="Selection criteria for staffing the Performer Profiles with matching individuals, specifically for this Business Process.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_seleccionDePersonal_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_seleccionDePersonal_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Criterios para seleccionar el personal de los Perfiles ejecutores de este proceso de negocio especifico.",
        duplicates="0",
        label2="Human Resources Selection",
        ea_localid="238",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Selection criteria for staffing the Performer Profiles with matching individuals, specifically for this Business Process.",
        ea_guid="{D823D784-F46A-43bf-9FC4-56881646DC0E}",
        write_permission='Modify portal content',
        scale="0",
        label="Seleccion de Personal",
        length="0",
        containment="Not Specified",
        position="7",
        owner_class_name="BPDProcesoDeNegocio"
    ),

    BooleanField(
        name='esPlaneado',
        widget=BooleanField._properties['widget'](
            label="Es Planificado",
            label2="Is Planned",
            description="Cada instancia del Proceso de Negocio ha de ser planeada previamente (p.e., tiempo y recursos).",
            description2="Each Business Process instance shall be planned in advance (i.e., time and resources).",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_esPlaneado_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_esPlaneado_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Cada instancia del Proceso de Negocio ha de ser planeada previamente (p.e., tiempo y recursos).",
        duplicates="0",
        label2="Is Planned",
        ea_localid="233",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Each Business Process instance shall be planned in advance (i.e., time and resources).",
        ea_guid="{825E14F7-ACB9-44fe-BD10-A6E3AD626823}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Es Planificado",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDProcesoDeNegocio"
    ),

    BooleanField(
        name='esContinuo',
        widget=BooleanField._properties['widget'](
            label="Es Continuo",
            label2="Is Continuous",
            description="El Proceso se ejercita continuadamente, comenzando una nueva instancia al completar la anterior, sin necesidad de iniciacion explicita por su Responsable o la Organizacion.",
            description2="The Business Process is executed continuously, starting a new instance when the previous one completes, whithout any explicit initiation by a participant Profile or Organisational Unit.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_esContinuo_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_esContinuo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El Proceso se ejercita continuadamente, comenzando una nueva instancia al completar la anterior, sin necesidad de iniciacion explicita por su Responsable o la Organizacion.",
        duplicates="0",
        label2="Is Continuous",
        ea_localid="234",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="The Business Process is executed continuously, starting a new instance when the previous one completes, whithout any explicit initiation by a participant Profile or Organisational Unit.",
        ea_guid="{6D7A800C-2EA2-429f-82FA-AC871296D402}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Es Continuo",
        length="0",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDProcesoDeNegocio"
    ),

    BooleanField(
        name='esRepetible',
        widget=BooleanField._properties['widget'](
            label="Es Repetible",
            label2="Is  Repeteable",
            description="El Proceso se puede aplicar varias veces una tras otra sobre la misma instancia de informacion, por ejemplo, hasta conseguir un Resultado de calidad aceptable.",
            description2="Whether the Business Process may iterate and execute multiple times on the same instance of information, por example, until obtaining a sufficiently satisfactory result.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_esRepetible_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_esRepetible_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El Proceso se puede aplicar varias veces una tras otra sobre la misma instancia de informacion, por ejemplo, hasta conseguir un Resultado de calidad aceptable.",
        duplicates="0",
        label2="Is  Repeteable",
        ea_localid="235",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Whether the Business Process may iterate and execute multiple times on the same instance of information, por example, until obtaining a sufficiently satisfactory result.",
        ea_guid="{5C122DA3-18FD-416a-8948-195B081ECE38}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Es Repetible",
        length="0",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDProcesoDeNegocio"
    ),

    ComputedField(
        name='coleccionesProcesosDeNegocio',
        widget=ComputedWidget(
            label="Procesos de Negocio anidados",
            label2="Nested Business Processes",
            description="Colecciones de Procesos de Negocio de orden inferior, definidos en el contexto de este Proceso de negocio, realizando cursos de accion persiguiendo metas subordinadas.",
            description2="Collections of Lower level Business Processes, defined in the context of this Business Process realising courses of action pusuing subordinate goals.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_contents_coleccionesProcesosDeNegocio_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_contents_coleccionesProcesosDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Nested Business Processes',
        label='Procesos de Negocio anidados',
        represents_aggregation=True,
        description2='Collections of Lower level Business Processes, defined in the context of this Business Process realising courses of action pusuing subordinate goals.',
        multiValued=1,
        owner_class_name="BPDProcesoDeNegocio",
        expression="context.objectValues(['BPDColeccionProcesosDeNegocio'])",
        computed_types=['BPDColeccionProcesosDeNegocio'],
        non_framework_elements=False,
        description='Colecciones de Procesos de Negocio de orden inferior, definidos en el contexto de este Proceso de negocio, realizando cursos de accion persiguiendo metas subordinadas.'
    ),

    ComputedField(
        name='detallesProceso',
        widget=ComputedField._properties['widget'](
            label="Detalles del Proceso de Negocio",
            label2="Business Process details",
            description="Detalles acerca de las caracteristicas del Proceso de Negocio.",
            description2="Details about the fetarues of the Busienss Process",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_detallesProceso_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_attr_detallesProceso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Detalles acerca de las caracteristicas del Proceso de Negocio.",
        duplicates="0",
        label2="Business Process details",
        ea_localid="296",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the fetarues of the Busienss Process",
        ea_guid="{A3169B74-8F74-4c2b-BF02-9BEF2465A7AC}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del Proceso de Negocio",
        length="0",
        containment="Not Specified",
        position="8",
        owner_class_name="BPDProcesoDeNegocio",
        expression="context.fTFLVs([ 'esPlaneado', 'esContinuo','esRepetible', ])",
        computed_types="string"
    ),

    RelationField(
        name='usadoComoSubProcesos',
        inverse_relation_label="Proceso de Negocio usado",
        additional_columns=['proposito','responsableMantenimiento','detallesProceso','estado','nivelDeImposicion',],
        inverse_relation_description="Proceso de Negocio que se ejecuta como parte del Proceso de Negocio de mayor alcance.",
        description="Pasos de otros Procesos de Negocio donde este proceso se ejecuta de principio a fin, como un Paso Sub-Proceso.",
        relationship='BPDUsadoComoSubProcesos',
        inverse_relation_field_name='procesoUsado',
        sourcestyle="Owned=0;Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;",
        inverse_relation_label2="Used Business Process",
        label2="Used as Sub-Business Process in",
        inverse_relation_description2="Business Process executed as part of the current one.",
        widget=ReferenceBrowserWidget(
            label="Usos como Sub-Proceso de Negocio",
            label2="Used as Sub-Business Process in",
            description="Pasos de otros Procesos de Negocio donde este proceso se ejecuta de principio a fin, como un Paso Sub-Proceso.",
            description2="Business Processes where this one is used as a Sub-Process",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_usadoComoSubProcesos_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_usadoComoSubProcesos_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Usos como Sub-Proceso de Negocio",
        description2="Business Processes where this one is used as a Sub-Process",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDProcesoUsado',
        dependency_supplier=True
    ),

    RelationField(
        name='reglasDeNegocioDirigentes',
        inverse_relation_label="Procesos de Negocio dirigidos",
        inverse_relation_description="Procesos de Negocio que toman en cuenta la Regla de Negocio durante su ejecucion.",
        description="Reglas de Negocio a tomar en cuenta durante durante la ejecucion del Proceso de Negocio.",
        relationship='BPDReglasDeNegocioDirigentes',
        label2="Guiding Business Rules",
        widget=ReferenceBrowserWidget(
            label="Reglas de Negocio Dirigentes",
            label2="Guiding Business Rules",
            description="Reglas de Negocio a tomar en cuenta durante durante la ejecucion del Proceso de Negocio.",
            description2="Business Rules to take into account when executing the Business Process.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_reglasDeNegocioDirigentes_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_reglasDeNegocioDirigentes_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Rules to take into account when executing the Business Process.",
        inverse_relation_label2="Guided Business Processes",
        deststyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        write_permission='Modify portal content',
        inverse_relation_field_name='procesosDeNegocioDirigidos',
        inverse_relation_description2="Business Process applying or enforcing during their execution this Business Rule.",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label="Reglas de Negocio Dirigentes",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDProcesosDeNegocioDirigidos',
        owner_class_name="BPDProcesoDeNegocio"
    ),

    RelationField(
        name='politicasDeNegocioGobernantes',
        inverse_relation_label="Procesos de Negocio gobernados",
        inverse_relation_description="Procesos de Negocio que respetan o se esfuerzan en hacer cumplir la Politica de Negocio.",
        description="Politicas de Negocio a respetar durante la ejecucion del Proceso de Negocio.",
        relationship='BPDPoliticasDeNegocioGobernantes',
        label2="Governing Business Policies",
        widget=ReferenceBrowserWidget(
            label="Politicas de Negocio Gobernantes",
            label2="Governing Business Policies",
            description="Politicas de Negocio a respetar durante la ejecucion del Proceso de Negocio.",
            description2="Business Policies to observe when executing the Business Process.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_politicasDeNegocioGobernantes_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_politicasDeNegocioGobernantes_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Policies to observe when executing the Business Process.",
        inverse_relation_label2="Governed Business Processes",
        deststyle="Owned=0;Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;",
        write_permission='Modify portal content',
        inverse_relation_field_name='procesosDeNegocioGobernados',
        inverse_relation_description2="Business Processes that abide by, or enforce the Business Policy.",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label="Politicas de Negocio Gobernantes",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDProcesosDeNegocioGobernados',
        owner_class_name="BPDProcesoDeNegocio"
    ),

    RelationField(
        name='ejecutores',
        inverse_relation_label="Procesos Ejecutados",
        inverse_relation_description="Procesos de Negocio que se encarga de ejecutar el Perfil o Unidad Organizacional.",
        description="Los Perfiles o Unidades Organizacionales a cargo de ejecutar el Proceso de Negocio.",
        relationship='BPDEjecutoresDelProceso',
        label2="Performers",
        widget=ReferenceBrowserWidget(
            label="Ejecutores del Proceso",
            label2="Performers",
            description="Los Perfiles o Unidades Organizacionales a cargo de ejecutar el Proceso de Negocio.",
            description2="Participant Profiles and Organisational Units allowed to execute the Business Process.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_ejecutores_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_ejecutores_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Participant Profiles and Organisational Units allowed to execute the Business Process.",
        inverse_relation_label2="Performed Business Processes",
        deststyle="Owned=0;Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;",
        write_permission='Modify portal content',
        inverse_relation_field_name='procesosEjecutados',
        inverse_relation_description2="Business Process that can be executed by the participant Profile or Organisational Unit.",
        additional_columns=['abreviatura', 'responsabilidadesClave'],
        label="Ejecutores del Proceso",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDProcesosEjecutados',
        owner_class_name="BPDProcesoDeNegocio"
    ),

    RelationField(
        name='supervisor',
        inverse_relation_label="Procesos Supervisados",
        inverse_relation_description="Procesos de Negocio que se encarga de supervisar el Perfil o Unidad Organizacional.",
        description="El Perfil o Unidad Organizacional a cargo de velar por que el cumplimiento del Proceso de Negocio se realize de acuerdo con la regulacion aplicable.",
        relationship='BPDSupervisor',
        label2="Supervisor",
        widget=ReferenceBrowserWidget(
            label="Supervisor",
            label2="Supervisor",
            description="El Perfil o Unidad Organizacional a cargo de velar por que el cumplimiento del Proceso de Negocio se realize de acuerdo con la regulacion aplicable.",
            description2="The participant Profile or Organisational Unit is responsible to ensure the compliance of the Business Process execution with applicable directives.",
            label_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_supervisor_label',
            description_msgid='gvSIGbpd_BPDProcesoDeNegocio_rel_supervisor_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="The participant Profile or Organisational Unit is responsible to ensure the compliance of the Business Process execution with applicable directives.",
        inverse_relation_label2="Supervised Business Processes",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='procesosSupervisados',
        inverse_relation_description2="Business Process under supervision of the participant Profile or Organisational Unit.",
        additional_columns=['abreviatura', 'responsabilidadesClave'],
        label="Supervisor",
        multiValued=0,
        containment="Unspecified",
        inverse_relationship='BPDProcesosSupervisados',
        owner_class_name="BPDProcesoDeNegocio"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDProcesoDeNegocio_schema = getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDProcesoDeNegocio(OrderedBaseFolder, BPDArquetipoConAdopcion):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),)



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



    allowed_content_types = ['BPDColeccionProcesosDeNegocio'] + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', []))

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

    schema = BPDProcesoDeNegocio_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getText')
    def getText(self):
        """
        """
        
        return self.getProposito()

    security.declarePublic('setText')
    def setText(self,theText):
        """
        """
        
        self.setProposito( theText)
# end of class BPDProcesoDeNegocio

##code-section module-footer #fill in your manual code here
##/code-section module-footer



