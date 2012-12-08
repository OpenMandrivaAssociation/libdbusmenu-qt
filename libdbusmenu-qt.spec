%define name	libdbusmenu-qt
%define version	0.6.6
%define release	%mkrel 3
%define Summary	 Qt implementation of the DBusMenu spec
%define major 2
%define libname %mklibname dbusmenu-qt %{major}
%define develname %mklibname dbusmenu-qt -d

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://launchpad.net/libdbusmenu-qt/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
License:	GPLv2
Group:		System/Libraries
URL:		https://launchpad.net/libdbusmenu-qt
BuildRequires:	qjson-devel
BuildRequires:	qt4-devel
BuildRequires:	cmake

%description
This library provides a Qt implementation of the DBusMenu spec.

#-----------------------------------------------------------------------

%package -n	%{libname}
Summary:	Qt implementation of the DBUSMenu Spec
Group:		System/Libraries

%description -n	%{libname}
Qt implementation of the DBUSMenu Spec


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libdbusmenu-qt.so.%{major}*

#---------------------------------------------------------------------

%package -n	%{develname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n	%{develname}
%defattr(-,root,root)
%{_libdir}/libdbusmenu-qt.so
%{_includedir}/dbusmenu-qt/
%{_libdir}/pkgconfig/dbusmenu-qt.pc

#-----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_qt4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%clean
%__rm -rf %buildroot


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-2mdv2011.0
+ Revision: 661456
- mass rebuild

* Tue Jan 04 2011 John Balcaen <mikala@mandriva.org> 0.6.6-1mdv2011.0
+ Revision: 628442
- Update to 0.6.6

* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 0.6.4-1mdv2011.0
+ Revision: 602230
- new version 0.6.4

* Tue Sep 14 2010 John Balcaen <mikala@mandriva.org> 0.6.2-1mdv2011.0
+ Revision: 578128
- Update to 0.6.2

* Thu Jul 22 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.3.5-1mdv2011.0
+ Revision: 556954
- Fix typo
- Fix source

  + John Balcaen <mikala@mandriva.org>
    - Update to 0.3.5
    - Update URL & Source0

* Sat Mar 13 2010 John Balcaen <mikala@mandriva.org> 0.3.0-1mdv2010.1
+ Revision: 518771
- import libdbusmenu-qt


