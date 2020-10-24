#!/usr/bin/env python
"""
Quick test that shows code working

Author: Matthew C. Jones
Email: matt.c.jones.aoe@gmail.com

:copyright: 2020 Matthew C. Jones
:license: MIT License, see LICENSE for more details.
"""

from engutils import *

z_alt = 5000 * unit('ft')

h_inf, T_inf, p_inf, rho_inf, a_inf, nu_inf = standard_atm(z_alt)

printv(h_inf)
printv(T_inf)
printv(p_inf)
printv(rho_inf)
printv(a_inf)
printv(nu_inf)
