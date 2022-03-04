# TODO

* Describe the "governance process": https://unifiedcyberontology.atlassian.net/browse/OC-140?focusedCommentId=10641

Table of Contents

* [Contribute to the Vocabulary of Devices and their Types (Voc-DT)](#contribute-to-the-vocabulary-of-devices-and-their-types-(voc-dt))
* [Ground rules & expectations](#ground-rules-&-expectations)
* [Contribute!](#contribute!)
  * [Background](#background)
    * [Nodes and labels](#nodes-and-labels)
    * [SKOS implementation](#skos-implementation)
  * [Types of contributions we're looking for](#types-of-contributions-we're-looking-for)
  * [How to contribute: Adding new entries](#how-to-contribute:-adding-new-entries)
    * [Define your change](#define-your-change)
    * [Hierarchy of your change](#hierarchy-of-your-change)
    * [Fork git](#fork-git)
    * [Implement your change](#implement-your-change)
    * [Test your change](#test-your-change)
    * [Pull Request Process](#pull-request-process)
  * [Style guide](#style-guide)
  * [How to contribute: Modifying existing entries](#how-to-contribute:-modifying-existing-entries)
  * [Community](#community)
* [References](#references)

# Contribute to the Vocabulary of Devices and their Types (Voc-DT)

# Ground rules & expectations

Before engaging on this project, please take note of a few things that we expect from you and that you can expect from others:

* When contributing to this vocabulary, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change. 
* When adding content, please consider that your contributions are widely used. As a consequence, maximise the quality of your contributions by accounting for clarity, comprehensibility and correctness. When in doubt, please consult us.
* If you open a pull request, please ensure that your contribution passes all tests. If there are test failures, you will need to address them before we can merge your contribution.
* Open Source Guides are released with a Contributor Code of Conduct. By participating in this project, you agree to abide by the terms expressed here: [Contributor Covenant][case:coc]. Please follow it in all your interactions with the project.

# Contribute!

## Background

We build on the [SKOS infrastructure](https://www.w3.org/TR/2009/REC-skos-reference-20090818/#L879) that allows for simplicity as well as consistency. This implies that you are expected to be familiar with SKOS, so please refer to the [SKOS Primer](https://www.w3.org/TR/skos-primer/) if you are not, yet. 

### Nodes and labels
Adding a new device, or a new category of devices, or any other concept in a SKOS-taxonomy translates in adding a node to the taxonomy. It is this node that is used by any mechanical operation involving this taxonomy. The consequence of this is that a node shall be unique: locally amongst all other nodes in the taxonomy, as well as globally amongst all other nodes that are defined in any other taxonomy or ontology. Being globally unique is accomplished by applying a unique namespace for this taxonomy that sets it apart from any other taxonomy or ontology in the world. Being locally unique is achieved by [generating a Universal Unique Identifier (UUID)][uuid]. Although the latter can also be considered globally unique, the combination of both is not only guaranteed to be globally unique, but also to be *dereferencable* as it embodies a URI: "the act of retrieving a representation of a resource identified by a URI is known as dereferencing that URI. This way, user agents can retrieve facts about the concept the URI is identifying."[^1] 

One of Time Berners-Lee's Four Rules[^2] reads "When someone looks up a URI, provide useful information, using the standards". However, the node itself may uniquely identify the concept but in itself does not provide any useful information whatsoever. Enter *labels*. Labels are defined as annotation properties that should be used to provide a human-readable version of a resource's name[^3]. Labels have proven to be of unquestionable assistance for human understanding, supporting ontology developers and adopters in checking consistency and avoiding inaccuracies. 

In conclusion, any newly added concept adds a node, uniquely identified by URI, with human readable labels.

### SKOS implementation
Every node that you add will be implemented as part of a larger skos-taxonomy. In the context of this SKOS-taxonomy, a *device* or *category of devices* will be implemented as a [`skos:Concept`][skos:concept], particularly as an [`observable:DeviceTypeConcept`][uco:devicetypeconcept] (refer to the [Style guide](#style-guide)). 

The intent of a [`skos:ConceptScheme`][skos:conceptscheme] is to capture a single complete taxonomy, enforcing a hierarchy of terms (a tree). Higher terms denote more abstract categories that address only a single or few shared characteristics, whereas lower terms denote more specific categories that share a lot of characteristics. The most specific categories, i.e., the *leafs*, of a concept scheme can almost describe individuals.


## Types of contributions we're looking for

Contributions to this **Vocabulary of Devices and their Types** (Voc-DT) come in two flavours:

1. Suggestions to correct, modify or otherwise improve what is already available in Voc-DT.
1. Suggestions to add new devices or category of devices.

We apply the following definitions:

**device**: Any piece of equipment or mechanism designed to serve a special purpose or perform a special function in the digital domain. Although a device can require additional devices before it can be effectively used, in itself it embodies a complete unit.

**category**: A class or division of devices regarded as having particular shared characteristics. These characteristics are not required to be of technological nature. 

## How to contribute: Adding new entries
 
> This and lower sections are under development

### Define your change

> Describe the new concept (term) or category in plain english.

### Hierarchy of your change

> You are adding vocabulary elements to this taxonomy, hence be aware of the current taxonomic structure and specify where your contributions fit the right level. Include a description of narrower / broader;

### Fork git

> refer to ....

### Implement your change

### Test your change

### Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
1. You may merge the Pull Request in once you have the sign-off of two other developers, or if you 
   do not have permission to do that, you may request the second reviewer to merge it for you.


## Style guide
Please make sure that your contributions match these styles:
* `skos:prefLabel`: One preferred label as short name for the device, including the @en-US language tag;
  * More preferred labels are ***only*** allowed with distinct language tag.
* `rdfs:seeAlso`: Refer to a product page or other proof of device existence;
* base name of taxon is must be a UUID
* manufacturer if I can find a proper already available property name, e.g., DCT.
* (opt) alt-labels, abbrevs (non-unique)

You can make use of the following template; lines starting with `#` denote optional labels:
```

dt:<device UUID>                                        # Your generated UUID for this device's make and model
  a observable:DeviceTypeConcept ;                      # Necessary to integrate it in CASE
  skos:inScheme dt:Device_Types_Scheme ;                # Necessary to integrate in in CASE
  skos:prefLabel "<The device's used name>"@en-US ;     # The (preferrably) unique name of the device, e.g., "Samsung SM-G925F"
  skos:definition "<The device's full name>"@en-US ;    # The full descriptive name of the device, e.g., "Samsung SM-G925F Galaxy S6 Edge"
#  skos:altLabel "<Abbrevs, synonyms>"@en-US ;          # Zero or more altLabels providing other characteristics, carrying an appropriate language tag
#  omr-rs:RegStatus omr-rs:1002 ;
  skos:broader dt:Android_Phone ;                       # Specifying its place in the hierarchy
  rdfs:seeAlso <https://shop.fairphone.com/en/fairphone-4-overview> .  # Link to product page or other proof of device's existence.

```


## How to contribute: Modifying existing entries
 
> This section is under development

## Community
Discussions about the Open Source Guides take place on this repository's [Issues](https://github.com/plbt5/voc-dt/issues) and [Pull Requests](https://github.com/plbt5/voc-dt/pulls) sections. Anybody is welcome to join these conversations.

Wherever possible, do not take these conversations to private channels, including contacting the maintainers directly. Keeping communication public means everybody can benefit and learn from the conversation.

# References

[^1]: Colpaert P., Verborgh R., Mannens E., Van de Walle R. (2014) [Painless URI Dereferencing Using the DataTank](https://doi.org/10.1007/978-3-319-11955-7_39). In: Presutti V., Blomqvist E., Troncy R., Sack H., Papadakis I., Tordai A. (eds) The Semantic Web: ESWC 2014 Satellite Events. ESWC 2014. Lecture Notes in Computer Science, vol 8798. Springer

[^2]: Tim Berners-Lee, [Design Issues / Linked Data](https://www.w3.org/DesignIssues/LinkedData.html), 2009, Status: personal view only. Editing status: imperfect but published. 

[^3] Brickley, Dan and Guha, R.V. (2004), [RDF Vocabulary Description Language 1.0: RDF Schema](http://www.w3.org/TR/2004/REC-rdf-schema-20040210/)


[skos:concept]: https://www.w3.org/TR/2009/REC-skos-reference-20090818/#concepts
[skos:conceptscheme]: https://www.w3.org/TR/2009/REC-skos-reference-20090818/#schemes
[skos:label]: https://www.w3.org/TR/2009/REC-skos-reference-20090818/#labels
[uuid]: https://www.uuidtools.com/what-is-uuid
[uco:devicetypeconcept]: https://caseontology.org/documentation/class-observabledevicetypeconcept.html
[case:coc]: https://caseontology.org/resources/coc.html
