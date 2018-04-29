# -*- coding: utf-8 -*-
#
# File: BPDPasoConRestriccionesTiempo.py
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
            label_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeComienzo_label',
            description_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeComienzo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica con respecto a que momento se especifica el comienzo del paso. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
        vocabulary=['Ninguno','ComienzoProceso', 'ComienzoPaso', 'FinPaso', 'FechaFija', 'Evento'],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeComienzo_option_Ninguno', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeComienzo_option_ComienzoProceso', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeComienzo_option_ComienzoPaso', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeComienzo_option_FinPaso', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeComienzo_option_FechaFija', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeComienzo_option_Evento'],
        label2="Reference Start Moment",
        ea_localid="382",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the moment on which starting the step depends. Relative to the start of the process, the start or end of previous steps, a fixed date, or events of certain types conforming to certain conditions.",
        ea_guid="{D5A3F350-E903-4d5e-B951-FA5F629CC9E7}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Momento de Referencia deComienzo",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="0",
        owner_class_name="BPDPasoConRestriccionesTiempo",
        vocabulary2=['None','ProcessStart','StepStart','StepEnd','FixedDate','Event',]
    ),

    FloatField(
        name='desplazamientoMomentoDeComienzo',
        widget=DecimalWidget(
            label="Tiempo desde Momento de Comenzo",
            label2="Time from Start Moment",
            description="Indica un tiempo (en unidades segun campo asociado) con respecto al cual comenzara el paso.",
            description2="Indicates an amount of time, measured in the unit indicated by companion field,  with respect to the Start Reference Moment, to define the moment on which the step shall start or fail its deadline.",
            label_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_desplazamientoMomentoDeComienzo_label',
            description_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_desplazamientoMomentoDeComienzo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica un tiempo (en unidades segun campo asociado) con respecto al cual comenzara el paso.",
        duplicates="0",
        label2="Time from Start Moment",
        ea_localid="383",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates an amount of time, measured in the unit indicated by companion field,  with respect to the Start Reference Moment, to define the moment on which the step shall start or fail its deadline.",
        ea_guid="{4070547B-82E8-4bf5-B2B6-900EC35DBCDE}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Tiempo desde Momento de Comenzo",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="1",
        owner_class_name="BPDPasoConRestriccionesTiempo"
    ),

    StringField(
        name='unidadMomentoDeComienzo',
        widget=SelectionWidget(
            label="Unidad de tiempo desde el Momento de Comienzo",
            label2="Unit of Time from Start Moment",
            description="Indica la unidad de tiempo con que se mide el retraso con respecto al momento en que el paso debe comienzar. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
            description2="Indicates the time unit measuring delay to start the step. Relative to the start of the process, the start or end of previous steps, a fixed date, or events with certain types and conditions.",
            label_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_label',
            description_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica la unidad de tiempo con que se mide el retraso con respecto al momento en que el paso debe comienzar. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
        vocabulary=[ 'Ninguno','Anos','Semestres','Trimestres','Meses','Quncenas','Semanas','EntreSemanas','FinesSemana','Dias','Jornadas','MediasJornadas','Horas','MediasHoras','CuartosHora','Minutos','Segundos', 'Decimas',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Ninguno', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Anos', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Semestres', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Trimestres', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Meses', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Quncenas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Semanas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_EntreSemanas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_FinesSemana', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Dias', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Jornadas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_MediasJornadas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Horas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_MediasHoras', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_CuartosHora', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Minutos', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Segundos', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeComienzo_option_Decimas'],
        label2="Unit of Time from Start Moment",
        ea_localid="384",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the time unit measuring delay to start the step. Relative to the start of the process, the start or end of previous steps, a fixed date, or events with certain types and conditions.",
        ea_guid="{8A8AB54F-9ED8-4770-8547-0974A44BC61E}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Unidad de tiempo desde el Momento de Comienzo",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="2",
        owner_class_name="BPDPasoConRestriccionesTiempo",
        vocabulary2=['None','Years','Semesters','Trimesters','Months','Forthnights','Weeks','WeekDays','WeekEnds','Days','Jornadas','MediasJornadas','Hours','HalfHours','QuarterHours','Minutes','Seconds','Tenths',]
    ),

    StringField(
        name='momentoDeReferenciaDeFin',
        widget=SelectionWidget(
            label="Momento de Referencia de Final",
            label2="Reference End Moment",
            description="Indica con respecto a que momento la ejecucion del paso debera estar completada. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
            description2="Indicates the moment on which the step shall have completed its execution. Relative to the start of the process, the start or end of previous steps, a fixed date, or events of certain types conforming to certain conditions.",
            label_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeFin_label',
            description_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeFin_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica con respecto a que momento la ejecucion del paso debera estar completada. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
        vocabulary=['Ninguno','ComienzoProceso', 'ComienzoPaso', 'FinPaso', 'FechaFija', 'Evento'],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeFin_option_Ninguno', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeFin_option_ComienzoProceso', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeFin_option_ComienzoPaso', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeFin_option_FinPaso', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeFin_option_FechaFija', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_momentoDeReferenciaDeFin_option_Evento'],
        label2="Reference End Moment",
        ea_localid="375",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the moment on which the step shall have completed its execution. Relative to the start of the process, the start or end of previous steps, a fixed date, or events of certain types conforming to certain conditions.",
        ea_guid="{8F64C08D-C93A-49ae-82A6-9D587E131F2D}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Momento de Referencia de Final",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="3",
        owner_class_name="BPDPasoConRestriccionesTiempo",
        vocabulary2=['None','ProcessStart','StepStart','StepEnd','FixedDate','Event',]
    ),

    FloatField(
        name='desplazamientoMomentoDeFin',
        widget=DecimalWidget(
            label="Tiempo desde Momento de Fin",
            label2="Time from End Moment",
            description="Indica un tiempo (en unidades segun campo asociado= con respecto al cual debe terminar el paso.",
            description2="Indicates an amount of time, measured in the unit indicated by companion field,  with respect to the Reference Moment, to define the moment on which the step complete or fail its deadline.",
            label_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_desplazamientoMomentoDeFin_label',
            description_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_desplazamientoMomentoDeFin_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica un tiempo (en unidades segun campo asociado= con respecto al cual debe terminar el paso.",
        duplicates="0",
        label2="Time from End Moment",
        ea_localid="376",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates an amount of time, measured in the unit indicated by companion field,  with respect to the Reference Moment, to define the moment on which the step complete or fail its deadline.",
        ea_guid="{4C682AAC-4859-4422-99A6-363F65778672}",
        write_permission='Modify portal content',
        scale="0",
        default="0",
        label="Tiempo desde Momento de Fin",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="4",
        owner_class_name="BPDPasoConRestriccionesTiempo"
    ),

    StringField(
        name='unidadMomentoDeFin',
        widget=SelectionWidget(
            label="Unidad del tiempo desde el Momento de Fin",
            label2="Unit of time from End Moment",
            description="Indica la unidad con que se mide el retraso con respecto al momento en que el paso debe terminar. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
            description2="Indicates the unit measuring delay to end the step. Relative to the start of the process, the start or end of previous steps, a fixed date, or events with certain types and conditions.",
            label_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_label',
            description_msgid='gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_help',
            i18n_domain='gvSIGbpd',
        ),
        description="Indica la unidad con que se mide el retraso con respecto al momento en que el paso debe terminar. Relativo al comienzo del proceso, o al princicipio o el fin de pasos anteriores, a una fecha fija, o eventos de cierto tipo y condiciones.",
        vocabulary=['Ninguno','Anos','Semestres','Trimestres','Meses','Quncenas','Semanas','EntreSemanas','FinesSemana','Dias','Jornadas','MediasJornadas','Horas','MediasHoras','CuartosHora','Minutos','Segundos',],
        duplicates="0",
        vocabulary_msgids=['gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Ninguno', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Anos', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Semestres', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Trimestres', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Meses', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Quncenas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Semanas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_EntreSemanas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_FinesSemana', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Dias', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Jornadas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_MediasJornadas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Horas', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_MediasHoras', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_CuartosHora', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Minutos', 'gvSIGbpd_BPDPasoConRestriccionesTiempo_attr_unidadMomentoDeFin_option_Segundos'],
        label2="Unit of time from End Moment",
        ea_localid="377",
        derived="0",
        precision=0,
        collection="false",
        styleex="volatile=0;",
        description2="Indicates the unit measuring delay to end the step. Relative to the start of the process, the start or end of previous steps, a fixed date, or events with certain types and conditions.",
        ea_guid="{9A1FF698-5C39-49f4-ABEC-6EBADC62B4ED}",
        write_permission='Modify portal content',
        scale="0",
        default="Ninguno",
        label="Unidad del tiempo desde el Momento de Fin",
        length="0",
        exclude_from_traversalconfig="True",
        containment="Not Specified",
        position="5",
        owner_class_name="BPDPasoConRestriccionesTiempo",
        vocabulary2=['None','Years','Semesters','Trimesters','Months','Forthnights','Weeks','WeekDays','WeekEnds','Days','Jornadas','MediasJornadas','Hours','HalfHours','QuarterHours','Minutes','Seconds',]
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

BPDPasoConRestriccionesTiempo_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class BPDPasoConRestriccionesTiempo:
    """
    """
    security = ClassSecurityInfo()

    allowed_content_types = []
    _at_rename_after_creation = True

    schema = BPDPasoConRestriccionesTiempo_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
# end of class BPDPasoConRestriccionesTiempo

##code-section module-footer #fill in your manual code here
##/code-section module-footer



