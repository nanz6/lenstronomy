from __future__ import print_function, division, absolute_import, unicode_literals
__author__ = 'sibirrer'

import numpy as np
import lenstronomy.Util.constants as const


class Background(object):
    """
    class to compute cosmological distances
    """
    def __init__(self, cosmo=None):
        """

        :param param_file: parameter file for pycosmo
        :return:
        """
        from astropy.cosmology import default_cosmology

        if cosmo is None:
            cosmo = default_cosmology.get()
        self.cosmo = cosmo

    def a_z(self, z):
        """
        returns scale factor (a_0 = 1) for given redshift
        """
        return 1./(1+z)

    def D_xy(self, z_observer, z_source):
        """
        angular diamter distance in units of Mpc
        :param z_observer: observer
        :param z_source: source
        :return:
        """
        a_S = self.a_z(z_source)
        D_xy = (self.cosmo.comoving_transverse_distance(z_source) - self.cosmo.comoving_transverse_distance(z_observer))*a_S
        return D_xy.value

    def T_xy(self, z_observer, z_source):
        """
        transverse comoving distance in units of Mpc
        :param z_observer: observer
        :param z_source: source
        :return:
        """
        T_xy = self.cosmo.comoving_transverse_distance(z_source) - self.cosmo.comoving_transverse_distance(z_observer)
        return T_xy.value

    @property
    def rho_crit(self):
        """
        critical density
        :return: value in M_sol/Mpc^3
        """
        h = self.cosmo.H(0).value / 100.
        return 3 * h ** 2 / (8 * np.pi * const.G) * 10 ** 10 * const.Mpc / const.M_sun


