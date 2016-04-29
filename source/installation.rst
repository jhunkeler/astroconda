############
Installation
############

Before you begin, note the following requirements and limitations of AstroConda:

    - AstroConda supports Linux (glibc ≥ 2.12) and Mac OS X (≥ 10.7; 10.6 is NOT supported)
    - AstroConda packages support Python versions 2.7, 3.4, or 3.5 on 64-bit platforms. (If you don't know whether you have a 32-bit or 64-bit processor, assume you have 64-bit.)
    - If :abbr:`IRAF (Image Reduction and Analysis Facility)` is required as part of your personal workflow it is *highly recommended* you install Anaconda for Python 2.7 (see :ref:`iraf_python3`).
    - If you do not use :abbr:`IRAF (Image Reduction and Analysis Facility)`, choose the Anaconda installer with the Python version best suited for your scripting needs.
    - This documentation specifically targets Anaconda for Python 3 installations. However, the same commands should still work interchangeably between versions.

Obtain Anaconda
===============

Go grab a copy of the `Anaconda <https://www.continuum.io/downloads>`_ distribution from Continuum, Inc. Be sure to select the installation medium appropriate for your operating system (Linux or Mac) and architecture (64-bit).

Follow the installation instructions for your platform given on the download page. Before moving on to the next step, open a new terminal window, run the ``conda`` command, and ensure your terminal can find it.

.. note::

    Are you using ``bash`` as your shell? Run ``echo $SHELL`` in a terminal and make sure it says something like ``/bin/bash``.
    If it does not, you will have to change your default shell (which is outside the scope of these instructions).

    In the meantime, you can start ``bash -l`` from within your terminal to use ``bash`` temporarily to follow these instructions.


Configure Conda
===============

In order to install packages directly from the AstroConda repository, you will need to configure Anaconda to do so.
This will permanently add the repository to Conda's search path. Be aware that adding additional
`anaconda.org <https://anaconda.org>`_ or direct-url repositories may affect the stability of AstroConda's run-time
environment.

.. code-block:: sh

    $ conda config --add channels http://ssb.stsci.edu/astroconda
    # Writes changes to ~/.condarc


Install AstroConda
==================

Standard installation (without IRAF)
------------------------------------

Now that Conda is configured to pull from our repository, you may now go ahead and install the ``stsci`` metapackage.
The example below will generate a new environment called "astroconda" (using the ``-n`` flag),
however, this is merely a suggestion. Feel free to use a name that works best for you.

.. code-block:: sh

    $ conda create -n astroconda stsci

This will prompt you to confirm the installation of all the STScI packages available in AstroConda. Once they are installed, the following command "activates" the astroconda environment, making these packages available to you.

.. code-block:: sh

    $ source activate astroconda

.. note::

    Though it is repeated a lot in examples, ``source activate astroconda`` only needs to be run once per terminal session. Running this command ensures subsequent commands will take effect only in the ``astroconda`` environment, keeping your system organized.

    To deactivate the ``astroconda`` environment, close your terminal window or run ``source deactivate astroconda``.


Installation with legacy IRAF support
-------------------------------------

The developers of AstroConda have limited resources to support :abbr:`IRAF (Image Reduction and Analysis Facility)`, but users that require the ability to run IRAF and PyRAF tasks may want to install it through AstroConda.

IRAF is not installed by default, so the AstroConda install command is a little different.

.. code-block:: sh

    $ conda create -n astroconda python=2.7 iraf pyraf stsci

Then, just as with the default installation, it is necessary to activate the environment to make its commands and packages available.

.. code-block:: sh

    $ source activate astroconda

.. note::

    Support for using Python 2.7 and IRAF is being gradually phased out by STScI maintainers. In the transitional period, you may wish to install AstroConda with the default settings but maintain a Python 2.7 + IRAF environment for testing. The following commands create an ``astroconda`` environment with the default settings, and an ``iraf27`` environment with IRAF.

    .. code-block:: sh

        $ conda create -n astroconda stsci
        $ conda create -n iraf27 python=2.7 iraf pyraf stsci

    Then, simply ``source activate astroconda`` for day-to-day use or ``source activate iraf27`` for work that requires IRAF. These two environments will be managed separately, allowing you to update only one or the other (see :doc:`updating`).

Fine-tuning the installation
============================

If you are short on hard drive space, have a slow internet connection, or are simply not interested in installing
*everything but the kitchen sink*; please feel free to peruse the `manifest <http://ssb.stsci.edu/astroconda>`_ and
install a custom mix of packages tailored to your needs.

.. code-block:: sh

    $ conda create -n astroconda [package [package ...]]
    $ source activate astroconda

Installing other packages
=========================

AstroConda provides a suite of packages that are known to work well together and are supported by engineers from STScI. However, being built on top of the widely-used ``conda`` tools for managing Python environments, AstroConda also supports the installation of additional 3rd-party packages.

Full documentation of the ``conda`` tool is available from Continuum Analytics, its creators and maintainers: http://conda.pydata.org/docs/using/index.html. However, we have provided a brief explanation of 3rd-party package installation below for quick reference.

For scientific packages available through Anaconda, installation is as simple as::

    $ source activate astroconda
    $ conda install nameofpkg

Often, the easiest way to see if the package is available through Anaconda is to try installing it. The full list of packages is available here: http://repo.continuum.io/pkgs/.

The Python-standard tool ``pip`` is also available to install packages distributed through the Python Package Index (PyPI)::

    $ source activate astroconda
    $ pip install nameofpkg
