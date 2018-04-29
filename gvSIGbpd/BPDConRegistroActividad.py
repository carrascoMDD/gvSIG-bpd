# -*- coding: utf-8 -*-
#
# File: BPDConRegistroActividad.py
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
from Products.gvSIGbpd.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    DateTimeField(
        name='fechaCreacion',
        widget=CalendarWidget(
            label="Fecha de Creacion",
            label2="Creation Date",
            description="Fecha en que se creo el elemento.",
            description2="Date when the element was created.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_fechaCreacion_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_fechaCreacion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Fecha en que se creo el elemento.",
        duplicates="0",
        label2="Creation Date",
        ea_localid="309",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        is_modification_date=False,
        description2="Date when the element was created.",
        is_creator_user=False,
        is_modificator_user=False,
        ea_guid="{97A945B0-6F43-47b5-877E-06E98DC8D0A2}",
        is_creation_date=True,
        read_only="True",
        scale="0",
        label="Fecha de Creacion",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    StringField(
        name='usuarioCreador',
        widget=StringWidget(
            label="Usuario Creador",
            label2="Creator User",
            description="Usuario que creo el elemento.",
            description2="User who created the element.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_usuarioCreador_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_usuarioCreador_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Usuario que creo el elemento.",
        duplicates="0",
        label2="Creator User",
        ea_localid="310",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="User who created the element.",
        ea_guid="{0B6C81A2-D8FE-4ef6-99A5-556F6CAD807B}",
        is_creation_user="True",
        read_only="True",
        scale="0",
        label="Usuario Creador",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    DateTimeField(
        name='fechaModificacion',
        widget=CalendarWidget(
            label="Fecha de Modificacion",
            label2="Modification Date",
            description="Fecha en que se modifico el elemento.",
            description2="Date when the element was modified.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_fechaModificacion_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_fechaModificacion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Fecha en que se modifico el elemento.",
        duplicates="0",
        label2="Modification Date",
        ea_localid="311",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        is_modification_date="True",
        description2="Date when the element was modified.",
        ea_guid="{59086B92-7266-4d6a-9E98-15EBA9CCAE81}",
        read_only="True",
        scale="0",
        label="Fecha de Modificacion",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    StringField(
        name='usuarioModificador',
        widget=StringWidget(
            label="Usuario Modificador",
            label2="Modification User",
            description="Usuario que modifico el elemento.",
            description2="User who modified the element.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_usuarioModificador_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_usuarioModificador_help',
            i18n_domain='gvSIGbpd',
        ),
        containment="Not Specified",
        description="Usuario que modifico el elemento.",
        duplicates="0",
        label2="Modification User",
        ea_localid="338",
        derived="0",
        precision=0,
        collection="false",
        styleex="IsLiteral=0;volatile=0;",
        description2="User who modified the element.",
        ea_guid="{196FA06C-1D3B-44a0-B576-8EAC1CF32E17}",
        read_only="True",
        scale="0",
        label="Usuario Modificador",
        length="0",
        exclude_from_traversalconfig="True",
        is_modification_user="True",
        position="3",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    DateTimeField(
        name='fechaEliminacion',
        widget=CalendarWidget(
            label="Fecha de Eliminacion",
            label2="Modification Date",
            description="Fecha en que se elimino el elemento.",
            description2="Date when the element was deleted.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_fechaEliminacion_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_fechaEliminacion_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Fecha en que se elimino el elemento.",
        duplicates="0",
        is_deletion_date="True",
        label2="Modification Date",
        ea_localid="314",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="Date when the element was deleted.",
        ea_guid="{5132EA63-CD71-492e-B548-0F4B87812C4F}",
        read_only="True",
        scale="0",
        label="Fecha de Eliminacion",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    StringField(
        name='usuarioEliminador',
        is_deletion_user="True",
        widget=StringWidget(
            label="Usuario Eliminador",
            label2="Deletion User",
            description="Usuario que elimino el elemento.",
            description2="User who deleted the element.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_usuarioEliminador_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_usuarioEliminador_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Usuario que elimino el elemento.",
        duplicates="0",
        label2="Deletion User",
        ea_localid="315",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="User who deleted the element.",
        ea_guid="{9716A48D-4D97-4bf3-9370-93D1D497913A}",
        read_only="True",
        scale="0",
        label="Usuario Eliminador",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="5",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    TextField(
        name='registroDeCambios',
        widget=TextAreaWidget(
            label="Historia de Cambios",
            label2="Change Log",
            description="Regitro de los cambios efectuados sobre el elemento a lo largo del tiempo por diferentes usuarios.",
            description2="Record of changes made to the element over time by different users.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_registroDeCambios_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_registroDeCambios_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Regitro de los cambios efectuados sobre el elemento a lo largo del tiempo por diferentes usuarios.",
        duplicates="0",
        label2="Change Log",
        ea_localid="313",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="Record of changes made to the element over time by different users.",
        position="7",
        ea_guid="{EF63B072-CBCC-4ce7-87B9-2B5349CA8E28}",
        read_only="True",
        scale="0",
        label="Historia de Cambios",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        is_change_log=True,
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    IntegerField(
        name='contadorCambios',
        widget=IntegerField._properties['widget'](
            label="Contador de Cambios",
            label2="Change Counter",
            description="Contador de cambios realizados a lo largo del tiempo. Util para descubrir si han tenido lugar cambios desde que se leyeron los datos del elemento.",
            description2="Counter of changes over time. Useful to learn if any changes happened since the reading of the element information.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_contadorCambios_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_contadorCambios_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Contador de cambios realizados a lo largo del tiempo. Util para descubrir si han tenido lugar cambios desde que se leyeron los datos del elemento.",
        duplicates="0",
        label2="Change Counter",
        ea_localid="325",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="Counter of changes over time. Useful to learn if any changes happened since the reading of the element information.",
        ea_guid="{624ACD6A-7313-481d-B567-DFCEF2B81620}",
        read_only="True",
        scale="0",
        default="0",
        label="Contador de Cambios",
        length="0",
        is_change_counter="True",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="8",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    StringField(
        name='contadoresDeFuentes',
        widget=StringWidget(
            label="Claves de Secuencia de elementos fuente",
            label2="Source elements Sequence Keys",
            description="Identificadores unicos de secuencia de cambios que identifican el estado en que estaban los elementos fuentes de los que se copio este elemento, en el momento de la copia.",
            description2="Unique identifiers of the changes sequence identifying the state of the source elemetns from which this element was copied, in the moment of the copy.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_contadoresDeFuentes_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_contadoresDeFuentes_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Identificadores unicos de secuencia de cambios que identifican el estado en que estaban los elementos fuentes de los que se copio este elemento, en el momento de la copia.",
        duplicates="0",
        label2="Source elements Sequence Keys",
        ea_localid="303",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;IsLiteral=0;",
        description2="Unique identifiers of the changes sequence identifying the state of the source elemetns from which this element was copied, in the moment of the copy.",
        ea_guid="{2668D740-F5B6-4623-8805-354552357ADB}",
        is_sources_counters="True",
        write_permission='Modify portal content',
        scale="0",
        label="Claves de Secuencia de elementos fuente",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="9",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

    BooleanField(
        name='estaInactivo',
        widget=BooleanField._properties['widget'](
            label="El Elemento esta Inactivo",
            label2="Element is Inactive",
            description="Si Verdadero, entonces el elemento esta inactivo porque ha sido eliminado. Los elementos eliminados no se presentan a los usuario en los usos normales de la aplicacion, y se reservan a funciones especiales de administracion.",
            description2="If True, then the element is inactive because it has been delete. Deleted elements are not presented to users in the usual application use cases, and reserved for specialized administration functions.",
            label_msgid='gvSIGbpd_BPDConRegistroActividad_attr_estaInactivo_label',
            description_msgid='gvSIGbpd_BPDConRegistroActividad_attr_estaInactivo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Si Verdadero, entonces el elemento esta inactivo porque ha sido eliminado. Los elementos eliminados no se presentan a los usuario en los usos normales de la aplicacion, y se reservan a funciones especiales de administracion.",
        duplicates="0",
        label2="Element is Inactive",
        ea_localid="341",
        derived="0",
        precision=0,
        collection="false",
        styleex="IsLiteral=0;volatile=0;",
        description2="If True, then the element is inactive because it has been delete. Deleted elements are not presented to users in the usual application use cases, and reserved for specialized administration functions.",
        ea_guid="{8B7ECAF2-C942-40ab-B18E-F84698F1E179}",
        read_only="True",
        scale="0",
        default="0",
        label="El Elemento esta Inactivo",
        length="0",
        is_inactive_state="True",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="6",
        owner_class_name="BPDConRegistroActividad",
        exclude_from_copyconfig="True"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDConRegistroActividad_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDConRegistroActividad:
    """
    """
    security = ClassSecurityInfo()



    # Change Audit fields

    creation_date_field = 'fechaCreacion'
    creation_user_field = 'usuarioCreador'
    modification_date_field = 'fechaModificacion'
    modification_user_field = 'usuarioModificador'
    deletion_date_field = 'fechaEliminacion'
    deletion_user_field = 'usuarioEliminador'
    is_inactive_field = 'estaInactivo'
    change_counter_field = 'contadorCambios'
    sources_counters_field = 'contadoresDeFuentes'
    change_log_field = 'registroDeCambios'



    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDConRegistroActividad_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDConRegistroActividad

##code-section module-footer #fill in your manual code here
##/code-section module-footer



