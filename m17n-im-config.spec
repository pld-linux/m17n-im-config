#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Input method configuration library for m17n-lib
#Summary(pl.UTF-8):	-
Name:		m17n-im-config
Version:	0.9.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.m17n.org/m17n-lib-download/%{name}-%{version}.tar.gz
# Source0-md5:	dfb1812d604c5b2392ebb7e47034c3f9
Source1:	m17n-im-config.1
URL:		http://www.m17n.org/
BuildRequires:	gtk+2-devel
BuildRequires:	m17n-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
m17n-im-config is a library to create a GTK+ widget for per-user
configuration of input methods provided by the m17n library, and a
standalone GUI program which demonstrates the library.

#%description -l pl.UTF-8

%package devel
Summary:	Header files for m17n-im-config library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki m17n-im-config
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for m17n-im-config library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki m17n-im-config.

%package static
Summary:	Static m17n-im-config library
Summary(pl.UTF-8):	Statyczna biblioteka m17n-im-config
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static m17n-im-config library.

%description static -l pl.UTF-8
Statyczna biblioteka m17n-im-config.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1/m17n-im-config.1

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/m17n-im-config.1

%find_lang m17n-im-config

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f m17n-im-config.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libm17n-im-config.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libm17n-im-config.so.0
%{_mandir}/man1/m17n-im-config.1*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libm17n-im-config.so
%{_includedir}/m17n-im-config.h
%{_pkgconfigdir}/m17n-im-config.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libm17n-im-config.a
%endif
