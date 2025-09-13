Name:		python-spdx-license-list
Version:	3.27.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/spdx-license-list/spdx_license_list-%{version}.tar.gz
Summary:	SPDX License List as a Python dictionary
URL:		https://pypi.org/project/spdx-license-list/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
SPDX License List as a Python dictionary

%files
%{py_sitedir}/spdx_license_list
%{py_sitedir}/spdx_license_list-*.*-info
