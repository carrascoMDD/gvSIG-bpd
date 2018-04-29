# -*- coding: utf-8 -*-
#
# File: gvSIGbpd AppConfig.py
#       config.py imports this module,
#       providing the opportunity to extend it
#
#       Used here to add dependencies of the gvSIGbpd product
#       to other products.
#
#       The product installer shall install these before the
#       gvSIGbpd product.
#
# Copyright (c) 2009 by Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana
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

__author__ = """Conselleria de Infraestructuras y Transporte de la Generalidad Valenciana <gvSIGbpd@gvSIG.org>, 
Model Driven Development sl <gvSIGbpd@ModelDD.org>, 
Antonio Carrasco Valero <carrasco@ModelDD.org>"""
__docformat__ = 'plaintext'




# Dependencies of Products to be installed by quick-installer
# defined originally in config.py
# and overriden  in custom configuration

DEPENDENCIES = [ 'ModelDDvlPlone',]



