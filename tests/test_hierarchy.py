#!/usr/bin/env python3

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

import logging
import pathlib

import owlrl
import pytest
import rdflib

NS_KB = rdflib.Namespace("http://example.org/kb/")
NS_SKOS = rdflib.SKOS
NS_UCO_CORE = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/core#")
NS_UCO_DT = rdflib.Namespace("https://taxonomy.unifiedcyberontology.org/uco/device-types/")
NS_UCO_OBSERVABLE = rdflib.Namespace("https://unifiedcyberontology.org/ontology/uco/observable#")


@pytest.fixture(scope="session")
def graph() -> rdflib.Graph:
    top_srcdir = pathlib.Path(__file__).parent / ".."
    graph = rdflib.Graph()

    # Guarantee some prefixes
    graph.bind("kb", NS_KB)
    graph.bind("core", NS_UCO_CORE)
    graph.bind("dt", NS_UCO_DT)
    graph.bind("skos", NS_SKOS)
    graph.bind("observable", NS_UCO_OBSERVABLE)

    logging.debug("Loading sample knowledge-base file 1.")
    graph.parse(str(top_srcdir / "SM-G925F.json"), format="json-ld")

    logging.debug("Loading sample knowledge-base file 2.")
    graph.parse(str(top_srcdir / "counterfeit-iphone4.json"), format="json-ld")

    logging.debug("Loading device types ontology.")
    graph.parse(str(top_srcdir / "taxonomy" / "device-types" / "device-types.ttl"), format="turtle")

    logging.debug("Loading SKOS.")
    graph.parse(str(top_srcdir / "dependencies" / "skos-owl1-dl.rdf"), format="xml")

    # The closure is expanded before loading UCO because these unit tests happen to only need the SKOS relationship properties expanded.
    logging.debug("Building SKOS closure.")
    logging.debug("  len(graph) = %d...", len(graph))
    owlrl.RDFSClosure.RDFS_Semantics(graph, False, False, False).closure()
    logging.debug("  -> %d.", len(graph))
    
    logging.debug("Loading monolithic ontology.")
    graph.parse(str(top_srcdir / "dependencies" / "UCO" / "tests" / "uco_monolithic.ttl"), format="turtle")

    return graph


def test_exact_match(graph: rdflib.Graph) -> None:
    """
    Find subject Samsung device by exact taxon match.
    """

    expected = {str(NS_KB["samsung-device-uuid"])}
    computed = set()

    query = """\
SELECT ?nDevice
WHERE {
  ?nDevice
    core:hasFacet ?nDeviceFacet ;
    .

  ?nDeviceFacet
    observable:deviceType ?nDeviceTypeTaxon ;
    .

  ?nDeviceTypeTaxon
    skos:prefLabel "Samsung SM-G925F"@en-US ;
    .

}"""
    for result in graph.query(query):
        (n_device,) = result
        computed.add(str(n_device))

    logging.debug("Query results: %r.", sorted(computed))

    assert expected == computed


def test_android_phone_direct_match(graph: rdflib.Graph) -> None:
    """
    Confirm the Samsung device can be found by merit of being, "most directly," an Android Phone.  "Most directly" means skos:broader is used in the query.  This query is also written to accept if the instance data merely tagged the phone as an Android Phone instead of a more specific model.
    """

    expected = {str(NS_KB["samsung-device-uuid"])}
    computed = set()

    query = """\
SELECT ?nDevice
WHERE {
  ?nDevice
    core:hasFacet ?nDeviceFacet ;
    .

  ?nDeviceFacet
    observable:deviceType ?nDeviceType ;
    .

  ?nDeviceType
    skos:broader? ?nDeviceTypeTaxon
    .

  ?nDeviceTypeTaxon
    skos:prefLabel "Android_Phone"@en-US ;
    .
}"""
    for result in graph.query(query):
        (n_device,) = result
        computed.add(str(n_device))

    logging.debug("Query results: %r.", sorted(computed))

    assert expected == computed


def test_android_phone_transitive_match(graph: rdflib.Graph) -> None:
    """
    Confirm the Samsung device can be found by merit of being an Android Phone.  This test uses the transitive property skos:broaderTransitive to find whether the device is an Android Phone, or has Android Phone as a broader class 0 or mor skos:broader's away in the hierarchy.
    """

    expected = {str(NS_KB["samsung-device-uuid"])}
    computed = set()

    query = """\
SELECT ?nDevice
WHERE {
  ?nDevice
    core:hasFacet ?nDeviceFacet ;
    .

  ?nDeviceFacet
    observable:deviceType ?nDeviceType ;
    .

  ?nDeviceType
    skos:broaderTransitive* ?nDeviceTypeTaxon ;
    .

  ?nDeviceTypeTaxon
    skos:prefLabel "Android_Phone"@en-US ;
    .
}"""
    for result in graph.query(query):
        (n_device,) = result
        computed.add(str(n_device))

    logging.debug("Query results: %r.", sorted(computed))

    assert expected == computed


def test_mobile_phone_transitive_match(graph: rdflib.Graph) -> None:
    """
    Confirm the Samsung device can be found by merit of being a Mobile Phone.  However, at this breadth of search, at least one other phone is found.
    """

    expected = {str(NS_KB["samsung-device-uuid"])}
    computed = set()

    query = """\
SELECT ?nDevice
WHERE {
  ?nDevice
    core:hasFacet ?nDeviceFacet ;
    .

  ?nDeviceFacet
    observable:deviceType ?nDeviceType ;
    .

  ?nDeviceType
    skos:broaderTransitive* ?nDeviceTypeTaxon ;
    .

  ?nDeviceTypeTaxon
    skos:prefLabel "Mobile_Phone"@en-US ;
    .
}"""
    for result in graph.query(query):
        (n_device,) = result
        computed.add(str(n_device))

    logging.debug("Query results: %r.", sorted(computed))

    assert expected < computed
