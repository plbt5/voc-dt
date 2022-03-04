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

import argparse
import typing

import pandas
import rdflib.plugins.sparql

def apply_prefix(iri: str) -> str:
    return iri.replace("https://taxonomy.unifiedcyberontology.org/uco/device-types/", "dt:")



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("out_md", type=argparse.FileType("w"))
    parser.add_argument("taxonomy_ttl", type=argparse.FileType("r"))
    args = parser.parse_args()

    print(
        """\
# Device types documentation


## Taxonomy members
""",
        file=args.out_md
    )
    graph = rdflib.Graph()
    graph.parse(args.taxonomy_ttl)

    # Build hierarchy.
    taxon_to_broader_set: typing.Dict[rdflib.URIRef, typing.Set[rdflib.URIRef]] = dict()
    for result in graph.query(
        """\
SELECT ?nTaxon ?nBroaderTaxon
WHERE {
  ?nTaxon a observable:DeviceTypeConcept .
  OPTIONAL {
    ?nTaxon skos:broader ?nBroaderTaxon .
  }
}
"""
    ):
        (n_taxon, n_broader_taxon) = result
        if not n_broader_taxon is None:
            if not n_taxon in taxon_to_broader_set:
                taxon_to_broader_set[n_taxon] = set()
            taxon_to_broader_set[n_taxon].add(n_broader_taxon)

    records: typing.List[typing.Tuple[str, str, str]] = []
    for result in graph.query(
        """\
SELECT DISTINCT ?nTaxon ?lPrefLabel
WHERE {
  ?nTaxon a observable:DeviceTypeConcept .
  OPTIONAL {
    ?nTaxon skos:prefLabel ?lPrefLabel .
  }
}
ORDER BY ?lPrefLabel ?nTaxon
"""
    ):
        (n_taxon, l_pref_label) = result
        records.append(
            (
                "`%s`" % str(l_pref_label),
                "`%s`" % apply_prefix(str(n_taxon)),
                ", ".join(map(lambda x: "`%s`"%apply_prefix(x), sorted(taxon_to_broader_set.get(n_taxon, []))))
            )
        )
    df = pandas.DataFrame(records, columns=("Preferred label", "Taxon IRI", "Broader taxons"))
    table_text = df.to_markdown(index=False, tablefmt="github")
    print(table_text, file=args.out_md)

if __name__ == "__main__":
    main()
