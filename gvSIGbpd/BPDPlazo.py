# -*- coding: utf-8 -*-
#
# File: BPDPlazo.py
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
from Products.gvSIGbpd.BPDPasoConSiguientes import BPDPasoConSiguientes
from Products.gvSIGbpd.BPDPasoConAnteriores import BPDPasoConAnteriores
from Products.gvSIGbpd.BPDPasoGestorExcepciones import BPDPasoGestorExcepciones
from Products.gvSIGbpd.BPDPasoConExcepciones import BPDPasoConExcepciones
from Products.gvSIGbpd.BPDPasoMinimo import BPDPasoMinimo
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATContentTypes.content.base import ATCTMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    BooleanField(
        name='agotarPlazo',
        widget=BooleanField._properties['widget'](
            label="Agotar Plazo",
            label2="Wait for Deadline to expire",
            description="Si se desea agotar el tiempo antes de continuar, aunque se haya satisfecho la ocurrencia del paso requerido.",
            description2="Whether or not to wait for the Deadline to expire, even if the required step has been fulfilled.",
            label_msgid='gvSIGbpd_BPDPlazo_attr_agotarPlazo_label',
            description_msgid='gvSIGbpd_BPDPlazo_attr_agotarPlazo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Si se desea agotar el tiempo antes de continuar, aunque se haya satisfecho la ocurrencia del paso requerido.",
        duplicates="0",
        label2="Wait for Deadline to expire",
        ea_localid="223",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Whether or not to wait for the Deadline to expire, even if the required step has been fulfilled.",
        ea_guid="{0E40AB44-F6D5-4c70-AC8F-8AAA46A46647}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Agotar Plazo",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDPlazo"
    ),

    ComputedField(
        name='detallesPaso',
        widget=ComputedField._properties['widget'](
            label="Detalles del Paso",
            label2="Step details",
            description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
            description2="Details about the fetarues of the Busienss Process Step",
            label_msgid='gvSIGbpd_BPDPlazo_attr_detallesPaso_label',
            description_msgid='gvSIGbpd_BPDPlazo_attr_detallesPaso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
        duplicates="0",
        label2="Step details",
        ea_localid="283",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the fetarues of the Busienss Process Step",
        ea_guid="{617DDDA8-5804-4a14-9150-67EAD18FA235}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del Paso",
        length="0",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDPlazo",
        expression="context.fTFLVs([ 'esInicial', 'agotarPlazo','momentoDeComienzo','tiempoDeEspera','unidadDeTiempo','ejecutores'])",
        computed_types="string"
    ),

    BooleanField(
        name='esInicial',
        widget=BooleanField._properties['widget'](
            label="Es Inicial",
            label2="Is Initial",
            description="Indica si el Paso puede ser el primero en ejecutar  en el Proceso.",
            description2="Whether this Step can be the first to execute in the Business Process.",
            label_msgid='gvSIGbpd_BPDPlazo_attr_esInicial_label',
            description_msgid='gvSIGbpd_BPDPlazo_attr_esInicial_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica si el Paso puede ser el primero en ejecutar  en el Proceso.",
        duplicates="0",
        label2="Is Initial",
        ea_localid="293",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Whether this Step can be the first to execute in the Business Process.",
        ea_guid="{A648D06D-CBF0-424b-A429-90B3D6FF946C}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Es Inicial",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPlazo"
    ),

    RelationField(
        name='pasosRequeridos',
        inverse_relation_label="Plazos a cumplir",
        inverse_relation_description="Plazos en los que este Paso debe ejecutarse.",
        description="Pasos que deben ejecutarse dentro del Plazo. Son los pasos que se espera que acontezcan en el tiempo de espera indicado.",
        relationship='PasosRequeridosEnPlazo',
        label2="Required steps",
        widget=ReferenceBrowserWidget(
            label="Pasos requeridos",
            label2="Required steps",
            description="Pasos que deben ejecutarse dentro del Plazo. Son los pasos que se espera que acontezcan en el tiempo de espera indicado.",
            description2="Steps that must execute whithin the Deadline. It is what the Deadline actually expects and waits to happen.",
            label_msgid='gvSIGbpd_BPDPlazo_rel_pasosRequeridos_label',
            description_msgid='gvSIGbpd_BPDPlazo_rel_pasosRequeridos_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Steps that must execute whithin the Deadline. It is what the Deadline actually expects and waits to happen.",
        inverse_relation_label2="Deadlines to meet",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='requeridoEnPlazos',
        inverse_relation_description2="Deadlines by which this step must execute.",
        additional_columns=['detallesPaso'],
        label="Pasos requeridos",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='RequeridosEnPlazos',
        owner_class_name="BPDPlazo"
    ),

    IntegerField(
        name='tiempoDeEspera',
        widget=IntegerField._properties['widget'](
            label="Tiempo de Espera",
            label2="Deadline Wait Time",
            description="El Plazo se abre para el tiempo especificado. Al transcurrir el tiempo indicado, el Proceso continuara en el paso siguiente tras expiracion.",
            description2="Deadline's Time interval. When this amount of time is over, the Business Process will proceed with the Business Process Step identified for continuation upon expiration.",
            label_msgid='gvSIGbpd_BPDPlazo_attr_tiempoDeEspera_label',
            description_msgid='gvSIGbpd_BPDPlazo_attr_tiempoDeEspera_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El Plazo se abre para el tiempo especificado. Al transcurrir el tiempo indicado, el Proceso continuara en el paso siguiente tras expiracion.",
        duplicates="0",
        label2="Deadline Wait Time",
        ea_localid="229",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Deadline's Time interval. When this amount of time is over, the Business Process will proceed with the Business Process Step identified for continuation upon expiration.",
        ea_guid="{08B76CCE-4DF2-488e-B25A-3ECA62F2EEAB}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Tiempo de Espera",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDPlazo"
    ),

    StringField(
        name='unidadDeTiempo',
        widget=SelectionWidget(
            label="Unidad de Tiempo",
            label2="Time Unit",
            description="La unidad de tiempo en que se define el Tiempo de Espera del Plazo.",
            description2="Time unit measuring the Deadline's time limit.",
            label_msgid='gvSIGbpd_BPDPlazo_attr_unidadDeTiempo_label',
            description_msgid='gvSIGbpd_BPDPlazo_attr_unidadDeTiempo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="La unidad de tiempo en que se define el Tiempo de Espera del Plazo.",
        vocabulary=['Meses', 'Semanas', 'Dias', 'Horas', 'Minutos'],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPlazo_attr_unidadDeTiempo_option_Meses', 'gvSIGbpd_BPDPlazo_attr_unidadDeTiempo_option_Semanas', 'gvSIGbpd_BPDPlazo_attr_unidadDeTiempo_option_Dias', 'gvSIGbpd_BPDPlazo_attr_unidadDeTiempo_option_Horas', 'gvSIGbpd_BPDPlazo_attr_unidadDeTiempo_option_Minutos'],
        label2="Time Unit",
        ea_localid="230",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Time unit measuring the Deadline's time limit.",
        ea_guid="{03DD28DA-972C-4894-B7C0-6D5E2929D1C1}",
        write_permission='Modify portal content',
        scale="0",
        label="Unidad de Tiempo",
        length="0",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDPlazo",
        vocabulary2=['Months', 'Weeks', 'Days', 'Hours', 'Minutes']
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPlazo_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDPasoConSiguientes, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConAnteriores, 'schema', Schema(())).copy() + \
    getattr(BPDPasoGestorExcepciones, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConExcepciones, 'schema', Schema(())).copy() + \
    getattr(BPDPasoMinimo, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPlazo(OrderedBaseFolder, BPDPasoConSiguientes, BPDPasoConAnteriores, BPDPasoGestorExcepciones, BPDPasoConExcepciones, BPDPasoMinimo):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDPasoConSiguientes,'__implements__',()),) + (getattr(BPDPasoConAnteriores,'__implements__',()),) + (getattr(BPDPasoGestorExcepciones,'__implements__',()),) + (getattr(BPDPasoConExcepciones,'__implements__',()),) + (getattr(BPDPasoMinimo,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Plazo de Tiempo'

    meta_type = 'BPDPlazo'
    portal_type = 'BPDPlazo'
    allowed_content_types = [] + list(getattr(BPDPasoConSiguientes, 'allowed_content_types', [])) + list(getattr(BPDPasoConAnteriores, 'allowed_content_types', [])) + list(getattr(BPDPasoGestorExcepciones, 'allowed_content_types', [])) + list(getattr(BPDPasoConExcepciones, 'allowed_content_types', [])) + list(getattr(BPDPasoMinimo, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdplazo.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Un Plazo de tiempo durante el que se espera que empiecen o completen ciertos pasos, tras lo cual se continua en cierto paso, o por otro paso en caso de expiracion del tiempo."
    typeDescMsgId =  'gvSIGbpd_BPDPlazo_help'
    archetype_name2 = 'Deadline'
    typeDescription2 = '''A period of time during which to wait for the happening of the start or finish of a certain Business Process Step, continuing with different steps, depending upon the Deadline expiring or not.'''
    archetype_name_msgid = 'gvSIGbpd_BPDPlazo_label'
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

    schema = BPDPlazo_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('manage_afterAdd')
    def manage_afterAdd(self,item,container):
        """
        """
        
        return self.pHandle_manage_afterAdd(  item, container)

registerType(BPDPlazo, PROJECTNAME)
# end of class BPDPlazo

##code-section module-footer #fill in your manual code here
##/code-section module-footer



