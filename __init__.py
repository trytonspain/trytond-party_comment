# This file is part party_comment module for Tryton.  The COPYRIGHT file at the
# top level of this repository contains the full copyright notices and license
# terms.
from trytond.pool import Pool
from . import party


def register():
    Pool.register(
        party.Party,
        module='party_comment', type_='model')
