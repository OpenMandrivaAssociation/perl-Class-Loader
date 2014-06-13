%define upstream_name    Class-Loader
%define upstream_version 2.03

Summary:	Load modules and create objects on demand
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	12
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

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
%setup -qn %{upstream_name}-%{upstream_version}

%build
CFLAGS="%{optflags}" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Class
%{_mandir}/man3/*

