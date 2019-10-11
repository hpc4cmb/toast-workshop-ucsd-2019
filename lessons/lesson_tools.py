"""Helper tools common to all notebooks.
"""

import os
import numpy as np

from toast.tod import hex_pol_angles_radial, hex_pol_angles_qu, hex_layout


def check_nersc(reservation=None):
    """Check if we are running at NERSC.
    
    If we are at NERSC, select the account to use for batch jobs.
    
    Args:
        reservation (str):  Attempt to use this reservation for slurm jobs.
        
    Returns:
        (tuple):  The (host, repo) configured.

    """
    nersc_host = None
    nersc_repo = None
    if "NERSC_HOST" in os.environ:
        nersc_host = os.environ["NERSC_HOST"]
        os.environ["OMP_NUM_THREADS"] = "4"
        import subprocess as sp
        repos = sp.check_output(
            "getnim -U $(whoami) | awk '{print $1}'", 
            shell=True,
            universal_newlines=True
        ).split()
        print(
            "Running on NERSC machine '{}'\n  with access to repos: {}".format(
                nersc_host, ", ".join(repos)
            )
        )
        if reservation is not None:
            # We would like to use a reservation
            if reservation in repos:
                # We are allowed to use the reservation
                nersc_repo = reservation
                print("Using requested reservation {}".format(nersc_repo))
            else:
                # Not allowed, use the default repo
                nersc_repo = repos[0]
                print(
                    "Access to reservation {} not enabled, using {} instead"
                    .format(reservation, nersc_repo)
                )
        else:
            nersc_repo = repos[0]
            print("Using default repo {}".format(nersc_repo))
    else:
        print("Not running at NERSC, slurm jobs disabled.")
    return (nersc_host, nersc_repo)


def fake_focalplane(
    samplerate=20,
    epsilon=0,
    net=1,
    fmin=0,
    alpha=1,
    fknee=0.05,
    fwhm=30,
    npix=7,
):
    """Create a set of fake detectors.

    This generates 7 pixels (14 dets) in a hexagon layout at the boresight
    and with a made up polarization orientation.

    Args:
        None

    Returns:
        (dict):  dictionary of detectors and their properties.

    """
    zaxis = np.array([0, 0, 1.0])
    
    pol_A = hex_pol_angles_qu(npix)
    pol_B = hex_pol_angles_qu(npix, offset=90.0)
    
    dets_A = hex_layout(npix, 3.0, "", "", pol_A)
    dets_B = hex_layout(npix, 3.0, "", "", pol_B)
    
    dets = dict()
    for p in range(npix):
        pstr = "{:01d}".format(p)
        for d, layout in zip(["A", "B"], [dets_A, dets_B]):
            props = dict()
            props["quat"] = layout[pstr]["quat"]
            props["epsilon"] = epsilon
            props["rate"] = samplerate
            props["alpha"] = alpha
            props["NET"] = net
            props["fmin"] = fmin
            props["fknee"] = fknee
            props["fwhm_arcmin"] = fwhm
            dname = "{}{}".format(pstr, d)
            dets[dname] = props
    return dets
