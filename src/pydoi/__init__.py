from __future__ import annotations

import logging
from typing import Any, Optional, Union

import requests

logger = logging.getLogger("pydoi")


API_RESPONSES = {
    1: {"msg": "Success.", "status_code": 200},
    2: {
        "msg": "Error. Something unexpected went wrong during handle resolution.",
        "status_code": 500,
    },
    100: {"msg": "Handle Not Found.", "status_code": 404},
    200: {
        "msg": "Values Not Found. The handle exists but has no values (or no values according to the types and indices specified).",
        "status_code": 200,
    },
}


def resolve(
    handle: str,
    /,
    *,
    params: Union[dict[str, Any], list[Union[tuple, bytes]]] = None,
    **kwargs,
) -> dict:
    r"""Return a dict of the server JSON response for a given DOI.

    According to https://www.doi.org/factsheets/DOIProxy.html#rest-api

    :param handle: (str) DOI.
    :param params: (optional) Dictionary, list of tuples or bytes to send in the query
        string for the :class:`Request` (cf ``request.get()``). Known query keywords
        are:
          - ``callback`` (bool) Get JSONP callback
          - ``pretty`` (bool) Get pretty printed JSON output
          - ``auth`` (bool) Bypass proxy server cache and query a primary handle server
              directly for the newest handle data.
          - ``cert`` (bool) Request an authenticated response from the source handle
              server. Not generally needed by end users.
          - ``type`` (str) Allows the resolution response to be restricted to specific
              types of interest.
          - ``index`` (int) Allows the resolution response to be restricted to specific
              indexes of interest.
         Multiple "type" and "index" parameters are allowed. Returned values match *any*
         of the specified types or indexes.
    :param \*\*kwargs: Optional arguments that ``request.get()`` takes.
    :return: :class:`dict` object
    :rtype: dict
    """

    if "url" in kwargs:
        logger.warning("Key 'url' is not passed to requests.get()")
        kwargs.pop("url")
    url = "https://doi.org/api/handles/" + handle

    response = requests.get(url, params=params, **kwargs)

    if response.status_code not in [
        api_response["status_code"] for api_response in API_RESPONSES.values()
    ]:
        logger.critical(
            "Status Code %s: %s",
            response.status_code,
            requests.status_codes._codes[response.status_code][0],
        )
        # TODO: raise error and pass on status_code
        return None

    data = response.json()
    logger.debug("Response data: %s", data)
    if data["responseCode"] != 1:
        logger.error(
            "Response Code %s: %s",
            data["responseCode"],
            API_RESPONSES[data["responseCode"]]["msg"],
        )
        # TODO: raise error and pass on responseCode ?
        # return
    return data


def get_url(doi: str) -> str:
    """Resolve given DOI and return its target URL."""
    response = resolve(doi, params={"type": "URL"})
    if "values" in response:
        return response["values"][0]["data"]["value"]

    logger.error("Failed to get URL from DOI.")
    return None
