from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"


@dataclass(kw_only=True)
class GenericOrganisationIdentification31:
    """
    GenericOrganisationIdentification3__1 Information related to an
    identification of an organisation.

    :ivar id: Identification Identification assigned by an institution.
    """

    class Meta:
        name = "GenericOrganisationIdentification3__1"

    id: str = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 20,
        }
    )


@dataclass(kw_only=True)
class OrganisationIdentification391:
    """
    OrganisationIdentification39__1 Unique and unambiguous way to identify
    an organisation.

    :ivar lei: LEI Legal entity identification as an alternate
        identification for a party.
    :ivar othr: Other Unique identification of an organisation, as
        assigned by an institution, using an identification scheme.
    """

    class Meta:
        name = "OrganisationIdentification39__1"

    lei: None | str = field(
        default=None,
        metadata={
            "name": "LEI",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "pattern": r"[A-Z0-9]{18,18}[0-9]{2,2}",
        },
    )
    othr: None | GenericOrganisationIdentification31 = field(
        default=None,
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass(kw_only=True)
class OrganisationIdentification392:
    """
    OrganisationIdentification39__2 Unique and unambiguous way to identify
    an organisation.

    :ivar othr: Other Unique identification of an organisation, as
        assigned by an institution, using an identification scheme.
    """

    class Meta:
        name = "OrganisationIdentification39__2"

    othr: GenericOrganisationIdentification31 = field(
        metadata={
            "name": "Othr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        }
    )


@dataclass(kw_only=True)
class Party52Choice1:
    """
    Party52Choice__1 Specifies the identification of a person or an
    organisation.

    :ivar org_id: OrganisationIdentification Unique and unambiguous way
        to identify an organisation.
    """

    class Meta:
        name = "Party52Choice__1"

    org_id: None | OrganisationIdentification391 = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass(kw_only=True)
class Party52Choice2:
    """
    Party52Choice__2 Specifies the identification of a person or an
    organisation.

    :ivar org_id: OrganisationIdentification Unique and unambiguous way
        to identify an organisation.
    """

    class Meta:
        name = "Party52Choice__2"

    org_id: None | OrganisationIdentification392 = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass(kw_only=True)
class PartyIdentification2721:
    """
    PartyIdentification272__1 Specifies the identification of a person or
    an organisation.

    :ivar id: Identification Unique and unambiguous identification of a
        party.
    """

    class Meta:
        name = "PartyIdentification272__1"

    id: Party52Choice1 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        }
    )


@dataclass(kw_only=True)
class PartyIdentification2722:
    """
    PartyIdentification272__2 Specifies the identification of a person or
    an organisation.

    :ivar id: Identification Unique and unambiguous identification of a
        party.
    """

    class Meta:
        name = "PartyIdentification272__2"

    id: Party52Choice2 = field(
        metadata={
            "name": "Id",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        }
    )


@dataclass(kw_only=True)
class Party51Choice1:
    """
    Party51Choice__1 Identification of a person, an organisation or a
    financial institution.

    :ivar org_id: OrganisationIdentification Identification of a person
        or an organisation.
    """

    class Meta:
        name = "Party51Choice__1"

    org_id: None | PartyIdentification2721 = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass(kw_only=True)
class Party51Choice2:
    """
    Party51Choice__2 Identification of a person, an organisation or a
    financial institution.

    :ivar org_id: OrganisationIdentification Identification of a person
        or an organisation.
    """

    class Meta:
        name = "Party51Choice__2"

    org_id: None | PartyIdentification2722 = field(
        default=None,
        metadata={
            "name": "OrgId",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        },
    )


@dataclass(kw_only=True)
class BusinessApplicationHeaderV04:
    """
    BusinessApplicationHeaderV04 The Business Layer deals with Business
    Messages.

    The behaviour of the Business Messages is fully described by the
    Business Transaction and the structure of the Business Messages is
    fully described by the Message Definitions and related Message Rules,
    Rules and Market Practices. All of which are registered in the ISO
    20022 Repository.&#13; A single new Business Message (with its
    accompagnying business application header) is created - by the sending
    MessagingEndpoint - for each business event; that is each interaction
    in a Business Transaction. A Business Message adheres to the following
    principles:&#13; " A Business Message (and its business application
    header) must not contain information about the Message Transport System
    or the mechanics or mechanism of message sending, transportation, or
    receipt. &#13; " A Business Message must be comprehensible outside of
    the context of the Transport Message. That is the Business Message must
    not require knowledge of the Transport Message to be understood.&#13; "
    A Business Message may contain headers, footers, and envelopes that are
    meaningful for the business. When present, they are treated as any
    other message content, which means that they are considered part of the
    Message Definition of the Business Message and as such will be part of
    the ISO 20022 Repository.&#13; " A Business Message refers to Business
    Actors by their Name. Each instance of a Business Actor has one Name.
    The Business Actor must not be referred to in the Transport Layer.&#13;
    Specific usage of this BusinessMessageHeader may be defined by the
    relevant SEG.

    :ivar fr: From The sending MessagingEndpoint that has created this
        Business Message for the receiving MessagingEndpoint that will
        process this Business Message.&#13; &#13; Note    the sending
        MessagingEndpoint might be different from the sending address
        potentially contained in the transport header (as defined in the
        transport layer).
    :ivar to: To The MessagingEndpoint designated by the sending
        MessagingEndpoint to be the recipient who will ultimately
        process this Business Message.&#13; &#13; Note the receiving
        MessagingEndpoint might be different from the receiving address
        potentially contained in the transport header (as defined in the
        transport layer).
    :ivar biz_msg_idr: BusinessMessageIdentifier Unambiguously
        identifies the Business Message to the MessagingEndpoint that
        has created the Business Message.
    :ivar msg_def_idr: MessageDefinitionIdentifier The Message
        Definition Identifier of the Business Message instance with
        which this Business Application Header instance is associated.
    :ivar cre_dt: CreationDate Date and time when this Business Message
        (header) was created.
    """

    fr: Party51Choice1 = field(
        metadata={
            "name": "Fr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        }
    )
    to: Party51Choice2 = field(
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        }
    )
    biz_msg_idr: str = field(
        metadata={
            "name": "BizMsgIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        }
    )
    msg_def_idr: str = field(
        metadata={
            "name": "MsgDefIdr",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
            "min_length": 1,
            "max_length": 35,
        }
    )
    cre_dt: XmlDateTime = field(
        metadata={
            "name": "CreDt",
            "type": "Element",
            "namespace": "urn:iso:std:iso:20022:tech:xsd:head.001.001.04",
        }
    )


@dataclass(kw_only=True)
class AppHdr(BusinessApplicationHeaderV04):
    class Meta:
        namespace = "urn:iso:std:iso:20022:tech:xsd:head.001.001.04"
