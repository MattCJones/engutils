#!/usr/bin/env python
"""Importable utilties for engineering problem solving.

Author: Matthew C. Jones
Email: matt.c.jones.aoe@gmail.com

:copyright: 2020 Matthew C. Jones
:license: MIT License, see LICENSE for more details.
"""

from inspect import currentframe

from numpy import sqrt
from ambiance import Atmosphere
from pint import UnitRegistry

unit = UnitRegistry(system='mks')
unit.default_format = '~P'
dimless = unit('dimensionless')


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
    which extends the US 1976 Standard Atmospheric Model to 80 km.

    :h: altitude
    :returns: h_geop, T_inf, p_inf, rho_inf, a_inf, nu_inf

    """
    h_meters = h.to('m').magnitude

    atm = Atmosphere(h_meters)  # output units in SI
    arr_len = len(atm.H)
    if arr_len == 1:
        h_geop = atm.H[0] * unit('m')
        T_inf = atm.temperature[0] * unit('K')
        p_inf = atm.pressure[0] * unit('Pa')
        rho_inf = atm.density[0] * unit('kg/m^3')
        a_inf = atm.speed_of_sound[0] * unit('m/s')
        nu_inf = atm.kinematic_viscosity[0] * unit('m^2/s')
    else:
        h_geop = atm.H * unit('m')
        T_inf = atm.temperature * unit('K')
        p_inf = atm.pressure * unit('Pa')
        rho_inf = atm.density * unit('kg/m^3')
        a_inf = atm.speed_of_sound * unit('m/s')
        nu_inf = atm.kinematic_viscosity * unit('m^2/s')

    return h_geop, T_inf, p_inf, rho_inf, a_inf, nu_inf
