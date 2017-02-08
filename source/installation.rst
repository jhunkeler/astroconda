############
Installation
############

System Requirements
===================

    - 64-bit Intel/AMD processor (x86_64)
    - 64-bit Linux (glibc ≥ 2.12)
    - Mac OS X (≥ 10.7)
    - BASH or ZSH as your default shell environment (T/CSH is NOT supported)

Prerequisites
=============

AstroConda is a third-party addon channel designed for use with the Conda package management system, so therefore in order to install software provided by our channel, you must first install a basic Conda environment on your system. This can be achieved in multiple ways (described below). Our channel's software is compatible with both of the ``2`` and ``3`` variants of Continuum Analytics, Inc.'s Miniconda and Anaconda distributions (i.e. Miniconda2, Miniconda3, Anaconda2, and Anaconda3).

Getting Conda - The choice is yours
-----------------------------------

Miniconda2 and Miniconda3 provide a bare-minimum Conda root environment with Python 2.7 or Python 3.x respectfully. (*Recommended*)

Anaconda2 and Anaconda3 are Continuum Analytics Inc.'s flagship products, and provide a full-featured Conda root environment as well as hundreds of useful tools, libraries, and utilities by default.

Both of Continuum's official distributions support a variety of operating systems and architectures, however the AstroConda channel specifically provides packages for Linux and Apple OS X running on x86_64 Intel/AMD processors. It is important to note Microsoft Windows is not supported at this time.

Now head over to **one** of the following sites and download a copy of the installer of your choice:

- Download `Miniconda <https://conda.io/miniconda.html>`_
- Download `Anaconda <https://www.continuum.io/downloads>`_ (OS X users should choose the command-line installer)

The installation method used for Miniconda and Anaconda are identical, however keep in mind the scripts are written in BASH (not SH), so therefore you *must* execute the installer using ``bash``:

.. code-block:: sh

    $ cd <download_directory_here>
    $ bash <install_script_here>

After the installation is complete double-check the bottom of ``~/.bash_profile`` to ensure Miniconda or Anaconda has been added to your ``PATH``. Otherwise, you will be unable to successfully complete this guide.


Verifying your Conda Environment
--------------------------------

Execute the command: ``which conda``
If the path to ``conda`` (i.e. ``/home/username/miniconda3/bin/conda``), is not returned, continue reading, otherwise skip ahead to :ref:`configure_astroconda_channel`.

If you answered ``Y`` or ``Yes`` when prompted during installation to place Miniconda or Anaconda in your ``PATH``, and ``which conda`` still does not return a path leading back to ``conda``, go ahead and execute ``source ~/.bash_profile``, then re-execute ``which conda``. If the path to ``conda`` appears, skip ahead to :ref:`configure_astroconda_channel`.

However, if you answered ``N`` or ``No`` when prompted, you will need to fix your ``PATH`` manually. If you installed Miniconda or Anaconda using the defaults selected by the installer, but are not sure what the directory is named, use the following command to find out:

