# -*- coding: utf-8 -*-
#
# File: BPDPasoGeneral.py
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
from Products.gvSIGbpd.BPDPasoEstimado import BPDPasoEstimado
from Products.gvSIGbpd.BPDPasoConAnteriores import BPDPasoConAnteriores
from Products.gvSIGbpd.BPDPasoConExcepciones import BPDPasoConExcepciones
from Products.gvSIGbpd.BPDPasoGestorExcepciones import BPDPasoGestorExcepciones
from Products.gvSIGbpd.BPDPasoMinimo import BPDPasoMinimo
from Products.gvSIGbpd.BPDPasoConSiguientes import BPDPasoConSiguientes
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

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
            label_msgid='gvSIGbpd_BPDPasoGeneral_attr_esInicial_label',
            description_msgid='gvSIGbpd_BPDPasoGeneral_attr_esInicial_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica si el Paso se ejecuta al comenzar el Proceso.",
        duplicates="0",
        label2="Is Initial",
        ea_localid="289",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Whether this Step executes at the beginning of the Business Process.",
        ea_guid="{C05A7701-39A3-406c-A5E8-5BDA11A321FE}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Es Inicial",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPasoGeneral"
    ),

    RelationField(
        name='ejecutores',
        inverse_relation_label="Pasos Ejecutados",
        inverse_relation_description="Pasos de Negocio que se encarga de ejecutar el Perfil o Unidad Organizacional",
        description="Perfiles y Unidades Organizacionales a cargo de ejecutar el Paso.",
        relationship='BPDEjecutoresDelPaso',
        label2="Performers",
        widget=ReferenceBrowserWidget(
            label="Ejecutores",
            label2="Performers",
            description="Perfiles y Unidades Organizacionales a cargo de ejecutar el Paso.",
            description2="Participant Profiles and Organisational Units allowed to execute the Step.",
            label_msgid='gvSIGbpd_BPDPasoGeneral_rel_ejecutores_label',
            description_msgid='gvSIGbpd_BPDPasoGeneral_rel_ejecutores_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Participant Profiles and Organisational Units allowed to execute the Step.",
        inverse_relation_label2="Performed Business Process Steps",
        deststyle="Owned=0;Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;",
        write_permission='Modify portal content',
        inverse_relation_field_name='pasosEjecutados',
        inverse_relation_description2="Business Process Steps performed by the participant Profile or Organisational Unit.",
        additional_columns=['abreviatura'],
        label="Ejecutores",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDPasosEjecutados',
        owner_class_name="BPDPasoGeneral"
    ),

    RelationField(
        name='requeridoEnPlazos',
        inverse_relation_label="Pasos requeridos",
        containment="Unspecified",
        inverse_relation_description="Pasos que deben ejecutarse dentro del Plazo. Son los pasos que se espera que acontezcan en el tiempo de espera indicado.",
        description="Plazos en los que este Paso debe ejecutarse.",
        relationship='BPDRequeridosEnPlazos',
        inverse_relation_field_name='pasosRequeridos',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Deadlines to meet",
        inverse_relation_description2="Steps that must execute whithin the Deadline. It is what the Deadline actually expects and waits to happen.",
        widget=ReferenceBrowserWidget(
            label="Plazos a cumplir",
            label2="Deadlines to meet",
            description="Plazos en los que este Paso debe ejecutarse.",
            description2="Deadlines by which this step must execute.",
            label_msgid='gvSIGbpd_BPDPasoGeneral_rel_requeridoEnPlazos_label',
            description_msgid='gvSIGbpd_BPDPasoGeneral_rel_requeridoEnPlazos_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Plazos a cumplir",
        description2="Deadlines by which this step must execute.",
        multiValued=1,
        inverse_relation_label2="Required steps",
        inverse_relationship='BPDPasosRequeridosEnPlazo',
        write_permission='Modify portal content',
        additional_columns=['detallesPaso']
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoGeneral_schema = getattr(BPDPasoEstimado, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConAnteriores, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConExcepciones, 'schema', Schema(())).copy() + \
    getattr(BPDPasoGestorExcepciones, 'schema', Schema(())).copy() + \
    getattr(BPDPasoMinimo, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConSiguientes, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoGeneral(OrderedBaseFolder, BPDPasoEstimado, BPDPasoConAnteriores, BPDPasoConExcepciones, BPDPasoGestorExcepciones, BPDPasoMinimo, BPDPasoConSiguientes):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDPasoEstimado,'__implements__',()),) + (getattr(BPDPasoConAnteriores,'__implements__',()),) + (getattr(BPDPasoConExcepciones,'__implements__',()),) + (getattr(BPDPasoGestorExcepciones,'__implements__',()),) + (getattr(BPDPasoMinimo,'__implements__',()),) + (getattr(BPDPasoConSiguientes,'__implements__',()),)



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



    allowed_content_types = [] + list(getattr(BPDPasoEstimado, 'allowed_content_types', [])) + list(getattr(BPDPasoConAnteriores, 'allowed_content_types', [])) + list(getattr(BPDPasoConExcepciones, 'allowed_content_types', [])) + list(getattr(BPDPasoGestorExcepciones, 'allowed_content_types', [])) + list(getattr(BPDPasoMinimo, 'allowed_content_types', [])) + list(getattr(BPDPasoConSiguientes, 'allowed_content_types', []))

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

    schema = BPDPasoGeneral_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDPasoGeneral

##code-section module-footer #fill in your manual code here
##/code-section module-footer



