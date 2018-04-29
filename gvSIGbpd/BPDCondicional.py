# -*- coding: utf-8 -*-
#
# File: BPDCondicional.py
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

__author__ = """acv <gvSIGbpd@gvSIG.org>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.gvSIGbpd.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='condiciones',
        widget=ComputedWidget(
            label="Condiciones",
            label2="Conditions",
            description="Condiciones que restringen la validad del elemento condicional.",
            description2="Conditions that restrict the validity of the conditional element.",
            label_msgid='gvSIGbpd_BPDCondicional_contents_condiciones_label',
            description_msgid='gvSIGbpd_BPDCondicional_contents_condiciones_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Conditions',
        additional_columns=['condicion', 'sumarioProgramas'],
        label='Condiciones',
        represents_aggregation=True,
        description2='Conditions that restrict the validity of the conditional element.',
        multiValued=1,
        owner_class_name="BPDCondicional",
        expression="context.objectValues(['BPDCondicion'])",
        computed_types=['BPDCondicion'],
        non_framework_elements=False,
        description='Condiciones que restringen la validad del elemento condicional.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDCondicional_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDCondicional:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = ['BPDCondicion']
    _at_rename_after_creation = True

    schema = BPDCondicional_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDCondicional

##code-section module-footer #fill in your manual code here
##/code-section module-footer



