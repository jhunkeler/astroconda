Release Notes
=============

ACSTOOLS
--------

ACSTOOLS v2.0.0 Release Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*2016-03-17 16:37:53+00:00*

The following changes were made since the last release in April 2014:

-  Removed standalone ``PixCteCorr`` task. Use ACSCTE step from HSTCAL
   instead to have parallelization and consistent results with the
   CALACS pipeline.

-  Removed ``runastrodriz`` task (moved to ``drizzlepac``).

-  Added masking, post-flash processing, iterative cleaning, and
   alternative statistics to ``acs_destripe`` task. Masking is
   particularly useful for polarized data.

-  Fixed bugs in ``acs_destripe`` task, including proper error handling
   and pixel weighting.

-  Added new ``acs_destripe_plus`` task, which is particularly useful
   for destriping subarrays with ``acs_destripe`` in the middle of
   CALACS processing (between ACSCCD and ACSCTE steps).

-  Added new ``satdet`` module, which can detect and flag satellite
   trails.

-  Added Python 3 support (untested).

DRIZZLEPAC
----------

Public Release of v2.1.3
~~~~~~~~~~~~~~~~~~~~~~~~

*2016-04-05 19:23:04+00:00*

This version represents the same code, with a few additional
enhancements, as the code that was installed for operational calibration
of HST data as of 23 Feb 2016. This represents a major update to the
DrizzlePac software, and also the last version with significant new
features. Future releases will focus primarily on bug fixes that affect
operational use of this code. Full support for this package can be found
at http://drizzlepac.stsci.edu.

A brief overview of the new features and major bug fixes found in this
version (relative to what was released as part of v1.1.16) includes:

-  Full Python 2.7 and 3.5 support

-  Built-in support for automatic mosaic creation

-  Tweakreg now aligns all images in a mosaic into a single undistorted
   output frame even if some images do not overlap others in the mosaic

-  Improved sky matching

-  Produce seamless mosaics using new sky matching techniques. More
   details can be found in an example where these techniques are
   compared.

-  Support for the improved time-dependent ACS distortion model

-  Supports the new ACS distortion calibration: Only DrizzlePac 2.0 is
   able to interpret and apply the latest ACS/WFC distortion reference
   files

-  Support for alignment of data from different HST cameras

-  Specify separate source finding parameters for input and reference
   images to optimize source detection from images taken with different
   HST cameras.

-  Support for use of inclusion/exclusion regions in image alignment

-  Improved support for WFPC2 data

-  resolved problems processing WFPC2 data which had DGEOFILEs
   specified.

-  now requires user to run 'updatewcs' task on WFPC2 data to enable
   astrodrizzle and tweakreg to work with them seamlessly

-  **[API change]** Use of 'updatewcs' removed from TEAL interfaces

-  User and pipeline will need to run this task independently prior to
   running astrodrizzle or tweakreg

-  Python scripts calling astrodrizzle and tweakreg can still set the
   'updatewcs' parameter and have it run as part of those tasks
   (presumably, the user understands when this task will wipe out
   previous updates in their own script)

-  **[API change]** The user interfaces to all 3 coordinate
   transformation tasks now use 'coordfile' as the input file of
   coordinates to transform. The use of 'coords' has been deprecated,
   but still can be used if needed. However, use of 'coordfile' will
   always override any input provided simultaneously with 'coords'
   parameter. Help files have been updated to document this as clearly
   as possible for users.

-  Now relies on astropy for WCS, coordinate specification and I/O
   libraries

-  A full 6-parameter general linear fit can now be performed using
   tweakreg, in addition to shift and rscale

-  WCS keywords updated by tweakreg will result in an undistorted output
   frame with NO residual skew (as represented in the CD matrix
   keywords)

The full set of Release Notes can be found at
http://ssb.stsci.edu/doc/stsci\_python\_x/drizzlepac.doc/html/release\_v2\_0\_0\_notes.html.

FITSBLENDER
-----------

Public Release of v0.2.6
~~~~~~~~~~~~~~~~~~~~~~~~

*2016-04-05 19:35:00+00:00*

This version of fitsblender supports the release of drizzlepac v2.1.3 as
used in the operational HST calibration pipeline and archive as of 23
Feb 2016. It primarily includes bug fixes; namely,

-  Fixed problem with random results from fitsblender by replacing use
   of dict with OrderedDict. This problem resolves issues with which
   image was interpreted as first and last when looking for values to
   use to populate the combined header.

-  Default pipeline processing rules files for all instruments amended
   to reset FLASHCUR header value to 'multi' instead of first.

-  Simple update to insure that any keyword deletion works cleanly with
   astropy by trapping any KeyError? exceptions explicitly.

-  Replace use of pyfits with astropy.io.fits.

-  Now works as-is under Python 2.7 and Python 3.5

HSTCAL
------

HSTCAL v1.0.0 Release Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*2016-03-17 17:46:33+00:00*

The following changes were made since the last release in April 2014,
broken down by sub-components:

General
^^^^^^^

-  Fixed compilation warnings.

WFC3 (v3.3)
^^^^^^^^^^^

