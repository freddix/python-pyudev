%define 	module	pyudev

Summary:	Pure Python libudev binding
Name:		python-%{module}
Version:	0.16.1
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/pyudev/%{module}-%{version}.tar.gz
# Source0-md5:	4034de584b6d9efcbfc590a047c63285
URL:		http://pyudev.readthedocs.org/en/latest/index.html
BuildRequires:	python-modules
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pyudev is a LGPL licenced, pure Python 2 binding to libudev,
the device and hardware management and information library of Linux.

%package -n python3-%{module}
Summary:	Pure Python libudev binding
Group:		Development/Languages/Python
Requires:	python3-modules

%description -n python3-%{module}
pyudev is a LGPL licenced, pure Python 3 binding to libudev,
the device and hardware management and information library of Linux.

%prep
%setup -qn %{module}-%{version}

%build
%{__python} setup.py build -b python
%{__python3} setup.py build -b python3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b python install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%{__python3} setup.py build -b python3 install \
	--optimize=2		\
	--root=$RPM_BUILD_ROOT	\
	--skip-build

%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info

