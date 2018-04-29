# -*- coding: utf-8 -*-
#
# File: BPDPoliticaDeNegocio.py
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
        name='coleccionesPoliticasDeNegocio',
        widget=ComputedWidget(
            label="Politicas de Negocio mas detalladas",
            label2="More specific Business Policies",
            description="Colecciones de Politicas de Negocio subordinadas o mas detalladas, que gobiernan la Organizacion y sus Procesos de Negocio, y constituyen la base de las Reglas de Negocio, definidas en el contexto de esta Politica de Negocio.",
            description2="Collections of Subordinated Business Policies  governing the Organisation and its Business Processes, and constitute the basis for the Business Rules, defined in the context of this Business Policy.",
            label_msgid='gvSIGbpd_BPDPoliticaDeNegocio_contents_coleccionesPoliticasDeNegocio_label',
            description_msgid='gvSIGbpd_BPDPoliticaDeNegocio_contents_coleccionesPoliticasDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        description='Colecciones de Politicas de Negocio subordinadas o mas detalladas, que gobiernan la Organizacion y sus Procesos de Negocio, y constituyen la base de las Reglas de Negocio, definidas en el contexto de esta Politica de Negocio.',
        label2='More specific Business Policies',
        label='Politicas de Negocio mas detalladas',
        description2='Collections of Subordinated Business Policies  governing the Organisation and its Business Processes, and constitute the basis for the Business Rules, defined in the context of this Business Policy.',
        multiValued=1,
        owner_class_name="BPDPoliticaDeNegocio",
        expression="context.objectValues(['BPDColeccionPoliticasDeNegocio'])",
        computed_types=['BPDColeccionPoliticasDeNegocio'],
        represents_aggregation=True
    ),

    RelationField(
        name='reglasDeNegocioDerivadas',
        inverse_relation_label="Politicas de Negocio base",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        inverse_relation_description="Politicas de Negocio de las que se deriva la Regla de Negocio",
        description="Reglas de Negocio que refinan la Politica de Negocio en terminos decidibles.",
        relationship='ReglasDeNegocioDerivadas',
        inverse_relation_field_name='politicasDeNegocioBase',
        inverse_relation_label2="Base Business Policies",
        label2="Derived Business Rules",
        inverse_relation_description2="Business Policies that are the basis of the Business Rule",
        widget=ReferenceBrowserWidget(
            label="Reglas de Negocio derivadas",
            label2="Derived Business Rules",
            description="Reglas de Negocio que refinan la Politica de Negocio en terminos decidibles.",
            description2="Business Rules derived from the Business Policy.",
            label_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_reglasDeNegocioDerivadas_label',
            description_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_reglasDeNegocioDerivadas_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Reglas de Negocio derivadas",
        description2="Business Rules derived from the Business Policy.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='PoliticasDeNegocioBase',
        owner_class_name="BPDPoliticaDeNegocio",
        dependency_supplier=True
    ),

    RelationField(
        name='herramientasGobernadas',
        inverse_relation_label="Politicas de Negocio gobernantes",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        inverse_relation_description="Politicas de Negocio que prescriben o gobiernan el uso de la Herramienta en la Organizacion.",
        description="Herramientas cuya utilizacion esta prescrita o gobernada por la Politica de Negocio.",
        relationship='HerramientasGobernadas',
        inverse_relation_field_name='politicasDeNegocioGobernantes',
        inverse_relation_label2="Governing Business Policies",
        label2="Governed Tools",
        inverse_relation_description2="Business Policies that prescribe or govern the utilisation of the Tool in the Organisation",
        widget=ReferenceBrowserWidget(
            label="Herramientas Gobernadas",
            label2="Governed Tools",
            description="Herramientas cuya utilizacion esta prescrita o gobernada por la Politica de Negocio.",
            description2="Tools whose usage is prescribed or governed by the Business Policy.",
            label_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_herramientasGobernadas_label',
            description_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_herramientasGobernadas_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Herramientas Gobernadas",
        description2="Tools whose usage is prescribed or governed by the Business Policy.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='HerramientaAfectadaPorPoliticasDeNegocio',
        owner_class_name="BPDPoliticaDeNegocio",
        dependency_supplier=True
    ),

    RelationField(
        name='participantesGobernados',
        inverse_relation_label="Politicas de Negocio gobernantes",
        additional_columns=['abreviatura', 'responsabilidadesClave'],
        inverse_relation_description="Las Politicas de Negocio que afectan a la labor del Perfil o Unidad Organizacional",
        description="Perfiles y Unidades Organizacionales que aplican la Politica de Negocio durante su labor.",
        relationship='ParticipantesGobernados',
        inverse_relation_field_name='politicasDeNegocioGobernantes',
        inverse_relation_label2="Governing Business Policies",
        label2="Governed participant Profiles and Organisational Units",
        inverse_relation_description2="Business Policies governing the participant Profile or Organisational Unit.",
        widget=ReferenceBrowserWidget(
            label="Participantes gobernados",
            label2="Governed participant Profiles and Organisational Units",
            description="Perfiles y Unidades Organizacionales que aplican la Politica de Negocio durante su labor.",
            description2="Participant Profiles and Organisational Units that must endeavour to apply the Business Policy.",
            label_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_participantesGobernados_label',
            description_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_participantesGobernados_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Participantes gobernados",
        description2="Participant Profiles and Organisational Units that must endeavour to apply the Business Policy.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='AfectadoPorPoliticasDeNegocio',
        owner_class_name="BPDPoliticaDeNegocio",
        dependency_supplier=True
    ),

    RelationField(
        name='artefactosGobernados',
        inverse_relation_label="Politicas de Negocio gobernantes",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        inverse_relation_description="Politicas de Negocio que prescriben o gobiernan el uso del Artefacto en la Organizacion.",
        description="Artefactos cuya utilizacion esta prescrita o gobernada por la Politica de Negocio.",
        relationship='ArtefactosGobernados',
        inverse_relation_field_name='politicasDeNegocioGobernantes',
        inverse_relation_label2="Geverning Business Policies",
        label2="Governed Artefacts",
        inverse_relation_description2="Business Policies that prescribe or govern the utilisation of the Artefact in the Organisation",
        widget=ReferenceBrowserWidget(
            label="Artefactos Gobernados",
            label2="Governed Artefacts",
            description="Artefactos cuya utilizacion esta prescrita o gobernada por la Politica de Negocio.",
            description2="Artefacts whose usage is directed by the Business Policy.",
            label_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_artefactosGobernados_label',
            description_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_artefactosGobernados_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Artefactos Gobernados",
        description2="Artefacts whose usage is directed by the Business Policy.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='ArtefactoAfectadoPorPoliticasDeNegocio',
        owner_class_name="BPDPoliticaDeNegocio",
        dependency_supplier=True
    ),

    RelationField(
        name='procesosDeNegocioGobernados',
        inverse_relation_label="Politicas de Negocio Gobernantes",
        inverse_relation_description="Politicas de Negocio a respetar durante la ejecucion del Proceso de Negocio.",
        description="Procesos de Negocio que respetan o se esfuerzan en hacer cumplir la Politica de Negocio.",
        relationship='ProcesosDeNegocioGobernados',
        label2="Governed Business Processes",
        widget=ReferenceBrowserWidget(
            label="Procesos de Negocio gobernados",
            label2="Governed Business Processes",
            description="Procesos de Negocio que respetan o se esfuerzan en hacer cumplir la Politica de Negocio.",
            description2="Business Processes that abide by, or enforce the Business Policy.",
            label_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_procesosDeNegocioGobernados_label',
            description_msgid='gvSIGbpd_BPDPoliticaDeNegocio_rel_procesosDeNegocioGobernados_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Processes that abide by, or enforce the Business Policy.",
        sourcestyle="Owned=0;Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;",
        inverse_relation_label2="Governing Business Policies",
        dependency_supplier=True,
        inverse_relation_field_name='politicasDeNegocioGobernantes',
        inverse_relation_description2="Business Policies to observe when executing the Business Process.",
        additional_columns=['codigo','estado','nivelDeImposicion',],
        write_permission='Modify portal content',
        label="Procesos de Negocio gobernados",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='PoliticasDeNegocioGobernantes'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPoliticaDeNegocio_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPoliticaDeNegocio(OrderedBaseFolder, BPDArquetipoConAdopcion):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Politica de Negocio'

    meta_type = 'BPDPoliticaDeNegocio'
    portal_type = 'BPDPoliticaDeNegocio'
    allowed_content_types = ['BPDColeccionPoliticasDeNegocio'] + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdpoliticadenegocio.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Directiva general a desarrollar mediante Reglas y realizar mediante Procesos de Negocio."
    typeDescMsgId =  'gvSIGbpd_BPDPoliticaDeNegocio_help'
    archetype_name2 = 'Business Policy'
    typeDescription2 = '''General directive to develop into Rules and realise with Business Processes'''
    archetype_name_msgid = 'gvSIGbpd_BPDPoliticaDeNegocio_label'
    factory_methods = None
    factory_enablers = None


    actions =  (


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
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


       {'action': "string:${object_url}/MDDExport",
        'category': "object",
        'id': 'mddexport',
        'name': 'Export',
        'permissions': ("View",),
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
        'category': "object",
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

    schema = BPDPoliticaDeNegocio_schema

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

registerType(BPDPoliticaDeNegocio, PROJECTNAME)
# end of class BPDPoliticaDeNegocio

##code-section module-footer #fill in your manual code here
##/code-section module-footer



