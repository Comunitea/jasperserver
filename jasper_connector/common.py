# -*- coding: utf-8 -*-
##############################################################################
#
#   jasper_connector module for OpenERP, Management module for Jasper Server
#   Copyright (C) 2011 SYLEAM (<http://www.syleam.fr/>)
#                 2013-2016 MIROUNGA <http://mirounga.fr>
#                           Christophe CHAUVET <christophe.chauvet@gmail.com>
#
#   This file is a part of jasper_connector
#
#   jasper_connector is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   jasper_connector is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import logging
from odoo import report
from odoo.addons.jasper_connector.report.jasper import report_jasper

_logger = logging.getLogger(__name__)

KNOWN_PARAMETERS = [
    'OERP_ACTIVE_ID', 'OERP_ACTIVE_IDS',
    'OERP_COMPANY_NAME', 'OERP_COMPANY_LOGO', 'OERP_COMPANY_HEADER1',
    'OERP_COMPANY_FOOTER1', 'OERP_COMPANY_FOOTER2', 'OERP_COMPANY_WEBSITE',
    'OERP_COMPANY_CURRENCY', 'OERP_COMPANY_STREET', 'OERP_COMPANY_STREET2',
    'OERP_COMPANY_ZIP', 'OERP_COMPANY_CITY', 'OERP_COMPANY_COUNTRY',
    'OERP_COMPANY_PHONE', 'OERP_COMPANY_FAX', 'OERP_COMPANY_MAIL',
]


def registered_report(name):
    """ Register dynamicaly the report for each entry"""
    gname = 'report.' + name
    if gname in report.interface.report_int._reports:
        return
    report_jasper(gname)
    _logger.info('Register the jasper report service [%s]' % name)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
