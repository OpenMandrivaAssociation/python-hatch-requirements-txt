%define module hatch-requirements-txt
%define oname hatch_requirements_txt

Name:		python-hatch-requirements-txt
Version:	0.4.1
Release:	1
Summary:	Hatchling plugin to read project dependencies from requirements.txt
License:	MIT
Group:		Development/Python
URL:		https://github.com/repo-helper/hatch-requirements-txt/
Source0:	https://github.com/repo-helper/hatch-requirements-txt/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
Hatchling plugin to read project dependencies from requirements.txt

%files
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}.dist-info