-  A new processing step, FLUXCORR, was added to the UVIS pipeline, and
   is performed at the end of processing. It will scale the chip2 image
   using the new PHTFLAM1 and PHTFLAM2 values in the IMPHTAB. New flat
   fields for all filters, as well as a new IMPHTTAB have been delivered
   by the team for this step to be completely implemented.

-  The CTE correction has been implemented for all full-frame UVIS data.
   This is done in conjunction with a full run through of the pipeline
   code without the CTE correction applied, such that both CTE corrected
   and non-CTE corrected output files are saved. This correction is for
   the same reasons as in ACS, but the CTE correction algorithm is
   different; it is applied to the raw file instead of later in the
   processing. Some sections of the CTE code support parallel processing
   with OpenMP. The default for calwf3 is to use all available
   processors. To restrict processing to 1 cpu use the flag -1 in the
   call to calwf3.e The CTE processing is controlled with the PCTECORR
   keyword. New CTE corrected output products will be produced at all
   stages which involved changes to most of the controlling routines and
   output trailers. See the team documentation for more complete
   information on the updates.

-  In conjunction with the CTE correction, a standalone interface
   ``wf3cte`` was created to perform just the CTE correction, similar to
   ``wf32d`` etc.

-  Sink pixel detection is now performed in the UVIS pipeline for
   full-frame images, using the SNKCFILE reference image, and the
   science data DQ mask is updated with the detections. The reference
   image has 2 extensions, each in the pre-overscan trimmed format. This
   step is performed if DQICORR is PERFORM, and is done before BLEVCORR
   while the science image is still untrimmed.

-  Some of the new reference files required new code to read them,
   including the new format for the UVIS IMPHTTAB associated with the
   FLUXCORR step

-  The default CRCORR behavior for IR SCAN data will now be set to OMIT
   by default so that the resulting calibrated image is last read -
   first read instead of the fit to the ramp.

-  All IR scan related keywords formerly in the SPT file will also be
   present in the FLT file

-  For UVIS and IR, a copy of the CSMID keyword, formerly in the SPT
   will also be in the FLT file, CSMID lists the channel select
   mechanism ID.

-  bug fix: nrej initialized in ``wf3rej`` so that REJ\_RATE reported
   consistently correct for the IR pipeline

-  bug fix: a wfc3 uvis association which specifies multiple products
   wont finish processing and segfaults

-  An assortment of memory leaks were fixed

-  Explicit error added to report a non-WFC3 image used as input to the
   pipeline

-  updated text in ``wf3rej`` to report that Astrodrizzle should be used
   to align images instead of PyDrizzle since that’s how it’s advertised
   to users

-  fixed SEGFAULT error in reference file checking when iref environment
   variable not set by user, so can’t find file

ACS
^^^

-  Added support for 2K subarrays in PCTECORR.

-  ``acs2d.e`` reads calibration flags from image header instead of
   command line.

-  Improved temporary file handling.

-  Improved error message if input image does not belong to ACS.

-  Added support for very long input list for ACSREJ.

-  Fixed memory leaks (non-critical).

PYSYNPHOT
---------

PySynphot v0.9.8.2 Release Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*2016-03-17 17:20:03+00:00*

The following changes were made since the last PyPi release (v0.9.7) in
October 19, 2015:

-  Updated spectra data including ACS ``wavecat`` and Vega reference
   spectrum.

-  Replaced PyFITS dependency with ``astropy.io.fits``.

-  Added a lot of documentation and tutorials.

-  Bug fixes.

-  Python 3 support (untested).

REFTOOLS
--------

REFTOOLS v1.7.1 Release Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*2016-03-17 16:55:15+00:00*

The following changes were made since the last release in April 2014:

-  Added ``interpretdq`` module to interpret individual DQ flags from DQ
   array.

-  Updated ``mkimphttab`` to handle WFC3 photometry keywords.

-  Replaced old ``stsci.*`` dependencies with SciPy.

-  Added Python 3 support (untested).

SPECVIEW
--------

Pre-release for May2015 JWST DA User Training
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*2015-04-28 15:44:58+00:00*

SPECVIZ
-------

v0.1rc3
~~~~~~~

*2016-03-17 19:14:04+00:00*

Feature complete (for this release) version of SpecViz. However,
usability bugs and minor tweaks are still to be expected.

v0.1rc2
~~~~~~~

*2016-02-15 17:55:20+00:00*

-  Installation improvements

-  Model fitting

-  ASCII table ingestion implemented

-  Bug fixes

STSCI.TOOLS
-----------

stsci.tools v3.4.1 Release Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*2016-03-17 17:08:24+00:00*

The following changes were made since the last release in October 19,
2015:

-  New ``convertlog`` task, which converts ASCII trailer files into FITS
   files to replace use of IRAF ``stwfits`` in HST pipeline operations.

-  Bug fixes.

-  Python 3 support.

WFPC2TOOLS
----------

WFPC2TOOLS v1.0.3 Release Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*2016-03-17 16:44:13+00:00*

The following changes were made since the last release in April 2014:

-  Replaced old ``stsci.*`` dependencies with SciPy.

-  Added Python 3 support (untested).
