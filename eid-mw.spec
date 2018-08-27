%define Werror_cflags %nil
%define _disable_rebuild_configure 1

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

%description
Software that support electronic person identification for Belgian eID.

%libpackage beidpkcs11 0

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

desktop-file-edit --set-key=Exec --set-value=%{_bindir}/about-eid-mw %{buildroot}%{_datadir}/applications/about-eid-mw.desktop

%find_lang about-%{name}

%files -f about-%{name}.lang

%doc AUTHORS README NEWS
%{_bindir}/about-eid-mw
%{_libexecdir}/beid-*
%{_libdir}/*.so
%{_datadir}/applications/about-eid-mw.desktop
%{_datadir}/mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/belgiumeid@eid.belgium.be.xpi

