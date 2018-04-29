# -*- coding: utf-8 -*-
#
# File: BPDElemento_MappingConfig.py
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
# Authors: 
# Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana, Model Driven Development sl, Antonio Carrasco Valero
#
#

__author__ = """Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana
<gvSIGbpd@gvSIG.org>, Model Driven Development sl <gvSIGbpd@ModelDD.org>,
Antonio Carrasco Valero <carrasco@ModelDD.org>"""

__docformat__ = 'plaintext'

from AccessControl                  import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.gvSIGbpd.config import *



class BPDElemento_MappingConfig:            

    """
    """
    security = ClassSecurityInfo()

 
    security.declarePublic('mappingConfig')
    def mappingConfig( self):
        return [
    {   'abstract':        True,
        'portal_types':    [ 'BPDArtefacto', 'BPDColeccionArtefactos', 'BPDColeccionEntradas', 'BPDColeccionHerramientas', 'BPDColeccionPasos', 'BPDColeccionPerfiles', 'BPDColeccionPoliticasDeNegocio', 'BPDColeccionProcesosDeNegocio', 'BPDColeccionReglasDeNegocio', 'BPDColeccionSalidas', 'BPDColeccionUnidadesOrganizacionales', 'BPDDecision', 'BPDEntrada', 'BPDEnvio', 'BPDExitoFinal', 'BPDFracasoFinal', 'BPDHerramienta', 'BPDOrganizacion', 'BPDPasoSimple', 'BPDPerfil', 'BPDPlazo', 'BPDPoliticaDeNegocio', 'BPDProcesoDeNegocioSimple', 'BPDRecepcion', 'BPDReferenciaCualificada', 'BPDReglaDeNegocio', 'BPDSalida', 'BPDSubProceso', 'BPDUnidadOrganizacional', ],
        'same_features':   [ 'description', 'imagenes', 'archivos', 'documentos', 'noticias', 'enlaces',  ],
    },
    {   'abstract':        True,
        'portal_types':    [ 'BPDPoliticaDeNegocio', 'BPDReglaDeNegocio', 'BPDHerramienta', 'BPDArtefacto',],
        'same_features':   [ 'text', 'codigo', 'estado', 'fechaAdopcion', 'fechaObsolescencia', 'nivelDeImposicion', 'version', ],
    },
    {   'portal_types':    [ 'BPDPoliticaDeNegocio', 'BPDReglaDeNegocio'],
        'mapped_features': [ 
            [ 'coleccionesPoliticasDeNegocio', 'coleccionesReglasDeNegocio', ], 
            [ 'herramientasGobernadas',        'herramientasDirigidas', ], 
            [ 'artefactosGobernados',          'artefactosDirigidos', ], 
            [ 'participantesGobernados',       'participantesDirigidos', ], 
            [ 'procesosDeNegocioGobernados',   'procesosDeNegocioDirigidos', ], 
        ],
    },
    {   'portal_types':    [ 'BPDColeccionPoliticasDeNegocio', 'BPDColeccionReglasDeNegocio'],
        'same_features':   [ 'text', ],
        'mapped_features': [ 
            [ 'politicasDeNegocio', 'reglasDeNegocio', ], 
        ],
    },
    {   'portal_types':    [ 'BPDHerramienta', 'BPDArtefacto'],
        'same_features':   [ 'reglasDeNegocioDirigentes', 'politicasDeNegocioGobernantes', ],
        'mapped_features': [ 
            [ 'coleccionesHerramientas',         'coleccionesArtefactos', ],
            [ 'responsablesDeHerramienta',       'responsablesDeArtefacto', ],
            [ 'pasosAsistidos',                  'pasosQueEnvianElArtefacto',], 
            [ 'pasosAsistidos',                  'pasosQueRecibenElArtefacto',], 
        ],
    },
    {   'portal_types':    [ 'BPDColeccionHerramientas', 'BPDColeccionArtefactos'],
        'same_features':   [ 'text', ],
        'mapped_features': [ 
            [ 'herramientas',  'artefactos',],  
        ],
    },
    {   'abstract':        True,
        'portal_types':    [ 'BPDUnidadOrganizacional', 'BPDOrganizacion', 'BPDPerfil'],
        'same_features':   [ 'text', 'abreviatura', 'responsabilidadesClave', 'politicasDeNegocioGobernantes', 'reglasDeNegocioDirigentes', 'procesosEjecutados', 'procesosSupervisados', 'responsableDeArtefactos', 'responsableDeHerramientas', 'pasosEjecutados', 'destinatarioDeEnvios', 'remitenteDeRecepciones', ],
    },
    {   'portal_types':    [ 'BPDUnidadOrganizacional', 'BPDPerfil'],
    },
    {   'portal_types':    [ 'BPDUnidadOrganizacional', 'BPDOrganizacion', ],
        'same_features':   [ 'coleccionesUnidadesOrganizacionales',  ],
    },
    {   'portal_types':    [ 'BPDColeccionUnidadesOrganizacionales', 'BPDColeccionPerfiles'],
        'same_features':   [ 'text', ],
        'mapped_features': [ 
            [ 'unidadesOrganizacionales', 'perfiles',], 
        ],
    },
    {   'portal_types':    [ 'BPDEntrada', 'BPDSalida'],
        'same_features':   [ 'text', ],
        'mapped_features': [ 
            [ 'esRequerida',   'esRequerido',], 
            [ 'valorDefecto',  'text', ], 
            [ 'artefactosDeEntrada',   'artefactosDeSalida',], 
        ],
    },
    {   'portal_types':    [ 'BPDEntrada', 'BPDRecepcion'],
        'same_features':   [ 'text', ],
        'mapped_features': [ 
            [ 'artefactosDeEntrada',   'artefactosRecibidos',], 
            [ 'valorDefecto',  'text', ], 
        ],
    },
    {   'portal_types':    [ 'BPDSalida', 'BPDEnvio'],
        'same_features':   [ 'text', ],
        'mapped_features': [ 
            [ 'artefactosDeSalida',   'artefactosEnviados',], 
        ],
    },
    {   'portal_types':    [ 'BPDDecision', 'BPDEnvio', 'BPDExitoFinal', 'BPDFracasoFinal', 'BPDPasoSimple',  'BPDPlazo', 'BPDRecepcion', 'BPDSubProceso',],
        'same_features':   [ 'text', 'esInicial', 'pasosSiguientes', 'pasosAnteriores', 'pasosOriginandoExcepcion', 'pasosSiguientesEnCasoExcepcion', 'pasosRequeridos', 'requeridoEnPlazos', ],
    },
    {   'portal_types':    [  'BPDEnvio',  'BPDRecepcion', ],
        'mapped_features': [ 
            [ 'artefactosEnviados', 'artefactosRecibidos', ], 
            [ 'destinatarios',      'remitente',], 
        ],
    },
        ]
