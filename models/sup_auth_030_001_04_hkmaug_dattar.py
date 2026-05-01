from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "auth.030.001.04_HKMAUG_DATTAR/extension"


@dataclass(kw_only=True)
class Remarks:
    """
    Remarks.

    :ivar remarks: Remarks
    :ivar remarks1: Remarks1
    :ivar remarks2: Remarks2
    :ivar remarks3: Remarks3
    :ivar remarks4: Remarks4
    :ivar remarks5: Remarks5
    :ivar remarks6: Remarks6
    :ivar remarks7: Remarks7
    :ivar remarks8: Remarks8
    :ivar remarks9: Remarks9
    :ivar remarks10: Remarks10
    :ivar remarks11: Remarks11
    :ivar remarks12: Remarks12
    :ivar remarks13: Remarks13
    """

    remarks: None | str = field(
        default=None,
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 19,
        },
    )
    remarks1: None | str = field(
        default=None,
        metadata={
            "name": "Remarks1",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks2: None | str = field(
        default=None,
        metadata={
            "name": "Remarks2",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks3: None | str = field(
        default=None,
        metadata={
            "name": "Remarks3",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks4: None | str = field(
        default=None,
        metadata={
            "name": "Remarks4",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks5: None | str = field(
        default=None,
        metadata={
            "name": "Remarks5",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks6: None | str = field(
        default=None,
        metadata={
            "name": "Remarks6",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks7: None | str = field(
        default=None,
        metadata={
            "name": "Remarks7",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks8: None | str = field(
        default=None,
        metadata={
            "name": "Remarks8",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks9: None | str = field(
        default=None,
        metadata={
            "name": "Remarks9",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks10: None | str = field(
        default=None,
        metadata={
            "name": "Remarks10",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks11: None | str = field(
        default=None,
        metadata={
            "name": "Remarks11",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks12: None | str = field(
        default=None,
        metadata={
            "name": "Remarks12",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )
    remarks13: None | str = field(
        default=None,
        metadata={
            "name": "Remarks13",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
            "min_length": 1,
            "max_length": 255,
        },
    )


@dataclass(kw_only=True)
class HktrExtension:
    """
    HktrExtension.

    :ivar remarks: Remarks
    """

    remarks: Remarks = field(
        metadata={
            "name": "Remarks",
            "type": "Element",
            "namespace": "auth.030.001.04_HKMAUG_DATTAR/extension",
        }
    )


@dataclass(kw_only=True)
class Document:
    class Meta:
        namespace = "auth.030.001.04_HKMAUG_DATTAR/extension"

    hktr_extension: HktrExtension = field(
        metadata={
            "name": "HktrExtension",
            "type": "Element",
        }
    )
