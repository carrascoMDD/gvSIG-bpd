# -*- coding: utf-8 -*-
#
# File: BPDConTraducciones.py
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
        name='esTraduccionInterna',
        widget=ComputedField._properties['widget'](
            label="Es Traduccion (uso interno)",
            label2="Is Translation (internal)",
            description="Si Verdadero, entonces el elemento es una traduccion de algun otro elemento en un idioma canonico.",
            description2="If True, then the element is a translation of another element in a canonical language.",
            label_msgid='gvSIGbpd_BPDConTraducciones_attr_esTraduccionInterna_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_attr_esTraduccionInterna_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Si Verdadero, entonces el elemento es una traduccion de algun otro elemento en un idioma canonico.",
        duplicates="0",
        label2="Is Translation (internal)",
        ea_localid="300",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="If True, then the element is a translation of another element in a canonical language.",
        ea_guid="{972AFBB2-DD9C-41a4-9858-7CE2F4DB88BA}",
        write_permission='Modify portal content',
        scale="0",
        default="False",
        label="Es Traduccion (uso interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDConTraducciones",
        expression="context.fDerive_EsTraduccionInterna()",
        computed_types="boolean",
        exclude_from_copyconfig="True"
    ),

    StringField(
        name='codigoIdiomaInterno',
        widget=StringWidget(
            label="Codigo de Idioma (uso interno de la aplicacion)",
            label2="Language Code (application internal)",
            description="Codigo del idioma en que se ha creado el contenido del elemento. Es manejado directamente por la aplicacion. No es un dato de usuario.",
            description2="Code of the language used to edit the element contents. It is managed directly by the application. It is not a user data element.",
            label_msgid='gvSIGbpd_BPDConTraducciones_attr_codigoIdiomaInterno_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_attr_codigoIdiomaInterno_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Codigo del idioma en que se ha creado el contenido del elemento. Es manejado directamente por la aplicacion. No es un dato de usuario.",
        duplicates="0",
        label2="Language Code (application internal)",
        ea_localid="255",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        is_language="True",
        description2="Code of the language used to edit the element contents. It is managed directly by the application. It is not a user data element.",
        ea_guid="{B7601699-AE23-4127-B9B2-1E2A8D4C064B}",
        write_permission='Modify portal content',
        scale="0",
        label="Codigo de Idioma (uso interno de la aplicacion)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDConTraducciones"
    ),

    StringField(
        name='camposPendientesTraduccionInterna',
        is_fields_pending_translation="True",
        widget=StringWidget(
            label="Campos Pendientes de traducir (interno)",
            label2="Translation Pending fields (internal)",
            description="Campos traducibles del elemento, que aun no han sido traducidos.",
            description2="Translatable fields in the element,  not translated yet.",
            label_msgid='gvSIGbpd_BPDConTraducciones_attr_camposPendientesTraduccionInterna_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_attr_camposPendientesTraduccionInterna_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Campos traducibles del elemento, que aun no han sido traducidos.",
        duplicates="0",
        label2="Translation Pending fields (internal)",
        ea_localid="301",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="Translatable fields in the element,  not translated yet.",
        ea_guid="{F4C9ED97-040A-4337-AF88-EBF4B93E896F}",
        write_permission='Modify portal content',
        scale="0",
        label="Campos Pendientes de traducir (interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDConTraducciones"
    ),

    StringField(
        name='camposPendientesRevisionInterna',
        widget=StringWidget(
            label="Campos pendiente de Revisar (interno)",
            label2="Revision Pending fields (internal)",
            description="Campos traducibles del elemento, que han sido traducidos, y cuya traduccion aun no ha sido revisada.",
            description2="Translatable fields in the element,  that have been translated, but not reviewed yet.",
            label_msgid='gvSIGbpd_BPDConTraducciones_attr_camposPendientesRevisionInterna_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_attr_camposPendientesRevisionInterna_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Campos traducibles del elemento, que han sido traducidos, y cuya traduccion aun no ha sido revisada.",
        duplicates="0",
        label2="Revision Pending fields (internal)",
        ea_localid="302",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="Translatable fields in the element,  that have been translated, but not reviewed yet.",
        ea_guid="{1CC69390-39AF-493d-8E3D-7221897C31C9}",
        is_fields_pending_revision="True",
        write_permission='Modify portal content',
        scale="0",
        label="Campos pendiente de Revisar (interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDConTraducciones"
    ),

    RelationField(
        name='originalDeTraduccion',
        inverse_relation_label="Elementos Traducidos",
        containment="Unspecified",
        inverse_relation_description="Traducciones de este elemento a otros idiomas.",
        description="El elemento original de esta traduccion a otro idioma.",
        relationship='BPDOriginalDeTraduccion',
        inverse_relation_field_name='elementosTraducidos',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="Original of this translation",
        inverse_relation_description2="Translations of this element into other languages.",
        widget=ReferenceBrowserWidget(
            label="Original de esta Traduccion",
            label2="Original of this translation",
            description="El elemento original de esta traduccion a otro idioma.",
            description2="The original element of this translation into a different language.",
            label_msgid='gvSIGbpd_BPDConTraducciones_rel_originalDeTraduccion_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_rel_originalDeTraduccion_help',
            i18n_domain='gvSIGbpd',
        ),
        label="Original de esta Traduccion",
        description2="The original element of this translation into a different language.",
        multiValued=0,
        inverse_relation_label2="Translated Elements",
        inverse_relationship='BPDElementosTraducidos',
        write_permission='Modify portal content'
    ),

    StringField(
        name='esTraduccionInternaAlmacenada',
        widget=SelectionWidget(
            label="Es Traduccion (uso interno)  Almacenada",
            label2="Is Translation (internal) Stored",
            description="Si Verdadero, entonces el elemento es una traduccion de algun otro elemento en un idioma canonic. Almacenado en este elemento. No se usa a menos que sea un elemento raiz, como Organizacion, u otro tipo sin raiz Organizacion.",
            description2="If True, then the element is a translation of another element in a canonical language. Stored in this element. Unused unless the element is a root, as an Organization, or has noOrganization  root.",
            label_msgid='gvSIGbpd_BPDConTraducciones_attr_esTraduccionInternaAlmacenada_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_attr_esTraduccionInternaAlmacenada_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Si Verdadero, entonces el elemento es una traduccion de algun otro elemento en un idioma canonic. Almacenado en este elemento. No se usa a menos que sea un elemento raiz, como Organizacion, u otro tipo sin raiz Organizacion.",
        vocabulary=[ 'Segun Contedor', 'No Traducible', 'Traduccion', 'Canonica',  ],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDConTraducciones_attr_esTraduccionInternaAlmacenada_option_Segun Contedor', 'gvSIGbpd_BPDConTraducciones_attr_esTraduccionInternaAlmacenada_option_No Traducible', 'gvSIGbpd_BPDConTraducciones_attr_esTraduccionInternaAlmacenada_option_Traduccion', 'gvSIGbpd_BPDConTraducciones_attr_esTraduccionInternaAlmacenada_option_Canonica'],
        label2="Is Translation (internal) Stored",
        ea_localid="588",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="If True, then the element is a translation of another element in a canonical language. Stored in this element. Unused unless the element is a root, as an Organization, or has noOrganization  root.",
        ea_guid="{EB9AE814-AFC7-4ed5-8A03-94DEC8CACEC0}",
        vocabulary2=[  'By Container', 'Not Translatable', 'Translation',  'Canonical',],
        scale="0",
        default="Segun Contedor",
        write_permission='Modify portal content',
        label="Es Traduccion (uso interno)  Almacenada",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDConTraducciones",
        exclude_from_exportconfig="True",
        exclude_from_copyconfig="""True
        True"""
    ),

    RelationField(
        name='traduccionesDeIdiomaCanonico',
        inverse_relation_label="En Idioma Canonico",
        containment="Unspecified",
        inverse_relation_description="El Original de este modelo en su Idioma Canonico, del que se derivan todas las traducciones a otros Idiomas.",
        description="Traducciones del Modelo en Idioma Canonico a otros Idiomas.",
        relationship='BPDEnIdiomaCanonicoDe',
        inverse_relation_field_name='idiomaCanonico',
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        label2="In Canonical Language For",
        inverse_relation_description2="The Original of this model in its Original Language, from where all other translations are derived from.",
        widget=ReferenceBrowserWidget(
            label="En Idioma Canonico De",
            label2="In Canonical Language For",
            description="Traducciones del Modelo en Idioma Canonico a otros Idiomas.",
            description2="Translations of the Model in Canonical Language into other Languages.",
            label_msgid='gvSIGbpd_BPDConTraducciones_rel_traduccionesDeIdiomaCanonico_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_rel_traduccionesDeIdiomaCanonico_help',
            i18n_domain='gvSIGbpd',
        ),
        label="En Idioma Canonico De",
        description2="Translations of the Model in Canonical Language into other Languages.",
        multiValued=1,
        inverse_relation_label2="In Canonical Language",
        inverse_relationship='BPDIdiomaCanonico',
        write_permission='Modify portal content'
    ),

    RelationField(
        name='elementosTraducidos',
        inverse_relation_label="Original de esta Traduccion",
        inverse_relation_description="El elemento original de esta traduccion a otro idioma.",
        description="Traducciones de este elemento a otros idiomas.",
        relationship='BPDElementosTraducidos',
        inverse_relation_field_name='originalDeTraduccion',
        inverse_relation_label2="Original of this translation",
        label2="Translated Elements",
        inverse_relation_description2="The original element of this translation into a different language.",
        widget=ReferenceBrowserWidget(
            label="Elementos Traducidos",
            label2="Translated Elements",
            description="Traducciones de este elemento a otros idiomas.",
            description2="Translations of this element into other languages.",
            label_msgid='gvSIGbpd_BPDConTraducciones_rel_elementosTraducidos_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_rel_elementosTraducidos_help',
            i18n_domain='gvSIGbpd',
        ),
        write_permission='Modify portal content',
        label="Elementos Traducidos",
        description2="Translations of this element into other languages.",
        multiValued=1,
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        containment="Unspecified",
        inverse_relationship='BPDOriginalDeTraduccion',
        owner_class_name="BPDConTraducciones",
        dependency_supplier=True
    ),

    RelationField(
        name='idiomaCanonico',
        inverse_relation_label="En Idioma Canonico De",
        inverse_relation_description="Traducciones del Modelo en Idioma Canonico a otros Idiomas.",
        description="El Original de este modelo en su Idioma Canonico, del que se derivan todas las traducciones a otros Idiomas.",
        relationship='BPDIdiomaCanonico',
        label2="In Canonical Language",
        widget=ReferenceBrowserWidget(
            label="En Idioma Canonico",
            label2="In Canonical Language",
            description="El Original de este modelo en su Idioma Canonico, del que se derivan todas las traducciones a otros Idiomas.",
            description2="The Original of this model in its Original Language, from where all other translations are derived from.",
            label_msgid='gvSIGbpd_BPDConTraducciones_rel_idiomaCanonico_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_rel_idiomaCanonico_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="The Original of this model in its Original Language, from where all other translations are derived from.",
        inverse_relation_label2="In Canonical Language For",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='traduccionesDeIdiomaCanonico',
        inverse_relation_description2="Translations of the Model in Canonical Language into other Languages.",
        label="En Idioma Canonico",
        multiValued=0,
        containment="Unspecified",
        inverse_relationship='BPDEnIdiomaCanonicoDe',
        owner_class_name="BPDConTraducciones"
    ),

    StringField(
        name='uidInterTraduccionesInterno',
        widget=StringWidget(
            label="Identificador Inter Traducciones (uso interno)",
            label2="Inter-Version identifier (internal)",
            description="Identificador compartido entre todas las traducciones del elemento, para uso interno de la aplicacion.",
            description2="Identifier shared by all translations of an element, used internally by the application.",
            label_msgid='gvSIGbpd_BPDConTraducciones_attr_uidInterTraduccionesInterno_label',
            description_msgid='gvSIGbpd_BPDConTraducciones_attr_uidInterTraduccionesInterno_help',
            i18n_domain='gvSIGbpd',
        ),
        ea_localid="594",
        description="Identificador compartido entre todas las traducciones del elemento, para uso interno de la aplicacion.",
        duplicates="0",
        label2="Inter-Version identifier (internal)",
        is_inter_translation="True",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Identifier shared by all translations of an element, used internally by the application.",
        ea_guid="{93C931F4-2835-4425-BE69-E0DF2F9D2094}",
        write_permission='Modify portal content',
        scale="0",
        label="Identificador Inter Traducciones (uso interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDConTraducciones"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDConTraducciones_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDConTraducciones:
    """
    """
    security = ClassSecurityInfo()


    # Versioning and Translation fields

    inter_translation_field = 'uidInterTraduccionesInterno'
    language_field = 'codigoIdiomaInterno'
    fields_pending_translation_field = 'camposPendientesTraduccionInterna'
    fields_pending_revision_field = 'camposPendientesRevisionInterna'



    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDConTraducciones_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDConTraducciones

##code-section module-footer #fill in your manual code here
##/code-section module-footer



