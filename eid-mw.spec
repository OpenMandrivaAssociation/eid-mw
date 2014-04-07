%define Werror_cflags %nil

Name:           eid-mw
Version:        4.0.0
Release:        1
Summary:        The eID Middleware offers components for using the Belgian eID
License:        LGPLv3
Group:          Networking/Other
URL:            http://code.google.com/p/eid-mw/
Source0:        http://eid-mw.googlecode.com/files/%{name}-%{version}-1135.tar.gz
Patch0:			eid-mw-4.0.2_p1188+gcc-4.7.patch
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(gtk+-2.0)

%description
Software that support electronic person identification for Belgian eID.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--with-qt

%make

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog
