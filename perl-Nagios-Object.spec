#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Nagios
%define		pnam	Object
Summary:	Nagios::Object - Perl objects to represent Nagios objects
Summary(pl.UTF-8):	Nagios::Object - obiekty Perla reprezentujące obiekty Nagiosa
Name:		perl-Nagios-Object
Version:	0.21.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DU/DUNCS/Nagios-Object-%{version}.tar.gz
# Source0-md5:	1b64bd73b045e9e111bc0755f0c692a0
URL:		http://search.cpan.org/dist/Nagios-Object/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains the code for creating Perl objects to represent
any of the Nagios objects. All of the Perl classes are auto-generated
at compile-time, so it's pretty trivial to add new attributes or even
entire objects.

%description -l pl.UTF-8
Ten moduł zawiera kod do tworzenia obiektów Perla reprezentujących
dowolne obiekty Nagiosa. Wszystkie klasy Perla są generowane
automatycznie w czasie kompilacji, więc łatwo dodawać nowe atrybuty
czy nawet całe obiekty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT{%{_bindir}/*,%{_examplesdir}/%{name}-%{version}}

rm -rf $RPM_BUILD_ROOT%{_mandir}/man1
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Nagios
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
