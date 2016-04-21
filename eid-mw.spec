%define Werror_cflags %nil

Name:           eid-mw
Version:        4.1.12
Release:        1
Summary:        The eID Middleware offers components for using the Belgian eID
License:        LGPLv3
Group:          Networking/Other
URL:            http://github.com/Fedict/eid-mw2
Source0:        https://dist.eid.belgium.be/continuous/sources/%{name}-%{version}-v%{version}.tar.gz
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Software that support electronic person identification for Belgian eID.

%libpackage beidpkcs11 0

%prep
%setup -qn %{name}-%{version}-v%{version}
%apply_patches

%build
%configure2_5x \
	--with-qt --disable-static

%make

%install
%makeinstall_std

%find_lang about-%{name}

%files -f about-%{name}.lang

%doc AUTHORS README NEWS
%{_bindir}/about-eid-mw
%{_libexecdir}/beid-*
%{_libdir}/*.so
%{_datadir}/applications/about-eid-mw.desktop
%{_datadir}/mozilla/extensions/{ec8030f7-c20a-464f-9b0e-13a3a9e97384}/belgiumeid@eid.belgium.be.xpi

