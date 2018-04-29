# -*- coding: utf-8 -*-
#
# File: BPDOrganizacion.py
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
from Products.gvSIGbpd.BPDUnidadOrganizacional import BPDUnidadOrganizacional
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Acquisition  import aq_inner, aq_parent

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    BooleanField(
        name='permiteLeer',
        widget=BooleanField._properties['widget'](
            label="Permite ver Organizacion",
            label2="Allow to see Organization",
            description="Si Verdadero, entonces los usuarios pueden ver la Organizacion. Puede ser Falso durante  procesos de importacion largos, o por indicacion del administrador.",
            description2="If True, then the users may see  the Organization. It may be False during long import processes or by manager request.",
            label_msgid='gvSIGbpd_BPDOrganizacion_attr_permiteLeer_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_attr_permiteLeer_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Si Verdadero, entonces los usuarios pueden ver la Organizacion. Puede ser Falso durante  procesos de importacion largos, o por indicacion del administrador.",
        duplicates="0",
        label2="Allow to see Organization",
        ea_localid="344",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="If True, then the users may see  the Organization. It may be False during long import processes or by manager request.",
        ea_guid="{4AB95A00-7009-4f7d-8E86-E26666E1849C}",
        read_only="True",
        default="True",
        label="Permite ver Organizacion",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDOrganizacion",
        exclude_from_exportconfig="True",
        exclude_from_copyconfig="True"
    ),

    BooleanField(
        name='permiteModificar',
        widget=BooleanField._properties['widget'](
            label="Permite modificar Organizacion",
            label2="Allow to change Organization",
            description="Si Verdadero, entonces los usuarios pueden cambiar la Organizacion. Puede ser Falso durante  procesos de importacion largos, o por indicacion del administrador.",
            description2="If True, then the users may change the Organization. It may be False during long import processes or by manager request.",
            label_msgid='gvSIGbpd_BPDOrganizacion_attr_permiteModificar_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_attr_permiteModificar_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Si Verdadero, entonces los usuarios pueden cambiar la Organizacion. Puede ser Falso durante  procesos de importacion largos, o por indicacion del administrador.",
        duplicates="0",
        label2="Allow to change Organization",
        ea_localid="345",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="If True, then the users may change the Organization. It may be False during long import processes or by manager request.",
        ea_guid="{159316D0-39EF-4c8d-8CF7-FF2DBFE4C49D}",
        read_only="True",
        default="True",
        label="Permite modificar Organizacion",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDOrganizacion",
        exclude_from_exportconfig="True",
        exclude_from_copyconfig="True"
    ),

    StringField(
        name='versionInterna',
        widget=StringWidget(
            label="Version (uso interno)",
            label2="Version identifier (internal)",
            description="Identificador de version para uso interno de la aplicacion.",
            description2="Version identifier used internally by the application.",
            label_msgid='gvSIGbpd_BPDOrganizacion_attr_versionInterna_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_attr_versionInterna_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Identificador de version para uso interno de la aplicacion.",
        duplicates="0",
        label2="Version identifier (internal)",
        ea_localid="372",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Version identifier used internally by the application.",
        ea_guid="{6F804C0A-A2C8-47e1-8D1D-3D708FAF4D61}",
        write_permission='Modify portal content',
        scale="0",
        is_version="True",
        label="Version (uso interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDOrganizacion"
    ),

    ComputedField(
        name='coleccionesPoliticasDeNegocio',
        widget=ComputedWidget(
            label="Politicas de Negocio (colecciones)",
            label2="Business Policies (collections)",
            description="Colecciones de Politicas de Negocio que gobiernan la Organizacion y sus Procesos de Negocio, y constituyen la base de las Reglas de Negocio.",
            description2="Collections of Business Policies  governing the Organisation and its Business Processes, and constitute the basis for the Business Rules.",
            label_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesPoliticasDeNegocio_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesPoliticasDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Business Policies (collections)',
        label='Politicas de Negocio (colecciones)',
        represents_aggregation=True,
        description2='Collections of Business Policies  governing the Organisation and its Business Processes, and constitute the basis for the Business Rules.',
        multiValued=1,
        owner_class_name="BPDOrganizacion",
        expression="context.objectValues(['BPDColeccionPoliticasDeNegocio'])",
        computed_types=['BPDColeccionPoliticasDeNegocio'],
        non_framework_elements=False,
        description='Colecciones de Politicas de Negocio que gobiernan la Organizacion y sus Procesos de Negocio, y constituyen la base de las Reglas de Negocio.'
    ),

    ComputedField(
        name='coleccionesReglasDeNegocio',
        widget=ComputedWidget(
            label="Reglas de Negocio (colecciones)",
            label2="Business Rules (collections)",
            description="Colecciones de Reglas deNegocio que se derivan de las politicas de Negocio, y dirigen los Procesos de Negocio de la Organizacion.",
            description2="Collections of Business Rules derived from Business Policies, and driving the Business Process in the Organisation.",
            label_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesReglasDeNegocio_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesReglasDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Business Rules (collections)',
        label='Reglas de Negocio (colecciones)',
        represents_aggregation=True,
        description2='Collections of Business Rules derived from Business Policies, and driving the Business Process in the Organisation.',
        multiValued=1,
        owner_class_name="BPDOrganizacion",
        expression="context.objectValues(['BPDColeccionReglasDeNegocio'])",
        computed_types=['BPDColeccionReglasDeNegocio'],
        non_framework_elements=False,
        description='Colecciones de Reglas deNegocio que se derivan de las politicas de Negocio, y dirigen los Procesos de Negocio de la Organizacion.'
    ),

    ComputedField(
        name='coleccionesProcesosDeNegocio',
        widget=ComputedWidget(
            label="Procesos de Negocio (colecciones)",
            label2="Business Processes (collections)",
            description="Colecciones de Procesos de Negocio realizando cursos de accion con los que la Organizacion persigue propositos especificos.",
            description2="Collections of Business Processes realising courses of action through which the Organisation pursues specific goals.",
            label_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesProcesosDeNegocio_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesProcesosDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Business Processes (collections)',
        label='Procesos de Negocio (colecciones)',
        represents_aggregation=True,
        description2='Collections of Business Processes realising courses of action through which the Organisation pursues specific goals.',
        multiValued=1,
        owner_class_name="BPDOrganizacion",
        expression="context.objectValues(['BPDColeccionProcesosDeNegocio'])",
        computed_types=['BPDColeccionProcesosDeNegocio'],
        non_framework_elements=False,
        description='Colecciones de Procesos de Negocio realizando cursos de accion con los que la Organizacion persigue propositos especificos.'
    ),

    ComputedField(
        name='coleccionesArtefactos',
        widget=ComputedWidget(
            label="Artefactos (colecciones)",
            label2="Artefacts (collections)",
            description="Colecciones de Artefactos que se producen, consumen, consultan, editan, y en general son el objeto del esfuerzo de la Organizacion.",
            description2="Collections of Artefacts produced, consumed, consulted, edited, or otherwise object of the Organisation effort.",
            label_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesArtefactos_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesArtefactos_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Artefacts (collections)',
        label='Artefactos (colecciones)',
        represents_aggregation=True,
        description2='Collections of Artefacts produced, consumed, consulted, edited, or otherwise object of the Organisation effort.',
        multiValued=1,
        owner_class_name="BPDOrganizacion",
        expression="context.objectValues(['BPDColeccionArtefactos'])",
        computed_types=['BPDColeccionArtefactos'],
        non_framework_elements=False,
        description='Colecciones de Artefactos que se producen, consumen, consultan, editan, y en general son el objeto del esfuerzo de la Organizacion.'
    ),

    ComputedField(
        name='coleccionesHerramientas',
        widget=ComputedWidget(
            label="Herramientas (colecciones)",
            label2="Tools (collections)",
            description="Colecciones de Herramientas que la Organizacion aplica para manejar ciertos Artefactos y asistir en la ejecucion de Pasos de Procesos de Negocio.",
            description2="Collections of Tools applied in the Organisation to handle certain Artefacts, and assist in the execution of Business Process Steps.",
            label_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesHerramientas_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_contents_coleccionesHerramientas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=True,
        label2='Tools (collections)',
        label='Herramientas (colecciones)',
        represents_aggregation=True,
        description2='Collections of Tools applied in the Organisation to handle certain Artefacts, and assist in the execution of Business Process Steps.',
        multiValued=1,
        owner_class_name="BPDOrganizacion",
        expression="context.objectValues(['BPDColeccionHerramientas'])",
        computed_types=['BPDColeccionHerramientas'],
        non_framework_elements=False,
        description='Colecciones de Herramientas que la Organizacion aplica para manejar ciertos Artefactos y asistir en la ejecucion de Pasos de Procesos de Negocio.'
    ),

    TextField(
        name='comentarioVersionInterna',
        widget=TextAreaWidget(
            label="Comentario de Version (uso interno)",
            label2="Version Comment (internal)",
            description="Comentario a la version para uso interno de la aplicacion.",
            description2="Comments on the Version used internally by the application.",
            label_msgid='gvSIGbpd_BPDOrganizacion_attr_comentarioVersionInterna_label',
            description_msgid='gvSIGbpd_BPDOrganizacion_attr_comentarioVersionInterna_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Comentario a la version para uso interno de la aplicacion.",
        duplicates="0",
        label2="Version Comment (internal)",
        ea_localid="373",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Comments on the Version used internally by the application.",
        ea_guid="{E772FF53-10E9-4299-B6DB-1CE6FA85B39C}",
        is_version_comment="True",
        scale="0",
        write_permission='Modify portal content',
        label="Comentario de Version (uso interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDOrganizacion"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDOrganizacion_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDUnidadOrganizacional, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDOrganizacion(OrderedBaseFolder, BPDUnidadOrganizacional):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDUnidadOrganizacional,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Organizacion'

    meta_type = 'BPDOrganizacion'
    portal_type = 'BPDOrganizacion'


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



    allowed_content_types = ['BPDColeccionPoliticasDeNegocio', 'BPDColeccionHerramientas', 'BPDColeccionProcesosDeNegocio', 'BPDColeccionReglasDeNegocio', 'BPDColeccionArtefactos'] + list(getattr(BPDUnidadOrganizacional, 'allowed_content_types', []))
    filter_content_types = 1
    global_allow = 1
    content_icon = 'bpdorganizacion.gif'
    immediate_view = 'Textual'
    default_view = 'Textual'
    suppl_views = ('Textual', 'Tabular', )
    typeDescription = "Raiz de contenidos para definicion y publicacion de procedimientos de gestion."
    typeDescMsgId =  'gvSIGbpd_BPDOrganizacion_help'
    archetype_name2 = 'Organisation'
    typeDescription2 = '''Root of all definition and publicacion content.'''
    archetype_name_msgid = 'gvSIGbpd_BPDOrganizacion_label'
    factory_methods = None
    factory_enablers = None


    actions =  (


       {'action': "string:$object_url/base_edit",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("ModifyPortalContent",),
        'condition': """python:('portal_factory' in object.getPhysicalPath())"""
       },


       {'action': "string:$object_url/Editar",
        'category': "object",
        'id': 'editar',
        'name': 'Edit',
        'permissions': ("ModifyPortalContent",),
        'condition': """python:( not ('portal_factory' in object.getPhysicalPath())) and object.fAllowWrite()"""
       },


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
        'permissions': ("View",),
        'condition': """python:0"""
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

    schema = BPDOrganizacion_schema

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

    security.declarePublic('cb_isMoveable')
    def cb_isMoveable(self):
        """
        """
        
        return self._at_rename_after_creation or  ('portal_factory' in self.getPhysicalPath()) or ((  not self.getEsRaiz()) and self.fAllowWrite())

    security.declarePublic('getEsRaiz')
    def getEsRaiz(self):
        """
        """
        
        return not aq_parent( aq_inner( self)) or ( not( aq_parent( aq_inner( self)).meta_type == "BPDColeccionUnidadesOrganizacionales")) # First test for objects still not hooed up into the hierarchy

    security.declarePublic('fAllowRead')
    def fAllowRead(self):
        """
        """
        
        return self.getPermiteLeer() and ( self.getEsRaiz() or self.getRaiz().fAllowRead())

    security.declarePublic('fAllowWrite')
    def fAllowWrite(self):
        """
        """
        
        return self.fAllowRead() and self.getPermiteModificar() and ( self.getEsRaiz() or self.getRaiz().fAllowWrite())

registerType(BPDOrganizacion, PROJECTNAME)
# end of class BPDOrganizacion

##code-section module-footer #fill in your manual code here
##/code-section module-footer



