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

all: \
  README.md

README.md: \
  $(top_srcdir)/dependencies/UCO/tests/.venv.done.log \
  $(top_srcdir)/taxonomy/device-types/device-types.ttl \
  README_md.py
	rm -f _$@
	source $(top_srcdir)/dependencies/UCO/tests/venv/bin/activate \
	  && python3 README_md.py \
	    _$@ \
  	    $(top_srcdir)/taxonomy/device-types/device-types.ttl 
	mv _$@ $@
