from typing import List

from entities.search_parameter import SearchParameter
from repositories.base_repository import BaseRepository


class SearchParameterRepository(BaseRepository):
    """
    A repository class for managing SearchParameters and collections of them.
    """

    def get_collection_names(self) -> List[str]:
        """
        Returns list of the names of the search parameter collections.
        """
        rows = self.trivial_select("search_parameter_collection", ["name"])
        return [row["name"] for row in rows]

    def create_collection(self, name: str):
        """
        Creates a SearchParameter collection with `name`.
        """
        self.trivial_insert("search_parameter_collection", {"name": name})

    def get_collection_id_by_name(self, name: str) -> int | None:
        """
        Returns SearchParameter id by name `name`,
        """
        row = self.trivial_id_select(
            "search_parameter_collection", ["search_parameter_collection_id"], "name", name
        )
        if row is None:
            return None
        return row["search_parameter_collection_id"]

    def get_collection_params(self, collection_id: int) -> List[SearchParameter]:
        """
        Returns all SearchParameter that belong to collection with id `collection_id`,
        """
        param = SearchParameter("search_parameter_collection_id", collection_id)
        rows = self.trivial_select_with_params(
            "search_parameter", SearchParameter.columns(), [param]
        )
        return [SearchParameter.from_row(row) for row in rows]

    def create_many_search_parameters(self, search_parameters: List[SearchParameter]):
        """
        Creates many SearchParameters with information from elements of `search_parameters`.
        """
        self.trivial_insert_many(
            "search_parameter",
            [
                {
                    "column": param.column,
                    "value": param.value,
                    "relation": param.relation,
                    "search_parameter_collection_id": param.search_parameter_collection_id,
                }
                for param in search_parameters
            ],
        )
