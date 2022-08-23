#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sos
Version  : 3.8
Release  : 42
URL      : https://github.com/sosreport/sos/archive/3.8.tar.gz
Source0  : https://github.com/sosreport/sos/archive/3.8.tar.gz
Summary  : Script of Scripts (SoS): an interactive, cross-platform, and cross-language workflow system for reproducible data analysis
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: sos-bin = %{version}-%{release}
Requires: sos-data = %{version}-%{release}
Requires: sos-license = %{version}-%{release}
Requires: sos-locales = %{version}-%{release}
Requires: sos-man = %{version}-%{release}
Requires: sos-python = %{version}-%{release}
Requires: sos-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(coverage)
BuildRequires : pypi(nose)
BuildRequires : pypi(pycodestyle)
BuildRequires : pypi(sphinx)
BuildRequires : pypi-six
Patch1: 0001-Add-stateless-handling.patch

%description
Sos is a set of tools that gathers information about system
hardware and configuration. The information can then be used for
diagnostic purposes and debugging. Sos is commonly used to help
support technicians and developers.

%package bin
Summary: bin components for the sos package.
Group: Binaries
Requires: sos-data = %{version}-%{release}
Requires: sos-license = %{version}-%{release}

%description bin
bin components for the sos package.


%package data
Summary: data components for the sos package.
Group: Data

%description data
data components for the sos package.


%package license
Summary: license components for the sos package.
Group: Default

%description license
license components for the sos package.


%package locales
Summary: locales components for the sos package.
Group: Default

%description locales
locales components for the sos package.


%package man
Summary: man components for the sos package.
Group: Default

%description man
man components for the sos package.


%package python
Summary: python components for the sos package.
Group: Default
Requires: sos-python3 = %{version}-%{release}

%description python
python components for the sos package.


%package python3
Summary: python3 components for the sos package.
Group: Default
Requires: python3-core
Provides: pypi(sos)
Requires: pypi(fasteners)
Requires: pypi(jinja2)
Requires: pypi(nbformat)
Requires: pypi(networkx)
Requires: pypi(pexpect)
Requires: pypi(psutil)
Requires: pypi(ptyprocess)
Requires: pypi(pydot)
Requires: pypi(pydotplus)
Requires: pypi(pygments)
Requires: pypi(pyyaml)
Requires: pypi(pyzmq)
Requires: pypi(six)
Requires: pypi(tqdm)

%description python3
python3 components for the sos package.


%prep
%setup -q -n sos-3.8
cd %{_builddir}/sos-3.8
%patch1 -p1
pushd ..
cp -a sos-3.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658940764
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sos
cp %{_builddir}/sos-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/sos/1f199f2dcc0341653fc919334d9c26d0d2098f93
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
%find_lang sos
## install_append content
install -D sos.conf %{buildroot}/usr/share/defaults/sos/sos.conf
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sosreport

%files data
%defattr(-,root,root,-)
/usr/share/defaults/sos/sos.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sos/1f199f2dcc0341653fc919334d9c26d0d2098f93

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sosreport.1
/usr/share/man/man5/sos.conf.5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f sos.lang
%defattr(-,root,root,-)

