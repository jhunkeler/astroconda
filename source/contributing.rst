******************
Contributing Guide
******************


.. attention::

    A `GitHub <https://github.com>`_ account is required to begin contributing to AstroConda

Adding a recipe to astroconda-contrib
=====================================

In this example we will be adding a new recipe to the AstroConda repository for `sympy <http://sympy.org>`_, the symbolic
mathematics library.

Navigate to the `astroconda-contrib <https://github.com/astroconda/astroconda-contrib>`_ repository on GitHub, login,
and create a fork (or click `here <https://github.com/astroconda/astroconda-contrib/fork>`_ to have your fork created automatically).

Now that you have a fork of astroconda-contrib, go ahead and clone it to your system:

.. code-block:: sh

    git clone https://github.com/[Your_Account]/astroconda-contrib
    cd astroconda-contrib


To get started adding our recipe, create a new branch and name it ``sympy-contrib``:

.. code-block:: sh

    git checkout -t -b sympy-contrib

Git will automatically switch your branch from ``master`` to ``sympy-contrib`` as denoted by the following output:

.. code-block:: sh

    Branch sympy-contrib set up to track local branch master.
    Switched to a new branch 'sympy-contrib'

If you have taken the liberty of looking around the astroconda-contrib directory, you will have noticed a bunch of
directories are sitting in there all named by-package. So let's keep things simple and straight forward. Go ahead and
create a directory and name it ``sympy``, and proceed inside:

.. code-block:: sh

    mkdir sympy
    cd sympy

.. note::

    This is not an Anaconda packaging tutorial. For more information about creating recipes from scratch, please refer to
    the `conda-build documentation <http://conda.pydata.org/docs/build_tutorials/pkgs2.html>`_.

    **Hint:** Investigate the contents of the recipes in astroconda-contrib. For most cases, copying an existing recipe and
    changing its values will suffice.

Copy the contents of the ``astroconda-contrib/template`` recipe.  Three files ``bld.bat``, ``build.sh``, and ``meta.yaml``
will be copied to your working directory:

.. code-block:: sh

    cp ../template/* .


Go ahead and open ``meta.yaml`` with your favorite plain-text editor:

.. caution::

    It is *highly recommended* that you enable "tabs to spaces" for your editor. Tab widths are unpredictable and may cause
    Conda's YAML parser to fail.

.. code-block:: sh

    vim meta.yaml

The general structure of the file is as follows:

.. code-block:: yaml

    # These directives are commented here due to Pygments
    # failing to parse this section of code.
    # ... They are not commented in the real file.

    #{% set name = '' %}
    #{% set version = '' %}
    #{% set number = '0' %}

    about:
        # Package homepage
        home:
        # Package license
        license:
        # A brief description
        summary:

    package:
        # Define these values above
        name: {{ name }}
        version: {{ version }}

    build:
        # Define this value above
        number: {{ number }}

    source:
        fn: {{ name }}-{{ version }}.tar.gz
        url: http://example.com/example/{{ name }}-{{ version }}.tar.gz

    requirements:
        build:
        # Dependencies required at BUILD-TIME go here
        - setuptools
        - python x.x
        run:
        # Dependencies required at RUN-TIME go here
        # - ...

    #test:
    #   imports:
    #   # - (e.g. a_python_module)
    #
    #   commands:
    #   # - (e.g. program --help)


First, let's fill in the blanks. Modify the JINJA2 template markers for ``name``, ``version``:

.. code-block:: none

    {% set name = 'sympy' %}
    {% set version = '1.0' %}

Fill in the ``about`` section with relevant information regarding the package:

.. code-block:: yaml

    about:
        home: http://sympy.org
        license: GPL
        summary: Python library for symbolic mathematics

Next, modfy the ``source`` section's ``url`` variable so that it points to ``sympy``'s source archive (on the internet):

.. code-block:: sh

    source:
        fn: {{ name }}-{{ version }}.tar.gz
        url: https://github.com/{{ name }}/{{ name }}/releases/download/{{ name }}-{{ version }}/{{ name }}-{{ version }}.tar.gz

What's with the never-ending stream of bracket encapsulated keywords, you ask? JINJA2 provides basic string interpolation. If you
decide to build, for example, ``sympy-1.1`` in the future, you need only modify the first two settings in this file (assuming
the URL structure has not changed).

