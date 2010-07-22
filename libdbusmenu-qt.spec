%define name	libdbusmenu-qt
%define version	0.3.5
%define release	%mkrel 1
%define Summary	 Qt implementation of the DBusMenu spec
%define major 2
%define libname %mklibname dbusmenu-qt %{major}
%define develname %mklibname dbusmenu-qt -d

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://launchpad.net/libdbusmenu-qt/trunk/%{version}/+download/%{name}-%{version}tar..bz2
License:	GPLv2
Group:		System/Libraries
URL:		https://launchpad.net/libdbusmenu-qt
BuildRequires:	libqjson-devel
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
