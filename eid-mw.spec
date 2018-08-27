%define Werror_cflags %nil
%define _disable_rebuild_configure 1
%define devname %mklibname eid-viewer -d

Name:           eid-mw
Version:        4.4.5
Release:        1
Summary:        The eID Middleware offers components for using the Belgian eID
License:        LGPLv3
Group:          Networking/Other
URL:            http://github.com/Fedict/eid-mw
Source0:	https://github.com/Fedict/eid-mw/archive/v%{version}.tar.gz
Source100:	%{name}.rpmlintrc
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	openssl-perl
Requires:	%{mklibname eidviewer 0} = %{EVRD}
Requires:	%{mklibname beidpkcs11i 0} = %{EVRD}

%description
Software that support electronic person identification for Belgian eID.

%libpackage beidpkcs11 0
%libpackage eidviewer 0

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{mklibname eidviewer 0} = %{EVRD}
Requires:	%{mklibname beidpkcs11 0} = %{EVRD}

%description -n	%{devname}
This package includes the development files for %{name}.

%package -n	eid-viewer
Summary:	Belgium electronic identity card viewer
Requires:	eid-mw
Requires:	ccid
Requires:	pcsc-lite

%description -n eid-viewer
The eid-viewer application allows the user to read out any information from
a Belgian electronic identity card. Both identity information and information
about the stored cryptographic keys can be read in a user-friendly manner,
and can easily be printed out or stored for later reviewal.

The application verifies the signature of the identity information,
checks whether it was signed by a government-issued key, and optionally
checks the certificate against the government's Trust Service.

%prep
%setup -q
%apply_patches

%build
sed -i -e 's:/beid/rsaref220:/rsaref220:' configure.ac
sed -i -e 's:/beid::' cardcomm/pkcs11/src/libbeidpkcs11.pc.in
%config_update
autoreconf -fiv
autoreconf -i --force

%configure \
	--with-qt --disable-static

%make

%install
%makeinstall_std

%find_lang dialogs-beid

%files -f dialogs-beid.lang
%doc AUTHORS
%{_bindir}/about-eid-mw
%{_libexecdir}/beid-*
%{_bindir}/beid-update-nssdb
%{_datadir}/mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/belgiumeid@eid.belgium.be.xpi
%{_datadir}/p11-kit/
%{_prefix}/lib/mozilla/
%{_libdir}/pkcs11/beidpkcs11.so
%{_libdir}/libbeidpkcs11.so
%{_sysconfdir}/xdg/autostart/beid-update-nssdb.desktop

%files -n %{devname}
%{_includedir}/eid-util/
%{_libdir}/pkgconfig/
%{_includedir}/rsaref220/
%{_includedir}/eid-viewer/
%{_libdir}/libeid*.so

%files -n eid-viewer
%{_bindir}/eid-viewer
%{_datadir}/locale/*/LC_MESSAGES/eid-viewer.mo
%{_datadir}/applications/eid-viewer.desktop
%{_datadir}/eid-mw/
%{_datadir}/icons/hicolor/*/*/eid-viewer.png
%{_datadir}/glib-2.0/schemas/
