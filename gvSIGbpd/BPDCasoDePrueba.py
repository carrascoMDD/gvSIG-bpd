# -*- coding: utf-8 -*-
#
# File: BPDCasoDePrueba.py
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
from Products.gvSIGbpd.BPDProgramable import BPDProgramable
from Products.gvSIGbpd.BPDArquetipoConAdopcion import BPDArquetipoConAdopcion
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='datosDePrueba',
        widget=ComputedWidget(
            label="Datos de Prueba",
            label2="Test Data",
            description="Definiciones de valores concretos para el Caso de Prueba contenedor.",
            description2="Definitions of concrete values for the container Test Case.",
            label_msgid='gvSIGbpd_BPDCasoDePrueba_contents_datosDePrueba_label',
            description_msgid='gvSIGbpd_BPDCasoDePrueba_contents_datosDePrueba_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Test Data',
        label='Datos de Prueba',
        represents_aggregation=True,
        description2='Definitions of concrete values for the container Test Case.',
        multiValued=1,
        owner_class_name="BPDCasoDePrueba",
        expression="context.objectValues(['BPDDatosDePrueba'])",
        computed_types=['BPDDatosDePrueba'],
        non_framework_elements=False,
        description='Definiciones de valores concretos para el Caso de Prueba contenedor.'
    ),

    ComputedField(
        name='coleccionesCasosDePrueba',
        widget=ComputedWidget(
            label="Casos de Prueba mas detallados",
            label2="More specific Test Cases",
            description="Casos de Prueba mas especificos definiendo conjuntos de valores concretos para los Escenarios relacionados.",
            description2="More specific Test Cases defining concrete data sets of values for the related Scenarios.",
            label_msgid='gvSIGbpd_BPDCasoDePrueba_contents_coleccionesCasosDePrueba_label',
            description_msgid='gvSIGbpd_BPDCasoDePrueba_contents_coleccionesCasosDePrueba_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='More specific Test Cases',
        label='Casos de Prueba mas detallados',
        represents_aggregation=True,
        description2='More specific Test Cases defining concrete data sets of values for the related Scenarios.',
        multiValued=1,
        owner_class_name="BPDCasoDePrueba",
        expression="context.objectValues(['BPDColeccionCasosDePrueba'])",
        computed_types=['BPDColeccionCasosDePrueba'],
        non_framework_elements=False,
        description='Casos de Prueba mas especificos definiendo conjuntos de valores concretos para los Escenarios relacionados.'
    ),

    RelationField(
        name='escenario',
        inverse_relation_label="Escenario",
        inverse_relation_description="Escenario para el que se definen los conjuntos de valores.",
        description="Casos de Prueba definiendo conjuntos de valores concretos para el Escenario contenedor.",
        relationship='CasosDePrueba_Escenario',
        inverse_relation_field_name='casosDePrueba',
        inverse_relation_label2="Scenario",
        label2="Test Cases",
        inverse_relation_description2="Scenario for which concreate value sets are defined.",
        widget=ReferenceBrowserWidget(
            label="Casos de Prueba",
            label2="Test Cases",
            description="Casos de Prueba definiendo conjuntos de valores concretos para el Escenario contenedor.",
            description2="Test Cases defining concrete data sets of values for the container Scenario.",
            label_msgid='gvSIGbpd_BPDCasoDePrueba_rel_escenario_label',
            description_msgid='gvSIGbpd_BPDCasoDePrueba_rel_escenario_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Casos de Prueba",
        description2="Test Cases defining concrete data sets of values for the container Scenario.",
        multiValued=0,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='Escenario_CasosDePrueba',
        owner_class_name="BPDCasoDePrueba",
        dependency_supplier=True
    ),

    RelationField(
        name='listasDePruebas',
        inverse_relation_label="Casos de Prueba",
        containment="Unspecified",
        inverse_relation_description="Casos de Prueba ensablados en esta Lista de Prueba, para ser ejercitados en secuencia.",
        description="Listas de Pruebas en cuya secuencia se ejercita este Caso de Prueba.",
        relationship='CasosDePrueba_ListasDePruebas',
        inverse_relation_field_name='casosDePrueba',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Test Suites",
        inverse_relation_description2="Test Cases assembled in this Test Suite, to be exercised in sequence.",
        widget=ReferenceBrowserWidget(
            label="Listas de Pruebas",
            label2="Test Suites",
            description="Listas de Pruebas en cuya secuencia se ejercita este Caso de Prueba.",
            description2="Test Suites exercising this Test Case as part of their sequences.",
            label_msgid='gvSIGbpd_BPDCasoDePrueba_rel_listasDePruebas_label',
            description_msgid='gvSIGbpd_BPDCasoDePrueba_rel_listasDePruebas_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Listas de Pruebas",
        description2="Test Suites exercising this Test Case as part of their sequences.",
        multiValued=1,
        inverse_relation_label2="Test Cases",
        inverse_relationship='ListasDePruebas_CasosDePrueba',
        write_permission='Modify portal content',
        additional_columns=[]
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDCasoDePrueba_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDProgramable, 'schema', Schema(())).copy() + \
    getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDCasoDePrueba(OrderedBaseFolder, BPDProgramable, BPDArquetipoConAdopcion):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDProgramable,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Caso de Prueba'

    meta_type = 'BPDCasoDePrueba'
    portal_type = 'BPDCasoDePrueba'


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



    allowed_content_types = ['BPDDatosDePrueba', 'BPDColeccionCasosDePrueba'] + list(getattr(BPDProgramable, 'allowed_content_types', [])) + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdcasodeprueba.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Definicion de un conjunto de valores concretos para el Escenario relacionado"
    typeDescMsgId                    =  'gvSIGbpd_BPDCasoDePrueba_help'
    archetype_name2                  = 'Test Case'
    typeDescription2                 = '''Definition of a concrete data set of values for the related Scenario.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDCasoDePrueba_label'
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

    schema = BPDCasoDePrueba_schema

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

registerType(BPDCasoDePrueba, PROJECTNAME)
# end of class BPDCasoDePrueba

##code-section module-footer #fill in your manual code here
##/code-section module-footer



