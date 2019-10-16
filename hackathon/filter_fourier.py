import numpy as np

import toast


# A working numpy version of this filtering
class OpFouierFilter(toast.Operator):
    def __init__(self, name="signal", filt_funct=None, out_name=None):
        """ 
        A function to apply a fourier space filter on all the data
        
        Arguments:
        name(str) : Cache prefix to operate on
        filt_funct(function) : A function which takes frequency (in Hz) and returns 
                               the complex filter function
        out_name(str) : Cache prefix to output. If None, use name
        """
        self._name = name
        if filt_funct is None:
            raise ValueError("The filtering function definition is required")
        self._function = filt_funct
        
        if out_name is None:
            self._out = self._name
        else:
            self._out = out_name
    
    def exec(self, data):
        # We loop here over all local data but do nothing with it.
        for obs in data.obs:
            tod = obs["tod"]
            freqs = np.fft.fftfreq(tod.local_samples[1]-tod.local_samples[0],
                                   np.median(np.diff(tod.local_times())) )
            filter = self._function(freqs)

            for det in tod.local_dets:
                signal = tod.local_signal( det, self._name )
                out = np.real( np.fft.ifft( filter*np.fft.fft(signal) ) )
                tod.cache.put("{}_{}".format(self._out, det), out, replace=True)

# A working numpy version of this filtering
class OpTimeConst(toast.Operator):
    def __init__(self, name="signal", tau_name="tau", out_name=None, inverse=True):
        """ 
        A function to apply or remove a detector time constant to the data
        
        Arguments:
        name(str) : Cache prefix to operate on
        tau_name(str) : Where to look in the focal plane for time contants to apply / remove
            FIXME : How would we set this up to work with different time constants per detector per observation?
        out_name(str) : Cache prefix to output. If None, use name
        """
        self._name = name
        self._taus = tau_name
        self.inverse = inverse
        if out_name is None:
            self._out = self._name
        else:
            self._out = out_name
    
    def exec(self, data):
        # We loop here over all local data but do nothing with it.
        for obs in data.obs:
            tod = obs["tod"]
            freqs = np.fft.fftfreq(tod.local_samples[1]-tod.local_samples[0],
                                   np.median(np.diff(tod.local_times())) )

            for det in tod.local_dets:
                signal = tod.local_signal( det, self._name )
                tau = obs["focalplane"][det][self._taus]
                filter = 1.0/(1+2.0j*np.pi*freqs*tau)
                if self.inverse:
                    filter = filter**-1
                out = np.real( np.fft.ifft( filter*np.fft.fft(signal) ) )
                tod.cache.put("{}_{}".format(self._out, det), out, replace=True)