# -*- coding: utf-8 -*-
#
# File: BPDPrePostCondicional.py
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
        name='preCondiciones',
        widget=ComputedWidget(
            label="Pre Condiciones",
            label2="Pre-Conditions",
            description="Condiciones que han de cumplirse para que pueda considerarse valido el elemento pre condicionado.",
            description2="Conditions that must hold true for the pre-conditioned element to be valid.",
            label_msgid='gvSIGbpd_BPDPrePostCondicional_contents_preCondiciones_label',
            description_msgid='gvSIGbpd_BPDPrePostCondicional_contents_preCondiciones_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Pre-Conditions',
        additional_columns=['condition'],
        label='Pre Condiciones',
        represents_aggregation=True,
        description2='Conditions that must hold true for the pre-conditioned element to be valid.',
        multiValued=1,
        owner_class_name="BPDPrePostCondicional",
        expression="context.objectValues(['BPDPreCondicion'])",
        computed_types=['BPDPreCondicion'],
        non_framework_elements=False,
        description='Condiciones que han de cumplirse para que pueda considerarse valido el elemento pre condicionado.'
    ),

    ComputedField(
        name='postCondiciones',
        widget=ComputedWidget(
            label="Post Condiciones",
            label2="Post-Conditions",
            description="Condiciones que han de cumplirse para que pueda considerarse valido el elemento post condicionado.",
            description2="Conditions that must hold true for the post-conditioned element to be valid.",
            label_msgid='gvSIGbpd_BPDPrePostCondicional_contents_postCondiciones_label',
            description_msgid='gvSIGbpd_BPDPrePostCondicional_contents_postCondiciones_help',
            i18n_domain='gvSIGbpd',
        ),
        contains_collections=False,
        label2='Post-Conditions',
        additional_columns=['condition'],
        label='Post Condiciones',
        represents_aggregation=True,
        description2='Conditions that must hold true for the post-conditioned element to be valid.',
        multiValued=1,
        owner_class_name="BPDPrePostCondicional",
        expression="context.objectValues(['BPDPostCondicion'])",
        computed_types=['BPDPostCondicion'],
        non_framework_elements=False,
        description='Condiciones que han de cumplirse para que pueda considerarse valido el elemento post condicionado.'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPrePostCondicional_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPrePostCondicional:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = ['BPDPreCondicion', 'BPDPostCondicion']
    _at_rename_after_creation = True

    schema = BPDPrePostCondicional_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDPrePostCondicional

##code-section module-footer #fill in your manual code here
##/code-section module-footer



