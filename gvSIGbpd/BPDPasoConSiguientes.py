# -*- coding: utf-8 -*-
#
# File: BPDPasoConSiguientes.py
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

__author__ = """Antonio Carrasco Valero (Model Driven Development sl) <gvSIGbpd@gvSIG.org>"""
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
        name='titulosPasosSiguientes',
        widget=ComputedField._properties['widget'](
            label="Pasos Siguientes",
            label2="Next Steps",
            description="Pasos que se ejecutaran tras completarse este paso.",
            description2="Steps that will execute after the completion of this step.",
            label_msgid='gvSIGbpd_BPDPasoConSiguientes_attr_titulosPasosSiguientes_label',
            description_msgid='gvSIGbpd_BPDPasoConSiguientes_attr_titulosPasosSiguientes_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Pasos que se ejecutaran tras completarse este paso.",
        duplicates="0",
        label2="Next Steps",
        ea_localid="294",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Steps that will execute after the completion of this step.",
        ea_guid="{60BCA907-2644-4f7d-B722-2938608EF8CD}",
        exclude_from_values_form="True",
        label="Pasos Siguientes",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPasoConSiguientes",
        expression="', '.join( [a.Title() for a in context.getPasosSiguientes()])",
        computed_types="string"
    ),

    RelationField(
        name='pasosSiguientes',
        inverse_relation_label="Pasos Anteriores",
        inverse_relation_description="Pasos que se ejecutan antes de este paso. Este paso se ejecuta tras completarse alguno de sus pasos anteriores.",
        description="Pasos que se ejecutaran tras completarse este paso.",
        relationship='BPDPasosSiguientes',
        label2="Next Steps",
        widget=ReferenceBrowserWidget(
            label="Pasos Siguientes",
            label2="Next Steps",
            description="Pasos que se ejecutaran tras completarse este paso.",
            description2="Steps that will execute after the completion of this step.",
            label_msgid='gvSIGbpd_BPDPasoConSiguientes_rel_pasosSiguientes_label',
            description_msgid='gvSIGbpd_BPDPasoConSiguientes_rel_pasosSiguientes_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Steps that will execute after the completion of this step.",
        inverse_relation_label2="Previous Steps",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='pasosAnteriores',
        inverse_relation_description2="Steps that execute before this step. This step will execute after the completion of any of its previous steps.",
        additional_columns=['detallesPaso'],
        label="Pasos Siguientes",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDPasosAnteriores',
        owner_class_name="BPDPasoConSiguientes"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoConSiguientes_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoConSiguientes:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDPasoConSiguientes_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDPasoConSiguientes

##code-section module-footer #fill in your manual code here
##/code-section module-footer



