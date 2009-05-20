%define 	name		cloog-ppl
%define		version		0.15.3
%define		release		%mkrel 1
%define		major		1
%define		libname		%mklibname cloog %major
%define		libnamedev	%mklibname -d cloog

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        The Chunky Loop Generator

Group:          System/Libraries
License:        GPLv2+
URL:            http://www.cloog.org
Source0:        %{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  ppl-devel >= 0.10, gmp-devel >= 4.1.3, texinfo >= 4.12
Requires(post): info-install
Requires(preun): info-install

%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package -n %libname
Summary: Parma Polyhedra Library backend (ppl) based version of the Cloog binaries
Group: Development/Libraries
%description -n %libname
The dynamic shared libraries of the Chunky Loop Generator

%package -n %libnamedev
Summary:        Development tools for the ppl based version of Chunky Loop Generator
Group:          Development/Libraries
Requires:       %{libname} = %{version}-%{release}
Requires:       ppl-devel >= 0.10, gmp-devel >= 4.1.3
Provides: 	%name-devel = %version-%release
%description -n %libnamedev
The header files and dynamic shared libraries of the Chunky Loop Generator.

%prep
%setup -q -n cloog-ppl

%build
%configure2_5x --with-ppl
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900 
%post -n %libname -p /sbin/ldconfig 
%endif 
%if %mdkversion < 200900 
%postun -n %libname -p /sbin/ldconfig 
%endif 

%files -n %libname
%defattr(-,root,root,-)
%{_infodir}/cloog.info*
%{_bindir}/cloog
%{_libdir}/libcloog.so.*

%files -n %libnamedev
%defattr(-,root,root,-)
%{_includedir}/cloog
%{_libdir}/libcloog.so
%exclude %{_libdir}/libcloog.a
%exclude %{_libdir}/libcloog.la

%post -n %libname
%_install_info %{name}.info

%preun -n %libname
%_remove_install_info %{name}.info
