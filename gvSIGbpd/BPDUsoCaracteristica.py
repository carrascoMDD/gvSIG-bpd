# -*- coding: utf-8 -*-
#
# File: BPDUsoCaracteristica.py
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
from Products.gvSIGbpd.BPDArquetipoReferenciable import BPDArquetipoReferenciable
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    BooleanField(
        name='esRequerida',
        widget=BooleanField._properties['widget'](
            label="Es Requerida",
            label2="Is Required",
            description="Indica si la Caracteristica es absolutamente necesaria para llevar a cabo el Paso del Proceso de Negocio.",
            description2="Whether the Feature is absolutely needed to carry out th eBusiness Process Step.",
            label_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_esRequerida_label',
            description_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_esRequerida_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica si la Caracteristica es absolutamente necesaria para llevar a cabo el Paso del Proceso de Negocio.",
        duplicates="0",
        label2="Is Required",
        ea_localid="438",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Whether the Feature is absolutely needed to carry out th eBusiness Process Step.",
        ea_guid="{09A8012B-2069-4e9e-9029-57CC2F467A06}",
        write_permission='Modify portal content',
        scale="0",
        default="1",
        label="Es Requerida",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDUsoCaracteristica"
    ),

    StringField(
        name='modoDeUso',
        widget=SelectionWidget(
            label="Modo de Uso",
            label2="Usage Mode",
            description="Como se usa la Caracteristica en este Paso del Proceso de Negocio: Crear, Leer, Actualizar, Eliminar y Enlazar.",
            description2="How the Feature is used in this Business Process Step, to Create, Read, Update, Delete or Link.",
            label_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_modoDeUso_label',
            description_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_modoDeUso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Como se usa la Caracteristica en este Paso del Proceso de Negocio: Crear, Leer, Actualizar, Eliminar y Enlazar.",
        vocabulary=['Leer','Actualizar','Crear','Eliminar','Enlazar',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDUsoCaracteristica_attr_modoDeUso_option_Leer', 'gvSIGbpd_BPDUsoCaracteristica_attr_modoDeUso_option_Actualizar', 'gvSIGbpd_BPDUsoCaracteristica_attr_modoDeUso_option_Crear', 'gvSIGbpd_BPDUsoCaracteristica_attr_modoDeUso_option_Eliminar', 'gvSIGbpd_BPDUsoCaracteristica_attr_modoDeUso_option_Enlazar'],
        label2="Usage Mode",
        ea_localid="439",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="How the Feature is used in this Business Process Step, to Create, Read, Update, Delete or Link.",
        ea_guid="{42967B81-572E-4b65-9CC8-A104CA3251FB}",
        write_permission='Modify portal content',
        scale="0",
        default="Leer",
        label="Modo de Uso",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDUsoCaracteristica",
        vocabulary2=['Read','Update','Create','Delete','Link',]
    ),

    IntegerField(
        name='multiplicidadMinima',
        widget=IntegerField._properties['widget'](
            label="Multiplicidad Minima",
            label2="Minimum Multiplicity",
            description="Numero minimo de elementos usados en el Paso. Si el Uso del Artefacto Es Requerido, se considera que la Multiplicidad Minima es mayor or igual que 1.",
            description2="Minimum number of elements used in the Step. If the Artefact Use Is Required,  then it is considered that the Minimum Multiplicity is equal or bigger than 1.",
            label_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_multiplicidadMinima_label',
            description_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_multiplicidadMinima_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Numero minimo de elementos usados en el Paso. Si el Uso del Artefacto Es Requerido, se considera que la Multiplicidad Minima es mayor or igual que 1.",
        duplicates="0",
        label2="Minimum Multiplicity",
        ea_localid="441",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Minimum number of elements used in the Step. If the Artefact Use Is Required,  then it is considered that the Minimum Multiplicity is equal or bigger than 1.",
        ea_guid="{79F13D98-E034-4437-8451-CAB3668D5F67}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Multiplicidad Minima",
        length="0",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDUsoCaracteristica"
    ),

    IntegerField(
        name='multiplicidadMaxima',
        widget=IntegerField._properties['widget'](
            label="Multiplicidad Maxima",
            label2="Maximum Multiplicity",
            description="Numero maximo de elementos disponibles al comienzo del Proceso de Negocio. Introduzca -1 para indicar que no hay limite superior para el numero de Artefactos.",
            description2="Maximum number of elements available at the beginning of the Business Process.  Enter -1 to indicate that there is no upper limit in the number of elements.",
            label_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_multiplicidadMaxima_label',
            description_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_multiplicidadMaxima_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Numero maximo de elementos disponibles al comienzo del Proceso de Negocio. Introduzca -1 para indicar que no hay limite superior para el numero de Artefactos.",
        duplicates="0",
        label2="Maximum Multiplicity",
        ea_localid="442",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Maximum number of elements available at the beginning of the Business Process.  Enter -1 to indicate that there is no upper limit in the number of elements.",
        ea_guid="{F27A1A1F-4AAC-4c72-8919-51F4BD38161D}",
        write_permission='Modify portal content',
        scale="0",
        default="-1",
        label="Multiplicidad Maxima",
        length="0",
        containment="Not Specified",
        position="5",
        owner_class_name="BPDUsoCaracteristica"
    ),

    ComputedField(
        name='tituloPasoDeProcesoDeNegocio',
        widget=ComputedField._properties['widget'](
            label="Paso de Proceso de Negocio",
            label2="Business Process Step",
            description="El titulo del Paso de Proceso de Negocio que contiene el Uso de Artefacto.",
            description2="Title of the Business Process Step containing the Use Artefact.",
            label_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_tituloPasoDeProcesoDeNegocio_label',
            description_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_tituloPasoDeProcesoDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="El titulo del Paso de Proceso de Negocio que contiene el Uso de Artefacto.",
        duplicates="0",
        label2="Business Process Step",
        ea_localid="443",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Title of the Business Process Step containing the Use Artefact.",
        ea_guid="{2730B2E1-2C3F-473b-AB41-58609D266E38}",
        exclude_from_values_form="True",
        scale="0",
        label="Paso de Proceso de Negocio",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDUsoCaracteristica",
        expression="context.getContenedor().Title()",
        computed_types="string"
    ),

    ComputedField(
        name='tituloProcesoDeNegocio',
        widget=ComputedField._properties['widget'](
            label="Proceso de Negocio",
            label2="Business Process",
            description="El titulo del Proceso de Negocio que contiene el Uso de Artefacto",
            description2="Title of the Business Process containing the Use Artefact",
            label_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_tituloProcesoDeNegocio_label',
            description_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_tituloProcesoDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="El titulo del Proceso de Negocio que contiene el Uso de Artefacto",
        duplicates="0",
        label2="Business Process",
        ea_localid="440",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Title of the Business Process containing the Use Artefact",
        ea_guid="{362EBF35-550F-43aa-A249-D2CDFD5EEADF}",
        exclude_from_values_form="True",
        scale="0",
        label="Proceso de Negocio",
        length="0",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDUsoCaracteristica",
        expression="context.getContenedor().getTituloProcesoDeNegocio()",
        computed_types="string"
    ),

    ComputedField(
        name='titulosCaracteristicasUsadas',
        widget=ComputedField._properties['widget'](
            label="Caracteristicas Usadas",
            label2="Used Features",
            description="Caracteristicas que se usan en el Paso del Proceso de Negocio.",
            description2="Features Used in the Business Process Step",
            label_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_titulosCaracteristicasUsadas_label',
            description_msgid='gvSIGbpd_BPDUsoCaracteristica_attr_titulosCaracteristicasUsadas_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Caracteristicas que se usan en el Paso del Proceso de Negocio.",
        duplicates="0",
        label2="Used Features",
        ea_localid="437",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Features Used in the Business Process Step",
        containment="Not Specified",
        ea_guid="{62DE8709-2D4F-4485-8025-D7539C17B176}",
        position="7",
        owner_class_name="BPDUsoCaracteristica",
        label="Caracteristicas Usadas",
        expression="', '.join( [ a.fTFLVsUnless([ ['title','',], ['tituloArtefacto','',],]) for a in context.getCaracteristicasUsadas()])",
        exclude_from_values_form="True"
    ),

    RelationField(
        name='caracteristicasUsadas',
        inverse_relation_label="Usos de la Caracteristica",
        inverse_relation_description="Usos de la Caracteristica en Pasos de Procesos de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.",
        description="Caracteristicas de Artefactos que se usan en el Paso del Proceso de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.",
        relationship='BPDCaracteristicasUsadas',
        label2="Used Features",
        widget=ReferenceBrowserWidget(
            label="Caracteristicas Usadas",
            label2="Used Features",
            description="Caracteristicas de Artefactos que se usan en el Paso del Proceso de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.",
            description2="Artefact Features used in the Business Process Step, to Create, Read, Update, Delete or Link.",
            label_msgid='gvSIGbpd_BPDUsoCaracteristica_rel_caracteristicasUsadas_label',
            description_msgid='gvSIGbpd_BPDUsoCaracteristica_rel_caracteristicasUsadas_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Artefact Features used in the Business Process Step, to Create, Read, Update, Delete or Link.",
        inverse_relation_label2="Feature Usages",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='usosDeLaCaracteristica',
        inverse_relation_description2="Uses of the Artefact Feature in Business Process Steps, to Create, Read, Update, Delete or Link.",
        additional_columns=['claseCaracteristica', 'tituloArtefacto'],
        label="Caracteristicas Usadas",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDUsosDeCaracteristicas',
        owner_class_name="BPDUsoCaracteristica"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDUsoCaracteristica_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoReferenciable, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDUsoCaracteristica(OrderedBaseFolder, BPDArquetipoReferenciable):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoReferenciable,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Uso de Caracteristica de Artefacto'

    meta_type = 'BPDUsoCaracteristica'
    portal_type = 'BPDUsoCaracteristica'


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



    allowed_content_types = [] + list(getattr(BPDArquetipoReferenciable, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdusocaracteristica.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Caracteristicas de Artefacto que se usan en el Paso del Proceso de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar."
    typeDescMsgId                    =  'gvSIGbpd_BPDUsoCaracteristica_help'
    archetype_name2                  = 'Use Feature in Artefact'
    typeDescription2                 = '''Artefact Features used in the Business Process Step, to Create, Read, Update, Delete or Link.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDUsoCaracteristica_label'
    factory_methods                  = None
    factory_enablers                 = None
    propagate_delete_impact_to       = [ ['contenedor_contenedorYPropietario',],]


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

    schema = BPDUsoCaracteristica_schema

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

registerType(BPDUsoCaracteristica, PROJECTNAME)
# end of class BPDUsoCaracteristica

##code-section module-footer #fill in your manual code here
##/code-section module-footer



