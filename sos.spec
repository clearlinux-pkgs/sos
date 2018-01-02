#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sos
Version  : 3.5
Release  : 1
URL      : https://github.com/sosreport/sos/archive/3.5.tar.gz
Source0  : https://github.com/sosreport/sos/archive/3.5.tar.gz
Summary  : A set of tools to gather troubleshooting information from a system
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: sos-bin
Requires: sos-legacypython
Requires: sos-python3
Requires: sos-locales
Requires: sos-doc
Requires: sos-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Sos is a set of tools that gathers information about system
hardware and configuration. The information can then be used for
diagnostic purposes and debugging. Sos is commonly used to help
support technicians and developers.

%package bin
Summary: bin components for the sos package.
Group: Binaries

%description bin
bin components for the sos package.


%package doc
Summary: doc components for the sos package.
Group: Documentation

%description doc
doc components for the sos package.


%package legacypython
Summary: legacypython components for the sos package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the sos package.


%package locales
Summary: locales components for the sos package.
Group: Default

%description locales
locales components for the sos package.


%package python
Summary: python components for the sos package.
Group: Default
Requires: sos-legacypython
Requires: sos-python3

%description python
python components for the sos package.


%package python3
Summary: python3 components for the sos package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sos package.


%prep
%setup -q -n sos-3.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514919668
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1514919668
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
%find_lang sos

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sosreport

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f sos.lang
%defattr(-,root,root,-)

