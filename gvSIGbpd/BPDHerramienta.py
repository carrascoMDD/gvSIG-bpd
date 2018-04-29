# -*- coding: utf-8 -*-
#
# File: BPDHerramienta.py
#
# Copyright (c) 2011 by Conselleria de Infraestructuras y Transporte de la
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
        name='coleccionesHerramientas',
        widget=ComputedWidget(
            label="Herramientas subordinadas",
            label2="Subordinated Tools",
            description="Colecciones de Herramientas de orden inferior, que la Organizacion aplica para manejar ciertos Artefactos y asistir en la ejecucion de Pasos de Procesos de Negocio, albergadas en el contexto de esta herramienta.",
            description2="Collections of Subordinated Tools applied in the Organisation to handle certain Artefacts, and assist in the execution of Business Process Steps, hosted in the context of this tool.",
            label_msgid='gvSIGbpd_BPDHerramienta_contents_coleccionesHerramientas_label',
            description_msgid='gvSIGbpd_BPDHerramienta_contents_coleccionesHerramientas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Subordinated Tools',
        label='Herramientas subordinadas',
        represents_aggregation=True,
        description2='Collections of Subordinated Tools applied in the Organisation to handle certain Artefacts, and assist in the execution of Business Process Steps, hosted in the context of this tool.',
        multiValued=1,
        owner_class_name="BPDHerramienta",
        expression="context.objectValues(['BPDColeccionHerramientas'])",
        computed_types=['BPDColeccionHerramientas'],
        non_framework_elements=False,
        description='Colecciones de Herramientas de orden inferior, que la Organizacion aplica para manejar ciertos Artefactos y asistir en la ejecucion de Pasos de Procesos de Negocio, albergadas en el contexto de esta herramienta.'
    ),

    RelationField(
        name='artefactosDeHerramienta',
        inverse_relation_label="Herramientas",
        containment="Unspecified",
        inverse_relation_description="Herramientas utiles para manejar Artefactos de este tipo.",
        description="Artefactos que pueden ser manipulados con la Herramienta.",
        relationship='BPDArtefactos',
        inverse_relation_field_name='herramientas',
        sourcestyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        label2="Artefacts handled with the Tool",
        inverse_relation_description2="Useful tools to handle Artefacts of this type.",
        widget=ReferenceBrowserWidget(
            label="Artefactos",
            label2="Artefacts handled with the Tool",
            description="Artefactos que pueden ser manipulados con la Herramienta.",
            description2="Artefacts where the tool is applied to visualize, edit or otherwise handle the Artefact content.",
            label_msgid='gvSIGbpd_BPDHerramienta_rel_artefactosDeHerramienta_label',
            description_msgid='gvSIGbpd_BPDHerramienta_rel_artefactosDeHerramienta_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Artefactos",
        description2="Artefacts where the tool is applied to visualize, edit or otherwise handle the Artefact content.",
        multiValued=1,
        inverse_relation_label2="Tools",
        inverse_relationship='BPDHerramientas',
        write_permission='Modify portal content',
        additional_columns=['codigo',]
    ),

    RelationField(
        name='pasosAsistidos',
        inverse_relation_label="Herramientas aplicadas",
        inverse_relation_description="Herramientas a utilizar para ejecutar este Paso del Proceso de Negocio, o manejar los Artefactos usados en el Paso. Considere ademas las Herramientas referidas como usadas desde todo el Proceso de Negocio.",
        description="Pasos de procesos de negocio donde se aplica la Herramienta.La Herramienta puede ademas se usada por Procesos de Negocio completos.",
        relationship='BPDPasosAsistidos',
        label2="Assisted Steps",
        widget=ReferenceBrowserWidget(
            label="Pasos Asistidos",
            label2="Assisted Steps",
            description="Pasos de procesos de negocio donde se aplica la Herramienta.La Herramienta puede ademas se usada por Procesos de Negocio completos.",
            description2="Business Process Steps applying the Tool. The Tool may be also applied by whole Business Processes.",
            label_msgid='gvSIGbpd_BPDHerramienta_rel_pasosAsistidos_label',
            description_msgid='gvSIGbpd_BPDHerramienta_rel_pasosAsistidos_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Process Steps applying the Tool. The Tool may be also applied by whole Business Processes.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Applied Tools",
        dependency_supplier=True,
        inverse_relation_field_name='herramientasAplicadas',
        inverse_relation_description2="Tools to apply in the execution of the Business Process Step, or to manipulate the used Artefacts. Consider too the Tools refered as used in the whole Business Process.",
        additional_columns=['codigo',],
        write_permission='Modify portal content',
        label="Pasos Asistidos",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDHerramientasAplicadas'
    ),

    RelationField(
        name='procesosAsistidos',
        inverse_relation_label="Herramientas Aplicadas",
        additional_columns=['codigo',],
        inverse_relation_description="Herramientas aplicadas en la realizacion del Proceso de Negocio. Considere ademas las Herramientas que se aplican en Pasos individuales del Proceso de Negocio.",
        description="Procesos de Negocio donde se aplica la Herramienta.La Herramienta puede ademas se usada por Pasos individuales del Procesos de Negocio.",
        relationship='BPDProcesosAsistidos',
        inverse_relation_field_name='herramientasAplicadas',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Applied Tools",
        label2="Assisted Business Processes",
        inverse_relation_description2="Tools applied in executing the Business Process. Consider too the Tools applied in individual Business Process Steps.",
        widget=ReferenceBrowserWidget(
            label="Procesos de Negocio Asistidos",
            label2="Assisted Business Processes",
            description="Procesos de Negocio donde se aplica la Herramienta.La Herramienta puede ademas se usada por Pasos individuales del Procesos de Negocio.",
            description2="Business Processes applying the Tool. The Tool may be also applied by individual Business Processes Steps.",
            label_msgid='gvSIGbpd_BPDHerramienta_rel_procesosAsistidos_label',
            description_msgid='gvSIGbpd_BPDHerramienta_rel_procesosAsistidos_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Procesos de Negocio Asistidos",
        description2="Business Processes applying the Tool. The Tool may be also applied by individual Business Processes Steps.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDHerramientasAplicadasEnProcesos',
        dependency_supplier=True
    ),

    RelationField(
        name='reglasDeNegocioDirigentes',
        inverse_relation_label="Herramientas dirigidas",
        containment="Unspecified",
        inverse_relation_description="Herramientas cuya utilizacion esta dirigida por la Regla de Negocio.",
        description="Reglas de Negocio que dirigen el uso de la Herramienta en la Organizacion.",
        relationship='BPDHerramientasAfectadasPorReglasDeNegocio',
        inverse_relation_field_name='herramientasDirigidas',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Directing Business Rules",
        inverse_relation_description2="Tools whose usage is directed by the Business Rule.",
        widget=ReferenceBrowserWidget(
            label="Reglas de Negocio dirigentes",
            label2="Directing Business Rules",
            description="Reglas de Negocio que dirigen el uso de la Herramienta en la Organizacion.",
            description2="Business Rules directing the usage of the Tool.",
            label_msgid='gvSIGbpd_BPDHerramienta_rel_reglasDeNegocioDirigentes_label',
            description_msgid='gvSIGbpd_BPDHerramienta_rel_reglasDeNegocioDirigentes_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Reglas de Negocio dirigentes",
        description2="Business Rules directing the usage of the Tool.",
        multiValued=1,
        inverse_relation_label2="Driven Tools",
        inverse_relationship='BPDHerramientasDirigidas',
        write_permission='Modify portal content',
        additional_columns=['codigo',]
    ),

    RelationField(
        name='instrucciones',
        inverse_relation_label="Herramientas Documentadas",
        additional_columns=['proposito', 'detallesProceso'],
        inverse_relation_description="Herramientas cuya utilizacion se documenta en este proceso.",
        description="Instrucciones acerca de como utilizar la Herramienta para alcanzar un objetivo, expresado como un proceso con entradas, pasos y salidas.",
        relationship='BPDInstrucciones',
        inverse_relation_field_name='herramientasDocumentadas',
        inverse_relation_label2="Documented Tools",
        label2="Instructions",
        inverse_relation_description2="Tools whose usage is documented in this process.",
        widget=ReferenceBrowserWidget(
            label="Instrucciones",
            label2="Instructions",
            description="Instrucciones acerca de como utilizar la Herramienta para alcanzar un objetivo, expresado como un proceso con entradas, pasos y salidas.",
            description2="Instructions about how to use the Tool to accomplish a goal, expressed as a process with inputs, steps and outputs.",
            label_msgid='gvSIGbpd_BPDHerramienta_rel_instrucciones_label',
            description_msgid='gvSIGbpd_BPDHerramienta_rel_instrucciones_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Instrucciones",
        description2="Instructions about how to use the Tool to accomplish a goal, expressed as a process with inputs, steps and outputs.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDHerramientasDocumentadas',
        owner_class_name="BPDHerramienta",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;"
    ),

    RelationField(
        name='politicasDeNegocioGobernantes',
        inverse_relation_label="Herramientas Gobernadas",
        containment="Unspecified",
        inverse_relation_description="Herramientas cuya utilizacion esta prescrita o gobernada por la Politica de Negocio.",
        description="Politicas de Negocio que prescriben o gobiernan el uso de la Herramienta en la Organizacion.",
        relationship='BPDHerramientasAfectadasPorPoliticasDeNegocio',
        inverse_relation_field_name='herramientasGobernadas',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Governing Business Policies",
        inverse_relation_description2="Tools whose usage is prescribed or governed by the Business Policy.",
        widget=ReferenceBrowserWidget(
            label="Politicas de Negocio gobernantes",
            label2="Governing Business Policies",
            description="Politicas de Negocio que prescriben o gobiernan el uso de la Herramienta en la Organizacion.",
            description2="Business Policies that prescribe or govern the utilisation of the Tool in the Organisation",
            label_msgid='gvSIGbpd_BPDHerramienta_rel_politicasDeNegocioGobernantes_label',
            description_msgid='gvSIGbpd_BPDHerramienta_rel_politicasDeNegocioGobernantes_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Politicas de Negocio gobernantes",
        description2="Business Policies that prescribe or govern the utilisation of the Tool in the Organisation",
        multiValued=1,
        inverse_relation_label2="Governed Tools",
        inverse_relationship='BPDHerramientasGobernadas',
        write_permission='Modify portal content',
        additional_columns=['codigo',]
    ),

    RelationField(
        name='responsablesDeHerramienta',
        inverse_relation_label="Herramientas a su Cargo",
        inverse_relation_description="Herramientas que estan a cargo de el Perfil o Unidad Organizacional",
        description="Perfiles o Unidades Organizacionales a cargo de asistir a la organizacion en su manejo de esta Herramienta.",
        relationship='BPDResponsablesDeHerramienta',
        label2="Profiles or Organisational Units Responsible for the Tool",
        widget=ReferenceBrowserWidget(
            label="Responsables",
            label2="Profiles or Organisational Units Responsible for the Tool",
            description="Perfiles o Unidades Organizacionales a cargo de asistir a la organizacion en su manejo de esta Herramienta.",
            description2="Participant Profiles or Organisational Units generally in charge of handling, administering or assisting the Teams in their usage of the Tool.",
            label_msgid='gvSIGbpd_BPDHerramienta_rel_responsablesDeHerramienta_label',
            description_msgid='gvSIGbpd_BPDHerramienta_rel_responsablesDeHerramienta_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Participant Profiles or Organisational Units generally in charge of handling, administering or assisting the Teams in their usage of the Tool.",
        inverse_relation_label2="In charge of Tools",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='responsableDeHerramientas',
        inverse_relation_description2="Tools for which the the participant Profile or Organisational Unit is generally responsible for.",
        additional_columns=['abreviatura'],
        label="Responsables",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDHerramientasACargo',
        owner_class_name="BPDHerramienta"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDHerramienta_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDHerramienta(OrderedBaseFolder, BPDArquetipoConAdopcion):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Herramienta'

    meta_type = 'BPDHerramienta'
    portal_type = 'BPDHerramienta'


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



    allowed_content_types = ['BPDColeccionHerramientas'] + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdherramienta.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Una Herramienta es una aplicacion informatica aplicada en ciertos pasos de sus Procesos de Negocio, posiblemente para operar con algunos Artefactos."
    typeDescMsgId                    =  'gvSIGbpd_BPDHerramienta_help'
    archetype_name2                  = 'Tool'
    typeDescription2                 = '''A Tool is software applied in certain Business Process Steps, possibly to operate with some Artefacts.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDHerramienta_label'
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

    schema = BPDHerramienta_schema

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

registerType(BPDHerramienta, PROJECTNAME)
# end of class BPDHerramienta

##code-section module-footer #fill in your manual code here
##/code-section module-footer



