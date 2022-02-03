#!/usr/bin/make -f

# This software was developed at the National Institute of Standards
# and Technology by employees of the Federal Government in the course
# of their official duties. Pursuant to title 17 Section 105 of the
# United States Code this software is not subject to copyright
# protection and is in the public domain. NIST assumes no
# responsibility whatsoever for its use by other parties, and makes
# no guarantees, expressed or implied, about its quality,
# reliability, or any other characteristic.
#
# We would appreciate acknowledgement if the software is used.

SHELL := /bin/bash

top_srcdir := $(shell cd .. ; pwd)

all:

check: \
  check-pyshacl \
  check-pytest

# NOTE - This does not use `case_validate`, in order to avoid any circular submodule dependencies between UCO and the CASE Python Utilities.
check-pyshacl: \
  $(top_srcdir)/dependencies/UCO/tests/uco_monolithic.ttl
	source $(top_srcdir)/dependencies/UCO/tests/venv/bin/activate \
	  && pyshacl \
	    --data-file-format json-ld \
	    --inference none \
	    --ont-file-format turtle \
	    --ont-graph $(top_srcdir)/skos-DeviceTypes.ttl \
	    --shacl $(top_srcdir)/dependencies/UCO/tests/uco_monolithic.ttl \
	    --shacl-file-format turtle \
	    $(top_srcdir)/SM-G925F.json

check-pytest: \
  $(top_srcdir)/dependencies/UCO/tests/uco_monolithic.ttl
	source $(top_srcdir)/dependencies/UCO/tests/venv/bin/activate \
	  && pytest \
	    --log-level=DEBUG

# Nothing to do yet.
clean:
