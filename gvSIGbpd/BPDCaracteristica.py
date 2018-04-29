# -*- coding: utf-8 -*-
#
# File: BPDCaracteristica.py
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

    StringField(
        name='claseCaracteristica',
        widget=SelectionWidget(
            label="Clase de Caracteristica",
            label2="Feature Class",
            description="Puede ser Atributo, Referencia o Agregacion.",
            description2="How the Artefact is used in this Business Process Step, to Create, Read, Update, Delete or Link.",
            label_msgid='gvSIGbpd_BPDCaracteristica_attr_claseCaracteristica_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_attr_claseCaracteristica_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Puede ser Atributo, Referencia o Agregacion.",
        vocabulary=['Atributo', 'Referencia', 'Agregacion',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDCaracteristica_attr_claseCaracteristica_option_Atributo', 'gvSIGbpd_BPDCaracteristica_attr_claseCaracteristica_option_Referencia', 'gvSIGbpd_BPDCaracteristica_attr_claseCaracteristica_option_Agregacion'],
        label2="Feature Class",
        ea_localid="427",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="How the Artefact is used in this Business Process Step, to Create, Read, Update, Delete or Link.",
        ea_guid="{7F70ABA3-83C0-4cec-BF80-F23FFF9B3139}",
        write_permission='Modify portal content',
        scale="0",
        default="Atributo",
        label="Clase de Caracteristica",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDCaracteristica",
        vocabulary2=['Attribute' , 'Reference', 'Aggregation',]
    ),

    IntegerField(
        name='multiplicidadMinima',
        widget=IntegerField._properties['widget'](
            label="Multiplicidad Minima",
            label2="Minimum Multiplicity",
            description="Si la Clase de Caracteristica es Referencia o Agregacion, entonces restringe el numero minimo de Artefactos referenciados o agregados.",
            description2="If the Feature Class is Reference or Aggregation, then constrains the minimum number of  referenced or aggregated Artefacts.",
            label_msgid='gvSIGbpd_BPDCaracteristica_attr_multiplicidadMinima_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_attr_multiplicidadMinima_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Si la Clase de Caracteristica es Referencia o Agregacion, entonces restringe el numero minimo de Artefactos referenciados o agregados.",
        duplicates="0",
        label2="Minimum Multiplicity",
        ea_localid="428",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="If the Feature Class is Reference or Aggregation, then constrains the minimum number of  referenced or aggregated Artefacts.",
        ea_guid="{3E1C593E-E8A5-46ce-9304-5C0BB130B5F6}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Multiplicidad Minima",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDCaracteristica"
    ),

    StringField(
        name='restriccionTipo',
        widget=StringWidget(
            label="Restriccion del Tipo",
            label2="Type Constraint",
            description="Restringe el tipo de la Caracteristica. Puede ser el nombre de un tipo primitivo, e indicar longitudes o precisiones minimas y maximas. Puede restringir valores de Artefactos relacionados o agregados.",
            description2="Constrains the Feature Type. May be the name of a primitive type, and indicate minimum and maximum length and precision. May constrain values on referenced or aggregated artefacts.",
            label_msgid='gvSIGbpd_BPDCaracteristica_attr_restriccionTipo_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_attr_restriccionTipo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Restringe el tipo de la Caracteristica. Puede ser el nombre de un tipo primitivo, e indicar longitudes o precisiones minimas y maximas. Puede restringir valores de Artefactos relacionados o agregados.",
        searchable=1,
        duplicates="0",
        label2="Type Constraint",
        ea_localid="431",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Constrains the Feature Type. May be the name of a primitive type, and indicate minimum and maximum length and precision. May constrain values on referenced or aggregated artefacts.",
        ea_guid="{161B8055-D6F0-4596-8851-64AFC2CEFFC6}",
        write_permission='Modify portal content',
        scale="0",
        label="Restriccion del Tipo",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDCaracteristica"
    ),

    IntegerField(
        name='multiplicidadMaxima',
        widget=IntegerField._properties['widget'](
            label="Multiplicidad Maxima",
            label2="Maximum Multiplicity",
            description="Si la Clase de Caracteristica es Referencia o Agregacion, entonces restringe el numero maximo de Artefactos referenciados o agregados.",
            description2="If the Feature Class is Reference or Aggregation, then constrains the maximum number of  referenced or aggregated Artefacts.",
            label_msgid='gvSIGbpd_BPDCaracteristica_attr_multiplicidadMaxima_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_attr_multiplicidadMaxima_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Si la Clase de Caracteristica es Referencia o Agregacion, entonces restringe el numero maximo de Artefactos referenciados o agregados.",
        duplicates="0",
        label2="Maximum Multiplicity",
        ea_localid="429",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="If the Feature Class is Reference or Aggregation, then constrains the maximum number of  referenced or aggregated Artefacts.",
        ea_guid="{01DEB604-8644-4046-B84F-F4F1B4017C87}",
        write_permission='Modify portal content',
        scale="0",
        default="-1",
        label="Multiplicidad Maxima",
        length="0",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDCaracteristica"
    ),

    RelationField(
        name='tiposDeArtefactos',
        inverse_relation_label="Caracteristicas del Tipo",
        inverse_relation_description="Caracteristicas de Clase Referencia o Agregacion que estan restringidas a Artefactos de este tipo.",
        description="Si la Clase de Caracteristica es Referencia o Agregacion, entonces restringe los tipos de Artefactos referenciados o agregados.",
        relationship='BPDTiposDeCaracteristicas',
        label2="Artefact Types",
        widget=ReferenceBrowserWidget(
            label="Tipos de Artefactos",
            label2="Artefact Types",
            description="Si la Clase de Caracteristica es Referencia o Agregacion, entonces restringe los tipos de Artefactos referenciados o agregados.",
            description2="If the Feature Class is Reference or Aggregation, then constrains the types of Artefacts that can be referenced or aggregated.",
            label_msgid='gvSIGbpd_BPDCaracteristica_rel_tiposDeArtefactos_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_rel_tiposDeArtefactos_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="If the Feature Class is Reference or Aggregation, then constrains the types of Artefacts that can be referenced or aggregated.",
        inverse_relation_label2="Features of the Type",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='caracteristicasDelTipo',
        inverse_relation_description2="Features of Reference or Aggregation Class constrained to Artefacts of this type.",
        additional_columns=['codigo'],
        label="Tipos de Artefactos",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDCaracteristicasDelTipo',
        owner_class_name="BPDCaracteristica"
    ),

    RelationField(
        name='procesosGestores',
        inverse_relation_label="Caracteristicas Gestionadas",
        inverse_relation_description="Caracteristicas de Artefactos que se gestionan ejecutando el Proceso de Negocio.",
        description="Procesos de Negocio con que se gestiona esta Caracteristica de Artefacto.",
        relationship='BPDProcesosGestoresDeCaracteristicas',
        label2="Managing Business Processes",
        widget=ReferenceBrowserWidget(
            label="Procesos de Negocio Gestores",
            label2="Managing Business Processes",
            description="Procesos de Negocio con que se gestiona esta Caracteristica de Artefacto.",
            description2="Business Processes executed to manage this Artefact Feature.",
            label_msgid='gvSIGbpd_BPDCaracteristica_rel_procesosGestores_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_rel_procesosGestores_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Processes executed to manage this Artefact Feature.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Managed Features",
        dependency_supplier=True,
        inverse_relation_field_name='caracteristicasGestionadas',
        inverse_relation_description2="Artefact Features managed by executing this Business Process.",
        additional_columns=['claseCaracteristica','tituloArtefacto',],
        write_permission='Modify portal content',
        label="Procesos de Negocio Gestores",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDCaracteristicasGestionadasPorProcesos'
    ),

    RelationField(
        name='usosDeLaCaracteristica',
        inverse_relation_label="Caracteristicas Usadas",
        inverse_relation_description="Caracteristicas de Artefactos que se usan en el Paso del Proceso de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.",
        description="Usos de la Caracteristica en Pasos de Procesos de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.",
        relationship='BPDUsosDeCaracteristicas',
        label2="Feature Usages",
        widget=ReferenceBrowserWidget(
            label="Usos de la Caracteristica",
            label2="Feature Usages",
            description="Usos de la Caracteristica en Pasos de Procesos de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.",
            description2="Uses of the Artefact Feature in Business Process Steps, to Create, Read, Update, Delete or Link.",
            label_msgid='gvSIGbpd_BPDCaracteristica_rel_usosDeLaCaracteristica_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_rel_usosDeLaCaracteristica_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Uses of the Artefact Feature in Business Process Steps, to Create, Read, Update, Delete or Link.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Used Features",
        dependency_supplier=True,
        inverse_relation_field_name='caracteristicasUsadas',
        inverse_relation_description2="Artefact Features used in the Business Process Step, to Create, Read, Update, Delete or Link.",
        additional_columns=['claseCaracteristica','tituloArtefacto',],
        write_permission='Modify portal content',
        label="Usos de la Caracteristica",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDCaracteristicasUsadas'
    ),

    ComputedField(
        name='detallesCaracteristica',
        widget=ComputedField._properties['widget'](
            label="Detalles de la Caracteristica",
            label2="Feature details",
            description="Detalles acerca de la caracteristica, incluyendo restricciones de tipo y multiplicidad",
            description2="Details about the Feature, including type and multiplicity constrains.",
            label_msgid='gvSIGbpd_BPDCaracteristica_attr_detallesCaracteristica_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_attr_detallesCaracteristica_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Detalles acerca de la caracteristica, incluyendo restricciones de tipo y multiplicidad",
        duplicates="0",
        label2="Feature details",
        ea_localid="435",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the Feature, including type and multiplicity constrains.",
        ea_guid="{DDF26C05-6962-4e0c-A138-F3FF928109E8}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles de la Caracteristica",
        length="0",
        containment="Not Specified",
        position="6",
        owner_class_name="BPDCaracteristica",
        expression="context.fTFLVsUnless([ ['claseCaracteristica','',],['multiplicidadMinima','',],['multiplicidadMaxima',0,],[ 'restriccionTipo','',],])",
        computed_types="string"
    ),

    ComputedField(
        name='tituloArtefacto',
        widget=ComputedField._properties['widget'](
            label="Artefacto",
            label2="Artefact",
            description="El titulo del Artefacto con esta Caracteristica.",
            description2="Title of the Artefact with this Feature.",
            label_msgid='gvSIGbpd_BPDCaracteristica_attr_tituloArtefacto_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_attr_tituloArtefacto_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="El titulo del Artefacto con esta Caracteristica.",
        duplicates="0",
        label2="Artefact",
        ea_localid="434",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Title of the Artefact with this Feature.",
        ea_guid="{8928DBC7-0359-42d4-AF38-B2EFB737B0BB}",
        exclude_from_values_form="True",
        scale="0",
        label="Artefacto",
        length="0",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDCaracteristica",
        expression="context.getContenedor().Title()",
        computed_types="string"
    ),

    ComputedField(
        name='titulosTiposArtefactos',
        widget=ComputedField._properties['widget'](
            label="Tipos de Artefactos",
            label2="Artefact Types",
            description="Si la Clase de Caracteristica es Referencia o Agregacion, indica los tipos de Artefactos a referir o agregar.",
            description2="If the Feature Class is Reference or Aggregation, indicates the types of Artefacts to refer or aggregate.",
            label_msgid='gvSIGbpd_BPDCaracteristica_attr_titulosTiposArtefactos_label',
            description_msgid='gvSIGbpd_BPDCaracteristica_attr_titulosTiposArtefactos_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Si la Clase de Caracteristica es Referencia o Agregacion, indica los tipos de Artefactos a referir o agregar.",
        duplicates="0",
        label2="Artefact Types",
        ea_localid="432",
        derived="0",
        collection="false",
        label="Tipos de Artefactos",
        description2="If the Feature Class is Reference or Aggregation, indicates the types of Artefacts to refer or aggregate.",
        containment="Not Specified",
        ea_guid="{0A58E67F-660F-41fd-B787-D187C2F15216}",
        position="5",
        owner_class_name="BPDCaracteristica",
        styleex="volatile=0;",
        expression="', '.join( [a.Title() for a in context.getTiposDeArtefactos()])",
        exclude_from_values_form="True"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDCaracteristica_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDCaracteristica(OrderedBaseFolder, BPDArquetipoConAdopcion):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Caracteristica'

    meta_type = 'BPDCaracteristica'
    portal_type = 'BPDCaracteristica'


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



    allowed_content_types = [] + list(getattr(BPDArquetipoConAdopcion, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdcaracteristica.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Un Elemento de informacion que se especifican para el Artefacto, o que podra contener el Artefacto."
    typeDescMsgId                    =  'gvSIGbpd_BPDCaracteristica_help'
    archetype_name2                  = 'Feature'
    typeDescription2                 = '''Information elements specified for the Artefact, or that may be contained by the Artefact.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDCaracteristica_label'
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

    schema = BPDCaracteristica_schema

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

registerType(BPDCaracteristica, PROJECTNAME)
# end of class BPDCaracteristica

##code-section module-footer #fill in your manual code here
##/code-section module-footer



