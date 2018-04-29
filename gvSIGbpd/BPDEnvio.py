# -*- coding: utf-8 -*-
#
# File: BPDEnvio.py
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
from Products.gvSIGbpd.BPDPasoGeneral import BPDPasoGeneral
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
        name='multiplicidadMinima',
        widget=IntegerField._properties['widget'](
            label="Multiplicidad Minima",
            label2="Minimum Multiplicity",
            description="Numero minimo de elementos a enviar. Introduzca 0 para indicar que el Envio procedera con exito, aunque no se envie ningun artefacto.",
            description2="Minimum number of elements to send. Enter 0 to indicate that the Send will proceed with success, even if no Artefact of the type was sent",
            label_msgid='gvSIGbpd_BPDEnvio_attr_multiplicidadMinima_label',
            description_msgid='gvSIGbpd_BPDEnvio_attr_multiplicidadMinima_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Numero minimo de elementos a enviar. Introduzca 0 para indicar que el Envio procedera con exito, aunque no se envie ningun artefacto.",
        duplicates="0",
        label2="Minimum Multiplicity",
        ea_localid="410",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Minimum number of elements to send. Enter 0 to indicate that the Send will proceed with success, even if no Artefact of the type was sent",
        ea_guid="{5CDF47ED-7EA6-4b5a-96E9-8535F338B5C8}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Multiplicidad Minima",
        length="0",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDEnvio"
    ),

    IntegerField(
        name='multiplicidadMaxima',
        widget=IntegerField._properties['widget'](
            label="Multiplicidad Maxima",
            label2="Maximum Multiplicity",
            description="Numero maximo de elementos a enviar. Introduzca -1 para indicar que no hay limite superior para el numero de Artefactos a enviar.",
            description2="Maximum number of elements to send. Enter -1 to indicate that there is no upper limit in the number of elements to send.",
            label_msgid='gvSIGbpd_BPDEnvio_attr_multiplicidadMaxima_label',
            description_msgid='gvSIGbpd_BPDEnvio_attr_multiplicidadMaxima_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Numero maximo de elementos a enviar. Introduzca -1 para indicar que no hay limite superior para el numero de Artefactos a enviar.",
        duplicates="0",
        label2="Maximum Multiplicity",
        ea_localid="407",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Maximum number of elements to send. Enter -1 to indicate that there is no upper limit in the number of elements to send.",
        ea_guid="{878AAA95-0490-4fad-932B-24C2F6CA3C83}",
        write_permission='Modify portal content',
        scale="0",
        default="-1",
        label="Multiplicidad Maxima",
        length="0",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDEnvio"
    ),

    RelationField(
        name='destinatarios',
        inverse_relation_label="Destinatario de Envios",
        additional_columns=['abreviatura', 'responsabilidadesClave'],
        inverse_relation_description="Envios que se destinan a este Perfil o Unidad Organizacional.",
        description="Perfiles o Unidades Organizacionales a los que se destina el Envio.",
        relationship='BPDDestinatarios',
        inverse_relation_field_name='destinatarioDeEnvios',
        inverse_relation_label2="Receiver of Send steps",
        label2="Receivers",
        inverse_relation_description2="Send process steps addressed to this participant Profile or Organisational Unit.",
        widget=ReferenceBrowserWidget(
            label="Destinatarios",
            label2="Receivers",
            description="Perfiles o Unidades Organizacionales a los que se destina el Envio.",
            description2="Participant Profiles or Organisational Units to whom this is Sent",
            label_msgid='gvSIGbpd_BPDEnvio_rel_destinatarios_label',
            description_msgid='gvSIGbpd_BPDEnvio_rel_destinatarios_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Destinatarios",
        description2="Participant Profiles or Organisational Units to whom this is Sent",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDDestinatarioDeEnvios',
        owner_class_name="BPDEnvio",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;"
    ),

    ComputedField(
        name='detallesPaso',
        widget=ComputedField._properties['widget'](
            label="Detalles del Paso",
            label2="Step details",
            description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
            description2="Details about the fetarues of the Busienss Process Step",
            label_msgid='gvSIGbpd_BPDEnvio_attr_detallesPaso_label',
            description_msgid='gvSIGbpd_BPDEnvio_attr_detallesPaso_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
        duplicates="0",
        label2="Step details",
        ea_localid="278",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the fetarues of the Busienss Process Step",
        ea_guid="{5273BF3F-BBC0-4973-8DA6-2D1863879182}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del Paso",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDEnvio",
        expression="context.fTFLVsUnless([ ['esInicial', False,], ['titulosDestinatarios','',],['titulosArtefactosEnviados','',],['ejecutores',None,],[ 'titulosArtefactosUsados','',],[ 'titulosCaracteristicasUsadas','',],])",
        computed_types="string"
    ),

    RelationField(
        name='artefactosEnviados',
        inverse_relation_label="Enviado desde Pasos de Procesos de Negocio",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion', 'version', 'fechaAdopcion', 'fechaObsolescencia'],
        inverse_relation_description="Pasos de Proceso de Negocio que envian un Artefacto de este tipo a un Participante externo.",
        description="Artefactos que se envian en este paso a un Participante externo.",
        relationship='BPDArtefactosEnviados',
        inverse_relation_field_name='pasosQueEnvianElArtefacto',
        inverse_relation_label2="Sent from Business Process Steps",
        label2="Sent Artefacts",
        inverse_relation_description2="Business Process Steps sending Artefacts of this type to external participants.",
        widget=ReferenceBrowserWidget(
            label="Artefactos Enviados",
            label2="Sent Artefacts",
            description="Artefactos que se envian en este paso a un Participante externo.",
            description2="Artefacts thar shall be sent while in this step to an external participant.",
            label_msgid='gvSIGbpd_BPDEnvio_rel_artefactosEnviados_label',
            description_msgid='gvSIGbpd_BPDEnvio_rel_artefactosEnviados_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Artefactos Enviados",
        description2="Artefacts thar shall be sent while in this step to an external participant.",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDPasosQueEnvianElArtefacto',
        owner_class_name="BPDEnvio",
        deststyle="Navigable=Unspecified;Union=0;Derived=0;AllowDuplicates=0;Owned=0;"
    ),

    ComputedField(
        name='titulosArtefactosEnviados',
        widget=ComputedField._properties['widget'](
            label="Artefactos Enviados",
            label2="Sent Artefacts",
            description="Artefactos que se envian en este paso a un Participante externo.",
            description2="Artefacts thar shall be sent while in this step to an external participant.",
            label_msgid='gvSIGbpd_BPDEnvio_attr_titulosArtefactosEnviados_label',
            description_msgid='gvSIGbpd_BPDEnvio_attr_titulosArtefactosEnviados_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Artefactos que se envian en este paso a un Participante externo.",
        duplicates="0",
        label2="Sent Artefacts",
        ea_localid="270",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Artefacts thar shall be sent while in this step to an external participant.",
        containment="Not Specified",
        ea_guid="{FEE95966-1F45-469b-8A13-A9746A0E65E0}",
        position="1",
        owner_class_name="BPDEnvio",
        label="Artefactos Enviados",
        expression="context.fFV('artefactosEnviados')",
        exclude_from_values_form="True"
    ),

    ComputedField(
        name='titulosDestinatarios',
        widget=ComputedField._properties['widget'](
            label="Destinatarios",
            label2="Receivers",
            description="Perfiles o Unidades Organizacionales a los que se destina el Envio.",
            description2="Participant Profiles or Organisational Units to whom this is Sent",
            label_msgid='gvSIGbpd_BPDEnvio_attr_titulosDestinatarios_label',
            description_msgid='gvSIGbpd_BPDEnvio_attr_titulosDestinatarios_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Perfiles o Unidades Organizacionales a los que se destina el Envio.",
        duplicates="0",
        label2="Receivers",
        ea_localid="271",
        derived="0",
        collection="false",
        label="Destinatarios",
        description2="Participant Profiles or Organisational Units to whom this is Sent",
        containment="Not Specified",
        ea_guid="{AF512C2B-BF61-4a84-8E8A-4E954298FEE2}",
        position="0",
        owner_class_name="BPDEnvio",
        styleex="volatile=0;",
        expression="context.fFV('destinatarios')",
        exclude_from_values_form="True"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDEnvio_schema = OrderedBaseFolderSchema.copy() + \
    getattr(BPDPasoGeneral, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDEnvio(OrderedBaseFolder, BPDPasoGeneral):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDPasoGeneral,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Envio'

    meta_type = 'BPDEnvio'
    portal_type = 'BPDEnvio'


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



    allowed_content_types = [] + list(getattr(BPDPasoGeneral, 'allowed_content_types', []))
    filter_content_types             = 1
    global_allow                     = 0
    content_icon = 'bpdenvio.gif'
    immediate_view                   = 'Textual'
    default_view                     = 'Textual'
    suppl_views                      = ('Textual', 'Tabular', )
    typeDescription                  = "Representa un Paso de Proceso en que se envia una informacion al exterior del ambito del Proceso."
    typeDescMsgId                    =  'gvSIGbpd_BPDEnvio_help'
    archetype_name2                  = 'Send'
    typeDescription2                 = '''Represents a Business Process Step where some information is sent outside of the boudaries of the Business Process.'''
    archetype_name_msgid             = 'gvSIGbpd_BPDEnvio_label'
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


       {'action': "string:${object_url}/TextualRest",
        'category': "object_buttons",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDVersions",
        'category': "object",
        'id': 'mddversions',
        'name': 'Versions',
        'permissions': ("View",),
        'condition': """python:1"""
       },


       {'action': "string:${object_url}/MDDInspectCache/",
        'category': "object_buttons",
        'id': 'mddinspectcache',
        'name': 'Inspect Cache',
        'permissions': ("View",),
        'condition': """python:1"""
       },


    )

    _at_rename_after_creation = True

    schema = BPDEnvio_schema

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

registerType(BPDEnvio, PROJECTNAME)
# end of class BPDEnvio

##code-section module-footer #fill in your manual code here
##/code-section module-footer



