#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libffado
Version  : 2.4.3
Release  : 7
URL      : http://www.ffado.org/files/libffado-2.4.3.tgz
Source0  : http://www.ffado.org/files/libffado-2.4.3.tgz
Summary  : FFADO
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: libffado-bin = %{version}-%{release}
Requires: libffado-config = %{version}-%{release}
Requires: libffado-data = %{version}-%{release}
Requires: libffado-lib = %{version}-%{release}
Requires: libffado-man = %{version}-%{release}
Requires: libffado-python = %{version}-%{release}
Requires: libffado-python3 = %{version}-%{release}
BuildRequires : PyQt5
BuildRequires : alsa-lib
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-scons
BuildRequires : dbus-dev
BuildRequires : dbus-python-dev
BuildRequires : findutils
BuildRequires : jack2-dev
BuildRequires : libconfig-dev
BuildRequires : libconfig-staticdev
BuildRequires : libdbus-c++-dev
BuildRequires : libdbus-c++-staticdev
BuildRequires : libiec61883-dev
BuildRequires : libiec61883-staticdev
BuildRequires : libraw1394-dev
BuildRequires : libraw1394-staticdev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxmlplusplus-3.2-dev
BuildRequires : pkgconfig(dbus-c++-1)
BuildRequires : pkgconfig(dbus-c++-ecore-1)
BuildRequires : pkgconfig(dbus-c++-glib-1)
BuildRequires : pkgconfig(jack)
BuildRequires : pkgconfig(libconfig)
BuildRequires : pkgconfig(libconfig++)
BuildRequires : pkgconfig(libiec61883)
BuildRequires : pkgconfig(libraw1394)
BuildRequires : pkgconfig(libxml++-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(xdg-desktop-portal)
BuildRequires : pyside2-setup
BuildRequires : python3-core
BuildRequires : qscintilla
BuildRequires : qscintilla-dev
BuildRequires : sip
BuildRequires : sip-dev
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-utils
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Fix-install-under-sandbox.patch

%description
FFADO v2.4
==========
The FFADO project aims to provide a free driver implemenation for FireWire
(IEEE1394, iLink) based audio interfaces.  The focus of the project are on
audio/music production rather than consumer audio.  This means that although
we intend to supported all features at some point, consumer features are
considered less important.  The most obvious example of a consumer feature
is AC3/DTS passthrough support, which is unsupported at the moment.

%package bin
Summary: bin components for the libffado package.
Group: Binaries
Requires: libffado-data = %{version}-%{release}
Requires: libffado-config = %{version}-%{release}

%description bin
bin components for the libffado package.


%package config
Summary: config components for the libffado package.
Group: Default

%description config
config components for the libffado package.


%package data
Summary: data components for the libffado package.
Group: Data

%description data
data components for the libffado package.


%package dev
Summary: dev components for the libffado package.
Group: Development
Requires: libffado-lib = %{version}-%{release}
Requires: libffado-bin = %{version}-%{release}
Requires: libffado-data = %{version}-%{release}
Provides: libffado-devel = %{version}-%{release}
Requires: libffado = %{version}-%{release}

%description dev
dev components for the libffado package.


%package lib
Summary: lib components for the libffado package.
Group: Libraries
Requires: libffado-data = %{version}-%{release}

%description lib
lib components for the libffado package.


%package man
Summary: man components for the libffado package.
Group: Default

%description man
man components for the libffado package.


%package python
Summary: python components for the libffado package.
Group: Default
Requires: libffado-python3 = %{version}-%{release}

%description python
python components for the libffado package.


%package python3
Summary: python3 components for the libffado package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libffado package.


%prep
%setup -q -n libffado-2.4.3
cd %{_builddir}/libffado-2.4.3
%patch1 -p1

%build
## build_prepend content
find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'configure' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'SConstruct' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
export SHCCFLAGS="-fpic"
export SHCFLAGS="-fpic"
export SHCXXFLAGS="-fpic"
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export FCFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export FFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export CFFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
export LDFLAGS="-O3 -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native "
export CXXFLAGS="-O3 -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-sort-common -Wl,-z,now -Wl,-z,relro -Wno-error -Wp,-D_REENTRANT -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -feliminate-unused-debug-types -ffat-lto-objects -fipa-pta -floop-nest-optimize -flto=12 -fno-PIC -fno-PIE -fno-math-errno -fno-pie -fno-plt -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -fpic -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -fvisibility-inlines-hidden -g -m64 -malign-data=cacheline -march=native -mtls-dialect=gnu2 -mtune=native -pipe "
##
%define _lto_cflags 1
##
## make_prepend content
find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'configure' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'SConstruct' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
export SHCCFLAGS="-fpic"
export SHCFLAGS="-fpic"
export SHCXXFLAGS="-fpic"
## make_prepend end
scons %{?_smp_mflags}  PREFIX=/usr LIBDIR=/usr/lib64 UDEVDIR="/usr/lib/udev/rules.d" MANDIR="/usr/share/man" PYTHON_INTERPRETER="/usr/bin/python3" PYPKGDIR="/usr/lib/python3.8/site-packages" SHCCFLAGS="-fpic" SHCFLAGS="-fpic" SHCXXFLAGS="-fpic" ENABLE_FIREWORKS=True BUILD_MIXER=True BUILD_TESTS=True ENABLE_OPTIMIZATIONS=True CUSTOM_ENV=True DEBUG=no DEBUG=False DETECT_USERSPACE_ENV=False BUILD_STATIC_LIB=True

%install
## install_prepend content
find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'configure' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
find . -type f -name 'SConstruct' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
export SHCCFLAGS="-fpic"
export SHCFLAGS="-fpic"
export SHCXXFLAGS="-fpic"
## install_prepend end
scons PREFIX=/usr LIBDIR=/usr/lib64 UDEVDIR="/usr/lib/udev/rules.d" MANDIR="/usr/share/man" PYTHON_INTERPRETER="/usr/bin/python3" PYPKGDIR="/usr/lib/python3.8/site-packages" DESTDIR=%{buildroot} WILL_DEAL_WITH_XDG_MYSELF=True SHCCFLAGS="-fpic" SHCFLAGS="-fpic" SHCXXFLAGS="-fpic" BUILD_STATIC_LIB=True install
## Remove excluded files
rm -f %{buildroot}/usr/share/libffado/icons/hi64-apps-ffado.png
## install_append content
install -vDm 644 support/xdg/ffado.org-ffadomixer.desktop "%{buildroot}/usr/share/applications/ffado-mixer.desktop"
install -vDm 644 support/xdg/hi64-apps-ffado.png "%{buildroot}/usr/share/icons/hicolor/64x64/apps/ffado-mixer.png"
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dumpiso_mod
/usr/bin/ffado-bridgeco-downloader
/usr/bin/ffado-dbus-server
/usr/bin/ffado-diag
/usr/bin/ffado-dice-firmware
/usr/bin/ffado-fireworks-downloader
/usr/bin/ffado-mixer
/usr/bin/ffado-set-nickname
/usr/bin/ffado-test
/usr/bin/ffado-test-isorecv
/usr/bin/ffado-test-isoxmit
/usr/bin/ffado-test-streaming
/usr/bin/ffado-test-streaming-ipc
/usr/bin/ffado-test-streaming-ipcclient
/usr/bin/gen-loadpulses
/usr/bin/scan-devreg
/usr/bin/set-default-router-config-dice-eap
/usr/bin/test-avccmd
/usr/bin/test-bufferops
/usr/bin/test-clock_nanosleep
/usr/bin/test-cycle-time
/usr/bin/test-devicestringparser
/usr/bin/test-dice-eap
/usr/bin/test-echomixer
/usr/bin/test-enhanced-mixer
/usr/bin/test-focusrite
/usr/bin/test-fw410
/usr/bin/test-ieee1394service
/usr/bin/test-ipcringbuffer
/usr/bin/test-messagequeue
/usr/bin/test-scs
/usr/bin/test-shm
/usr/bin/test-streamdump
/usr/bin/test-sysload
/usr/bin/test-timestampedbuffer
/usr/bin/test-volume
/usr/bin/test-watchdog
/usr/bin/unmute-ozonic

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/60-ffado.rules

%files data
%defattr(-,root,root,-)
/usr/share/applications/ffado-mixer.desktop
/usr/share/dbus-1/services/org.ffado.Control.service
/usr/share/icons/hicolor/64x64/apps/ffado-mixer.png
/usr/share/libffado/configuration
/usr/share/libffado/fw410.xml
/usr/share/libffado/fwap.xml
/usr/share/libffado/refdesign.xml
/usr/share/metainfo/ffado-mixer.appdata.xml

%files dev
%defattr(-,root,root,-)
/usr/include/libffado/ffado.h
/usr/lib64/libffado.so
/usr/lib64/libffado/static_info.txt
/usr/lib64/pkgconfig/libffado.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libffado.so.2
/usr/lib64/libffado.so.2.4.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ffado-bridgeco-downloader.1
/usr/share/man/man1/ffado-dbus-server.1
/usr/share/man/man1/ffado-diag.1
/usr/share/man/man1/ffado-dice-firmware.1
/usr/share/man/man1/ffado-fireworks-downloader.1
/usr/share/man/man1/ffado-mixer.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
