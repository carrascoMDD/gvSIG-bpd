# -*- coding: utf-8 -*-
#
# File: BPDConVersiones.py
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
from Products.Relations.field import RelationField
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='versionInterna',
        widget=ComputedField._properties['widget'](
            label="Version (uso interno)",
            label2="Version identifier (internal)",
            description="Identificador de version para uso interno de la aplicacion.",
            description2="Version identifier used internally by the application.",
            label_msgid='gvSIGbpd_BPDConVersiones_attr_versionInterna_label',
            description_msgid='gvSIGbpd_BPDConVersiones_attr_versionInterna_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Identificador de version para uso interno de la aplicacion.",
        duplicates="0",
        label2="Version identifier (internal)",
        ea_localid="254",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Version identifier used internally by the application.",
        ea_guid="{285124FC-4C3A-4c00-9645-4A026E460B11}",
        write_permission='Modify portal content',
        scale="0",
        is_version="True",
        label="Version (uso interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDConVersiones",
        expression="context.fDerive_VersionInterna()",
        computed_types="string"
    ),

    ComputedField(
        name='comentarioVersionInterna',
        widget=ComputedField._properties['widget'](
            label="Comentario de Version (uso interno)",
            label2="Version Comment (internal)",
            description="Comentario a la version para uso interno de la aplicacion.",
            description2="Comments on the Version used internally by the application.",
            label_msgid='gvSIGbpd_BPDConVersiones_attr_comentarioVersionInterna_label',
            description_msgid='gvSIGbpd_BPDConVersiones_attr_comentarioVersionInterna_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Comentario a la version para uso interno de la aplicacion.",
        duplicates="0",
        label2="Version Comment (internal)",
        ea_localid="357",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Comments on the Version used internally by the application.",
        ea_guid="{6D55FB7D-845F-4d6f-A0EC-16D50104B872}",
        is_version_comment_storage="True",
        write_permission='Modify portal content',
        scale="0",
        label="Comentario de Version (uso interno)",
        is_version_comment="True",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDConVersiones",
        expression="context.fDerive_ComentarioVersionInterna()",
        computed_types="text"
    ),

    TextField(
        name='comentarioVersionInternaAlmacenada',
        widget=TextAreaWidget(
            label="Comentario Almacenado de Version (uso interno)",
            label2="Version Comment Stored (internal)",
            description="Comentario a la version para uso interno de la aplicacion, almacenado en este elemento. No se usa a menos que sea un elemento raiz, como Organizacion, u otro tipo sin raiz Organizacion.",
            description2="Comments on the Version used internally by the application, stored in this element. Unused unless the element is a root, as an Organization, or has noOrganization  root.",
            label_msgid='gvSIGbpd_BPDConVersiones_attr_comentarioVersionInternaAlmacenada_label',
            description_msgid='gvSIGbpd_BPDConVersiones_attr_comentarioVersionInternaAlmacenada_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Comentario a la version para uso interno de la aplicacion, almacenado en este elemento. No se usa a menos que sea un elemento raiz, como Organizacion, u otro tipo sin raiz Organizacion.",
        duplicates="0",
        label2="Version Comment Stored (internal)",
        ea_localid="587",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Comments on the Version used internally by the application, stored in this element. Unused unless the element is a root, as an Organization, or has noOrganization  root.",
        ea_guid="{8E697EA1-7B3F-4109-86A0-5CD3F5A04A59}",
        is_version_comment_storage="True",
        write_permission='Modify portal content',
        scale="0",
        label="Comentario Almacenado de Version (uso interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDConVersiones",
        exclude_from_exportconfig="True",
        exclude_from_copyconfig="True"
    ),

    StringField(
        name='uidInterVersionesInterno',
        widget=StringWidget(
            label="Identificador Inter Versiones (uso interno)",
            label2="Inter-Version identifier (internal)",
            description="Identificador compartido entre todas las versiones del elemento, para uso interno de la aplicacion.",
            description2="Identifier shared by all versions of an element, used internally by the application.",
            label_msgid='gvSIGbpd_BPDConVersiones_attr_uidInterVersionesInterno_label',
            description_msgid='gvSIGbpd_BPDConVersiones_attr_uidInterVersionesInterno_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Identificador compartido entre todas las versiones del elemento, para uso interno de la aplicacion.",
        duplicates="0",
        label2="Inter-Version identifier (internal)",
        ea_localid="374",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Identifier shared by all versions of an element, used internally by the application.",
        ea_guid="{F10E126B-25CB-4bca-A85F-4BA84475227F}",
        write_permission='Modify portal content',
        scale="0",
        is_inter_version="True",
        label="Identificador Inter Versiones (uso interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDConVersiones"
    ),

    StringField(
        name='versionInternaAlmacenada',
        widget=StringWidget(
            label="Version Almacenada (uso interno)",
            label2="Version identifier Stored (internal)",
            description="Identificador de version para uso interno de la aplicacion, almacenado en este elemento. No se usa a menos que sea un elemento raiz, como Organizacion, u otro tipo sin raiz Organizacion.",
            description2="Version identifier used internally by the application, stored in this element. Unused unless the element is a root, as an Organization, or has noOrganization  root.",
            label_msgid='gvSIGbpd_BPDConVersiones_attr_versionInternaAlmacenada_label',
            description_msgid='gvSIGbpd_BPDConVersiones_attr_versionInternaAlmacenada_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Identificador de version para uso interno de la aplicacion, almacenado en este elemento. No se usa a menos que sea un elemento raiz, como Organizacion, u otro tipo sin raiz Organizacion.",
        duplicates="0",
        label2="Version identifier Stored (internal)",
        ea_localid="586",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        is_version_storage="True",
        description2="Version identifier used internally by the application, stored in this element. Unused unless the element is a root, as an Organization, or has noOrganization  root.",
        ea_guid="{65F698D8-7237-45b2-8C10-A6EF168D9E59}",
        write_permission='Modify portal content',
        scale="0",
        label="Version Almacenada (uso interno)",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDConVersiones",
        exclude_from_exportconfig="True",
        exclude_from_copyconfig="True"
    ),

    RelationField(
        name='versionesSiguientes',
        inverse_relation_label="Version Anterior",
        inverse_relation_description="Versiones predecesoras a la actual de este elemento",
        description="Versiones posteriores del Elemento",
        relationship='BPDSiguientesVersiones',
        label2="Next Versions",
        widget=ReferenceBrowserWidget(
            label="Siguientes Versiones",
            label2="Next Versions",
            description="Versiones posteriores del Elemento",
            description2="Versions after this element's version.",
            label_msgid='gvSIGbpd_BPDConVersiones_rel_versionesSiguientes_label',
            description_msgid='gvSIGbpd_BPDConVersiones_rel_versionesSiguientes_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Versions after this element's version.",
        inverse_relation_label2="Previous Versions",
        deststyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        write_permission='Modify portal content',
        inverse_relation_field_name='versionesAnteriores',
        inverse_relation_description2="Versions before this element's version.",
        label="Siguientes Versiones",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDVersionesAnteriores',
        owner_class_name="BPDConVersiones"
    ),

    RelationField(
        name='versionesAnteriores',
        inverse_relation_label="Siguientes Versiones",
        inverse_relation_description="Versiones posteriores del Elemento",
        description="Versiones predecesoras a la actual de este elemento",
        relationship='BPDVersionesAnteriores',
        label2="Previous Versions",
        widget=ReferenceBrowserWidget(
            label="Version Anterior",
            label2="Previous Versions",
            description="Versiones predecesoras a la actual de este elemento",
            description2="Versions before this element's version.",
            label_msgid='gvSIGbpd_BPDConVersiones_rel_versionesAnteriores_label',
            description_msgid='gvSIGbpd_BPDConVersiones_rel_versionesAnteriores_help',
            i18n_domain='gvSIGbpd',
        ),
        description2="Versions before this element's version.",
        sourcestyle="Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Unspecified;",
        inverse_relation_label2="Next Versions",
        dependency_supplier=True,
        inverse_relation_field_name='versionesSiguientes',
        inverse_relation_description2="Versions after this element's version.",
        write_permission='Modify portal content',
        label="Version Anterior",
        multiValued=1,
        containment="Unspecified",
        inverse_relationship='BPDSiguientesVersiones'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDConVersiones_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDConVersiones:
    """
    """
    security = ClassSecurityInfo()


    # Versioning and Translation fields

    inter_version_field = 'uidInterVersionesInterno'
    version_field = 'versionInterna'
    version_storage_field = 'versionInternaAlmacenada'
    version_comment_field = 'comentarioVersionInterna'
    version_comment_storage_field = 'comentarioVersionInternaAlmacenada'



    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDConVersiones_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDConVersiones

##code-section module-footer #fill in your manual code here
##/code-section module-footer



