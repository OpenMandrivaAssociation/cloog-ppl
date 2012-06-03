%define		sourcename	cloog-parma

%define		major		1
%define		libname		%mklibname cloog %{major}
%define		libnamedev	%mklibname -d cloog

Name:		cloog-ppl
Version:	0.16.1
Release:	2
Summary:	The Chunky Loop Generator

Group:		System/Libraries
License:	GPLv2+
URL:		http://www.cloog.org
Source0:	ftp://gcc.gnu.org/pub/gcc/infrastructure/%{sourcename}-%{version}.tar.gz
BuildRequires:	ppl-devel >= 0.11
BuildRequires:	ppl_c-devel >= 0.11
BuildRequires:	gmp-devel
BuildRequires:	texinfo

%description
CLooG is a software which generates loops for scanning Z-polyhedra. That is,
CLooG finds the code or pseudo-code where each integral point of one or more
parametrized polyhedron or parametrized polyhedra union is reached. CLooG is
designed to avoid control overhead and to produce a very efficient code.

%package -n %{libname}
Summary:	Parma Polyhedra Library backend (ppl) based version of the Cloog binaries
Group:		Development/C

%description -n %{libname}
The dynamic shared libraries of the Chunky Loop Generator

%package -n %{libnamedev}
Summary:	Development tools for the ppl based version of Chunky Loop Generator
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	gmp-devel
Requires:	ppl-devel >= 0.11
Requires:	ppl_c-devel >= 0.11
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
The header files and dynamic shared libraries of the Chunky Loop Generator.

%prep
%setup -q -n %{sourcename}-%{version}

%build
%configure2_5x --with-ppl=system --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_infodir}/dir

%files
%{_bindir}/cloog

%files -n %{libname}
%{_libdir}/libcloog-ppl.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/cloog
%{_libdir}/libcloog-ppl.so
%{_libdir}/pkgconfig/cloog-ppl.pc

