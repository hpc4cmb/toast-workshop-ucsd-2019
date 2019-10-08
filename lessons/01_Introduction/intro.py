
import toast
from toast.mpi import MPI

import numpy as np
import matplotlib.pyplot as plt

import toast.qarray as qa


# Runtime Environment

env = toast.Environment.get()
if MPI.COMM_WORLD.rank == 0:
    env.print()

# Create a fake focalplane

fp = fake_focalplane()

detnames = list(sorted(fp.keys()))
detquat = {x: fp[x]["quat"] for x in detnames}
detfwhm = {x: fp[x]["fwhm_arcmin"] for x in detnames}
detlabels = {x: x for x in detnames}
detpolcol = {x: "red" if i % 2 == 0 else "blue" for i, x in enumerate(detnames)}

if MPI.COMM_WORLD.rank == 0:
    outfile = "intro_focalplane.pdf"
    toast.tod.plot_focalplane(
        detquat, 4.0, 4.0, outfile, fwhm=detfwhm, polcolor=detpolcol, labels=detlabels
    )

# The TOD base and derived classes

nsamples = 1000

obs = dict()

# The type of TOD class is usually specific to the data processing job.
# For example it might be one of the simulation classes or it might be
# a class that loads experiment data.  Here we just use a simple class
# that is only used for testing and which reads / writes data to internal memory
# buffers.

tod = toast.tod.TODCache(MPI.COMM_WORLD, detnames, nsamples, detquats=detquat)
obs["tod"] = tod

# The TOD class has methods to get information about the data:

print("TOD has detectors {}".format(", ".join(tod.detectors)))
print("TOD has {} total samples for each detector".format(tod.total_samples))

# Write some data.  Not every TOD derived class supports writing (for example,
# TOD classes that represent simulations).

t_delta = 1.0 / fp[detnames[0]]["rate"]
tod.write_times(stamps=np.arange(0.0, nsamples * t_delta, t_delta))
tod.write_boresight(
    data=qa.from_angles(
        (np.pi / 2) * np.ones(nsamples),
        (2 * np.pi / nsamples) * np.arange(nsamples),
        np.zeros(nsamples)
    )
)
for d in detnames:
    tod.write(detector=d, data=np.random.normal(scale=fp[d]["NET"], size=nsamples))
    tod.write_flags(detector=d, flags=np.zeros(nsamples, dtype=np.uint8))

# Read it back

print("TOD timestampes = {} ...".format(tod.read_times()[:5]))
print("TOD boresight = \n{} ...".format(tod.read_boresight()[:5,:]))
for d in detnames:
    print("TOD detector {} = {} ...".format(d, tod.read(detector=d, n=5)))
    print("TOD detector {} flags = {} ...".format(d, tod.read_flags(detector=d, n=5)))

# Store some data in the cache.  The "cache" member variable looks like a dictionary of
# numpy arrays, but the memory used is allocated in C, so that we can actually clear
# these buffers when needed.

for d in detnames:
    processed = tod.read(detector=d)
    processed /= 2.0
    # By convention, we usually name buffers in the cache by <prefix>_<detector>
    tod.cache.put("processed_{}".format(d), processed)
print("TOD cache now contains {} bytes".format(tod.cache.report(silent=True)))

