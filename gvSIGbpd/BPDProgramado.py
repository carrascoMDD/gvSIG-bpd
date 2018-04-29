# -*- coding: utf-8 -*-
#
# File: BPDProgramado.py
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
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='tipoPrograma',
        widget=SelectionWidget(
            label="Tipo Programa",
            label2="Program Kind",
            description="El tipo del programa especificado en este elemento: Python Plone Docstring, or ... To Be Extended",
            description2="The kind of program specified for this element: Python Plone Docstring, or ... To Be Extended",
            label_msgid='gvSIGbpd_BPDProgramado_attr_tipoPrograma_label',
            description_msgid='gvSIGbpd_BPDProgramado_attr_tipoPrograma_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El tipo del programa especificado en este elemento: Python Plone Docstring, or ... To Be Extended",
        vocabulary=['No Especificado','Python-Plone docstring',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDProgramado_attr_tipoPrograma_option_No Especificado', 'gvSIGbpd_BPDProgramado_attr_tipoPrograma_option_Python-Plone docstring'],
        label2="Program Kind",
        ea_localid="598",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="The kind of program specified for this element: Python Plone Docstring, or ... To Be Extended",
        ea_guid="{2FA3B1AF-B132-4dbe-9CF4-CE27E6CF1ADA}",
        vocabulary2=['Unspecified','Python-Plone docstring',],
        scale="0",
        default="Python-Plone docstring",
        label="Tipo Programa",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDProgramado"
    ),

    TextField(
        name='fuentePrograma',
        widget=TextAreaWidget(
            label="Fuente del Programa",
            label2="Program Source",
            description="El codigo fuente del programa especificado en este elemento, expresado en el tipo de program especificado: Python Plone Docstring, or ... To Be Extended",
            description2="The source code of the program specified for this element, expressed in the specified program kind: Python Plone Docstring, or ... To Be Extended",
            label_msgid='gvSIGbpd_BPDProgramado_attr_fuentePrograma_label',
            description_msgid='gvSIGbpd_BPDProgramado_attr_fuentePrograma_help',
            i18n_domain='gvSIGbpd',
        ),
        scale="0",
        description="El codigo fuente del programa especificado en este elemento, expresado en el tipo de program especificado: Python Plone Docstring, or ... To Be Extended",
        duplicates="0",
        label2="Program Source",
        ea_localid="606",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        length="0",
        description2="The source code of the program specified for this element, expressed in the specified program kind: Python Plone Docstring, or ... To Be Extended",
        containment="Not Specified",
        ea_guid="{C5FD83AF-4915-48f3-B896-E7E6091B2C08}",
        position="1",
        owner_class_name="BPDProgramado",
        label="Fuente del Programa"
    ),

    ComputedField(
        name='sumarioPrograma',
        widget=ComputedField._properties['widget'](
            label="Resumen del Programa",
            label2="Program Summary",
            description="Un resumen del tipo del programa y el  codigo fuente del programa especificado en este elemento.",
            description2="A summary of the program type and  source code of the program specified for this element.",
            label_msgid='gvSIGbpd_BPDProgramado_attr_sumarioPrograma_label',
            description_msgid='gvSIGbpd_BPDProgramado_attr_sumarioPrograma_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Un resumen del tipo del programa y el  codigo fuente del programa especificado en este elemento.",
        duplicates="0",
        label2="Program Summary",
        ea_localid="625",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="A summary of the program type and  source code of the program specified for this element.",
        ea_guid="{FD2FF243-D2C9-4b51-871A-BA72D805E5F9}",
        exclude_from_values_form="True",
        scale="0",
        computed_types="string",
        label="Resumen del Programa",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDProgramado",
        expression="'%s:%s' %(( context.getTipoPrograma() or ''), ( context.getFuentePrograma() or ''))[:64]",
        exclude_from_exportconfig="True",
        exclude_from_copyconfig="True"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDProgramado_schema = getattr(BPDArquetipoConAdopcion, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDProgramado(OrderedBaseFolder, BPDArquetipoConAdopcion):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoConAdopcion,'__implements__',()),)



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

    schema = BPDProgramado_schema

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
# end of class BPDProgramado

##code-section module-footer #fill in your manual code here
##/code-section module-footer



