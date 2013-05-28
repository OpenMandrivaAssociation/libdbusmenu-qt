%define major	2
%define libname	%mklibname dbusmenu-qt %{major}
%define devname	%mklibname dbusmenu-qt -d

Summary:	Qt implementation of the DBusMenu spec
Name:		libdbusmenu-qt
Version:	0.9.2
Release:	2
License:	GPLv2
Group:		System/Libraries
Url:		https://launchpad.net/libdbusmenu-qt
Source0:	http://launchpad.net/libdbusmenu-qt/trunk/%{version}/+download/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QJson)

%description
This library provides a Qt implementation of the DBusMenu spec.

%package -n	%{libname}
Summary:	Qt implementation of the DBUSMenu Spec
Group:		System/Libraries

%description -n	%{libname}
Qt implementation of the DBUSMenu Spec

%files -n %{libname}
%{_libdir}/libdbusmenu-qt.so.%{major}*

%package -n	%{devname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{devname}
%doc %_docdir/dbusmenu-qt
%{_libdir}/libdbusmenu-qt.so
%{_includedir}/dbusmenu-qt/
%{_libdir}/pkgconfig/dbusmenu-qt.pc

%prep
%setup -q 

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build
%if "%{_lib}" != "lib"
sed -i -e "s,/lib,/%{_lib},g" %{buildroot}%{_libdir}/pkgconfig/*.pc
%endif

