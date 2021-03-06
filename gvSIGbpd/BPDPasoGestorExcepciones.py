# -*- coding: utf-8 -*-
#
# File: BPDPasoGestorExcepciones.py
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
        name='titulosPasosAnterioresEnCasoExcepcion',
        widget=ComputedField._properties['widget'](
            label="Alternativo o Excepcion de Pasos",
            label2="Alternative or Exception for Steps",
            description="Pasos a los que sigue este paso como flujo alternativo, o en caso de excepcion.",
            description2="Steps preceding this step, as an alternate flow or exceptional condition.",
            label_msgid='gvSIGbpd_BPDPasoGestorExcepciones_attr_titulosPasosAnterioresEnCasoExcepcion_label',
            description_msgid='gvSIGbpd_BPDPasoGestorExcepciones_attr_titulosPasosAnterioresEnCasoExcepcion_help',
            i18n_domain='gvSIGbpd',
        ),
        exclude_from_values_paragraph="True",
        description="Pasos a los que sigue este paso como flujo alternativo, o en caso de excepcion.",
        duplicates="0",
        label2="Alternative or Exception for Steps",
        ea_localid="295",
        derived="0",
        collection="false",
        styleex="volatile=0;",
        description2="Steps preceding this step, as an alternate flow or exceptional condition.",
        ea_guid="{2F0C5F56-475A-4cd0-ADD8-15A25D7D7400}",
        exclude_from_values_form="True",
        label="Alternativo o Excepcion de Pasos",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPasoGestorExcepciones",
        expression="', '.join( [a.Title() for a in context.getPasosOriginandoExcepcion()])",
        computed_types="string"
    ),

    RelationField(
        name='pasosOriginandoExcepcion',
        inverse_relation_label="Pasos Alternativos o en caso de Excepcion",
        containment="Unspecified",
        inverse_relation_description="Pasos que se ejecutan como alternativa al flujo principal de pasos siguientes, o cuando surje una condicion excepcional.",
        description="Pasos a los que sigue este paso como flujo alternativo, o en caso de excepcion.",
        relationship='BPDPasosOriginandoExcepcion',
        inverse_relation_field_name='pasosSiguientesEnCasoExcepcion',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Alternative or Exception for Steps",
        inverse_relation_description2="Steps that will execute as an alternative to the main flow of next steps, or when an exceptional condition arises.",
        widget=ReferenceBrowserWidget(
            label="Pasos anteriores en caso excepcion o flujo alternativo",
            label2="Alternative or Exception for Steps",
            description="Pasos a los que sigue este paso como flujo alternativo, o en caso de excepcion.",
            description2="Steps preceding this step, as an alternate flow or exceptional condition.",
            label_msgid='gvSIGbpd_BPDPasoGestorExcepciones_rel_pasosOriginandoExcepcion_label',
            description_msgid='gvSIGbpd_BPDPasoGestorExcepciones_rel_pasosOriginandoExcepcion_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Pasos anteriores en caso excepcion o flujo alternativo",
        description2="Steps preceding this step, as an alternate flow or exceptional condition.",
        multiValued=1,
        inverse_relation_label2="Alternative next steps or on Exception",
        inverse_relationship='BPDPasosSiguientesEnCasoExcepcion',
        write_permission='Modify portal content',
        additional_columns=['detallesPaso']
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoGestorExcepciones_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoGestorExcepciones:
    """
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'BPDPasoGestorExcepciones'

    meta_type = 'BPDPasoGestorExcepciones'
    portal_type = 'BPDPasoGestorExcepciones'
    allowed_content_types = []
    filter_content_types             = 0
    global_allow                     = 1
    #content_icon = 'BPDPasoGestorExcepciones.gif'
    immediate_view                   = 'base_view'
    default_view                     = 'base_view'
    suppl_views                      = ()
    typeDescription                  = "Incorpora la capacidad de servir como paso de continuacion alternativo de un paso anterior en que no se ha cumplido la condicion, o se ha agotado el plazo, o se ha dado alguna otra condicion excepcional."
    typeDescMsgId                    =  'gvSIGbpd_BPDPasoGestorExcepciones_help'
    archetype_name2                  = ''
    typeDescription2                 = ''''''
    archetype_name_msgid             = 'gvSIGbpd_BPDPasoGestorExcepciones_label'
    factory_methods                  = None
    factory_enablers                 = None
    propagate_delete_impact_to       = None

    _at_rename_after_creation = True

    schema = BPDPasoGestorExcepciones_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

# end of class BPDPasoGestorExcepciones

##code-section module-footer #fill in your manual code here
##/code-section module-footer



