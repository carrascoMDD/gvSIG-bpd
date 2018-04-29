# -*- coding: utf-8 -*-
#
# File: BPDPasoConExcepciones.py
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
        name='titulosPasosSiguientesEnCasoExcepcion',
        widget=ComputedField._properties['widget'](
            label="Pasos Alternativos o Excepcion",
            label2="Alternate or Exceptional Next Steps",
            description="Pasos que se ejecutan como alternativa al flujo principal de pasos siguientes, o cuando surje una condicion excepcional.",
            description2="Steps that will execute as an alternative to the main flow of next steps, or when an exceptional condition arises.",
            label_msgid='gvSIGbpd_BPDPasoConExcepciones_attr_titulosPasosSiguientesEnCasoExcepcion_label',
            description_msgid='gvSIGbpd_BPDPasoConExcepciones_attr_titulosPasosSiguientesEnCasoExcepcion_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Pasos que se ejecutan como alternativa al flujo principal de pasos siguientes, o cuando surje una condicion excepcional.",
        duplicates="0",
        label2="Alternate or Exceptional Next Steps",
        ea_localid="258",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Steps that will execute as an alternative to the main flow of next steps, or when an exceptional condition arises.",
        ea_guid="{1FA73A97-84BC-4683-B4A4-7C409954B00B}",
        exclude_from_values_form="True",
        label="Pasos Alternativos o Excepcion",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPasoConExcepciones",
        expression="', '.join( [a.Title() for a in context.getPasosSiguientesEnCasoExcepcion()])",
        computed_types="string"
    ),

    RelationField(
        name='pasosSiguientesEnCasoExcepcion',
        inverse_relation_label="Pasos anteriores en caso excepcion o flujo alternativo",
        inverse_relation_description="Pasos a los que sigue este paso como flujo alternativo, o en caso de excepcion.",
        description="Pasos que se ejecutan como alternativa al flujo principal de pasos siguientes, o cuando surje una condicion excepcional.",
        relationship='BPDPasosSiguientesEnCasoExcepcion',
        label2="Alternative next steps or on Exception",
        widget=ReferenceBrowserWidget(
            label="Pasos Alternativos o en caso de Excepcion",
            label2="Alternative next steps or on Exception",
            description="Pasos que se ejecutan como alternativa al flujo principal de pasos siguientes, o cuando surje una condicion excepcional.",
            description2="Steps that will execute as an alternative to the main flow of next steps, or when an exceptional condition arises.",
            label_msgid='gvSIGbpd_BPDPasoConExcepciones_rel_pasosSiguientesEnCasoExcepcion_label',
            description_msgid='gvSIGbpd_BPDPasoConExcepciones_rel_pasosSiguientesEnCasoExcepcion_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Steps that will execute as an alternative to the main flow of next steps, or when an exceptional condition arises.",
        inverse_relation_label2="Alternative or Exception for Steps",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='pasosOriginandoExcepcion',
        inverse_relation_description2="Steps preceding this step, as an alternate flow or exceptional condition.",
        additional_columns=['detallesPaso'],
        label="Pasos Alternativos o en caso de Excepcion",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDPasosOriginandoExcepcion',
        owner_class_name="BPDPasoConExcepciones"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoConExcepciones_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoConExcepciones:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDPasoConExcepciones_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDPasoConExcepciones

##code-section module-footer #fill in your manual code here
##/code-section module-footer



