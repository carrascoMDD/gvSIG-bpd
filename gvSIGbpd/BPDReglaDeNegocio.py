# -*- coding: utf-8 -*-
#
# File: BPDReglaDeNegocio.py
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
from Products.ATContentTypes.content.base import ATCTMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='coleccionesReglasDeNegocio',
        widget=ComputedWidget(
            label="Reglas de Negocio mas detalladas",
            label2="More specific Business Rules",
            description="Colecciones de Reglas de Negocio mas detalladas que se derivan de las politicas de Negocio, y dirigen los Procesos de Negocio de la Organizacion, definidas como un refinamiento de esta Regla de Negocio.",
            description2="Collections of Subordinated Business Rules derived from Business Policies, and driving the Business Process in the Organisation, defined as a refinement of this Business Rule.",
            label_msgid='gvSIGbpd_BPDReglaDeNegocio_contents_coleccionesReglasDeNegocio_label',
            description_msgid='gvSIGbpd_BPDReglaDeNegocio_contents_coleccionesReglasDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='More specific Business Rules',
        label='Reglas de Negocio mas detalladas',
        represents_aggregation=True,
        description2='Collections of Subordinated Business Rules derived from Business Policies, and driving the Business Process in the Organisation, defined as a refinement of this Business Rule.',
        multiValued=1,
        owner_class_name="BPDReglaDeNegocio",
        expression="context.objectValues(['BPDColeccionReglasDeNegocio'])",
        computed_types=['BPDColeccionReglasDeNegocio'],
        non_framework_elements=False,
        description='Colecciones de Reglas de Negocio mas detalladas que se derivan de las politicas de Negocio, y dirigen los Procesos de Negocio de la Organizacion, definidas como un refinamiento de esta Regla de Negocio.'
    ),

    RelationField(
        name='pasosAplicandoLaRegla',
        inverse_relation_label="Reglas de Negocio aplicadas",
        inverse_relation_description="Reglas de Negocio aplicadas durante la ejecucion del Paso.",
        description="Pasos de Procesos de Negocio donde se aplica la Regla de Negocio",
        relationship='PasosAplicandoLaRegla',
        label2="Business Process Steps applying the Business Rule",
        widget=ReferenceBrowserWidget(
            label="Pasos dirigidos",
            label2="Business Process Steps applying the Business Rule",
            description="Pasos de Procesos de Negocio donde se aplica la Regla de Negocio",
            description2="Business Process Steps applying the Business Rule.",
            label_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_pasosAplicandoLaRegla_label',
            description_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_pasosAplicandoLaRegla_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Process Steps applying the Business Rule.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Applied Business Rules",
        dependency_supplier=True,
        inverse_relation_field_name='reglasDeNegocioAplicadas',
        inverse_relation_description2="Business Rules applicable in the Business Process Steps.",
        additional_columns=['codigo','estado','nivelDeImposicion',],
        write_permission='Modify portal content',
        label="Pasos dirigidos",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ReglasDeNegocioAplicadas'
    ),

    RelationField(
        name='politicasDeNegocioBase',
        inverse_relation_label="Reglas de Negocio derivadas",
        containment="Unspecified",
        inverse_relation_description="Reglas de Negocio que refinan la Politica de Negocio en terminos decidibles.",
        description="Politicas de Negocio de las que se deriva la Regla de Negocio",
        relationship='PoliticasDeNegocioBase',
        inverse_relation_field_name='reglasDeNegocioDerivadas',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Base Business Policies",
        inverse_relation_description2="Business Rules derived from the Business Policy.",
        widget=ReferenceBrowserWidget(
            label="Politicas de Negocio base",
            label2="Base Business Policies",
            description="Politicas de Negocio de las que se deriva la Regla de Negocio",
            description2="Business Policies that are the basis of the Business Rule",
            label_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_politicasDeNegocioBase_label',
            description_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_politicasDeNegocioBase_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Politicas de Negocio base",
        description2="Business Policies that are the basis of the Business Rule",
        multiValued=1,
        inverse_relation_label2="Derived Business Rules",
        inverse_relationship='ReglasDeNegocioDerivadas',
        write_permission='Modify portal content',
        additional_columns=['codigo','estado','nivelDeImposicion',]
    ),

    RelationField(
        name='participantesDirigidos',
        inverse_relation_label="Reglas de Negocio dirigentes",
        inverse_relation_description="Las Reglas de Negocio que dirigen la labor de el Perfil o Unidad Organizacional.",
        description="Perfiles y Unidades Organizacionales que aplican la Regla de Negocio durante su labor.",
        relationship='ParticipantesDirigidos',
        label2="Directed Participant Profiles and Organisational Units",
        widget=ReferenceBrowserWidget(
            label="Participantes dirigidos",
            label2="Directed Participant Profiles and Organisational Units",
            description="Perfiles y Unidades Organizacionales que aplican la Regla de Negocio durante su labor.",
            description2="Participant Profiles and Organisational Units that apply the Business Rule.",
            label_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_participantesDirigidos_label',
            description_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_participantesDirigidos_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Participant Profiles and Organisational Units that apply the Business Rule.",
        inverse_relation_label2="Directing Business Rules",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='reglasDeNegocioDirigentes',
        inverse_relation_description2="Business Rule affecting the participant Profile or Organisational Unit",
        additional_columns=['abreviatura', 'responsabilidadesClave'],
        label="Participantes dirigidos",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='AfectadoPorReglasDeNegocio',
        owner_class_name="BPDReglaDeNegocio"
    ),

    RelationField(
        name='herramientasDirigidas',
        inverse_relation_label="Reglas de Negocio dirigentes",
        inverse_relation_description="Reglas de Negocio que dirigen el uso de la Herramienta en la Organizacion.",
        description="Herramientas cuya utilizacion esta dirigida por la Regla de Negocio.",
        relationship='HerramientasDirigidas',
        label2="Driven Tools",
        widget=ReferenceBrowserWidget(
            label="Herramientas dirigidas",
            label2="Driven Tools",
            description="Herramientas cuya utilizacion esta dirigida por la Regla de Negocio.",
            description2="Tools whose usage is directed by the Business Rule.",
            label_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_herramientasDirigidas_label',
            description_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_herramientasDirigidas_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Tools whose usage is directed by the Business Rule.",
        inverse_relation_label2="Directing Business Rules",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='reglasDeNegocioDirigentes',
        inverse_relation_description2="Business Rules directing the usage of the Tool.",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label="Herramientas dirigidas",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='HerramientaAfectadaPorReglasDeNegocio',
        owner_class_name="BPDReglaDeNegocio"
    ),

    RelationField(
        name='artefactosDirigidos',
        inverse_relation_label="Reglas de Negocio dirigentes",
        inverse_relation_description="Reglas de Negocio que dirigen el uso del Artefacto en la Organizacion.",
        description="Artefactos cuya utilizacion esta prescrita o gobernada por la Regla de Negocio.",
        relationship='ArtefactosDirigidos',
        label2="Affected Artefacts",
        widget=ReferenceBrowserWidget(
            label="Artefactos dirigidos",
            label2="Affected Artefacts",
            description="Artefactos cuya utilizacion esta prescrita o gobernada por la Regla de Negocio.",
            description2="Artefacts whose usage is directed by the Business Rule.",
            label_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_artefactosDirigidos_label',
            description_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_artefactosDirigidos_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Artefacts whose usage is directed by the Business Rule.",
        inverse_relation_label2="Affected by Business Rules",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='reglasDeNegocioDirigentes',
        inverse_relation_description2="Business Rules directing the use of the Artefact",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label="Artefactos dirigidos",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='ArtefactoAfectadoPorReglasDeNegocio',
        owner_class_name="BPDReglaDeNegocio"
    ),

    RelationField(
        name='procesosDeNegocioDirigidos',
        inverse_relation_label="Reglas de Negocio Dirigentes",
        containment="Unspecified",
        inverse_relation_description="Reglas de Negocio a tomar en cuenta durante durante la ejecucion del Proceso de Negocio.",
        description="Procesos de Negocio que toman en cuenta la Regla de Negocio durante su ejecucion.",
        relationship='ProcesosDeNegocioDirigidos',
        inverse_relation_field_name='reglasDeNegocioDirigentes',
        sourcestyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;",
        label2="Guided Business Processes",
        inverse_relation_description2="Business Rules to take into account when executing the Business Process.",
        widget=ReferenceBrowserWidget(
            label="Procesos de Negocio dirigidos",
            label2="Guided Business Processes",
            description="Procesos de Negocio que toman en cuenta la Regla de Negocio durante su ejecucion.",
            description2="Business Process applying or enforcing during their execution this Business Rule.",
            label_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_procesosDeNegocioDirigidos_label',
            description_msgid='gvSIGbpd_BPDReglaDeNegocio_rel_procesosDeNegocioDirigidos_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Procesos de Negocio dirigidos",
        description2="Business Process applying or enforcing during their execution this Business Rule.",
        multiValued=1,
        inverse_relation_label2="Guiding Business Rules",
        inverse_relationship='ReglasDeNegocioDirigentes',
        write_permission='Modify portal content',
        additional_columns=['codigo','estado','nivelDeImposicion',]
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDReglaDeNegocio_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDReglaDeNegocio(OrderedBaseFolder, BPDArquetipoConAdopcion):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Regla de Negocio'

    meta_type = 'BPDReglaDeNegocio'
    portal_type = 'BPDReglaDeNegocio'
    allowed_content_types = ['BPDColeccionReglasDeNegocio'] + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdregladenegocio.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Regla que desarrolla Politicas de Negocio,  posiblemente aplicada en la ejecucion de Procesos de Negocio, o afectando la operacion de Unidaddes Organizacionales, Perfiles, Artefactos y Herramientas."
    typeDescMsgId =  'gvSIGbpd_BPDReglaDeNegocio_help'
    archetype_name2 = 'Business Rule'
    typeDescription2 = '''Business Rule based in Busines Policies, possibly applied during the execution of Business Processes or their Steps, or affecting the operation of Organisational Units, Profiles, Artefacts and Tools.'''
    archetype_name_msgid = 'gvSIGbpd_BPDReglaDeNegocio_label'
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

    schema = BPDReglaDeNegocio_schema

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

registerType(BPDReglaDeNegocio, PROJECTNAME)
# end of class BPDReglaDeNegocio

##code-section module-footer #fill in your manual code here
##/code-section module-footer



