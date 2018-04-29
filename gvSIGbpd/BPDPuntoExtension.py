# -*- coding: utf-8 -*-
#
# File: BPDPuntoExtension.py
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
from Products.gvSIGbpd.BPDPasoConSiguientes import BPDPasoConSiguientes
from Products.gvSIGbpd.BPDPasoMinimo import BPDPasoMinimo
from Products.gvSIGbpd.BPDPasoGestorExcepciones import BPDPasoGestorExcepciones
from Products.gvSIGbpd.BPDPasoConAnteriores import BPDPasoConAnteriores
from Products.gvSIGbpd.BPDCondicional import BPDCondicional
from Products.gvSIGbpd.BPDPasoConExcepciones import BPDPasoConExcepciones
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.ATContentTypes.content.base import ATCTMixin

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    BooleanField(
        name='esInicial',
        widget=BooleanField._properties['widget'](
            label="Es Inicial",
            label2="Is Initial",
            description="Indica si el Paso se ejecuta al comenzar el Proceso.",
            description2="Whether this Step executes at the beginning of the Business Process.",
            label_msgid='gvSIGbpd_BPDPuntoExtension_attr_esInicial_label',
            description_msgid='gvSIGbpd_BPDPuntoExtension_attr_esInicial_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica si el Paso se ejecuta al comenzar el Proceso.",
        duplicates="0",
        label2="Is Initial",
        ea_localid="423",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Whether this Step executes at the beginning of the Business Process.",
        ea_guid="{787C71C9-EC4C-4c0e-8CAF-ED23A6398E9F}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Es Inicial",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPuntoExtension"
    ),

    ComputedField(
        name='detallesPaso',
        widget=ComputedField._properties['widget'](
            label="Detalles del Punto de Extension",
            label2="Extension Point Step details",
            description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
            description2="Details about the Extension Point Step, including the title of the used Business Process.",
            label_msgid='gvSIGbpd_BPDPuntoExtension_attr_detallesPaso_label',
            description_msgid='gvSIGbpd_BPDPuntoExtension_attr_detallesPaso_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
        duplicates="0",
        label2="Extension Point Step details",
        ea_localid="406",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the Extension Point Step, including the title of the used Business Process.",
        ea_guid="{1EB8DF5D-1ECC-4597-92F1-0C83E9F667A9}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del Punto de Extension",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDPuntoExtension",
        expression="context.fTFLVsUnless([ ['esInicial',False,],[ 'titulosProcesosExtensiones','',],[ 'titulosArtefactosUsados','',],[ 'titulosCaracteristicasUsadas','',],])",
        computed_types="string"
    ),

    RelationField(
        name='extensionesProcesos',
        inverse_relation_label="Puntos de Extension",
        additional_columns=['tituloProcesoDeNegocio',],
        inverse_relation_description="El Punto de Extension en el Proceso de Negocio que se extiende insertando el comportamiento de este Proceso de Negocio.",
        description="Extensiones de Procesos de Negocio insertando comportamiento en este Punto de Extension.",
        relationship='BPDExtensionesProcesos',
        inverse_relation_field_name='puntosExtension',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Extension Points",
        label2="Process Extensions",
        inverse_relation_description2="The Extension Point in the Business Process that is being extended by inserting the behavior of this Business Process.",
        widget=ReferenceBrowserWidget(
            label="Extensiones Procesos",
            label2="Process Extensions",
            description="Extensiones de Procesos de Negocio insertando comportamiento en este Punto de Extension.",
            description2="Business Process Extensions inserting behavior in this Extension Point.",
            label_msgid='gvSIGbpd_BPDPuntoExtension_rel_extensionesProcesos_label',
            description_msgid='gvSIGbpd_BPDPuntoExtension_rel_extensionesProcesos_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Extensiones Procesos",
        description2="Business Process Extensions inserting behavior in this Extension Point.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDPuntosExtension',
        dependency_supplier=True
    ),

    ComputedField(
        name='titulosProcesosExtensiones',
        widget=ComputedField._properties['widget'](
            label="Extensiones en Procesos de Negocio",
            label2="Extending Business Processes",
            description="Proceso de Negocio que extienden  este Proceso de Negocio insertando su comportamiento en este Punto de Extension.",
            description2="Business Processes extending this Business Process inserting their behavior in this Extension Point.",
            label_msgid='gvSIGbpd_BPDPuntoExtension_attr_titulosProcesosExtensiones_label',
            description_msgid='gvSIGbpd_BPDPuntoExtension_attr_titulosProcesosExtensiones_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Proceso de Negocio que extienden  este Proceso de Negocio insertando su comportamiento en este Punto de Extension.",
        duplicates="0",
        label2="Extending Business Processes",
        ea_localid="405",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Business Processes extending this Business Process inserting their behavior in this Extension Point.",
        ea_guid="{1EB39BC4-90C1-4f5c-B7E6-BBA8BB90F31D}",
        exclude_from_values_form="True",
        scale="0",
        label="Extensiones en Procesos de Negocio",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDPuntoExtension",
        expression="context.fTrTFLVs( ['extensionesProcesos',], [ 'tituloProcesoDeNegocio', ])",
        computed_types="string"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPuntoExtension_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDPasoConSiguientes, 'schema', Schema(())).copy() + \
    getattr(BPDPasoMinimo, 'schema', Schema(())).copy() + \
    getattr(BPDPasoGestorExcepciones, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConAnteriores, 'schema', Schema(())).copy() + \
    getattr(BPDCondicional, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConExcepciones, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPuntoExtension(OrderedBaseFolder, BPDPasoConSiguientes, BPDPasoMinimo, BPDPasoGestorExcepciones, BPDPasoConAnteriores, BPDCondicional, BPDPasoConExcepciones):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDPasoConSiguientes,'__implements__',()),) + (getattr(BPDPasoMinimo,'__implements__',()),) + (getattr(BPDPasoGestorExcepciones,'__implements__',()),) + (getattr(BPDPasoConAnteriores,'__implements__',()),) + (getattr(BPDCondicional,'__implements__',()),) + (getattr(BPDPasoConExcepciones,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Punto de Extension'

    meta_type = 'BPDPuntoExtension'
    portal_type = 'BPDPuntoExtension'


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



    allowed_content_types = [] + list(getattr(BPDPasoConSiguientes, 'allowed_content_types', [])) + list(getattr(BPDPasoMinimo, 'allowed_content_types', [])) + list(getattr(BPDPasoGestorExcepciones, 'allowed_content_types', [])) + list(getattr(BPDPasoConAnteriores, 'allowed_content_types', [])) + list(getattr(BPDCondicional, 'allowed_content_types', [])) + list(getattr(BPDPasoConExcepciones, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdpuntoextension.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Un Proceso de Negocio definido aparte, ejercita este Proceso de Negocio de principio a fin, y extiende este Proces de Negocio insertando comportamiento aditional en este punto del proceso."
    typeDescMsgId                    =  'gvSIGbpd_BPDPuntoExtension_help'
    archetype_name2                  = 'Extension Point'
    typeDescription2                 = '''A Business Process, specified elsewhere, executes this Business Process in its entirety, and extends this Business Process inserting additional behavior at this point of the process..'''
    archetype_name_msgid             = 'gvSIGbpd_BPDPuntoExtension_label'
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

    schema = BPDPuntoExtension_schema

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

registerType(BPDPuntoExtension, PROJECTNAME)
# end of class BPDPuntoExtension

##code-section module-footer #fill in your manual code here
##/code-section module-footer



