import typing as t


class Request(t.NamedTuple):
    id: str
    field1: str
    field2: str

    def to_json(self):
        return self._asdict()


requests_map = {item.id: item for item in [
    Request("1", "test", "test"),
    Request("2", "test", "test"),
    Request("3", "test", "test"),
]}


def get_response_by_request_id(request_id: str) -> dict:
    if request_id == "Cham":
        name = "Cham"
    elif request_id == "Serhii":
        name = "Serhii"
    elif request_id == "Ivan":
        name = "Ivan"
    else:
        return {}
    return {"hello": name}


def get_request_list() -> t.List[Request]:
    return list(requests_map.values())


def create_request(data: dict) -> t.Union[Request, None]:
    item = Request(**data)
    if requests_map.get(item.id):
        return None
    requests_map[item.id] = item
    return item


def get_request(request_id: str) -> t.Union[Request, None]:
    return requests_map.get(request_id)


def edit_request(request_id, data) -> t.Union[Request, None]:
    new_item = Request(**data)
    if not requests_map.get(request_id):
        return None
    requests_map[request_id] = new_item
    return new_item


def delete_request(request_id: str) -> bool:
    if not requests_map.get(requests_map):
        return False
    del requests_map[request_id]
    return True
