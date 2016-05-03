Name:       libpurple

Summary:    libpurple library for IM clients like Pidgin and Finch
Version:    2.10.11
Release:    1
Group:      Applications/Communications
License:    GPLv2+ and GPLv2 and MIT
URL:        http://pidgin.im/
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  gettext
BuildRequires:  python >= 2.4

%description

libpurple contains the core IM support for IM clients such as Pidgin and Finch.

libpurple supports a variety of messaging protocols including AIM, MSN,
Yahoo!, Jabber, Bonjour, Gadu-Gadu, ICQ, IRC, Novell Groupwise, QQ,
Lotus Sametime, SILC, Simple and Zephyr.


%package devel
Summary:    Development headers, documentation, and libraries for libpurple
Group:      Applications/Communications
Requires:   %{name} = %{version}-%{release}

%description devel
The libpurple-devel package contains the header files, developer
documentation, and libraries required for development of libpurple based
instant messaging clients or plugins for any libpurple based client.


%prep
%setup -q -n %{name}-%{version}/pidgin

%build
%autogen --disable-static \
    --disable-consoleui \
    --disable-gtkui \
    --disable-screensaver \
    --disable-startup-notification \
    --disable-gtkspell \
    --disable-avahi \
    --disable-nm \
    --disable-perl \
    --disable-tcl \
    --disable-meanwhile \
    --disable-gestures \
    --disable-gnutls

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/gconf/schemas/purple.schemas
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/purple-2/
%{_libdir}/libpurple.so.*
%{_datadir}/sounds/purple/
%{_datadir}/purple
%{_bindir}/purple-client-example
%{_bindir}/purple-remote
%{_bindir}/purple-send
%{_bindir}/purple-send-async
%{_bindir}/purple-url-handler
%{_libdir}/libpurple-client.so.*
%doc libpurple/purple-notifications-example

%files devel
%defattr(-,root,root,-)
%{_datadir}/aclocal/purple.m4
%{_libdir}/libpurple.so
%{_includedir}/libpurple/
%{_libdir}/pkgconfig/purple.pc
%{_libdir}/libpurple-client.so
