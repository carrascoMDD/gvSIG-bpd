# -*- coding: utf-8 -*-
#
# File: BPDConDatosDePrueba.py
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

__author__ = """acv <gvSIGbpd@gvSIG.org>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='sumarioDatosDePruebas',
        widget=ComputedField._properties['widget'](
            label="Resumen del Resoluciones de Datos",
            label2="Data Resolutions Summary",
            description="Un resumen de las resoluciones de items de informacion definidos para este elemento.",
            description2="A summary of the data item resolutions defined for this element.",
            label_msgid='gvSIGbpd_BPDConDatosDePrueba_attr_sumarioDatosDePruebas_label',
            description_msgid='gvSIGbpd_BPDConDatosDePrueba_attr_sumarioDatosDePruebas_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Un resumen de las resoluciones de items de informacion definidos para este elemento.",
        duplicates="0",
        label2="Data Resolutions Summary",
        ea_localid="640",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="A summary of the data item resolutions defined for this element.",
        ea_guid="{0EB377F4-303D-4a84-9764-61C516A9B15F}",
        exclude_from_values_form="True",
        scale="0",
        label="Resumen del Resoluciones de Datos",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDConDatosDePrueba",
        expression="'; '.join( [ '%s:%s' %(( aDatPru.getTipoPrograma() or ''), ( aDatPru.getFuentePrograma() or ''))[:64] for aDatPru in context.getDatosPruebas()])",
        computed_types="string",
        exclude_from_copyconfig="True",
        exclude_from_exportconfig="True"
    ),

    RelationField(
        name='datosDePruebas',
        inverse_relation_label="Datos de Pruebas",
        inverse_relation_description="Datos de Pruebas definidos para este elemento de proceso en varios Casos de Pruebas.",
        description="Elementos del Proceso de Negocio para los que se definen Datos de Prueba en el Caso de Prueba.",
        relationship='DatosDePrueba_ElementosProceso',
        inverse_relation_field_name='elementosDeProceso',
        inverse_relation_label2="Test Data",
        label2="Process Elements",
        inverse_relation_description2="Test Data defined for this process element in various Test Cases.",
        widget=ReferenceBrowserWidget(
            label="Elementos de Proceso",
            label2="Process Elements",
            description="Elementos del Proceso de Negocio para los que se definen Datos de Prueba en el Caso de Prueba.",
            description2="Business Process elements for which Test Data is defined in the Test Case.",
            label_msgid='gvSIGbpd_BPDConDatosDePrueba_rel_datosDePruebas_label',
            description_msgid='gvSIGbpd_BPDConDatosDePrueba_rel_datosDePruebas_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Elementos de Proceso",
        description2="Business Process elements for which Test Data is defined in the Test Case.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='ElementosProceso_DatosDePrueba',
        owner_class_name="BPDConDatosDePrueba",
        dependency_supplier=True
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDConDatosDePrueba_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDConDatosDePrueba:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDConDatosDePrueba_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDConDatosDePrueba

##code-section module-footer #fill in your manual code here
##/code-section module-footer



