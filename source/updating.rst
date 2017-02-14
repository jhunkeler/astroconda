#########################
Updating a Software Stack
#########################

Conda, will not automatically update unless a newer version of a package is detected during a routine package installation. Suffice to say, unless you keep your packages up to date with ``conda update``, the packages installed in your environment will remain static.


There are few simple ways to update packages obtained from AstroConda:

Updating via Metapackage
========================

.. code-block:: sh

    $ conda update -n astroconda stsci

This is best used by individuals that favor software stability over receiving the "bleeding edge". Remember, updating the ``stsci`` metapackage only effects packages part of the **official release** of our software. Packages provided by the AstroConda channel, but are not controlled by the ``stsci`` metapackage **will not receive updates**. This is true for other metapackages as well (e.g. stsci-hst, stsci-data-analysis, etc).

To clarify what this does, if the ``stsci`` metapackage (used to create your environment) has not been updated by STScI to accommodate recently added packages, or newer versions of those packages, nothing will be updated in your environment on behalf of ``stsci``. In general, to receive interim bug fix releases please consider updating all packages, or individual packages of interest.

Updating All Packages
=====================

.. code-block:: sh

    $ conda update -n astroconda --all

This will apply updates to all packages installed in your ``astroconda`` environment [1]_ regardless if they were installed via AstroConda, Continuum Analytics, Inc., or other third party channels defined within your ``$HOME/.condarc``.

(`ref <http://conda.io/docs/using/pkgs.html#package-update>`__)


Updating Individual Packages
============================
.. code-block:: sh

    $ conda update -n astroconda <name_of_pkg>

If you are interested in receiving updates for a particular package, then this method is for you. Be aware that packages may depend on other packages, so the total list of package updates returned by this command will vary.


Updating Conda
==============

.. code-block:: sh

    $ source deactivate
    $ conda update --all

Keeping AstroConda packages up to date is important, but not nearly as important as keeping your 'root' (i.e. the base installation) updated as well. Conda is like any other software project and it requires periodic refreshing to stay current with the latest changes. Failing to do this can, over time, cause side-effects such as, the inability to upgrade, install, remove, or search for packages.

Updating extremely old releases of Conda to the latest version have been known to break the 'root' environment due to a variety of API changes in the code. There is not much STScI can do about this as Conda itself is not our product, however if this happens to you, reinstalling the latest release of Miniconda or Anaconda, then regenerating your AstroConda software environment is the fastest way to resolve the problem. Refer to the `FAQ <faq.html#how-do-i-reinstall-miniconda>`_ for more details.

Downgrading Packages
====================

Did a recent update break your code? For example, if a bug is introduced into ``stsci.tools``, you can, for example, easily downgrade it to a known-good version:

.. code-block:: sh

    $ conda search stsci.tools
    .  3.4.0                  py35_6  http://ssb.stsci.edu/astroconda/linux-64
    *  3.4.1                  py35_0  http://ssb.stsci.edu/astroconda/linux-64

The ``*`` denotes the current version installed locally, while the ``.`` indicates Conda has cached that version of the package on your hard drive for quick-use. No prefix implies the package is neither cached, nor installed.

Now the only thing left to do, is to tell Conda to install the previous release of the package:

.. code-block:: sh

    $ conda install stsci.tools=3.4.0

At this point you will prompted to downgrade the package and hopefully be back in business. However, if you find yourself in this predicament please send an email to help@stsci.edu describing the situtation in detail so that we may either begin working on a bug fix release to accommodate you, or offer alternative solutions the problem.

(`ref <http://conda.io/docs/faq.html#managing-packages>`__)


Pinning Packages
================

.. caution:: Pinning packages has the potential to break Conda. Only pin packages as a last resort.

Let's take the previous example one step further... Imagine ``stsci.tools`` is broken, and the hotfix release of ``3.4.2`` only partially solved the original issue. Now what? You still need to receive updates to other packages, but ``stsci.tools`` keeps trying to update back to ``3.4.2`` every time you touch ``conda update``.


.. code-block:: sh

    $ echo "stsci.tools <=3.4.0" > ${CONDA_PREFIX}/conda-meta/pinned

From now on, future calls to ``conda update`` will omit ``stsci.tools`` while performing dependency resolution. However, a clear side-effect of this will also be losing the ability to update packages that depend strictly on version ``3.4.2``. Although this is not a permanent solution it can prove useful in a bad situation.

(`ref <http://conda.io/docs/faq.html?highlight=pinning#pinning-packages>`__)


.. rubric:: Footnotes

.. [1] (STScI-Specific) "Updating All Packages" now assumes the role of "SSBX" in the AstroConda distribution model.
