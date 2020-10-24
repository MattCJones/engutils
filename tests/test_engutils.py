#!/usr/bin/env python
"""
Quick test that shows code working
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
