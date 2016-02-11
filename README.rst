=============================================
Organizing services for Araport at Meyers Lab
=============================================

This is an example repository with code for a couple of services based
in the Meyers Lab services, for inclusion in Araport.

The proposal consists in having one git repository for the complete
collection of Meyers Lab services that want to be exposed at Araport.
Each service has its own directory.  Common code can be factored out.

Each of the services at https://mpss.danforthcenter.org/web/php/pages can
correspond to one microservice in Adama under the namespace
``meyerslab``.

The following is an explanation of the structure of this repository
and how to expand it to complete the remaining services.


Directory structure
===================

The directory structure is::

  ._ README.rst
  |_ LICENSE
  |_ services
      |_ __init__.py
      |_ common
      |   |_ tools.py
      |_ at_abundances
      |   |_ metadata.yml
      |   |_ main.py
      |_ pare_phasing_analysis
          |_ metadata.yml
          |_ main.py

The directory ``services`` is a Python package (indicated by the file
``__init__.py``, just an empty file).  The directory ``common``
contains any common code that wants to be used in all the services.
In this case we illustrate it by factoring out the code to do the HTTP
requests and the printing out of the results.

The remaining directories are the services themselves.  At the bare
minimum, they contain a file ``metadata.yml`` containing information
about the service, parameter documentation, authors, sources, etc.,
and a file ``main.py`` containing the actual code for the service.

The directory ``at_abundances`` contain a full example of all the
possible fields in the metadata, with comments where necessary.


Adding new services
===================

To complete the list of services at Meyers Lab, continue adding
directories, similar to ``at_abundances`` and ``pare_phasing_analysis``.
The directory ``pare_phasing_analysis`` contains an example to show
how the code in ``main.py`` is almost identical to the one in
``at_abundances``, once the bulk of the work has been moved to the
``common`` package.  Most of the differences across services will be
in the ``metadata.yml`` files.


Testing the service locally
===========================

Each service can be tested locally before submitting to Adama, to make
sure there are no errors in the code.  This is an example of testing
the service ``at_abundances``.

Go to the root directory of the git repository in your terminal and
execute::

  $ python
  >>> import services.at_abundances.main as m
  >>> m.search({'gene': 'AT1G01010', 'model': 1})
  ... output omitted ...

The terminal should display the output of the service.  If there are
errors in the code, they can be fixed either in ``common`` or in the
service itself, and iterated until correct.

Make sure to commit and push your repository to github or any other
public git hosting.


Example of registration
=======================

Once the service behaves correctly in your local machine, it can be
registered to Adama.  Here is an example using the tool http_ (similar
to ``curl`` but more powerful--strongly recommended):

.. code-block:: bash

  $ http https://api.araport.org/community/v0.3/meyerslab/services \
     Authorization:"Bearer $TOKEN" \
     git_repository=https://github.com/waltermoreira/meyerslab-proposal.git \
     metadata=services/at_abundances

Note the parameter ``metadata``.  This parameter (a path relative to
the root of the git repository) tells Adama where to find the metadata
file for the ``at_abundances`` service, since there are multiple services
in the same git repository.  Changing this parameter is the only
change needed to register the remaining services.


.. _http: https://github.com/jakubroztocil/httpie
