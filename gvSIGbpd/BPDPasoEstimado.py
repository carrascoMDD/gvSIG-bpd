# -*- coding: utf-8 -*-
#
# File: BPDPasoEstimado.py
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

    StringField(
        name='momentoDeReferenciaDeComienzo',
        widget=SelectionWidget(
            label="Momento de Referencia deComienzo",
            label2="Reference Start Moment",
            description="Indica con respecto a que momento se especifica el comienzo del paso. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
            description2="Indicates the moment on which starting the step depends. Relative to the start of the process, the start or end of previous steps, a fixed date, or events of certain types conforming to certain conditions.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeComienzo_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeComienzo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica con respecto a que momento se especifica el comienzo del paso. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
        vocabulary=['Ninguno','ComienzoProceso', 'ComienzoPaso', 'FinPaso', 'FechaFija', 'Evemto'],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeComienzo_option_Ninguno', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeComienzo_option_ComienzoProceso', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeComienzo_option_ComienzoPaso', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeComienzo_option_FinPaso', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeComienzo_option_FechaFija', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeComienzo_option_Evemto'],
        label2="Reference Start Moment",
        ea_localid="346",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the moment on which starting the step depends. Relative to the start of the process, the start or end of previous steps, a fixed date, or events of certain types conforming to certain conditions.",
        ea_guid="{D953556E-B4CD-4c3a-B215-3CA77E299875}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Momento de Referencia deComienzo",
        length="0",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPasoEstimado",
        vocabulary2=['None','ProcessStart','StepStart','StepEnd','FixedDate','Event',]
    ),

    FloatField(
        name='desplazamientoMomentoDeComienzo',
        widget=DecimalWidget(
            label="Tiempo desde Momento de Comenzo",
            label2="Time from Start Moment",
            description="Indica un tiempo (en unidades segun campo asociado) con respecto al cual comenzara el paso.",
            description2="Indicates an amount of time, measured in the unit indicated by companion field,  with respect to the Start Reference Moment, to define the moment on which the step shall start or fail its deadline.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_desplazamientoMomentoDeComienzo_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_desplazamientoMomentoDeComienzo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica un tiempo (en unidades segun campo asociado) con respecto al cual comenzara el paso.",
        duplicates="0",
        label2="Time from Start Moment",
        ea_localid="347",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates an amount of time, measured in the unit indicated by companion field,  with respect to the Start Reference Moment, to define the moment on which the step shall start or fail its deadline.",
        ea_guid="{AF97C45F-1EC5-48ef-B5C6-47F2EBB5BC0F}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Tiempo desde Momento de Comenzo",
        length="0",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDPasoEstimado"
    ),

    StringField(
        name='unidadMomentoDeComienzo',
        widget=SelectionWidget(
            label="Unidad de tiempo desde el Momento de Comienzo",
            label2="Unit of Time from Start Moment",
            description="Indica la unidad de tiempo con que se mide el retraso con respecto al momento en que el paso debe comienzar. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
            description2="Indicates the time unit measuring delay to start the step. Relative to the start of the process, the start or end of previous steps, a fixed date, or events with certain types and conditions.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica la unidad de tiempo con que se mide el retraso con respecto al momento en que el paso debe comienzar. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
        vocabulary=[ 'Ninguno','Siglos','Decadas','Lustros','Busiestos','Anos','Semestres','Trimestres','Meses','Quncenas','Semanas','EntreSemanas','FinesSemana','Dias','Jornadas','MediasJornadas','Horas','MediasHoras','CuartosHora','Minutos','Segundos', 'Decimas',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Ninguno', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Siglos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Decadas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Lustros', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Busiestos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Anos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Semestres', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Trimestres', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Meses', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Quncenas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Semanas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_EntreSemanas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_FinesSemana', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Dias', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Jornadas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_MediasJornadas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Horas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_MediasHoras', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_CuartosHora', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Minutos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Segundos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeComienzo_option_Decimas'],
        label2="Unit of Time from Start Moment",
        ea_localid="348",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the time unit measuring delay to start the step. Relative to the start of the process, the start or end of previous steps, a fixed date, or events with certain types and conditions.",
        ea_guid="{553C9714-C180-4aac-8658-194B70F79154}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Unidad de tiempo desde el Momento de Comienzo",
        length="0",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDPasoEstimado",
        vocabulary2=['None','Centuries','Decades','Lustros','Bisiestos','Years','Semesters','Trimesters','Months','Forthnights','Weeks','WeekDays','WeekEnds','Days','Jornadas','MediasJornadas','Hours','HalfHours','QuarterHours','Minutes','Seconds','Tenths',]
    ),

    StringField(
        name='momentoDeReferenciaDeFin',
        widget=SelectionWidget(
            label="Momento de Referencia de Final",
            label2="Reference End Moment",
            description="Indica con respecto a que momento la ejecucion del paso debera estar completada. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
            description2="Indicates the moment on which the step shall have completed its execution. Relative to the start of the process, the start or end of previous steps, a fixed date, or events of certain types conforming to certain conditions.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeFin_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeFin_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica con respecto a que momento la ejecucion del paso debera estar completada. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
        vocabulary=['Ninguno','ComienzoProceso', 'ComienzoPaso', 'FinPaso', 'FechaFija', 'Evemto'],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeFin_option_Ninguno', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeFin_option_ComienzoProceso', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeFin_option_ComienzoPaso', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeFin_option_FinPaso', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeFin_option_FechaFija', 'gvSIGbpd_BPDPasoEstimado_attr_momentoDeReferenciaDeFin_option_Evemto'],
        label2="Reference End Moment",
        ea_localid="350",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the moment on which the step shall have completed its execution. Relative to the start of the process, the start or end of previous steps, a fixed date, or events of certain types conforming to certain conditions.",
        ea_guid="{9BFA4B67-ABCA-4f65-8294-193B79DDE478}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Momento de Referencia de Final",
        length="0",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDPasoEstimado",
        vocabulary2=['None','ProcessStart','StepStart','StepEnd','FixedDate','Event',]
    ),

    FloatField(
        name='desplazamientoMomentoDeFin',
        widget=DecimalWidget(
            label="Tiempo desde Momento de Fin",
            label2="Time from End Moment",
            description="Indica un tiempo (en unidades segun campo asociado= con respecto al cual debe terminar el paso.",
            description2="Indicates an amount of time, measured in the unit indicated by companion field,  with respect to the Reference Moment, to define the moment on which the step complete or fail its deadline.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_desplazamientoMomentoDeFin_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_desplazamientoMomentoDeFin_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica un tiempo (en unidades segun campo asociado= con respecto al cual debe terminar el paso.",
        duplicates="0",
        label2="Time from End Moment",
        ea_localid="351",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates an amount of time, measured in the unit indicated by companion field,  with respect to the Reference Moment, to define the moment on which the step complete or fail its deadline.",
        ea_guid="{4E890222-AE6A-43fd-A6CB-EF29D2B03760}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Tiempo desde Momento de Fin",
        length="0",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDPasoEstimado"
    ),

    StringField(
        name='unidadMomentoDeFin',
        widget=SelectionWidget(
            label="Unidad del tiempo desde el Momento de Fin",
            label2="Unit of time from End Moment",
            description="Indica la unidad con que se mide el retraso con respecto al momento en que el paso debe terminar. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
            description2="Indicates the unit measuring delay to end the step. Relative to the start of the process, the start or end of previous steps, a fixed date, or events with certain types and conditions.",
            label_msgid='gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_label',
            description_msgid='gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica la unidad con que se mide el retraso con respecto al momento en que el paso debe terminar. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
        vocabulary=['Ninguno','Milenios','Siglos','Decadas','Lustros','Busiestos','Anos','Semestres','Trimestres','Meses','Quncenas','Semanas','EntreSemanas','FinesSemana','Dias','Jornadas','MediasJornadas','Horas','MediasHoras','CuartosHora','Minutos','Segundos',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Ninguno', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Milenios', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Siglos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Decadas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Lustros', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Busiestos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Anos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Semestres', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Trimestres', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Meses', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Quncenas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Semanas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_EntreSemanas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_FinesSemana', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Dias', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Jornadas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_MediasJornadas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Horas', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_MediasHoras', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_CuartosHora', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Minutos', 'gvSIGbpd_BPDPasoEstimado_attr_unidadMomentoDeFin_option_Segundos'],
        label2="Unit of time from End Moment",
        ea_localid="352",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the unit measuring delay to end the step. Relative to the start of the process, the start or end of previous steps, a fixed date, or events with certain types and conditions.",
        ea_guid="{C724611D-D7D1-41c3-94BE-076B45FB5A85}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Unidad del tiempo desde el Momento de Fin",
        length="0",
        containment="Not Specified",
        position="5",
        owner_class_name="BPDPasoEstimado",
        vocabulary2=['None','Milennia','Centuries','Decades','Lustros','Bisiestos','Years','Semesters','Trimesters','Months','Forthnights','Weeks','WeekDays','WeekEnds','Days','Jornadas','MediasJornadas','Hours','HalfHours','QuarterHours','Minutes','Seconds',]
    ),

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
        containment="Not Specified",
        position="6",
        owner_class_name="BPDPasoEstimado"
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
        containment="Not Specified",
        position="8",
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
        containment="Not Specified",
        position="9",
        owner_class_name="BPDPasoEstimado",
        vocabulary2=[ 'None','Person-Years','Person-Months','Person-Weeks','Person-Days','Person-Hours','Person-Minutes',]
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
        containment="Not Specified",
        position="7",
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



