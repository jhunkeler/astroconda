###############
Further Reading
###############

.. hmmmmmmmmmmmmmmmmmm what to do?

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

Removing a Conda Environment
============================

It is possible to remove a Conda environment by running:

.. code-block:: sh

    $ conda env remove -n <env_name>

Let's assume you've created a small test environment, "simple", with only a few packages you are interested in, such as ``drizzlepac`` and ``hstcal``.

.. code-block:: sh

    $ conda create -n simple drizzlepac hstcal
    $ source activate simple

You've played around for a bit, maybe calibrated some data or checked out a new feature, but at this point you've decided you no longer want the "simple" environment anymore. So you delete it:

.. code-block:: sh

    $ source deactivate
    $ conda env remove -n simple

And then you quickly verify your "simple" environment no longer exists using ``conda env list``:

.. code-block:: sh

    $ conda env list
    # ["simple" is not listed]
    astroconda               /home/username/miniconda3/envs/astroconda
    iraf27                   /home/username/miniconda3/envs/iraf27
    2016.2                   /home/username/miniconda3/envs/2016.2
    root                  *  /home/username/miniconda3


.. rubric:: Footnotes

.. [#archnote] Intel x86_64 architecture
