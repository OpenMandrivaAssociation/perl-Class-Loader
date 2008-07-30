%define realname        Class-Loader
Name:           perl-%{realname}
Version:        2.03
Release:        %mkrel 5
License:        Artistic

Group:          Development/Perl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Summary:        Load modules and create objects on demand
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/%{realname}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{realname}
Requires:       perl
BuildArch:      noarch

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
%setup -q -n %{realname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{perl_vendorlib}/Class
%{_mandir}/*/*

