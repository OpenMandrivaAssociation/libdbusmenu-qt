%define major 2
%define devname %mklibname dbusmenu-qt -d
%define devname5 %mklibname dbusmenu-qt5 -d
%define devname6 %mklibname dbusmenu-qt6 -d
%define snap	16.04.20160218

%bcond_with qt4
%bcond_without qt5
%bcond_without qt6

Summary:	Qt implementation of the DBusMenu spec
Name:		libdbusmenu-qt
Version:	0.9.3
Release:	13.%{snap}.1
License:	GPLv2
Group:		System/Libraries
Url:		https://launchpad.net/libdbusmenu-qt
Source0:	http://archive.ubuntu.com/ubuntu/pool/main/libd/%{name}/%{name}_%{version}+%{snap}.orig.tar.gz
Patch0:		https://github.com/desktop-app/libdbusmenu-qt/commit/dfcdb1635eb87b226f8942d27a4cd451a405cc81.patch
Patch1:		https://github.com/desktop-app/libdbusmenu-qt/commit/75afa1003c1d0f6fdfa3a76ce2db689b49f86968.patch
Patch2:		https://github.com/desktop-app/libdbusmenu-qt/commit/af9fa001dac49eedc76e15613b67abfd097105f3.patch
Patch3:		https://raw.githubusercontent.com/archlinux/svntogit-packages/packages/libdbusmenu-qt/trunk/libdbusmenu-qt6-cmake.patch
Patch4:		dbusmenu-qt-tests-have-not-been-ported-to-qt6-yet.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	doxygen

%if %{with qt4}
%libpackage dbusmenu-qt %{major}
%endif

%if %{with qt5}
%libpackage dbusmenu-qt5 %{major}
%endif

%if %{with qt6}
%libpackage dbusmenu-qt6 %{major}
%endif

%description
This library provides a Qt implementation of the DBusMenu spec.

%if %{with qt6}
%package -n %{devname6}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{mklibname dbusmenu-qt6} = %{EVRD}
Provides:	%{name}-devel = %{version}-%{release}
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)

%description -n	%{devname6}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n %{devname6}
%doc %_docdir/dbusmenu-qt6
%{_libdir}/libdbusmenu-qt6.so
%{_includedir}/dbusmenu-qt6/
%{_libdir}/cmake/dbusmenu-qt6
%{_libdir}/pkgconfig/dbusmenu-qt6.pc
%endif

%if %{with qt5}
%package -n %{devname5}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{mklibname dbusmenu-qt5} = %{EVRD}
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
%endif

%if %{with qt4}
%package -n %{devname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{mklibname dbusmenu-qt} = %{EVRD}
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
%autosetup -p1 -n %{name}-%{version}+%{snap}
%if %{with qt6}
export CMAKE_BUILD_DIR=build-qt6
%cmake -DUSE_QT6:BOOL=ON \
	-G Ninja
cd ..
%endif

%if %{with qt5}
export CMAKE_BUILD_DIR=build-qt5
%cmake -DUSE_QT5:BOOL=ON \
	-G Ninja
cd ..
%endif

%if %{with qt4}
export CMAKE_BUILD_DIR=build-qt4
%cmake \
	 -DUSE_QT4:BOOL=ON \
	 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	 -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
	 -DLIB_INSTALL_DIR:PATH=%{_lib} \
	 -DCMAKE_SKIP_RPATH:BOOL=ON \
	 -DLIB_INSTALL_DIR=%{_libdir} \
	 -DINCLUDE_INSTALL_DIR=%{_includedir} \
	 -G Ninja
%endif

%build
%if %{with qt4}
%ninja_build -C build-qt4
%endif

%if %{with qt5}
%ninja_build -C build-qt5
%endif

%if %{with qt6}
%ninja_build -C build-qt6
%endif

%install
%if %{with qt4}
%ninja_install -C build-qt4
%endif

%if %{with qt5}
%ninja_install -C build-qt5
%endif

%if %{with qt6}
%ninja_install -C build-qt6
%endif

%if "%{_lib}" != "lib"
sed -i -e "s,/lib,/%{_lib},g" %{buildroot}%{_libdir}/pkgconfig/*.pc
%endif
# Fix ubuntu-ish redundant doc names (no need for -doc in /usr/share/doc...)
%if %{with qt4}
mv %{buildroot}%{_docdir}/libdbusmenu-qt-doc %{buildroot}%{_docdir}/dbusmenu-qt
%endif
%if %{with qt5}
mv %{buildroot}%{_docdir}/libdbusmenu-qt5-doc %{buildroot}%{_docdir}/dbusmenu-qt5
%endif
%if %{with qt6}
mv %{buildroot}%{_docdir}/libdbusmenu-qt6-doc %{buildroot}%{_docdir}/dbusmenu-qt6
%endif
