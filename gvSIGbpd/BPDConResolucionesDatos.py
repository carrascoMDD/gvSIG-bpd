# -*- coding: utf-8 -*-
#
# File: BPDConResolucionesDatos.py
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
from Products.gvSIGbpd.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='sumarioResolucionesDatos',
        widget=ComputedField._properties['widget'](
            label="Resumen del Resoluciones de Datos",
            label2="Data Resolutions Summary",
            description="Un resumen de las resoluciones de items de informacion definidos para este elemento.",
            description2="A summary of the data item resolutions defined for this element.",
            label_msgid='gvSIGbpd_BPDConResolucionesDatos_attr_sumarioResolucionesDatos_label',
            description_msgid='gvSIGbpd_BPDConResolucionesDatos_attr_sumarioResolucionesDatos_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Un resumen de las resoluciones de items de informacion definidos para este elemento.",
        duplicates="0",
        label2="Data Resolutions Summary",
        ea_localid="626",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="A summary of the data item resolutions defined for this element.",
        ea_guid="{A7897045-42A9-4aae-A521-DAC4E881AC05}",
        exclude_from_values_form="True",
        scale="0",
        label="Resumen del Resoluciones de Datos",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDConResolucionesDatos",
        expression="'; '.join( [ '%s:%s' %(( aResDat.getTipoPrograma() or ''), ( aResDat.getFuentePrograma() or ''))[:64] for aResDat in context.getResolucionesDatos()])",
        computed_types="string",
        exclude_from_copyconfig="True",
        exclude_from_exportconfig="True"
    ),

    ComputedField(
        name='resolucionesDatos',
        widget=ComputedWidget(
            label="Resoluciones de Datos",
            label2="Data Item Resolutions",
            description="Resolucion de items de informacion con valores actuales de datos.",
            description2="Resolution of data items with actual data values.",
            label_msgid='gvSIGbpd_BPDConResolucionesDatos_contents_resolucionesDatos_label',
            description_msgid='gvSIGbpd_BPDConResolucionesDatos_contents_resolucionesDatos_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Data Item Resolutions',
        additional_columns=['sumarioPrograma'],
        label='Resoluciones de Datos',
        represents_aggregation=True,
        description2='Resolution of data items with actual data values.',
        multiValued=1,
        owner_class_name="BPDConResolucionesDatos",
        expression="context.objectValues(['BPDResolucionDatos'])",
        computed_types=['BPDResolucionDatos'],
        non_framework_elements=False,
        description='Resolucion de items de informacion con valores actuales de datos.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDConResolucionesDatos_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDConResolucionesDatos:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = ['BPDResolucionDatos']
    _at_rename_after_creation = True

    schema = BPDConResolucionesDatos_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDConResolucionesDatos

##code-section module-footer #fill in your manual code here
##/code-section module-footer



