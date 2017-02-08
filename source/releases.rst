Pipeline Releases
#################

.. note::

    - A working installation of Miniconda or Anaconda is required.
    - Python 2.x.x is not supported (unless noted otherwise).
    - 32-bit operating systems are not supported.

Pipeline releases differ from the standard software stack and serve a different purpose. The release files described below are immutable snapshots of STScI operational software, and can be used to replicate the environment used by STScI to perform mission-specific data processing. Be aware that upgrading packages with ``conda update [pkg]`` or ``conda update --all`` is not recommended as it will likely introduce unwanted bugs and/or break the environment all together.

If you have any questions, comments, or concerns related to pipeline releases please feel free to contact help@stsci.edu

Installation
============

Pipeline release installations use the following ``conda create`` command format:

.. code-block:: sh

    conda create -n [custom_env_name] --file [URL]
    source activate [custom_env_name]


Example
-------

.. code-block:: sh

    conda create -n demo_2016.1 \
        --file http://ssb.stsci.edu/conda/hstdp-2016.1/hstdp-2016.1-linux-py35.2.txt
    source activate demo_2016.1

The URL used here will not be updated to reflect the latest iteration available. Please consult the :ref:`files` section to ensure you are installing the correct release.


.. _files:

File URLs
=========

Select the URL that matches your intended platform and environment.

HST Data Processing (HSTDP)
---------------------------

*HSTDP* was previously known as *OPUS*.

2016.1
++++++

========  ======  ===
PLATFORM  Python  URL
========  ======  ===
Linux     3.5     http://ssb.stsci.edu/conda/hstdp-2016.1/hstdp-2016.1-linux-py35.2.txt
OS X      3.5     http://ssb.stsci.edu/conda/hstdp-2016.1/hstdp-2016.1-osx-py35.2.txt
========  ======  ===

2016.2
++++++

========  ======  ===
PLATFORM  Python  URL
========  ======  ===
Linux     3.5     http://ssb.stsci.edu/conda/hstdp-2016.2/hstdp-2016.2-linux-py35.2.txt
OS X      3.5     http://ssb.stsci.edu/conda/hstdp-2016.2/hstdp-2016.2-osx-py35.2.txt
========  ======  ===

Release Schema
==============

If you wish to write shell scripts to manage your local pipeline installations, this may be of interest to you:

.. code-block:: sh

    RELEASE_HOME=http://ssb.stsci.edu/conda

    #               hstdp 2016  1
    #               ^     ^     ^
    RELEASE_PARENT=$NAME-$YEAR.$BUILD

    #                              linux     py35            2
    #                              ^         ^               ^
    RELEASE_CHILD=$RELEASE_PARENT-$PLATFORM-$PYTHON_VERSION.$ITERATION.txt
