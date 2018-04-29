# -*- coding: utf-8 -*-
#
# File: BPDPerfil.py
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
from Products.gvSIGbpd.BPDParticipante import BPDParticipante
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='conocimientosPoseidos',
        widget=TextAreaWidget(
            label="Conocimientos Poseidos",
            label2="Skills",
            description="Necesarios en el personal para que se ajuste al Perfil.",
            description2="Skills to be possesed by people mathing this Profile.",
            label_msgid='gvSIGbpd_BPDPerfil_attr_conocimientosPoseidos_label',
            description_msgid='gvSIGbpd_BPDPerfil_attr_conocimientosPoseidos_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Necesarios en el personal para que se ajuste al Perfil.",
        duplicates="0",
        label2="Skills",
        ea_localid="215",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Skills to be possesed by people mathing this Profile.",
        ea_guid="{A17EC1A9-E9A2-480c-9E28-01884319A90D}",
        write_permission='Modify portal content',
        scale="0",
        label="Conocimientos Poseidos",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPerfil"
    ),

    TextField(
        name='habilidadesDemostradas',
        widget=TextAreaWidget(
            label="Habilidades Demostradas",
            label2="Demonstrated Habilities",
            description="Los individuos que se ajusta a este Perfil habran demostrado las habilidades indicadas.",
            description2="Individuals matching the participant Profile must have proven these habilities.",
            label_msgid='gvSIGbpd_BPDPerfil_attr_habilidadesDemostradas_label',
            description_msgid='gvSIGbpd_BPDPerfil_attr_habilidadesDemostradas_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Los individuos que se ajusta a este Perfil habran demostrado las habilidades indicadas.",
        duplicates="0",
        label2="Demonstrated Habilities",
        ea_localid="216",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Individuals matching the participant Profile must have proven these habilities.",
        ea_guid="{24D52A78-3DF0-47bf-974F-581C8850AC7E}",
        write_permission='Modify portal content',
        scale="0",
        label="Habilidades Demostradas",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDPerfil"
    ),

    TextField(
        name='seleccionDePersonal',
        widget=TextAreaWidget(
            label="Seleccion de Personal",
            label2="Human Resources Selection",
            description="Criterios para la seleccion de personal con este Perfil.",
            description2="Selection criteria for staffing the participant Profile with matching individuals.",
            label_msgid='gvSIGbpd_BPDPerfil_attr_seleccionDePersonal_label',
            description_msgid='gvSIGbpd_BPDPerfil_attr_seleccionDePersonal_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Criterios para la seleccion de personal con este Perfil.",
        duplicates="0",
        label2="Human Resources Selection",
        ea_localid="217",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Selection criteria for staffing the participant Profile with matching individuals.",
        ea_guid="{8C2DCEFC-323E-4d10-B506-5D746E07E652}",
        write_permission='Modify portal content',
        scale="0",
        label="Seleccion de Personal",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDPerfil"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPerfil_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDParticipante, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPerfil(OrderedBaseFolder, BPDParticipante):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDParticipante,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Perfil'

    meta_type = 'BPDPerfil'
    portal_type = 'BPDPerfil'


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
    version_comment_field = 'comentarioVersionInterna'
    language_field = 'codigoIdiomaInterno'
    fields_pending_translation_field = 'camposPendientesTraduccionInterna'
    fields_pending_revision_field = 'camposPendientesRevisionInterna'



    allowed_content_types = [] + list(getattr(BPDParticipante, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 0
    content_icon = 'bpdperfil.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Un Perfil representa un tipo de participante en los procesos de gestion de gvSIG. No identifica personas concretas, . Se definen los conocimientos y habilidades propias al Perfil."
    typeDescMsgId =  'gvSIGbpd_BPDPerfil_help'
    archetype_name2 = 'Profile'
    typeDescription2 = '''A Profile represents a kind of participant in the Business Processes. It does not identify concrete individuals.'''
    archetype_name_msgid = 'gvSIGbpd_BPDPerfil_label'
    factory_methods = None
    factory_enablers = None


    actions =  (


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
        'permissions': ("View",),
        'condition': """python:0"""
       },


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
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


       {'action': "string:${object_url}/TextualRest",
        'category': "object_buttons",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/Textual",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDNewVersion",
        'category': "object_buttons",
        'id': 'mddnewversion',
        'name': 'New Version',
        'permissions': ("Modify portal content",),
        'condition': """python:object.fAllowVersion() and object.getEsRaiz()"""
       },


       {'action': "string:${object_url}/MDDVersions",
        'category': "object",
        'id': 'mddversions',
        'name': 'Versions',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDNewTranslation",
        'category': "object_buttons",
        'id': 'mddnewtranslation',
        'name': 'New Translation',
        'permissions': ("Modify portal content",),
        'condition': """python:0 and object.fAllowTranslation() and object.getEsRaiz()"""
       },


    )

    _at_rename_after_creation = True

    schema = BPDPerfil_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('manage_afterAdd')
    def manage_afterAdd(self,item,container):
        """
        """
        
        return self.pHandle_manage_afterAdd(  item, container)

registerType(BPDPerfil, PROJECTNAME)
# end of class BPDPerfil

##code-section module-footer #fill in your manual code here
##/code-section module-footer



