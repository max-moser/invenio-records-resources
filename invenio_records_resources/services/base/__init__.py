# -*- coding: utf-8 -*-
#
# Copyright (C) 2020-2024 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Base Service API."""

from .config import ServiceConfig
from .links import (
    ConditionalLink,
    EndpointLink,
    ExternalLink,
    Link,
    LinksTemplate,
    NestedLinks,
)
from .results import ServiceItemResult, ServiceListResult
from .service import Service

__all__ = (
    "ConditionalLink",
    "EndpointLink",
    "ExternalLink",
    "Link",
    "LinksTemplate",
    "Service",
    "ServiceConfig",
    "ServiceItemResult",
    "ServiceListResult",
    "NestedLinks",
)
