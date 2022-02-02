# voc-dt
An open SKOS vocabulary on types of devices as a best-effort-taxonomy. A device might be inferrable to be a surveillance camera, but might not have a known market model, or might be completely custom-built)

# The current vocabulary

The following acronyms are used for relationships between terms:
* equivalence (USE/UF), 
* broader term (BT), 
* narrower term (NT),
* related term (RT)

## Device types
Paul Brandt (paul@brandt.name), Cyber-investigation Analysis Standard Expression (CASE)


    Adaptor
        DEF : Device that physical converts the pin outputs but does not alter the underlying protocol (e.g. uSD to SD, CF to ATA, etc.)
    Android_Phone
        DEF : A smart phone that applies the Android mobile operating system.
        BT : Smart_Phone
        TT : Mobile_Phone
    Cell_Phone
        UF : Cellular_Phone
        DEF : A cellular phone, cell phone, cellphone, handphone, or hand phone, sometimes shortened to simply mobile, cell or just phone, is a portable telephone that can make and receive calls over a radio frequency link while the user is moving within a telephone service area. Examples include Nokia 3310, Siemens A55
        BT : Mobile_Phone
        TT : Mobile_Phone
    Cellular_Phone
        USE : Cell_Phone
    Computer
        DEF : Floor/Desktop based computer, including standard workstations
    Digital_Camera
        DEF : A digital camera is a camera that captures photographs in digital memory as opposed to capturing images on photographic film.
    Embedded_Device
        DEF : An embedded device is a highly specialized microprocessor device meant for one or very few specific purposes and is usually embedded or included within another object or as part of a larger system. Examples include answer machine, door access logger, card scanner, etc.
    Laptop
        UF : Notebook
        DEF : Devices categorised by their manufacturer as a Laptop
        DEF : A laptop, laptop computer, or notebook computer is a small, portable personal computer with a screen and alphanumeric keyboard. These typically have a clam shell form factor with the screen mounted on the inside of the upper lid and the keyboard on the inside of the lower lid, although 2-in-1 PCs with a detachable keyboard are often marketed as laptops or as having a laptop mode.
    Media
        note : Possibly referenced by new MediaFacet
        DEF : Media refer to digital storage devices that apply electromagnetic or optical surfaces, or depend solely on electronic circuits as solid state storage, for storing digital data. Examples include HDD (PATA), SATA, SSD, Optical, Memory_Card, Tape, etc
    Mobile_Phone
        DEF : A portable telephone that at least can make and receive calls over a radio frequency link while the user is moving within a telephone service area. This category encompasses all types of mobiles, simple and smart and satellite ones all together.
        NT : Cell_Phone
        NT : Smart_Phone
    Notebook
        USE : Laptop
    Protocol_Converter
        DEF : Device that converts from one protocol to another (e.g. SD to USB, SATA to USB, etc.
    Server
        DEF : Server Rack-mount based computer, minicomputer, supercomputer, etc.
    Smart_Device
        DEF : Microprocessor IoT devices expected to be connected directly to cloud-based networks or via smartphone
    Smart_Phone
        note : Inferred by model and OperatingSystemFacet
        DEF : A smartphone is a portable device that combines mobile telephone and computing functions into one unit. Examples include iPhone, Samsung Galaxy, Huawei, Blackberry.
        BT : Mobile_Phone
        TT : Mobile_Phone
        NT : Android_Phone
    Tablet
        DEF : Devices categorised by their manufacturer as a Tablet
        DEF : A mobile computer that is primarily operated by touching the screen
    Write_Blocker
        DEF : Tableau, Cellibrite, Talon, et

    http://unifiedcyberontology.org/skos/Device_TypesDevice_Types_Scheme
        Adaptor
        Computer
        Digital_Camera
        Embedded_Device
        Laptop
        Media
        Mobile_Phone
            Cell_Phone
            Smart_Phone
                Android_Phone
        Protocol_Converter
        Server
        Smart_Device
        Tablet
        Write_Blocker

