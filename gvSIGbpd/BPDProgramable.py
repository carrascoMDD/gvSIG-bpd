# -*- coding: utf-8 -*-
#
# File: BPDProgramable.py
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
        name='sumarioProgramas',
        widget=ComputedField._properties['widget'](
            label="Resumenes de Programas",
            label2="Programs Summary",
            description="Un resumen de los tipos del programas y el  codigo fuente de los programas especificados en este elemento.",
            description2="A summary of the programs types and  source codes of the programs specified for this element.",
            label_msgid='gvSIGbpd_BPDProgramable_attr_sumarioProgramas_label',
            description_msgid='gvSIGbpd_BPDProgramable_attr_sumarioProgramas_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Un resumen de los tipos del programas y el  codigo fuente de los programas especificados en este elemento.",
        duplicates="0",
        label2="Programs Summary",
        ea_localid="627",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="A summary of the programs types and  source codes of the programs specified for this element.",
        ea_guid="{B50FFB52-5276-4846-931D-747DFFAB639C}",
        exclude_from_values_form="True",
        scale="0",
        label="Resumenes de Programas",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDProgramable",
        expression="'; '.join( [ '%s:%s' %(( aPrg.getTipoPrograma() or ''), ( aPrg.getFuentePrograma() or ''))[:64] for aPrg in context.getProgramas()])",
        computed_types="string",
        exclude_from_copyconfig="True",
        exclude_from_exportconfig="True"
    ),

    ComputedField(
        name='programas',
        widget=ComputedWidget(
            label="Programas",
            label2="Programs",
            description="Programas implementando el comportamiento de este elemento.",
            description2="Programs implementing the behavior of this element.",
            label_msgid='gvSIGbpd_BPDProgramable_contents_programas_label',
            description_msgid='gvSIGbpd_BPDProgramable_contents_programas_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Programs',
        additional_columns=['tipoPrograma', 'fuentePrograma'],
        label='Programas',
        represents_aggregation=True,
        description2='Programs implementing the behavior of this element.',
        multiValued=1,
        owner_class_name="BPDProgramable",
        expression="context.objectValues(['BPDPrograma'])",
        computed_types=['BPDPrograma'],
        non_framework_elements=False,
        description='Programas implementando el comportamiento de este elemento.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDProgramable_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDProgramable:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = ['BPDPrograma']
    _at_rename_after_creation = True

    schema = BPDProgramable_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDProgramable

##code-section module-footer #fill in your manual code here
##/code-section module-footer



