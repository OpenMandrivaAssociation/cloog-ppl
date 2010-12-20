%define 	name		cloog-ppl
%define		version		0.15.8
%define		release		%mkrel 2
%define		major		0
%define		libname		%mklibname cloog %major
%define		libnamedev	%mklibname -d cloog

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        The Chunky Loop Generator

Group:          System/Libraries
License:        GPLv2+
URL:            http://repo.or.cz/w/cloog-ppl.git
Source0:        ftp://gcc.gnu.org/pub/gcc/infrastructure/%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  ppl-devel >= 0.10, gmp-devel >= 4.1.3, texinfo >= 4.12
Requires(post): info-install
Requires(preun): info-install

%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package -n %{libname}
Summary: Parma Polyhedra Library backend (ppl) based version of the Cloog binaries
Group: Development/C
#cloog was originally imported to the repositories with a wrong '1' major, 
#this Obsoletes is here to make sure this badly named package is upgraded 
#smoothly
Obsoletes: %{mklibname cloog 1} < 0.15.7
%description -n %{libname}
The dynamic shared libraries of the Chunky Loop Generator

%package -n %{libnamedev}
Summary:        Development tools for the ppl based version of Chunky Loop Generator
Group:          Development/C
Requires:       %{libname} = %{version}-%{release}
Requires:       ppl-devel >= 0.10, gmp-devel >= 4.1.3
Provides: 	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
%description -n %{libnamedev}
The header files and dynamic shared libraries of the Chunky Loop Generator.

%prep
%setup -q -n cloog-ppl-%{version}

%build
%configure2_5x --with-ppl --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}/%{_infodir}/dir %{buildroot}/%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900 
%post -n %{libname} -p /sbin/ldconfig 
%endif 
%if %mdkversion < 200900 
%postun -n %{libname} -p /sbin/ldconfig 
%endif 

%files 
%defattr(-,root,root,-)
%{_infodir}/cloog.info*
%{_bindir}/cloog

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/libcloog.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root,-)
%{_includedir}/cloog
%{_libdir}/libcloog.so

%post -n %{libname}
%_install_info %{name}.info

%preun -n %{libname}
%_remove_install_info %{name}.info
