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

PYTHON3 ?= python3

all:

.git_submodule_init.done.log: \
  .gitmodules
	git submodule init
	git submodule update
	$(MAKE) \
	  --directory dependencies/UCO \
	  .git_submodule_init.done.log \
	  .lib.done.log
	touch $@

check: \
  .git_submodule_init.done.log
	# First, build monolithic render of UCO at tracked commit.
	$(MAKE) \
	  PYTHON3=$(PYTHON3) \
	  --directory dependencies/UCO/tests \
	  uco_monolithic.ttl
	$(MAKE) \
	  --directory tests \
	  check

clean:
	@$(MAKE) \
	  --directory tests \
	  clean
	@rm -f \
	  .git_submodule_init.done.log
	@test ! -r dependencies/UCO/README.md \
	  || $(MAKE) \
	    --directory dependencies/UCO \
	    clean
