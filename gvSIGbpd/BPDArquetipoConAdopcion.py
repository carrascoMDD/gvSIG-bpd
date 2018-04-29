# -*- coding: utf-8 -*-
#
# File: BPDArquetipoConAdopcion.py
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
from Products.gvSIGbpd.BPDArquetipoReferenciable import BPDArquetipoReferenciable
from Products.gvSIGbpd.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='codigo',
        widget=StringWidget(
            label="Codigo",
            label2="Code",
            description="Codigo unico del elemento.",
            description2="Unique code for the element.",
            label_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_codigo_label',
            description_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_codigo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Codigo unico del elemento.",
        searchable=1,
        duplicates="0",
        label2="Code",
        ea_localid="239",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Unique code for the element.",
        ea_guid="{F546FDFC-03EE-4d4d-8923-305F3A561385}",
        scale="0",
        label="Codigo",
        length="0",
        exclude_from_values_paragraph_when='',
        containment="Not Specified",
        position="0",
        owner_class_name="BPDArquetipoConAdopcion"
    ),

    StringField(
        name='estado',
        widget=SelectionWidget(
            label="Estado",
            label2="Status",
            description="Estado del ciclo de vida de creacion, adopcion y retiro.",
            description2="Status of the element's life-cycle of creation, adoption and retirement.",
            label_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_estado_label',
            description_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_estado_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Estado del ciclo de vida de creacion, adopcion y retiro.",
        vocabulary=['Redaccion', 'Pendiente de Revision', 'Aprobado', 'Retirado'],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDArquetipoConAdopcion_attr_estado_option_Redaccion', 'gvSIGbpd_BPDArquetipoConAdopcion_attr_estado_option_Pendiente de Revision', 'gvSIGbpd_BPDArquetipoConAdopcion_attr_estado_option_Aprobado', 'gvSIGbpd_BPDArquetipoConAdopcion_attr_estado_option_Retirado'],
        label2="Status",
        ea_localid="240",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Status of the element's life-cycle of creation, adoption and retirement.",
        ea_guid="{3A1C889E-1661-4cb6-9730-5DF9D7BF001A}",
        vocabulary2=['Draft', 'Review Pending', 'Approved', 'Retired', ],
        scale="0",
        label="Estado",
        length="0",
        exclude_from_values_paragraph_when='',
        containment="Not Specified",
        position="1",
        owner_class_name="BPDArquetipoConAdopcion",
        exclude_from_views="[ 'Textual', ]"
    ),

    DateTimeField(
        name='fechaAdopcion',
        widget=CalendarWidget(
            label="Fecha de Adopcion",
            label2="Adoption Date",
            description="Fecha en que el elemento de definicion ha sido o sera Adoptado, es decir, entra en vigor la obligacion de aplicarlo en la gestion de la organizacion.",
            description2="Date of adoption, past or future, when observance becomes enforceable.",
            label_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_fechaAdopcion_label',
            description_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_fechaAdopcion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Fecha en que el elemento de definicion ha sido o sera Adoptado, es decir, entra en vigor la obligacion de aplicarlo en la gestion de la organizacion.",
        duplicates="0",
        label2="Adoption Date",
        ea_localid="243",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Date of adoption, past or future, when observance becomes enforceable.",
        ea_guid="{A8E85ED1-4F01-49a8-A21C-A7A66823FBBA}",
        scale="0",
        label="Fecha de Adopcion",
        length="0",
        exclude_from_values_paragraph_when="""None
        None""",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDArquetipoConAdopcion",
        exclude_from_views="[ 'Textual', ]"
    ),

    DateTimeField(
        name='fechaObsolescencia',
        widget=CalendarWidget(
            label="Fecha de Obsolescencia",
            label2="Retirement Date",
            description="Fecha en que el elemento de definicion se va a retirar o se ha retirado, y en que dejara de ser obligado su cumplimiento en la gestion de la organizacion.",
            description2="Date of retirement, past or future, when observance ceases to be enforceable.",
            label_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_fechaObsolescencia_label',
            description_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_fechaObsolescencia_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Fecha en que el elemento de definicion se va a retirar o se ha retirado, y en que dejara de ser obligado su cumplimiento en la gestion de la organizacion.",
        duplicates="0",
        label2="Retirement Date",
        ea_localid="244",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Date of retirement, past or future, when observance ceases to be enforceable.",
        ea_guid="{857B79E6-C7BC-4ac1-BFB2-76B5227C0D91}",
        scale="0",
        label="Fecha de Obsolescencia",
        length="0",
        containment="Not Specified",
        position="5",
        owner_class_name="BPDArquetipoConAdopcion",
        exclude_from_views="[ 'Textual', ]"
    ),

    StringField(
        name='nivelDeImposicion',
        widget=SelectionWidget(
            label="Nivel de Imposicion",
            label2="With Enforcement Level",
            description="Indica el nivel de imposicion con que se debe aplicar un elemento de definicion, que puede expresarse en un rango de valores desde Imposicion Estricta a Guia Sugerida.",
            description2="Indicates the enforcement level for the element.",
            label_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_nivelDeImposicion_label',
            description_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_nivelDeImposicion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica el nivel de imposicion con que se debe aplicar un elemento de definicion, que puede expresarse en un rango de valores desde Imposicion Estricta a Guia Sugerida.",
        vocabulary=['Imposicion Estricta', 'Imposicion Diferida', 'Invalidacion Autorizada Previamente', 'Invalidacion Justificada Posteriormente', 'Invalidacion Explicada', 'Guia Sugerida'],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDArquetipoConAdopcion_attr_nivelDeImposicion_option_Imposicion Estricta', 'gvSIGbpd_BPDArquetipoConAdopcion_attr_nivelDeImposicion_option_Imposicion Diferida', 'gvSIGbpd_BPDArquetipoConAdopcion_attr_nivelDeImposicion_option_Invalidacion Autorizada Previamente', 'gvSIGbpd_BPDArquetipoConAdopcion_attr_nivelDeImposicion_option_Invalidacion Justificada Posteriormente', 'gvSIGbpd_BPDArquetipoConAdopcion_attr_nivelDeImposicion_option_Invalidacion Explicada', 'gvSIGbpd_BPDArquetipoConAdopcion_attr_nivelDeImposicion_option_Guia Sugerida'],
        label2="With Enforcement Level",
        ea_localid="241",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the enforcement level for the element.",
        ea_guid="{38EE6C24-0999-4a26-AEEE-07CD6191A430}",
        vocabulary2=['Strictly Enforced', 'Deferred Enforcement', 'Pre-Authorized Override', 'Post-Justified Override', 'Override with Explanation', 'Guideline'],
        scale="0",
        label="Nivel de Imposicion",
        length="0",
        exclude_from_values_paragraph_when='',
        containment="Not Specified",
        position="2",
        owner_class_name="BPDArquetipoConAdopcion",
        exclude_from_views="[ 'Textual', ]"
    ),

    StringField(
        name='version',
        widget=StringWidget(
            label="Version",
            label2="Version",
            description="El Proceso puede evolucionar a lo largo de versiones sucesivas.",
            description2="The Business Process may evolve through successive versions.",
            label_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_version_label',
            description_msgid='gvSIGbpd_BPDArquetipoConAdopcion_attr_version_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El Proceso puede evolucionar a lo largo de versiones sucesivas.",
        duplicates="0",
        label2="Version",
        ea_localid="242",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="The Business Process may evolve through successive versions.",
        ea_guid="{DCE3FFD5-504E-409f-97B4-FA35480666B4}",
        scale="0",
        label="Version",
        length="0",
        exclude_from_values_paragraph_when='',
        containment="Not Specified",
        position="3",
        owner_class_name="BPDArquetipoConAdopcion",
        exclude_from_views="[ 'Textual', ]"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDArquetipoConAdopcion_schema = getattr(BPDArquetipoReferenciable, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDArquetipoConAdopcion(BPDArquetipoReferenciable):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BPDArquetipoReferenciable,'__implements__',()),)



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

    schema = BPDArquetipoConAdopcion_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDArquetipoConAdopcion

##code-section module-footer #fill in your manual code here
##/code-section module-footer



