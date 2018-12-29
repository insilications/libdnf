#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libdnf
Version  : 0.17.2
Release  : 22
URL      : https://github.com/rpm-software-management/libdnf/archive/0.17.2.tar.gz
Source0  : https://github.com/rpm-software-management/libdnf/archive/0.17.2.tar.gz
Summary  : Library providing simplified C and Python API to libsolv
Group    : Development/Tools
License  : GPL-2.0+ LGPL-2.0 LGPL-2.1 LGPL-2.1+
Requires: libdnf-python3
Requires: libdnf-lib
Requires: libdnf-license
Requires: libdnf-locales
Requires: libdnf-python
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : gettext-dev
BuildRequires : glibc-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(cppunit)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk-doc)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(librepo)
BuildRequires : pkgconfig(libsolv)
BuildRequires : pkgconfig(modulemd)
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(smartcols)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : popt-dev
BuildRequires : python3-dev
BuildRequires : swig
Patch1: 0001-sphinx-build-isn-t-postfixed-with-3.patch
Patch2: 0002-Fix-lookup-for-LibSolv-package.patch
Patch3: less-fsync.patch

%description
A Library providing simplified C and Python API to libsolv.

%package dev
Summary: dev components for the libdnf package.
Group: Development
Requires: libdnf-lib
Provides: libdnf-devel

%description dev
dev components for the libdnf package.


%package doc
Summary: doc components for the libdnf package.
Group: Documentation

%description doc
doc components for the libdnf package.


%package lib
Summary: lib components for the libdnf package.
Group: Libraries
Requires: libdnf-license

%description lib
lib components for the libdnf package.


%package license
Summary: license components for the libdnf package.
Group: Default

%description license
license components for the libdnf package.


%package locales
Summary: locales components for the libdnf package.
Group: Default

%description locales
locales components for the libdnf package.


%package python
Summary: python components for the libdnf package.
Group: Default
Requires: libdnf-python3

%description python
python components for the libdnf package.


%package python3
Summary: python3 components for the libdnf package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libdnf package.


%prep
%setup -q -n libdnf-0.17.2
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535567255
mkdir -p clr-build
pushd clr-build
%cmake .. -DPYTHON_DESIRED=3
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1535567255
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libdnf
cp COPYING %{buildroot}/usr/share/doc/libdnf/COPYING
pushd clr-build
%make_install
popd
%find_lang libdnf

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libdnf/dnf-advisory.h
/usr/include/libdnf/dnf-advisorypkg.h
/usr/include/libdnf/dnf-advisoryref.h
/usr/include/libdnf/dnf-context.h
/usr/include/libdnf/dnf-db.h
/usr/include/libdnf/dnf-enums.h
/usr/include/libdnf/dnf-goal.h
/usr/include/libdnf/dnf-keyring.h
/usr/include/libdnf/dnf-lock.h
/usr/include/libdnf/dnf-package.h
/usr/include/libdnf/dnf-packagedelta.h
/usr/include/libdnf/dnf-reldep-list.h
/usr/include/libdnf/dnf-reldep.h
/usr/include/libdnf/dnf-repo-loader.h
/usr/include/libdnf/dnf-repo.h
/usr/include/libdnf/dnf-rpmts.h
/usr/include/libdnf/dnf-sack.h
/usr/include/libdnf/dnf-state.h
/usr/include/libdnf/dnf-transaction.h
/usr/include/libdnf/dnf-types.h
/usr/include/libdnf/dnf-utils.h
/usr/include/libdnf/dnf-version.h
/usr/include/libdnf/hy-goal.h
/usr/include/libdnf/hy-package.h
/usr/include/libdnf/hy-packageset.h
/usr/include/libdnf/hy-query.h
/usr/include/libdnf/hy-repo.h
/usr/include/libdnf/hy-selector.h
/usr/include/libdnf/hy-subject.h
/usr/include/libdnf/hy-types.h
/usr/include/libdnf/hy-util.h
/usr/include/libdnf/libdnf.h
/usr/include/libdnf/log.hpp
/usr/include/libdnf/logger.hpp
/usr/include/libdnf/nevra.hpp
/usr/include/libdnf/nsvcap.hpp
/usr/lib64/libdnf.so
/usr/lib64/pkgconfig/libdnf.pc
/usr/share/man/man3/hawkey.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libdnf/html/common.css
/usr/share/gtk-doc/html/libdnf/html/index.htm

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdnf.so.2

%files license
%defattr(-,root,root,-)
/usr/share/doc/libdnf/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f libdnf.lang
%defattr(-,root,root,-)

