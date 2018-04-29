# -*- coding: utf-8 -*-
#
# File: BPDPasoMinimo.py
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
from Products.gvSIGbpd.BPDArquetipoReferenciable import BPDArquetipoReferenciable
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

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
        name='reglasDeNegocioAplicadas',
        inverse_relation_label="Pasos dirigidos",
        inverse_relation_description="Pasos de Procesos de Negocio donde se aplica la Regla de Negocio",
        description="Reglas de Negocio aplicadas durante la ejecucion del Paso.",
        relationship='ReglasDeNegocioAplicadas',
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
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label="Reglas de Negocio aplicadas",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='PasosAplicandoLaRegla',
        owner_class_name="BPDPasoMinimo"
    ),

    RelationField(
        name='herramientasAplicadas',
        inverse_relation_label="Pasos Asistidos",
        inverse_relation_description="Pasos de procesos de negocio donde se aplica la Herramienta.",
        description="Herramientas a utilizar para ejecutar el paso de proceso de negocio o manejar los artefactos usados.",
        relationship='HerramientasAplicadas',
        label2="Applied Tools",
        widget=ReferenceBrowserWidget(
            label="Herramientas aplicadas",
            label2="Applied Tools",
            description="Herramientas a utilizar para ejecutar el paso de proceso de negocio o manejar los artefactos usados.",
            description2="Tools to apply in the execution of the business process step, or to manipulate the used artefacts.",
            label_msgid='gvSIGbpd_BPDPasoMinimo_rel_herramientasAplicadas_label',
            description_msgid='gvSIGbpd_BPDPasoMinimo_rel_herramientasAplicadas_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Tools to apply in the execution of the business process step, or to manipulate the used artefacts.",
        inverse_relation_label2="Assisted Steps",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='pasosAsistidos',
        inverse_relation_description2="Business process steps applying the tool.",
        additional_columns=['codigo', 'estado', 'nivelDeImposicion'],
        label="Herramientas aplicadas",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='PasosAsistidos',
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
        position="1",
        owner_class_name="BPDPasoMinimo",
        expression="context.getPropietario().Title()",
        computed_types="string"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoMinimo_schema = getattr(BPDArquetipoReferenciable, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoMinimo(OrderedBaseFolder, BPDArquetipoReferenciable):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(OrderedBaseFolder,'__implements__',()),) + (getattr(BPDArquetipoReferenciable,'__implements__',()),)

    allowed_content_types = [] + list(getattr(BPDArquetipoReferenciable, 'allowed_content_types', []))

    actions =  (


       {'action': "string:${object_url}/sharing",
        'category': "object",
        'id': 'local_roles',
        'name': 'Sharing',
        'permissions': ("Manage properties",),
        'condition': 'python:1'
       },


       {'action': "string:$object_url/content_status_history",
        'category': "object",
        'id': 'content_status_history',
        'name': 'State',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/MDDExport",
        'category': "object",
        'id': 'mddexport',
        'name': 'Export',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/Textual",
        'category': "object",
        'id': 'view',
        'name': 'View',
        'permissions': ("View",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/Editar",
        'category': "object",
        'id': 'edit',
        'name': 'Edit',
        'permissions': ("Modify portal content",),
        'condition': 'python:1'
       },


       {'action': "string:${object_url}/TextualRest",
        'category': "object",
        'id': 'textual_rest',
        'name': 'TextualRest',
        'permissions': ("View",),
        'condition': 'python:1'
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



