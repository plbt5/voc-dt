#!/usr/bin/make -f


SHELL := /bin/bash

# This Makefile is assumed to execute in a repository directory taxonomy/*.

top_srcdir := $(shell cd ../.. ; pwd)


all: \
  .check-device-types.ttl

.check-device-types.ttl: \
  device-types.ttl \
  $(top_srcdir)/.git_submodule_init.done.log
	java -jar $(top_srcdir)/dependencies/UCO/lib/rdf-toolkit.jar \
	  --inline-blank-nodes \
	  --source device-types.ttl \
	  --source-format turtle \
	  --target $@_ \
	  --target-format turtle
	mv $@_ $@

# Reminder: diff exits non-0 on finding any differences.
# Reminder: The $^ automatic Make variable is the name of all recipe prerequisites.
check: \
  device-types.ttl \
  .check-device-types.ttl
	diff $^	\
	  || (echo "ERROR: Makefile: The local $< does not match the normalized version. If the above reported changes look fine, run 'cp .check-$< $<' while in the sub-folder taxonomy/$$(basename $< .ttl)/ to get a file ready to commit to Git." >&2 ; exit 1)

clean:
	@rm -f .check-device-types.ttl
