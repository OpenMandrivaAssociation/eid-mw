%define Werror_cflags %nil
%define _disable_rebuild_configure 1
%define devname %mklibname eid-viewer -d

Summary:        The eID Middleware offers components for using the Belgian eID
Name:           eid-mw
Version:        5.1.11
Release:        2
License:        LGPLv3
Group:          Networking/Other
URL:            http://github.com/Fedict/eid-mw
Source0:		https://dist.eid.belgium.be/continuous/sources/%{name}-%{version}-v%{version}.tar.gz
#Source100:	%{name}.rpmlintrc
BuildRequires:	pkgconfig(gpg-error)
BuildRequires:	pkgconfig(gtk+-3.0)
#BuildRequires:	pkgconfig(gtk+-4.0)
BuildRequires:	pkgconfig(libassuan)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
#BuildRequires:	openssl
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(p11-kit-1)
#Requires:	%{mklibname eidviewer} = %{EVRD}
#Requires:	%{mklibname beidpkcs11} = %{EVRD}

#libpackage beidpkcs11 0
#libpackage eidviewer 0

%description
Software that support electronic person identification for Belgian eID.

%files -f about-eid-mw.lang
#-f dialogs-beid.lang
%{_bindir}/about-eid-mw
%{_bindir}/beid-update-nssdb
%{_datadir}/mozilla/
%{_datadir}/p11-kit/
%{_libdir}/mozilla/
%{_libdir}/pkcs11/
%{_libdir}/libbeidpkcs11.so.*
%{_sysconfdir}/xdg/autostart/beid-update-nssdb.desktop

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
#Requires:	%{mklibname eidviewer 0} = %{EVRD}
#Requires:	%{mklibname beidpkcs11 0} = %{EVRD}

%description -n	%{devname}
This package includes the development files for %{name}.

%files -n %{devname}
%license COPYING
%doc AUTHORS
%{_includedir}/beid/
%{_includedir}/eid-util/
%{_includedir}/eid-viewer/
%{_libdir}/pkgconfig/
%{_libdir}/libbeidpkcs11.so
%{_libdir}/libeidviewer.so
%{_libdir}/pkcs11/beidpkcs11.so

#----------------------------------------------------------------------------

%package -n	eid-viewer
Summary:	Belgium electronic identity card viewer
Requires:	%{name}
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

%files -n eid-viewer -f eid-viewer.lang
%{_bindir}/eid-viewer
%{_libdir}/libeidviewer.so.*
%{_datadir}/applications/eid-viewer.desktop
%{_datadir}/eid-mw/
%{_datadir}/metainfo/
%exclude %{_datadir}/metainfo/*metainfo.xml
%{_datadir}/icons/hicolor/*/*/eid-viewer.png
%if ! 0%{?el6}
%{_datadir}/glib-2.0/schemas/
%endif

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}-v%{version}

%build
#sed -i -e 's:/beid/rsaref220:/rsaref220:' configure.ac
#sed -i -e 's:/beid::' cardcomm/pkcs11/src/libbeidpkcs11.pc.in
#sed -i "s%c_rehash%openssl rehash%g" plugins_tools/eid-viewer/Makefile.am
#config_update
#autoreconf -fiv
#autoreconf -i --force

%configure \
	--enable-p11v220 \
	--disable-webextension \
	--disable-static
%make_build

%install
%make_install

# firefox web extension
mkdir -p %{buildroot}%{_libdir}/mozilla/
mv %{buildroot}/usr/lib/mozilla/pkcs11-modules %{buildroot}%{_libdir}/mozilla/ || true
mv %{buildroot}/usr/lib/mozilla/managed-storage %{buildroot}%{_libdir}/mozilla/ || true

# .desktop
#rm -f %{buildroot}%{_datadir}/applications/eid-viewer.desktop
#desktop-file-install \
#	--add-category="Office;Viewer;" \
#	--vendor fedict \
#	--dir %{buildroot}%{_datadir}/applications \
#	plugins_tools/eid-viewer/eid-viewer.desktop 


%find_lang about-eid-mw
#find_lang dialogs-beid
%find_lang eid-viewer