.. code-block:: sh

    $ ls -d ~/*conda?
    #[example output]
    /home/username/miniconda3

Now append **one of the following** ``export`` commands that best matches the output of `ls -d` above to the bottom of ``~/.bash_profile`` using a plain-text editor:

.. code-block:: sh

    export PATH="~/miniconda/bin:$PATH"
    export PATH="~/miniconda3/bin:$PATH"
    export PATH="~/anaconda/bin:$PATH"
    export PATH="~/anaconda3/bin:$PATH"

At this point, to assume the new environment with ``conda`` in your ``PATH``, open a new terminal or execute ``source ~/.bash_profile`` and continue to the next section.


.. _configure_astroconda_channel:

Configure Conda to use the Astroconda Channel
=============================================

In order to install packages directly from the AstroConda channel you will need to append our URL to Conda's channel search path.

.. code-block:: sh

    $ conda config --add channels http://ssb.stsci.edu/astroconda
    # Writes changes to ~/.condarc

Be aware that indiscriminately adding channels to your configuration, be it from `anaconda.org <https://anaconda.org>`_ or via direct-URL can effect the stability of software packages in your run-time environment.

For example, if you add a channel found on anaconda.org because it contains a software package you're interested in, but it too provides the same software found in AstroConda, it's possible you may lose track of where packages are coming from. Or worse, the software you installed from the other channel was built incorrectly or did not account for a special case, so now the packages in your environment relying on this as a dependency could very well cease to function correctly.

If you decide to have multiple channels defined in your configuration and bugs begin to appear, it may be best to check their origin before issuing a support ticket to help@stsci.edu. ``conda list`` can be used to display such information about the packages installed in your environment.


Using the AstroConda Channel
============================

.. attention::

    If you are on an instrument team or need to calibrate data using the same environment as STScI operations, please `click here <releases.html>`_.

.. attention::

    IRAF users, please skip to the next section: :ref:`iraf_install`

Standard Software Stack (without IRAF)
---------------------------------------------

The package management system, Conda, is now configured to pull from our repository, so you may go ahead and install the ``stsci`` metapackage. This metapackage installs nearly all of the software provided by STScI in one shot.

The following example generates a new conda environment named "astroconda", however this naming convention is merely a suggestion. Feel free to use a name that works best for you.

.. code-block:: sh

    $ conda create -n astroconda stsci

After the installation is complete go ahead and activate the "astroconda" environment. This command only needs to be executed one time per terminal session.

.. code-block:: sh

    $ source activate astroconda

To deactivate the "astroconda" environment, close your terminal window or run:

.. code-block:: sh

    $ source deactivate


.. _iraf_install:

Legacy Software Stack (with IRAF)
---------------------------------

The maintainers of the AstroConda channel have limited resources to support :abbr:`IRAF (Image Reduction and Analysis Facility)`, but users that require the ability to run IRAF and PyRAF tasks may want to install it via AstroConda. For help with any issues that come up during installation or use, please visit the `PyRAF FAQ <http://www.stsci.edu/institute/software_hardware/pyraf/pyraf_faq>`_. **Linux users** please be sure to visit `this FAQ entry <faq.html#in-linux-how-do-i-install-iraf-s-32-bit-dependencies>`_ for a quick guide to installing IRAF's 32-bit dependencies.


The package management system, Conda, is now configured to pull from our repository, so you may go ahead and install the ``stsci`` metapackage, as well as ``pyraf``, and finally ``iraf``. The ``stsci`` metapackage installs nearly all of the software provided by STScI in one shot, however if you prefer a slimmed down IRAF/PyRAF experience, feel free to omit it.

Due to Python 3.x incompatibilities present in several tasks, it is recommended to install IRAF alongside Python 2.7.

The following example generates a new conda environment named "iraf27", however this naming convention is merely a suggestion, so please feel free to apply a name that works best for you.

.. code-block:: sh

    $ conda create -n iraf27 python=2.7 stsci pyraf iraf

After the installation is complete go ahead and activate the "iraf27" environment. This command only needs to be executed one time per terminal session.

.. code-block:: sh

    $ source activate iraf27

To deactivate the "iraf27" environment, close your terminal window or run:

.. code-block:: sh

    $ source deactivate


Fine-tuning the Software
========================

If you are short on hard drive space, have a slow internet connection, or are simply not interested in installing *everything but the kitchen sink*; take a quick look at the package `manifest <http://ssb.stsci.edu/astroconda>`_ and select a custom mix of packages tailored to your needs.

.. code-block:: sh

    $ conda create -n <name> [package [package ...]]
    $ source activate <name>

For example, if the work you intend to perform requires ``drizzlepac`` and nothing else, you can simply create a custom environment that contains *only* ``drizzlepac`` and its dependencies.

.. code-block:: sh

    $ conda create -n mydriz drizzlepac
    $ source activate mydriz


Additional Software Considerations
==================================

While our channel provides a suite of scientific software packages that are known to work well together and are supported by engineers from STScI, by default, Conda already has access to a hundreds of packages provided directly by Continuum Analytics, Inc. The AstroConda channel itself relies heavily on Continuum for its own dependencies, so you may find it beneficial to explore what is available to you.

Conda's full documentation set covers topics ranging from installation to maintaining environments and is available from its creators and maintainers: http://conda.io/docs/using/index.html.

Installing additional software into your AstroConda environment is as simple as:

.. code-block:: sh

    $ source activate astroconda
    $ conda install <name_of_pkg>

Often, the fastest way to discover if a package exists in the ``conda`` ecosystem is to try searching for it with ``conda search <name_of_pkg>``. A comprehensive list of software available directly from Continuum's default channel can be found here: http://repo.continuum.io/pkgs/.

In addition to ``conda install`` the Python-standard tool ``pip`` is also available to install packages distributed through the Python Package Index (PyPI):

.. code-block:: sh

    $ source activate astroconda
    $ pip install <name_of_pkg>


.. rubric:: Footnotes

.. [#archnote] Intel x86_64 architecture
