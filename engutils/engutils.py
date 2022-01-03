#!/usr/bin/env python
"""Importable utilties for engineering problem solving.

Author: Matthew C. Jones
Email: matt.c.jones.aoe@gmail.com

:copyright: 2020 Matthew C. Jones
:license: MIT License, see LICENSE for more details.
"""

from inspect import currentframe

from numpy import ones, sqrt, shape
from aeroutils import Atmosphere, FlightCondition, unit, dimless


def name_of_var(var):
    """Find name of variables using local items.

    :var: dimensioned variable
    :returns: user-coded name of variable

    """
    try:
        local_vars = currentframe().f_back.f_back.f_locals.items()
        match = [name for name, val in local_vars if val is var]
    except AttributeError:
        local_vars = currentframe().f_back.f_locals.items()
        match = [name for name, val in local_vars if val is var]
    name = match[0] if match else "unknown"
    return name


def printv(var, to=None, var_name="", *args, **kwargs):
    """Print name and value of a Pint unit-specified variable.
    For example,

        distance = 99.9 * unit('m')
        printv(distance)
        # prints "distance = 99.9 m"

    *Note*: as of Python 3.8, simply use the f-string syntax, e.g.
        x=7
        print(f"{x=}")

    :var: variable to be printed
    :to: (str), convert to another unit
    :var_name: overwrite variable name
    :*args: additional arguments
    :**kwargs: additional keyword arguments
    :returns: None

    """
    formatted_output = (var.to(to) if to is not None else var.to_base_units())
    var_name = var_name if var_name else name_of_var(var)
    print(f"{var_name} = {formatted_output:.5g~P}", *args, **kwargs)


def standard_atm(h):
    """Compute quantities from International Civil Aviation Organization (ICAO)
    1993 which extends the US 1976 Standard Atmospheric Model to 80 km.
    Wrapping external package to extract quantities of interest in desired
    dimensional and array format.

    :h: altitude
    :returns: H, T_inf, p_inf, rho_inf, a_inf, nu_inf

    """
    atm = Atmosphere(h)  # output units are dimensional
    return atm.H, atm.T, atm.p, atm.rho, atm.a, atm.nu
