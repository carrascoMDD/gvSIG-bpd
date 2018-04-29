# -*- coding: utf-8 -*-
#
# File: BPDPasoConAnteriores.py
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
        name='titulosPasosAnteriores',
        widget=ComputedField._properties['widget'](
            label="Pasos Anteriores",
            label2="Previous Steps",
            description="Pasos que se ejecutan antes de este paso. Este paso se ejecuta tras completarse alguno de sus pasos anteriores.",
            description2="Steps that execute before this step. This step will execute after the completion of any of its previous steps.",
            label_msgid='gvSIGbpd_BPDPasoConAnteriores_attr_titulosPasosAnteriores_label',
            description_msgid='gvSIGbpd_BPDPasoConAnteriores_attr_titulosPasosAnteriores_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Pasos que se ejecutan antes de este paso. Este paso se ejecuta tras completarse alguno de sus pasos anteriores.",
        duplicates="0",
        label2="Previous Steps",
        ea_localid="257",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Steps that execute before this step. This step will execute after the completion of any of its previous steps.",
        containment="Not Specified",
        ea_guid="{F5A864F4-B3F6-484a-B71D-608CCBB08FEB}",
        position="0",
        owner_class_name="BPDPasoConAnteriores",
        label="Pasos Anteriores",
        expression="', '.join( [a.Title() for a in context.getPasosAnteriores()])",
        exclude_from_values_form="True"
    ),

    RelationField(
        name='pasosAnteriores',
        inverse_relation_label="Pasos Siguientes",
        inverse_relation_description="Pasos que se ejecutaran tras completarse este paso.",
        description="Pasos que se ejecutan antes de este paso. Este paso se ejecuta tras completarse alguno de sus pasos anteriores.",
        relationship='PasosAnteriores',
        label2="Previous Steps",
        widget=ReferenceBrowserWidget(
            label="Pasos Anteriores",
            label2="Previous Steps",
            description="Pasos que se ejecutan antes de este paso. Este paso se ejecuta tras completarse alguno de sus pasos anteriores.",
            description2="Steps that execute before this step. This step will execute after the completion of any of its previous steps.",
            label_msgid='gvSIGbpd_BPDPasoConAnteriores_rel_pasosAnteriores_label',
            description_msgid='gvSIGbpd_BPDPasoConAnteriores_rel_pasosAnteriores_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Steps that execute before this step. This step will execute after the completion of any of its previous steps.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Next Steps",
        dependency_supplier=True,
        inverse_relation_field_name='pasosSiguientes',
        inverse_relation_description2="Steps that will execute after the completion of this step.",
        additional_columns=['detallesPaso'],
        write_permission='Modify portal content',
        label="Pasos Anteriores",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='PasosSiguientes'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoConAnteriores_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoConAnteriores:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDPasoConAnteriores_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDPasoConAnteriores

##code-section module-footer #fill in your manual code here
##/code-section module-footer



