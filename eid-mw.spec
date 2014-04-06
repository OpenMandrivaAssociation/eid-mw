Name:           eid-mw
Version:        4.0.0
Release:        1
Summary:        The eID Middleware offers components for using the Belgian eID
License:        LGPLv3
Group:          Networking/Other
URL:            http://code.google.com/p/eid-mw/
Source0:        http://eid-mw.googlecode.com/files/%{name}-%{version}-1135.tar.gz
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:	pkgconfig(QtCore)

%description
Software that support electronic person identification for Belgian eID.

%prep
%setup -q

%build
%configure2_5x \
	--with-qt

%make

%install
%makeinstall_std

%files
%doc AUTHORS README ChangeLog
