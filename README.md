# pyDOI -- Python DOI Resolver

[![badge:pypi-version](https://img.shields.io/pypi/v/pyDOI.svg)](https://pypi.org/project/pyDOI)
[![badge:py-versions](https://img.shields.io/pypi/pyversions/pyDOI.svg)](https://pypi.org/project/pyDOI)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white.svg)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/lcnittl/pyDOI/master.svg)](https://results.pre-commit.ci/latest/github/lcnittl/pyDOI/master)
[![Code style: black](https://img.shields.io/badge/code_style-black-000000.svg)](https://github.com/psf/black)
[![Code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)

Wrapper for the [DOI system Proxy Server REST API][api-docs] (see also
[here][api-docs2]).

## Usage

```ipython
In [1]: import pydoi

In [2]: # Get full response

In [3]: pydoi.resolve("10.1002/chem.202000622")
Out[3]:
{'responseCode': 1,
 'handle': '10.1002/chem.202000622',
 'values': [{'index': 1,
   'type': 'URL',
   'data': {'format': 'string',
    'value': 'https://onlinelibrary.wiley.com/doi/10.1002/chem.202000622'},
   'ttl': 86400,
   'timestamp': '2020-09-25T16:02:07Z'},
  {'index': 700050,
   'type': '700050',
   'data': {'format': 'string', 'value': '2020100503563800217'},
   'ttl': 86400,
   'timestamp': '2020-10-05T12:25:43Z'},
  {'index': 100,
   'type': 'HS_ADMIN',
   'data': {'format': 'admin',
    'value': {'handle': '0.na/10.1002',
     'index': 200,
     'permissions': '111111110010'}},
   'ttl': 86400,
   'timestamp': '2020-03-30T02:01:43Z'}]}

In [4]: # Get URL

In [5]: pydoi.get_url("10.1016/j.chempr.2020.04.016")
Out[5]: 'https://linkinghub.elsevier.com/retrieve/pii/S2451929420301844'

In [6]: ## Get URL(s) from "10320/loc" type records

In [7]: pydoi.get_url("10.6567/IFToMM.14TH.WC.OS3.029")
Out[7]: 'https://www.airitilibrary.com/Publication/alDetailedMesh?DocID=P20150909001-201510-201510260026-201510260026-672-680'

In [8]: pydoi.get_url("10.6567/IFToMM.14TH.WC.OS3.029", allow_multi=True)
Out[8]:
['http://www.airitilibrary.cn/Publication/alDetailedMesh?DocID=P20150909001-201510-201510260026-201510260026-672-680',
 'https://www.airitilibrary.com/Publication/alDetailedMesh?DocID=P20150909001-201510-201510260026-201510260026-672-680']

In [9]: # pyDOI supports the use of query parameters

In [10]: pydoi.resolve("10.1002/anie.201804551", params=[("type", "URL")])
Out[10]:
{'responseCode': 1,
 'handle': '10.1002/anie.201804551',
 'values': [{'index': 1,
   'type': 'URL',
   'data': {'format': 'string',
    'value': 'https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.201804551'},
   'ttl': 86400,
   'timestamp': '2020-03-19T11:37:54Z'}]}

In [11]: pydoi.resolve("10.1002/anie.201804551", params=[("type", "HS_ADMIN")])
Out[11]:
{'responseCode': 1,
 'handle': '10.1002/anie.201804551',
 'values': [{'index': 100,
   'type': 'HS_ADMIN',
   'data': {'format': 'admin',
    'value': {'handle': '0.na/10.1002',
     'index': 200,
     'permissions': '111111110010'}},
   'ttl': 86400,
   'timestamp': '2018-05-15T11:31:52Z'}]}
```

### Installation

Installable with `pip`.

```cmd
pip install pyDOI
```

## License

GNU General Public License v3.0 or later

See [LICENSE][license] for the full text.

[api-docs]: https://www.doi.org/factsheets/DOIProxy.html#rest-api
[api-docs2]: https://www.doi.org/doi_handbook/3_Resolution.html#3.8.3
[license]: LICENSE
[pypi]: https://pypi.org/
