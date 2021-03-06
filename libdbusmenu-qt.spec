%define major 2
%define devname %mklibname dbusmenu-qt -d
%define devname5 %mklibname dbusmenu-qt5 -d
%define snap	16.04.20160218

%bcond_with qt4

Summary:	Qt implementation of the DBusMenu spec
Name:		libdbusmenu-qt
Version:	0.9.3
Release:	12.%{snap}.3
License:	GPLv2
Group:		System/Libraries
Url:		https://launchpad.net/libdbusmenu-qt
Source0:	http://archive.ubuntu.com/ubuntu/pool/main/libd/%{name}/%{name}_%{version}+%{snap}.orig.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	doxygen

%if %{with qt4}
%libpackage dbusmenu-qt %{major}
%endif

%libpackage dbusmenu-qt5 %{major}

%description
This library provides a Qt implementation of the DBusMenu spec.

%package -n %{devname5}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{mklibname dbusmenu-qt5 %{major}} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}
BuildRequires:	qt5-devel
# To make qmake happy
BuildRequires:	qt5-platformtheme-gtk3
BuildRequires:	cmake(Qt5Test)

%description -n	%{devname5}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{devname5}
%doc %_docdir/dbusmenu-qt5
%{_libdir}/libdbusmenu-qt5.so
%{_includedir}/dbusmenu-qt5/
%{_libdir}/cmake/dbusmenu-qt5
%{_libdir}/pkgconfig/dbusmenu-qt5.pc

%if %{with qt4}
%package -n %{devname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{mklibname dbusmenu-qt %{major}} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}
BuildRequires:	qt4-devel

%description -n	%{devname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{devname}
%doc %{_docdir}/dbusmenu-qt
%{_libdir}/libdbusmenu-qt.so
%{_includedir}/dbusmenu-qt/
%{_libdir}/cmake/dbusmenu-qt
%{_libdir}/pkgconfig/dbusmenu-qt.pc
%endif

%prep
%setup -q -n %{name}-%{version}+%{snap}

%build
%cmake -DUSE_QT5:BOOL=ON \
	-G Ninja
%ninja_build

%if %{with qt4}
cd ..
mkdir build-qt4
cd build-qt4
cmake .. \
	 -DUSE_QT4:BOOL=ON \
	 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	 -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
	 -DLIB_INSTALL_DIR:PATH=%{_lib} \
	 -DCMAKE_SKIP_RPATH:BOOL=ON \
	 -DLIB_INSTALL_DIR=%{_libdir} \
	 -DINCLUDE_INSTALL_DIR=%{_includedir}
%make
%endif

%install
%if %{with qt4}
%makeinstall_std -C build-qt4
%endif

%ninja_install -C build
%if "%{_lib}" != "lib"
sed -i -e "s,/lib,/%{_lib},g" %{buildroot}%{_libdir}/pkgconfig/*.pc
%endif
# Fix ubuntu-ish redundant doc names (no need for -doc in /usr/share/doc...)
%if %{with qt4}
mv %{buildroot}%{_docdir}/libdbusmenu-qt-doc %{buildroot}%{_docdir}/dbusmenu-qt
%endif
mv %{buildroot}%{_docdir}/libdbusmenu-qt5-doc %{buildroot}%{_docdir}/dbusmenu-qt5
