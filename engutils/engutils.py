#!/usr/bin/env python
"""Importable utilties for engineering problem solving.

Author: Matthew C. Jones
Email: matt.c.jones.aoe@gmail.com

:copyright: 2020 Matthew C. Jones
:license: MIT License, see LICENSE for more details.
"""

from inspect import currentframe

from numpy import sqrt
from skaero.atmosphere import coesa
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
    """Compute quantities from US 1976 Standard Atmospheric Model.

    :h: altitude
    :returns: h_inf, T_inf, p_inf, rho_inf, a_inf, nu_inf

    """
    h_meters = h.to('m').magnitude

    h_m, T_K, p_Pa, rho_kg_p_m3 = coesa.table(h_meters, kind='geometric')
    h_inf = h_m * unit('m')  # geopotential altitude in meters
    T_inf = T_K * unit('K')  # temperature in Kelvin
    p_inf = p_Pa * unit('Pa')  # pressure in Pascal
    rho_inf = rho_kg_p_m3 * unit('kg/m^3')

    R_s = 8.31432 * unit('(N m)/(mol K)')
    M_0 = 28.9644e-3 * unit('kg/mol')
    gamma = 1.4 * dimless

    R = R_s/M_0
    a_inf = sqrt(gamma*R*T_inf)

    # Method defined in the US Standard Atmospher 1976 for calculating
    # viscosity of air as a function of T only
    mu_inf = (1.458e-6*T_inf.to('K').magnitude**(1.5)) \
        / (T_inf.to('K').magnitude + 110.4) * unit('Pa s')
    nu_inf = mu_inf/rho_inf

    return h_inf, T_inf, p_inf, rho_inf, a_inf, nu_inf
