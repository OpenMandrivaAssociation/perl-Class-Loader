%define upstream_name    Class-Loader
%define upstream_version 2.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Load modules and create objects on demand
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Certain applications like to defer the decision to use a
particular module till runtime. This is possible in perl,
and is a useful trick in situations where the type of data
is not known at compile time and the application doesn't
wish to pre-compile modules to handle all types of data it
can work with. Loading modules at runtime can also provide
flexible interfaces for perl modules. Modules can let the
programmer decide what modules will be used by it instead
of hard-coding their names.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-5mdv2012.0
+ Revision: 765089
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-4
+ Revision: 763533
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-3
+ Revision: 676620
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 2.30.0-2
+ Revision: 676515
- rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2011.0
+ Revision: 406875
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 2.03-5mdv2009.0
+ Revision: 256023
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 2.03-3mdv2008.1
+ Revision: 168162
- fix no-buildroot-tag
- kill (multiple!) definitions of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-3mdv2008.0
+ Revision: 86125
- rebuild


* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:39:05 (58398)
- mkrel
- check section

* Mon Aug 28 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-08-28 14:36:18 (58397)
Import perl-Class-Loader

* Fri Apr 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.03-1mdk
- 2.03

* Mon Feb 23 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.02-2mdk
- rebuild
- own dirs

* Thu Nov 06 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 2.02-1mdk
- New package

