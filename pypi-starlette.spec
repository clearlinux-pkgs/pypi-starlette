#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: 5424026
#
Name     : pypi-starlette
Version  : 0.43.0
Release  : 18
URL      : https://files.pythonhosted.org/packages/af/36/3a623a561dc8585a90973c8c0ed87511beebbe658c7e8f883fdab7ba55e1/starlette-0.43.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/af/36/3a623a561dc8585a90973c8c0ed87511beebbe658c7e8f883fdab7ba55e1/starlette-0.43.0.tar.gz
Summary  : The little ASGI library that shines.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-starlette-license = %{version}-%{release}
Requires: pypi-starlette-python = %{version}-%{release}
Requires: pypi-starlette-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<p align="center">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/encode/starlette/master/docs/img/starlette_dark.svg" width="420px">
<source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/encode/starlette/master/docs/img/starlette.svg" width="420px">
<img alt="starlette-logo" src="https://raw.githubusercontent.com/encode/starlette/master/docs/img/starlette_dark.svg">
</picture>
</p>

%package license
Summary: license components for the pypi-starlette package.
Group: Default

%description license
license components for the pypi-starlette package.


%package python
Summary: python components for the pypi-starlette package.
Group: Default
Requires: pypi-starlette-python3 = %{version}-%{release}

%description python
python components for the pypi-starlette package.


%package python3
Summary: python3 components for the pypi-starlette package.
Group: Default
Requires: python3-core
Provides: pypi(starlette)
Requires: pypi(anyio)

%description python3
python3 components for the pypi-starlette package.


%prep
%setup -q -n starlette-0.43.0
cd %{_builddir}/starlette-0.43.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735244225
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-starlette
cp %{_builddir}/starlette-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-starlette/5783431d2a7aa697a58a8dc3b55582716b335ec5 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-starlette/5783431d2a7aa697a58a8dc3b55582716b335ec5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
