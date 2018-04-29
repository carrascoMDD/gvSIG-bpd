# -*- coding: utf-8 -*-
#
# File: BPDPasoEstimado.py
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

__author__ = """Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana
<gvSIGbpd@gvSIG.org>, Model Driven Development sl <gvSIGbpd@ModelDD.org>,
Antonio Carrasco Valero <carrasco@ModelDD.org>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.gvSIGbpd.config import *

# additional imports from tagged value 'import'
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    FloatField(
        name='minimoEsfuerzoEstimado',
        widget=DecimalWidget(
            label="Minimo Esfuerzo Estimado",
            label2="Minimum Estimated Effort",
            description="Indica el Minimo de Esfuerzo que se estima puede requerir el paso del proceso. Medido en las unidades segun la propiedad Unidad de Esfuerzo Minimo Estimado",
            description2="Indicates de Estimated Minimum amount of Effort that may be required for the process step. Measured in the units specified by the attribute Units for Minimal Estimated Effort.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_minimoEsfuerzoEstimado_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_minimoEsfuerzoEstimado_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica el Minimo de Esfuerzo que se estima puede requerir el paso del proceso. Medido en las unidades segun la propiedad Unidad de Esfuerzo Minimo Estimado",
        duplicates="0",
        label2="Minimum Estimated Effort",
        ea_localid="353",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates de Estimated Minimum amount of Effort that may be required for the process step. Measured in the units specified by the attribute Units for Minimal Estimated Effort.",
        ea_guid="{517B3EC3-E49A-41cd-A78C-12E81DAB0139}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Minimo Esfuerzo Estimado",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDPasoEstimado"
    ),

    StringField(
        name='unidadMinimoEsfuerzoEstimado',
        widget=SelectionWidget(
            label="Unidad para el Esfuerzo Minimo Estimado",
            label2="Unit for Minimum Estimated Effort",
            description="Indica la unidad de tiempo con que se mide el Minimo de Esfuerzo que se estima puede requerir el paso del proceso.",
            description2="Indicates the unit measuring the Estimated Minimum amount of Effort that may be required for the process step.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica la unidad de tiempo con que se mide el Minimo de Esfuerzo que se estima puede requerir el paso del proceso.",
        vocabulary=[ 'Ninguno','Anos-Persona','Meses-Persona','Semanas-Persona','Dias-Persona','Horas-Persona','Minutos-Persona',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_option_Ninguno', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_option_Anos-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_option_Meses-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_option_Semanas-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_option_Dias-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_option_Horas-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMinimoEsfuerzoEstimado_option_Minutos-Persona'],
        label2="Unit for Minimum Estimated Effort",
        ea_localid="354",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the unit measuring the Estimated Minimum amount of Effort that may be required for the process step.",
        ea_guid="{F6BB7195-CD9A-4a2a-AB7E-EF7453E59E5A}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Unidad para el Esfuerzo Minimo Estimado",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDPasoEstimado",
        vocabulary2=[ 'None','Person-Years','Person-Months','Person-Weeks','Person-Days','Person-Hours','Person-Minutes',]
    ),

    FloatField(
        name='maximoEsfuerzoEstimado',
        widget=DecimalWidget(
            label="Maximo Esfuerzo Estimado",
            label2="Maximum Estimated Effort",
            description="Indica el Maximo de Esfuerzo que se estima puede requerir el paso del proceso. Medido en las unidades segun la propiedad Unidad de Esfuerzo Minimo Estimado",
            description2="Indicates de Estimated Maximum amount of effort that may be required for the process step. Measured in the units specified by the attribute Units for Minimal Estimated Effort.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_maximoEsfuerzoEstimado_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_maximoEsfuerzoEstimado_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica el Maximo de Esfuerzo que se estima puede requerir el paso del proceso. Medido en las unidades segun la propiedad Unidad de Esfuerzo Minimo Estimado",
        duplicates="0",
        label2="Maximum Estimated Effort",
        ea_localid="355",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates de Estimated Maximum amount of effort that may be required for the process step. Measured in the units specified by the attribute Units for Minimal Estimated Effort.",
        ea_guid="{442287DE-A2D6-46ec-A6B9-AFB734EDE411}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Maximo Esfuerzo Estimado",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDPasoEstimado"
    ),

    StringField(
        name='unidadMaximoEsfuerzoEstimado',
        widget=SelectionWidget(
            label="Unidad para el Esfuerzo Maximo Estimado",
            label2="Unit for Maximum Estimated Effort",
            description="Indica la unidad de Tiempo con que se mide el Maximo de esfuerzo que se estima puede requerir el paso del proceso.",
            description2="Indicates the unit measuring the Estimated Maximum amount of effor that may be required for the process step.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica la unidad de Tiempo con que se mide el Maximo de esfuerzo que se estima puede requerir el paso del proceso.",
        vocabulary=[ 'Ninguno','Anos-Persona','Meses-Persona','Semanas-Persona','Dias-Persona','Horas-Persona','Minutos-Persona',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_option_Ninguno', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_option_Anos-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_option_Meses-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_option_Semanas-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_option_Dias-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_option_Horas-Persona', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMaximoEsfuerzoEstimado_option_Minutos-Persona'],
        label2="Unit for Maximum Estimated Effort",
        ea_localid="356",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the unit measuring the Estimated Maximum amount of effor that may be required for the process step.",
        ea_guid="{8FF8454A-DBA1-4a45-B5A0-AC8CF967F7F9}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Unidad para el Esfuerzo Maximo Estimado",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDPasoEstimado",
        vocabulary2=[ 'None','Person-Years','Person-Months','Person-Weeks','Person-Days','Person-Hours','Person-Minutes',]
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoEstimado_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoEstimado:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDPasoEstimado_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDPasoEstimado

##code-section module-footer #fill in your manual code here
##/code-section module-footer



