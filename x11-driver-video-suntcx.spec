ExclusiveArch:	sparc sparc64
Name: x11-driver-video-suntcx
Version: 1.1.0
Release: %mkrel 4
Summary: The X.org driver for sun tcx Cards
Group: Development/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-suntcx-1.1.0@mandriva suggested on upstream
# Tag at git checkout b55d0f6473fccff328bcd8febc9d376ade564b2d
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-suntcx  xorg/drivers/xf86-video-suntcx
# cd xorg/drivers/xf86-video/suntcx
# git-archive --format=tar --prefix=xf86-video-suntcx-1.1.0/ xf86-video-suntcx-1.1.0@mandriva | bzip2 -9 > xf86-video-suntcx-1.1.0.tar.bz2
########################################################################
Source0: xf86-video-suntcx-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-suntcx-1.1.0@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for sun tcx Cards

%prep
%setup -q -n xf86-video-suntcx-%{version}

%patch1 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/suntcx_drv.so
%{_mandir}/man4/suntcx.*
