# Monday October 14th (afternoon only)

## Introduction to TOAST

Quaternion array resources:

<https://eater.net/quaternions>

<https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19770024290.pdf>

<https://marctenbosch.com/quaternions/>

## Simulated Scan Strategies

## Simulated Sky Signals

# Tuesday October 15th

## Simulated Instrument Signals

## Interfacing to Real Data

## Map Making

## Pipelines

## Future Directions / Roadmap

## Hackathon Ideas and Discussion

1.  > Mapping ground signal
    
    1.  > Synthetic sidelobes model (Patricio Gallardo)
    
    2.  > Ground pickup (PG)--call with Kevin at 10:30 am, existing
        > jupyter notebook

2.  > Cross-talk

3.  > Planet and/or point source simulations - Aamir, Zhilei
    
    3.  > Write a planet mapper based on existing noise modeling (ACT) -
        > Marius (long term)

4.  > Long term noise fluctuations - Giuseppe

5.  > Long term gain fluctuations - Giuseppe

6.  > Quick coverage maps from TOAST ground schedules - Jason / Matthew
    > H.

7.  > Data I/O (i.e. support your favorite data format) - Erin

8.  > Convolve/deconvolve a transfer function - Katie
    
    4.  > Detector Time Constant Deconvolution
    
    5.  > Misc. Readout Filtering

9.  > Fixed elevation steps in the scheduler - Jason

10. > Gap length proportional to patch separation in scheduler
    
    6.  > Relaxation time from elevation changes into the scheduler.

11. > Boresight rotation - Pedro F.
    
    7.  > Rotation around an arbitrary axis? In case rotation axis is
        > slightly mis-aligned with boresight pointing?

12. > HWP demodulation and downsampling - Maria

13. > HWP-synchronous signal - Jack

14. > Compare South Pole atmospheric model to BICEP/SPT data - Colin

15. > Compare Atacama ATM sims to ACT data - Simone

16. > Scheduler for a specific optics tube instead of the boresight
    > pointing. - Zhilei

17. > Correlated modes with time lags. - Zhilei

18. > The making of flags on timestream data (detection of glitches /
    > jumps, etc) - Katie

19. > Making an instrumental model for S4 in TOAST - Sara
    
    8.  > Inverse hierarchy tracking for SO+S4 (i.e. detector knows what
        > wafer, tube,telescope, site, etc. it belongs to) - Sara
    
    9.  > Setting up S4 instrument model hierarchy (i.e. set up the
        > individual tubes for running)- Sara

20. > Work on TOAST documentation - Ted
    
    10. > Installing TOAST

21. > Add the ability to map V as well as IQU - Sasha, Katie, Maria
    
    11. > Generic Polarization Modulation. (ex: HWP w/ non-idealities.
        > VPMs)

22. > Config file integration

23. > 3g pipeline \<-\> TOAST pipeline integration - Sasha

24. > Instrument model for SPT-3G (reading the dfmux bolometer
    > properties, wiring map and housekeeping) - Sasha
    
    12. > Same thing, but for BICEP array\_info csv file - Colin

25. > Explore integration of pixel space beam convolution into TOAST
    > (connects with 3.) - Pedro F.

26. > Support for non-constant velocity scan profiles

27. > Support for balloon experiments

28. > Non-healpix pixelization (WCS)

# Wednesday October 16th
