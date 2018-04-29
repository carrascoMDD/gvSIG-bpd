# -*- coding: utf-8 -*-
#
# File: BPDPasoMinimo.py
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
from Products.gvSIGbpd.BPDProgramable import BPDProgramable
from Products.gvSIGbpd.BPDArquetipoReferenciable import BPDArquetipoReferenciable
from Products.gvSIGbpd.BPDPasoConRestriccionesTiempo import BPDPasoConRestriccionesTiempo
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='detallesPaso',
        widget=ComputedField._properties['widget'](
            label="Detalles del Paso",
            label2="Step details",
            description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
            description2="Details about the features of the Business Process Step",
            label_msgid='gvSIGbpd_BPDPasoMinimo_attr_detallesPaso_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_attr_detallesPaso_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Detalles acerca de las caracteristicas del Paso de Proceso de Negocio.",
        duplicates="0",
        label2="Step details",
        ea_localid="641",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Details about the features of the Business Process Step",
        ea_guid="{2D390F68-F8AD-4b54-8212-3FB8C5F43904}",
        exclude_from_values_form="True",
        scale="0",
        label="Detalles del Paso",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDPasoMinimo",
        expression="context.fTFLVsUnless([ [ 'titulosArtefactosUsados','',],[ 'titulosCaracteristicasUsadas','',],])",
        computed_types="string"
    ),

    ComputedField(
        name='numeroDePaso',
        widget=ComputedField._properties['widget'](
            label="Numero de Paso",
            label2="Step Order Index",
            description="El numero de orden del Paso en la lista de Pasos de su Proceso. Util para su identificacion rapida. Notese que este numero puede cambiar al modificar la lista de Pasos del Proceso.",
            description2="An index number of the Step in the Business Process, useful for fast reference, but volatile, as it changes whenever any previous steps are  removed, or steps added or moved before this step.",
            label_msgid='gvSIGbpd_BPDPasoMinimo_attr_numeroDePaso_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_attr_numeroDePaso_help',
            i18n_domain='gvSIGbpd',
        ),
        description="El numero de orden del Paso en la lista de Pasos de su Proceso. Util para su identificacion rapida. Notese que este numero puede cambiar al modificar la lista de Pasos del Proceso.",
        duplicates="0",
        label2="Step Order Index",
        ea_localid="221",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="An index number of the Step in the Business Process, useful for fast reference, but volatile, as it changes whenever any previous steps are  removed, or steps added or moved before this step.",
        ea_guid="{ACE5E9DA-5E01-41e7-A7F9-6BA25347EBD8}",
        exclude_from_values_form="True",
        scale="0",
        label="Numero de Paso",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPasoMinimo",
        expression="context.getNumeroOrdenEnPropietario()",
        computed_types="int"
    ),

    RelationField(
        name='episodios',
        inverse_relation_label="Episodios",
        inverse_relation_description="Episodios en los que se ejecuta el Paso.",
        description="Secuencia de Pasos del Proceso de Negocio a ejecutar como comportamiento del Episodio.",
        relationship='pasos_episodios',
        label2="Steps",
        widget=ReferenceBrowserWidget(
            label="Pasos",
            label2="Steps",
            description="Secuencia de Pasos del Proceso de Negocio a ejecutar como comportamiento del Episodio.",
            description2="Sequence of Business Process Steps to execute as the behavior of the Episode.",
            label_msgid='gvSIGbpd_BPDPasoMinimo_rel_episodios_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_rel_episodios_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Sequence of Business Process Steps to execute as the behavior of the Episode.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Episodes",
        dependency_supplier=True,
        inverse_relation_field_name='pasos',
        inverse_relation_description2="Episodes executing the Step.",
        additional_columns=['detallesPaso',],
        write_permission='Modify portal content',
        label="Pasos",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='Pasos_De_Episodio'
    ),

    RelationField(
        name='reglasDeNegocioAplicadas',
        inverse_relation_label="Pasos dirigidos",
        inverse_relation_description="Pasos de Procesos de Negocio donde se aplica la Regla de Negocio",
        description="Reglas de Negocio aplicadas durante la ejecucion del Paso.",
        relationship='BPDReglasDeNegocioAplicadas',
        label2="Applied Business Rules",
        widget=ReferenceBrowserWidget(
            label="Reglas de Negocio aplicadas",
            label2="Applied Business Rules",
            description="Reglas de Negocio aplicadas durante la ejecucion del Paso.",
            description2="Business Rules applicable in the Business Process Steps.",
            label_msgid='gvSIGbpd_BPDPasoMinimo_rel_reglasDeNegocioAplicadas_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_rel_reglasDeNegocioAplicadas_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Business Rules applicable in the Business Process Steps.",
        inverse_relation_label2="Business Process Steps applying the Business Rule",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='pasosAplicandoLaRegla',
        inverse_relation_description2="Business Process Steps applying the Business Rule.",
        additional_columns=['codigo'],
        label="Reglas de Negocio aplicadas",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDPasosAplicandoLaRegla',
        owner_class_name="BPDPasoMinimo"
    ),

    RelationField(
        name='herramientasAplicadas',
        inverse_relation_label="Pasos Asistidos",
        inverse_relation_description="Pasos de procesos de negocio donde se aplica la Herramienta.La Herramienta puede ademas se usada por Procesos de Negocio completos.",
        description="Herramientas a utilizar para ejecutar este Paso del Proceso de Negocio, o manejar los Artefactos usados en el Paso. Considere ademas las Herramientas referidas como usadas desde todo el Proceso de Negocio.",
        relationship='BPDHerramientasAplicadas',
        label2="Applied Tools",
        widget=ReferenceBrowserWidget(
            label="Herramientas aplicadas",
            label2="Applied Tools",
            description="Herramientas a utilizar para ejecutar este Paso del Proceso de Negocio, o manejar los Artefactos usados en el Paso. Considere ademas las Herramientas referidas como usadas desde todo el Proceso de Negocio.",
            description2="Tools to apply in the execution of the Business Process Step, or to manipulate the used Artefacts. Consider too the Tools refered as used in the whole Business Process.",
            label_msgid='gvSIGbpd_BPDPasoMinimo_rel_herramientasAplicadas_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_rel_herramientasAplicadas_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Tools to apply in the execution of the Business Process Step, or to manipulate the used Artefacts. Consider too the Tools refered as used in the whole Business Process.",
        inverse_relation_label2="Assisted Steps",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='pasosAsistidos',
        inverse_relation_description2="Business Process Steps applying the Tool. The Tool may be also applied by whole Business Processes.",
        additional_columns=['codigo'],
        label="Herramientas aplicadas",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDPasosAsistidos',
        owner_class_name="BPDPasoMinimo"
    ),

    ComputedField(
        name='tituloProcesoDeNegocio',
        widget=ComputedField._properties['widget'](
            label="Proceso de Negocio",
            label2="Business Process",
            description="El titulo del Proceso de Negocio que contiene el Paso.",
            description2="Title of the Business Process containing the Step.",
            label_msgid='gvSIGbpd_BPDPasoMinimo_attr_tituloProcesoDeNegocio_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_attr_tituloProcesoDeNegocio_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="El titulo del Proceso de Negocio que contiene el Paso.",
        duplicates="0",
        label2="Business Process",
        ea_localid="222",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Title of the Business Process containing the Step.",
        ea_guid="{4EE60B50-C473-4694-9E8B-AB35D47C9813}",
        exclude_from_values_form="True",
        scale="0",
        label="Proceso de Negocio",
        length="0",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDPasoMinimo",
        expression="context.getPropietario().Title()",
        computed_types="string"
    ),

    ComputedField(
        name='titulosArtefactosUsados',
        widget=ComputedField._properties['widget'](
            label="Artefactos Usados",
            label2="Used Artefacts",
            description="Artefactos que se usan en el Paso del Proceso de Negocio.",
            description2="Artefacts Used in the Business Process Step",
            label_msgid='gvSIGbpd_BPDPasoMinimo_attr_titulosArtefactosUsados_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_attr_titulosArtefactosUsados_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Artefactos que se usan en el Paso del Proceso de Negocio.",
        duplicates="0",
        label2="Used Artefacts",
        ea_localid="426",
        derived="0",
        collection="false",
        label="Artefactos Usados",
        description2="Artefacts Used in the Business Process Step",
        containment="Not Specified",
        ea_guid="{0B25CA4F-EE74-4ee0-9FEB-19F4EDBD5352}",
        position="2",
        owner_class_name="BPDPasoMinimo",
        styleex="volatile=0;",
        expression="', '.join( [ a.fTFLVsUnless([ ['title','',], ['titulosArtefactosUsados','',],]) for a in  context.getUsosArtefactos()])",
        exclude_from_values_form="True"
    ),

    ComputedField(
        name='titulosCaracteristicasUsadas',
        widget=ComputedField._properties['widget'](
            label="Caracteristicas Usadas",
            label2="Used Artefacts",
            description="Caracteristicas de Artefactos que se usan en el Paso del Proceso de Negocio.",
            description2="Artefact Featuress Used in the Business Process Step",
            label_msgid='gvSIGbpd_BPDPasoMinimo_attr_titulosCaracteristicasUsadas_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_attr_titulosCaracteristicasUsadas_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Caracteristicas de Artefactos que se usan en el Paso del Proceso de Negocio.",
        duplicates="0",
        label2="Used Artefacts",
        ea_localid="444",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Artefact Featuress Used in the Business Process Step",
        containment="Not Specified",
        ea_guid="{16A5583E-8246-491a-BA03-9461528824C6}",
        position="3",
        owner_class_name="BPDPasoMinimo",
        label="Caracteristicas Usadas",
        expression="', '.join( [ a.fTFLVsUnless([ ['title','',], ['titulosCaracteristicasUsadas','',],]) for a in  context.getUsosCaracteristicas()])",
        exclude_from_values_form="True"
    ),

    ComputedField(
        name='usosArtefactos',
        widget=ComputedWidget(
            label="Usa Artefactos",
            label2="Use Artefacts",
            description="Artefactos usados en el Paso del Proceso de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.",
            description2="Artefacts used in the Business Process Step, to Create, Read, Update, Delete or Link.",
            label_msgid='gvSIGbpd_BPDPasoMinimo_contents_usosArtefactos_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_contents_usosArtefactos_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Use Artefacts',
        additional_columns=['esRequerido', 'modoDeUso', 'titulosArtefactosUsados'],
        label='Usa Artefactos',
        represents_aggregation=True,
        description2='Artefacts used in the Business Process Step, to Create, Read, Update, Delete or Link.',
        multiValued=1,
        owner_class_name="BPDPasoMinimo",
        expression="context.objectValues(['BPDUsoArtefacto'])",
        computed_types=['BPDUsoArtefacto'],
        non_framework_elements=False,
        description='Artefactos usados en el Paso del Proceso de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.'
    ),

    ComputedField(
        name='usosCaracteristicas',
        widget=ComputedWidget(
            label="Usa Caracteristicas",
            label2="Use Features",
            description="Caracteristicas de Artefactos que se usan en el Paso del Proceso de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.",
            description2="Artefact Features used in the Business Process Step, to Create, Read, Update, Delete or Link.",
            label_msgid='gvSIGbpd_BPDPasoMinimo_contents_usosCaracteristicas_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_contents_usosCaracteristicas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Use Features',
        additional_columns=['esRequerida', 'modoDeUso', 'titulosCaracteristicasUsadas'],
        label='Usa Caracteristicas',
        represents_aggregation=True,
        description2='Artefact Features used in the Business Process Step, to Create, Read, Update, Delete or Link.',
        multiValued=1,
        owner_class_name="BPDPasoMinimo",
        expression="context.objectValues(['BPDUsoCaracteristica'])",
        computed_types=['BPDUsoCaracteristica'],
        non_framework_elements=False,
        description='Caracteristicas de Artefactos que se usan en el Paso del Proceso de Negocio, para Crear, Leer, Actualizar, Eliminar y Enlazar.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoMinimo_schema = getattr(BPDProgramable, 'schema', Schema(())).copy() + \
    getattr(BPDArquetipoReferenciable, 'schema', Schema(())).copy() + \
    getattr(BPDPasoConRestriccionesTiempo, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoMinimo(OrderedBaseFolder, BPDProgramable, BPDArquetipoReferenciable, BPDPasoConRestriccionesTiempo):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDProgramable,'__implements__',()),) + (getattr(BPDArquetipoReferenciable,'__implements__',()),) + (getattr(BPDPasoConRestriccionesTiempo,'__implements__',()),)



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



    allowed_content_types = ['BPDUsoArtefacto', 'BPDUsoCaracteristica'] + list(getattr(BPDProgramable, 'allowed_content_types', [])) + list(getattr(BPDArquetipoReferenciable, 'allowed_content_types', [])) + list(getattr(BPDPasoConRestriccionesTiempo, 'allowed_content_types', []))

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

    schema = BPDPasoMinimo_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDPasoMinimo

##code-section module-footer #fill in your manual code here
##/code-section module-footer



