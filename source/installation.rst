############
Installation
############


Obtain Anaconda
================

.. note:: AstroConda packages are 64-bit only. We may consider building 32-bit binaries for Linux if there is a demand for it.

Grab a copy of the `Anaconda3 <https://www.continuum.io/downloads>`_ distribution from Continuum, Inc.

Be sure to select the installer appropriate for your operating system and architecture. Installation instructions are
available on the download page.


Configure Conda
===============

In order to install packages directly from the AstroConda repository, you will need to configure Anaconda to do so.
This will permanently add the repository to Conda's search path. Be aware that adding additional
`anaconda.org <https://anaconda.org>`_ repositories to this file may affect the stability of AstroConda's run-time
environment.

Use a plain-text editor to append the following to $HOME/.condarc:

.. code-block:: sh

    channels:
      - astroconda
      - defaults


Install AstroConda
==================

Now that conda is configured to pull from our repository, you may now go ahead and install the ``astroconda``
meta-package.

.. code-block:: sh

    $ conda create -n astroconda astroconda
    $ source activate astroconda



Fine-tuning the installation
============================

If you are short on hard drive space, have a slow internet connection, or are simply not interested in installing
*everything but the kitchen sink*; please feel free to peruse the `manifest <http://ssb.stsci.edu/conda>`_ and
install a custom mix of packages *tailored to your needs*.

.. code-block:: sh

    $ conda create -n astroconda [package [package ...]]
    $ source activate astroconda



