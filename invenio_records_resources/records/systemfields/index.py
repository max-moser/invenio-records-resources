# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
# Copyright (C) 2022 TU Wien.
#
# Invenio-Records-Resources is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Index field."""

from invenio_records.systemfields import SystemField
from invenio_search import current_search_client
from invenio_search.engine import dsl
from invenio_search.utils import prefix_index
from werkzeug.local import LocalProxy


class IndexField(SystemField):
    """Index field."""

    def __init__(self, index_or_alias, search_alias=None):
        """Initialize the IndexField.

        :param index_or_alias: An index instance or name of index/alias.
        :param search_alias: Name of alias to use for searches.
        """

        if isinstance(index_or_alias, dsl.Index):
            self._index = index_or_alias
        else:
            name = LocalProxy(lambda: prefix_index(index_or_alias))
            self._index = dsl.Index(name, using=current_search_client)

        # Set search alias name directly on the index
        self._index.search_alias = search_alias or self._index._name

    #
    # Data descriptor methods (i.e. attribute access)
    #
    def __get__(self, record, owner=None):
        """Get the persistent identifier."""
        return self._index
