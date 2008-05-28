ExclusiveArch:	sparc sparc64
Name: x11-driver-video-suntcx
Version: 1.1.0
Release: %mkrel 4
Summary: X.org driver for sun tcx Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-suntcx-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-suntcx is the X.org driver for sun tcx Cards.

%prep
%setup -q -n xf86-video-suntcx-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/suntcx_drv.la
%{_libdir}/xorg/modules/drivers/suntcx_drv.so
%{_mandir}/man4/suntcx.*
