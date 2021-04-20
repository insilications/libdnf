#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libdnf
Version  : 0.62.0
Release  : 45
URL      : https://github.com/rpm-software-management/libdnf/archive/refs/tags/0.62.0.tar.gz
Source0  : https://github.com/rpm-software-management/libdnf/archive/refs/tags/0.62.0.tar.gz
Summary  : Library providing simplified C and Python API to libsolv
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-2.1+
Requires: libdnf-lib = %{version}-%{release}
Requires: libdnf-locales = %{version}-%{release}
Requires: libdnf-man = %{version}-%{release}
Requires: libdnf-python = %{version}-%{release}
Requires: libdnf-python3 = %{version}-%{release}
BuildRequires : Flask
BuildRequires : Sphinx
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : check-dev
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : expat-staticdev
BuildRequires : gettext-dev
BuildRequires : git
BuildRequires : glibc-bin
BuildRequires : gnupg
BuildRequires : gpgme
BuildRequires : gpgme-dev
BuildRequires : gtk-doc-data
BuildRequires : json-c
BuildRequires : json-c-dev
BuildRequires : json-c-staticdev
BuildRequires : libassuan-dev
BuildRequires : libcomps-dev
BuildRequires : libcomps-staticdev
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libmodulemd
BuildRequires : libmodulemd-dev
BuildRequires : libmodulemd-staticdev
BuildRequires : librepo-dev
BuildRequires : librepo-staticdev
BuildRequires : libsolv-dev
BuildRequires : libsolv-staticdev
BuildRequires : libstdc++
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : m4
BuildRequires : nettle-dev
BuildRequires : nettle-staticdev
BuildRequires : nose
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
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
BuildRequires : pkgconfig(modulemd-2.0)
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(smartcols)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : popt-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : swig
BuildRequires : xattr
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-lookup-for-LibSolv-package.patch
Patch2: 0002-do-fewer-fsyncs.patch

%description
A Library providing simplified C and Python API to libsolv.

%package dev
Summary: dev components for the libdnf package.
Group: Development
Requires: libdnf-lib = %{version}-%{release}
Provides: libdnf-devel = %{version}-%{release}
Requires: libdnf = %{version}-%{release}

%description dev
dev components for the libdnf package.


%package lib
Summary: lib components for the libdnf package.
Group: Libraries

%description lib
lib components for the libdnf package.


%package locales
Summary: locales components for the libdnf package.
Group: Default

%description locales
locales components for the libdnf package.


%package man
Summary: man components for the libdnf package.
Group: Default

%description man
man components for the libdnf package.


%package python
Summary: python components for the libdnf package.
Group: Default
Requires: libdnf-python3 = %{version}-%{release}

%description python
python components for the libdnf package.


%package python3
Summary: python3 components for the libdnf package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libdnf package.


%prep
%setup -q -n libdnf-0.62.0
cd %{_builddir}/libdnf-0.62.0
%patch1 -p1
%patch2 -p1

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618943926
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment  -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export FCFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment  -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export FFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment  -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment  -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_GEN"
export LDFLAGS_GENERATE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment  -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno  -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16  -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno  -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16  -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno  -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16  -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno  -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16  -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno  -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16  -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%cmake .. -DWITH_BINDINGS=ON \
-DWITH_GTKDOC=OFF \
-DWITH_HTML=OFF \
-DWITH_MAN=ON \
-DWITH_ZCHUNK=OFF \
-DENABLE_RHSM_SUPPORT=OFF \
-DENABLE_SOLV_URPMREORDER=OFF \
-DPYTHON_DESIRED=3 \
-DENABLE_STATIC=OFF
make  %{?_smp_mflags}

ctest --parallel 16 -V --progress || :
#make -j1 check || :
make -j1 test  || :
find . -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%cmake .. -DWITH_BINDINGS=ON \
-DWITH_GTKDOC=OFF \
-DWITH_HTML=OFF \
-DWITH_MAN=ON \
-DWITH_ZCHUNK=OFF \
-DENABLE_RHSM_SUPPORT=OFF \
-DENABLE_SOLV_URPMREORDER=OFF \
-DPYTHON_DESIRED=3 \
-DENABLE_STATIC=OFF
make  %{?_smp_mflags}
fi
popd

%install
export SOURCE_DATE_EPOCH=1618943926
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang libdnf

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libdnf/conf/Config.hpp
/usr/include/libdnf/conf/ConfigMain.hpp
/usr/include/libdnf/conf/ConfigParser.hpp
/usr/include/libdnf/conf/ConfigRepo.hpp
/usr/include/libdnf/conf/Option.hpp
/usr/include/libdnf/conf/OptionBinds.hpp
/usr/include/libdnf/conf/OptionBool.hpp
/usr/include/libdnf/conf/OptionChild.hpp
/usr/include/libdnf/conf/OptionEnum.hpp
/usr/include/libdnf/conf/OptionNumber.hpp
/usr/include/libdnf/conf/OptionPath.hpp
/usr/include/libdnf/conf/OptionSeconds.hpp
/usr/include/libdnf/conf/OptionString.hpp
/usr/include/libdnf/conf/OptionStringList.hpp
/usr/include/libdnf/config.h
/usr/include/libdnf/dnf-advisory.h
/usr/include/libdnf/dnf-advisorypkg.h
/usr/include/libdnf/dnf-advisoryref.h
/usr/include/libdnf/dnf-conf.h
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
/usr/include/libdnf/hy-nevra.h
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
/usr/include/libdnf/nevra.hpp
/usr/include/libdnf/nsvcap.hpp
/usr/include/libdnf/plugin/plugin.h
/usr/include/libdnf/utils/PreserveOrderMap.hpp
/usr/include/libdnf/utils/logger.hpp
/usr/lib64/libdnf.so
/usr/lib64/libdnf/plugins/README
/usr/lib64/pkgconfig/libdnf.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdnf.so.2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man3/hawkey.3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f libdnf.lang
%defattr(-,root,root,-)

