# -*- coding: utf-8 -*-
#
# File: gvSIGbpd.py
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


# There are three ways to inject custom code here:
#
#   - To set global configuration variables, create a file AppConfig.py.
#       This will be imported in config.py, which in turn is imported in
#       each generated class and in this file.
#   - To perform custom initialisation after types have been registered,
#       use the protected code section at the bottom of initialize().
#   - To register a customisation policy, create a file CustomizationPolicy.py
#       with a method register(context) to register the policy.

import logging
logger = logging.getLogger('gvSIGbpd')
logger.info('Installing Product')

try:
    import CustomizationPolicy
except ImportError:
    CustomizationPolicy = None

import os, os.path
from Globals import package_home
from Products.CMFCore import utils as cmfutils

try: # New CMF
    from Products.CMFCore import permissions as CMFCorePermissions 
except: # Old CMF
    from Products.CMFCore import CMFCorePermissions

from Products.CMFCore import DirectoryView
from Products.CMFPlone.utils import ToolInit
from Products.Archetypes.atapi import *
from Products.Archetypes import listTypes
from Products.Archetypes.utils import capitalize
from config import *

DirectoryView.registerDirectory('skins', product_globals)
DirectoryView.registerDirectory('skins/gvSIGbpd',
                                    product_globals)

##code-section custom-init-head #fill in your manual code here
##/code-section custom-init-head


def initialize(context):
    ##code-section custom-init-top #fill in your manual code here
    ##/code-section custom-init-top

    # imports packages and types for registration

    import BPDColeccionPoliticasDeNegocio
    import BPDPlazo
    import BPDArquetipo
    import BPDSalida
    import BPDConRegistroActividad
    import BPDPoliticaDeNegocio
    import BPDProgramable
    import BPDFracasoFinal
    import BPDEnvio
    import BPDArquetipoConAdopcion
    import BPDConTraducciones
    import BPDEscenario
    import BPDParticipante
    import BPDExitoFinal
    import BPDColeccionHerramientas
    import BPDColeccionPasos
    import BPDUnidadOrganizacional
    import BPDColeccionProcesosDeNegocio
    import BPDProcesoDeNegocioSimple
    import BPDPasoEstimado
    import BPDRecepcion
    import BPDProgramado
    import BPDListaDePruebas
    import BPDCasoDePrueba
    import BPDPreCondicion
    import BPDPrograma
    import BPDColeccionArquetipos
    import BPDPuntoExtension
    import BPDColeccionCasosDePrueba
    import BPDEntrada
    import BPDPasoConAnteriores
    import BPDColeccionSalidas
    import BPDHerramienta
    import BPDColeccionPerfiles
    import BPDDecision
    import BPDElemento
    import BPDPasoSimple
    import BPDCaracteristica
    import BPDResolucionDatos
    import BPDConDatosDePrueba
    import BPDSubProceso
    import BPDPasoConExcepciones
    import BPDUsoArtefacto
    import BPDExtensionProceso
    import BPDPerfil
    import BPDCondicion
    import BPDReglaDeNegocio
    import BPDEpisodio
    import BPDPrePostCondicional
    import BPDArtefacto
    import BPDProcesoDeNegocio
    import BPDPostCondicion
    import BPDCondicionante
    import BPDCondicional
    import BPDArquetipoReferenciable
    import BPDUsoCaracteristica
    import BPDConVersiones
    import BPDPasoGeneral
    import BPDColeccionReglasDeNegocio
    import BPDReferenciaCualificada
    import BPDPasoGestorExcepciones
    import BPDColeccionListasDePruebas
    import BPDPasoMinimo
    import BPDColeccionArtefactos
    import BPDColeccionEntradas
    import BPDConResolucionesDatos
    import BPDPasoConRestriccionesTiempo
    import BPDDatosDePrueba
    import BPDColeccionUnidadesOrganizacionales
    import BPDPasoConSiguientes
    import BPDOrganizacion

    # Initialize portal content
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    cmfutils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)

    # Apply customization-policy, if theres any
    if CustomizationPolicy and hasattr(CustomizationPolicy, 'register'):
        CustomizationPolicy.register(context)
        print 'Customization policy for gvSIGbpd installed'

    ##code-section custom-init-bottom #fill in your manual code here
    ##/code-section custom-init-bottom

