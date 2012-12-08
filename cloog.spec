%define		sourcename	cloog-parma

%define		major		1
%define		libname		%mklibname cloog %{major}
%define		libnamedev	%mklibname -d cloog

Name:		cloog-ppl
Version:	0.16.1
Release:	4
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



%changelog
* Sun Jun 03 2012 Andrey Bondrov <abondrov@mandriva.org> 0.16.1-2
+ Revision: 802126
- Drop some legacy junk

* Sun Apr 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.16.1-1
+ Revision: 652216
- Update to newer version

* Tue Mar 15 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.15.9-1
+ Revision: 645073
- update to new version 0.15.9

* Mon Dec 20 2010 Funda Wang <fwang@mandriva.org> 0.15.8-2mdv2011.0
+ Revision: 623247
- fix file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Mon Feb 22 2010 Emmanuel Andry <eandry@mandriva.org> 0.15.8-1mdv2010.1
+ Revision: 509626
- New version 0.15.8
- fix URL ans SOURCE url

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 0.15.7-4mdv2010.1
+ Revision: 503518
- rebuild for new gmp

* Wed Jan 06 2010 Emmanuel Andry <eandry@mandriva.org> 0.15.7-3mdv2010.1
+ Revision: 486799
- add missing provides for devel package

* Tue Aug 18 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.15.7-2mdv2010.0
+ Revision: 417805
- clean up librarification (don't put executable and info files in the library package)
- make sure the (badly named) libcloog1 package gets nicely upgraded by this one(otherwise we get file conflicts on libcloog.so.0.0.0)

* Thu Aug 13 2009 Emmanuel Andry <eandry@mandriva.org> 0.15.7-1mdv2010.0
+ Revision: 416105
- New version 0.15.7
- check major
- fix wrong major

* Wed May 20 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.15.3-1mdv2010.0
+ Revision: 377969
- Fix "Group"
- import cloog-ppl


* Thu Apr 09 2009 Dodji Seketeli <dodji@redhat.com> - 0.15-0.8.git1334c
- Update to new upstream git snapshot
- Drop the cloog.info patch as now upstreamed
- No need to add an argument to the --with-ppl
  configure switch anymore as new upstream fixed this

* Wed Apr 08 2009 Dodji Seketeli <dodji@redhat.org> - 0.15-0.7.gitad322
- Add BuildRequire texinfo needed to regenerate the cloog.info doc

* Wed Apr 08 2009 Dodji Seketeli <dodji@redhat.org> - 0.15-0.6.gitad322
- Remove the cloog.info that is in the tarball
  That forces the regeneration of a new cloog.info with
  suitable INFO_DIR_SECTION, so that install-info doesn't cry
  at install time.
- Slightly changed the patch to make install-info actually
  install the cloog information in the info directory file.
- Run install-info --delete in %%preun, not in %%postun,
  otherwise the info file is long gone with we try to
  run install-info --delete on it.

* Mon Apr 06 2009 Dodji Seketeli <dodji@redhat.org> - 0.15-0.5.gitad322
- Added patch to fix #492794
- Need to add an argument to the --with-ppl switch now.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-0.4.gitad322
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Dodji Seketeli <dodji@redhat.org> 0.15-0.3.gitad322
- Updated to upstream git hash foo
- Generate cloog-ppl and cloog-ppl-devel packages instead of cloog and
  cloog-devel.

* Mon Dec 01 2008 Dodji Seketeli <dodji@redhat.com> 0.15-0.2.git57a0bc
- Updated to upstream git hash 57a0bcd97c08f44a983385ca0389eb624e66e3c7
- Remove the -fomit-frame-pointer compile flag

* Wed Sep 24 2008 Dodji Seketeli <dodji@redhat.com> 0.15-0.1.git95753
- Initial version from git hash 95753d83797fa9a389c0c07f7cf545e90d7867d7

