
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


# Classes added here during runtime will be acceptable roots,
# after invocation of the fParentArchetypeClassNames_ResetCache method
#
gAdditionalParentArchetypeClassNames = [ ]



# Private Cache of class names
# 
gParentArchetypeClassNamesCache      = [ ]




class BPDElemento_Meta:            

    """
    """
    security = ClassSecurityInfo()


    



  
  
  
    security.declarePrivate('fParentArchetypeClassNames')
    def fParentArchetypeClassNames( self):
    
        if gParentArchetypeClassNamesCache:
            return gParentArchetypeClassNamesCache
        
        return self.fParentArchetypeClassNames_ResetCache()
        
        
        
        
        
        
        
    security.declarePrivate('fParentArchetypeClassNames_ResetCache')
    def fParentArchetypeClassNames_ResetCache( self):
    
        aWorkingCopy = self.fArchetypeClassNames()[:]
        
        # Thread safety to be assured here for cases when simultaneusly:
        #
        # Others may be adding to the gAdditionalParentArchetypeClassNames
        # Others may also invoke this method
        #
        if gAdditionalParentArchetypeClassNames:
            aWorkingCopy += gAdditionalParentArchetypeClassNames
        
        gParentArchetypeClassNamesCache = aWorkingCopy
        
        return gParentArchetypeClassNamesCache
        
            
    
    
    
    security.declarePrivate('fArchetypeSchemaByName')
    def fArchetypeSchemaByName( self, theMetaTypeName):
        if not theMetaTypeName:
            return None    
    
        aMetaType = self.fArchetypeClassByName( theMetaTypeName)
        if not aMetaType:
            return None
        return getattr( aMetaType, 'schema', None)
  

    security.declarePrivate('fArchetypeClassNames')
    def fArchetypeClassNames( self):
        return [ 
            'BPDArtefacto',
            'BPDCaracteristica',
            'BPDColeccionArtefactos',
            'BPDColeccionEntradas',
            'BPDColeccionHerramientas',
            'BPDColeccionPasos',
            'BPDColeccionPerfiles',
            'BPDColeccionPoliticasDeNegocio',
            'BPDColeccionProcesosDeNegocio',
            'BPDColeccionReglasDeNegocio',
            'BPDColeccionSalidas',
            'BPDColeccionUnidadesOrganizacionales',
            'BPDDecision',
            'BPDEntrada',
            'BPDEnvio',
            'BPDExitoFinal',
            'BPDExtensionProceso',
            'BPDFracasoFinal',
            'BPDHerramienta',
            'BPDOrganizacion',
            'BPDPasoGestorExcepciones',
            'BPDPasoSimple',
            'BPDPerfil',
            'BPDPlazo',
            'BPDPoliticaDeNegocio',
            'BPDProcesoDeNegocioSimple',
            'BPDPuntoExtension',
            'BPDRecepcion',
            'BPDReferenciaCualificada',
            'BPDReglaDeNegocio',
            'BPDSalida',
            'BPDSubProceso',
            'BPDUnidadOrganizacional',
            'BPDUsoArtefacto',
            'BPDUsoCaracteristica',
 
        ]
        
        
                    
    security.declarePrivate('fArchetypeClassByName')
    def fArchetypeClassByName( self, theMetaTypeName):
        if not theMetaTypeName:
            return None    

        try:            
            
            if theMetaTypeName == 'BPDArtefacto':
                from Products.gvSIGbpd.BPDArtefacto         import BPDArtefacto
                return BPDArtefacto            

            if theMetaTypeName == 'BPDCaracteristica':
                from Products.gvSIGbpd.BPDCaracteristica         import BPDCaracteristica
                return BPDCaracteristica            

            if theMetaTypeName == 'BPDColeccionArtefactos':
                from Products.gvSIGbpd.BPDColeccionArtefactos         import BPDColeccionArtefactos
                return BPDColeccionArtefactos            

            if theMetaTypeName == 'BPDColeccionEntradas':
                from Products.gvSIGbpd.BPDColeccionEntradas         import BPDColeccionEntradas
                return BPDColeccionEntradas            

            if theMetaTypeName == 'BPDColeccionHerramientas':
                from Products.gvSIGbpd.BPDColeccionHerramientas         import BPDColeccionHerramientas
                return BPDColeccionHerramientas            

            if theMetaTypeName == 'BPDColeccionPasos':
                from Products.gvSIGbpd.BPDColeccionPasos         import BPDColeccionPasos
                return BPDColeccionPasos            

            if theMetaTypeName == 'BPDColeccionPerfiles':
                from Products.gvSIGbpd.BPDColeccionPerfiles         import BPDColeccionPerfiles
                return BPDColeccionPerfiles            

            if theMetaTypeName == 'BPDColeccionPoliticasDeNegocio':
                from Products.gvSIGbpd.BPDColeccionPoliticasDeNegocio         import BPDColeccionPoliticasDeNegocio
                return BPDColeccionPoliticasDeNegocio            

            if theMetaTypeName == 'BPDColeccionProcesosDeNegocio':
                from Products.gvSIGbpd.BPDColeccionProcesosDeNegocio         import BPDColeccionProcesosDeNegocio
                return BPDColeccionProcesosDeNegocio            

            if theMetaTypeName == 'BPDColeccionReglasDeNegocio':
                from Products.gvSIGbpd.BPDColeccionReglasDeNegocio         import BPDColeccionReglasDeNegocio
                return BPDColeccionReglasDeNegocio            

            if theMetaTypeName == 'BPDColeccionSalidas':
                from Products.gvSIGbpd.BPDColeccionSalidas         import BPDColeccionSalidas
                return BPDColeccionSalidas            

            if theMetaTypeName == 'BPDColeccionUnidadesOrganizacionales':
                from Products.gvSIGbpd.BPDColeccionUnidadesOrganizacionales         import BPDColeccionUnidadesOrganizacionales
                return BPDColeccionUnidadesOrganizacionales            

            if theMetaTypeName == 'BPDDecision':
                from Products.gvSIGbpd.BPDDecision         import BPDDecision
                return BPDDecision            

            if theMetaTypeName == 'BPDEntrada':
                from Products.gvSIGbpd.BPDEntrada         import BPDEntrada
                return BPDEntrada            

            if theMetaTypeName == 'BPDEnvio':
                from Products.gvSIGbpd.BPDEnvio         import BPDEnvio
                return BPDEnvio            

            if theMetaTypeName == 'BPDExitoFinal':
                from Products.gvSIGbpd.BPDExitoFinal         import BPDExitoFinal
                return BPDExitoFinal            

            if theMetaTypeName == 'BPDExtensionProceso':
                from Products.gvSIGbpd.BPDExtensionProceso         import BPDExtensionProceso
                return BPDExtensionProceso            

            if theMetaTypeName == 'BPDFracasoFinal':
                from Products.gvSIGbpd.BPDFracasoFinal         import BPDFracasoFinal
                return BPDFracasoFinal            

            if theMetaTypeName == 'BPDHerramienta':
                from Products.gvSIGbpd.BPDHerramienta         import BPDHerramienta
                return BPDHerramienta            

            if theMetaTypeName == 'BPDOrganizacion':
                from Products.gvSIGbpd.BPDOrganizacion         import BPDOrganizacion
                return BPDOrganizacion            

            if theMetaTypeName == 'BPDPasoGestorExcepciones':
                from Products.gvSIGbpd.BPDPasoGestorExcepciones         import BPDPasoGestorExcepciones
                return BPDPasoGestorExcepciones            

            if theMetaTypeName == 'BPDPasoSimple':
                from Products.gvSIGbpd.BPDPasoSimple         import BPDPasoSimple
                return BPDPasoSimple            

            if theMetaTypeName == 'BPDPerfil':
                from Products.gvSIGbpd.BPDPerfil         import BPDPerfil
                return BPDPerfil            

            if theMetaTypeName == 'BPDPlazo':
                from Products.gvSIGbpd.BPDPlazo         import BPDPlazo
                return BPDPlazo            

            if theMetaTypeName == 'BPDPoliticaDeNegocio':
                from Products.gvSIGbpd.BPDPoliticaDeNegocio         import BPDPoliticaDeNegocio
                return BPDPoliticaDeNegocio            

            if theMetaTypeName == 'BPDProcesoDeNegocioSimple':
                from Products.gvSIGbpd.BPDProcesoDeNegocioSimple         import BPDProcesoDeNegocioSimple
                return BPDProcesoDeNegocioSimple            

            if theMetaTypeName == 'BPDPuntoExtension':
                from Products.gvSIGbpd.BPDPuntoExtension         import BPDPuntoExtension
                return BPDPuntoExtension            

            if theMetaTypeName == 'BPDRecepcion':
                from Products.gvSIGbpd.BPDRecepcion         import BPDRecepcion
                return BPDRecepcion            

            if theMetaTypeName == 'BPDReferenciaCualificada':
                from Products.gvSIGbpd.BPDReferenciaCualificada         import BPDReferenciaCualificada
                return BPDReferenciaCualificada            

            if theMetaTypeName == 'BPDReglaDeNegocio':
                from Products.gvSIGbpd.BPDReglaDeNegocio         import BPDReglaDeNegocio
                return BPDReglaDeNegocio            

            if theMetaTypeName == 'BPDSalida':
                from Products.gvSIGbpd.BPDSalida         import BPDSalida
                return BPDSalida            

            if theMetaTypeName == 'BPDSubProceso':
                from Products.gvSIGbpd.BPDSubProceso         import BPDSubProceso
                return BPDSubProceso            

            if theMetaTypeName == 'BPDUnidadOrganizacional':
                from Products.gvSIGbpd.BPDUnidadOrganizacional         import BPDUnidadOrganizacional
                return BPDUnidadOrganizacional            

            if theMetaTypeName == 'BPDUsoArtefacto':
                from Products.gvSIGbpd.BPDUsoArtefacto         import BPDUsoArtefacto
                return BPDUsoArtefacto            

            if theMetaTypeName == 'BPDUsoCaracteristica':
                from Products.gvSIGbpd.BPDUsoCaracteristica         import BPDUsoCaracteristica
                return BPDUsoCaracteristica            

        except:
            None
       
        return None
            
