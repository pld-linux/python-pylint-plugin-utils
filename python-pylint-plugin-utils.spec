#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	pylint-plugin-utils
Summary:	Utilities and helpers for writing Pylint plugins
Name:		python-%{module}
Version:	0.2.3
Release:	2
License:	GPL v2
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/pylint-plugin-utils/%{module}-%{version}.tar.gz
# Source0-md5:	6a4a1b351df33574c7e1650de6032bdb
URL:		https://github.com/landscapeio/pylint-plugin-utils
BuildRequires:	rpm-pythonprov
# for the py_build, py_install macros
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities and helpers for writing Pylint plugins.

%package -n python3-%{module}
Summary:	Utilities and helpers for writing Pylint plugins
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Utilities and helpers for writing Pylint plugins.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/pylint_plugin_utils
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/pylint_plugin_utils-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-pylint-plugin-utils
%defattr(644,root,root,755)
%{py3_sitescriptdir}/pylint_plugin_utils
%{py3_sitescriptdir}/pylint_plugin_utils-%{version}-py*.egg-info
%endif
