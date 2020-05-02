# uc_logging - A set of classes and functions that extend the log package.
# It is part of the Unicon project.
# https://unicon.10k.me
#
# Copyright © 2020 Eduard S. Markelov.
# All rights reserved.
# Author: Eduard S. Markelov <markeloveduard@gmail.com>
#
# This program is Free Software; you can redistribute it and/or modify it under
# the terms of version three of the GNU Affero General Public License as
# published by the Free Software Foundation and included in the file LICENSE.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
import os
import logging
import multiprocessing as mp
import threading
from time import sleep
import random
import uc_logging


format_standard_a = "%(asctime)s [%(levelname)s] - %(message)s"
format_standard_d = "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"

##################################################
# FORMATTER TEST
##################################################

def test_formatter():
    print("Begin Formatter test.")
    logger = logging.getLogger("formatter_test")
    logger.handlers.clear()
    logger.setLevel(logging.DEBUG)
    formatter = uc_logging.Formatter(default=format_standard_a, formats={logging.DEBUG: format_standard_d})
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info("TEST FORMATTER.")
    logger.debug("TEST FORMATTER.")

    print("End formatter test.")


test_formatter()


