######
F.A.Q.
######

After "``conda create ...``" why does "``source activate astroconda``" fail?
============================================================================

Anaconda does not support CSH (C-Shell). Please switch to a POSIX-compatible shell (e.g. BASH, KSH, ZSH).

.. note::

    STScI will not maintain a separate codebase of Anaconda's backend ``conda`` in order to implement CSH support. Feel free to
    create an issue with the `developers <http://github.com/conda/conda/issues>`_.

How does AstroConda differ from Ureka?
======================================

Ureka and AstroConda both provide applications and libraries in binary form, however Ureka was a *one size fits all* distribution
which included every package in one giant tarball. If an end-user only really wanted a small set of packages they were forced
to install everything *and then some*. AstroConda is a *if the shoe fits wear it* distribution of packages. If an end-user
needs ``HSTCAL``, for example, they can install ``HSTCAL`` and omit much of the rest of HST's software suite.

How often are updates released?
===============================

Updates to (STScI) software will be released as bugs are identified and squashed. The ``stsci-*`` metapackages, for example, provide
"releases" (i.e. a set of software used by our internal pipelines). After installing a release it is then possible to upgrade to the latest
out-of-band packages by simply running:

``conda update -n astroconda --all``

Non-STScI software will be upgraded on an as-needed basis. See the `Contibuting Guide <contributing.html>`_ to learn more about asking
for updates to existing packages.

What happened to SSBX?
======================

SSBX was a weekly release of STScI's software suite regardless of the stability of the codebase. This release was often times
broken and caused issues for external users. SSBX has been rolled into AstroConda as out-of-band package updates. This offers
a much better user experience, because as bugs are fixed, people will be able to upgrade without waiting until the following week.

What happened to SSBDEV?
========================

SSBDEV was a nightly snapshot release of STScI's software suite. This release was often times broken and caused issues for
external users. Nightly snapshots are ***no longer available*** for use by the public. Updates to AstroConda will be made
directly as existing software is improved and/or new software is released.

Why isn't IRAF installed by default?
====================================

IRAF is an extremely large software package. Not every developer or scientist requires it.

If you wish to use IRAF, simply install it:

``conda install -n iraf27 python=2.7 iraf && source activate iraf27``

Why is IRAF/PyRAF less functional under Python 3?
=================================================

The Python code in ``stsdas``, for example, is targeted specifically for Python 2.7 and earlier. If the demand for Python 3
support under IRAF is great enough we may be able pull our resources to accommodate the community. It is recommended to install
IRAF into its own environment under Python 2.7:

``conda create -n iraf27 python=2.7 iraf && source activate iraf27``


Will AstroConda interfere with other scientific distributions (e.g. SciSoft)?
=============================================================================

**Probably**, however unlike Ureka we will not impose any restrictions on your environment or issue compatibility warnings at run-time.
It is your responsibility to maintain a functional shell environment so it does not conflict with your Anaconda installation.



