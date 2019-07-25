import numpy as np
import pywt


class CwtTimeSuiteBase(object):
    """
    Set-up for CWT timing.
    """
    params = ([32, 128, 512, 2048],
              ['cmor', 'cgau4', 'fbsp', 'gaus4', 'mexh', 'morl', 'shan'],
              [16, 64, 256],
              ['conv', 'fft'])
    param_names = ('n', 'wavelet', 'max_scale', 'method')

    def setup(self, n, wavelet, max_scale, method):
        try:
            from pywt import cwt
        except ImportError:
            raise NotImplementedError("cwt not available")
        self.data = np.ones(n, dtype='float')
        self.scales = np.arange(1, max_scale+1)


class CwtTimeSuite(CwtTimeSuiteBase):
    def time_cwt(self, n, wavelet, max_scale, method):
        try:
            pywt.cwt(self.data, self.scales, wavelet, method=method)
        except TypeError:
            # older PyWavelets does not support use of the method argument
            if method == 'fft':
                raise NotImplementedError(
                    "fft-based convolution not available.")
            pywt.cwt(self.data, self.scales, wavelet)
