%define module spdx_license_list

Name:		python-spdx-license-list
Version:	3.28.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/spdx-license-list/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	SPDX License List as a Python dictionary
URL:		https://pypi.org/project/spdx-license-list/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
SPDX License List as a Python dictionary

%files
%doc README.md
%license LICENSE
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
