********
Updating
********

Anaconda's package manager, Conda, will not automatically update unless a newer version of a package is detected during a routine package installation. Suffice to say, unless you keep your packages up to date with ``conda update``, the packages installed in your Anaconda distribution will remain relatively static.

Updating AstroConda
===================

There are few simple ways to update packages obtained from AstroConda:

Updating the Release
--------------------

.. code-block:: sh

    $ conda update -n astroconda stsci

This is best used by individuals that favor software stability over receiving the "bleeding edge". Remember, updating the ``stsci`` metapackage only effects packages part of the **official public release** of our software. Packages that are provided by the AstroConda repository, but are not controlled by the ``stsci`` metapackage **will not receive updates**. This holds true for all other metapackages as well (e.g. stsci-hst, stsci-jwst, stsci-data-analysis, etc).

Updating All Packages
---------------------

.. code-block:: sh

    $ conda update -n astroconda --all

This will update the ``stsci`` metapackage, as well all other packages installed in your enviroment. [1]_

This updates **all packages** regardless if they were installed from AstroConda, Continuum, Inc., or other third party repositories defined in ``$HOME/.condarc``.

(`ref <http://conda.pydata.org/docs/using/pkgs.html#package-update>`__)


Updating Packages Individually
------------------------------

.. code-block:: sh

    $ conda update -n astroconda stsci.tools

If you are interested in receiving updates for a particular package, then this method is for you. Be aware that packages may depend on other packages, so the total list of package updates returned by this command will vary.


Downgrading Packages
====================

Did a recent update break your code? Don't wait around for a bugfix... Keep working. For example, if a bug is introduced into ``stsci.tools``, you can easily downgrade it to a known-good version:

.. code-block:: sh

    $ conda search stsci.tools
    .  3.4.0                  py35_6  http://ssb.stsci.edu/astroconda/linux-64
    *  3.4.1                  py35_0  http://ssb.stsci.edu/astroconda/linux-64

The ``*`` denotes the current version installed locally.

Now the only thing left to do, is to tell Conda to install the previous release of the package:

.. code-block:: sh

    $ conda install stsci.tools=3.4.0

At this point you should be back in business.

(`ref <http://conda.pydata.org/docs/faq.html#managing-packages>`__)


Pinning Packages
================

.. caution:: Pinning packages has the potential to break Conda. Only pin packages as a last resort.

Let's take the previous example one step further... Imagine ``stsci.tools`` is broken, and the hotfix release of ``3.4.2`` only partially solved the original issue. Now what? You still need to receive updates to other packages, but ``stsci.tools`` keeps trying to update back to ``3.4.2`` every time you touch ``conda update``.


.. code-block:: sh

    $ echo "stsci.tools <=3.4.0" > ${CONDA_PREFIX}/conda-meta/pinned

From now on, future calls to ``conda update`` will omit ``stsci.tools`` while performing dependency resolution. However, a clear side-effect of this will also be losing the ability to update packages that depend strictly on version ``3.4.2``. Although this is not a permanent solution it can prove useful in a bad situation.

(`ref <http://conda.pydata.org/docs/faq.html?highlight=pinning#pinning-packages>`__)


.. rubric:: Footnotes

.. [1] (STScI-Specific) "Updating All Packages" now assumes the role of "SSBX" in the AstroConda distribution model.
