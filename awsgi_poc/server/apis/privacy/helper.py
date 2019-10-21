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
