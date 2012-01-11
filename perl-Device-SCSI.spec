#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Device
%define	pnam	SCSI
Summary:	Device::SCSI - Perl module to control SCSI devices
Summary(pl.UTF-8):	Device::SCSI - moduł Perla do sterowania urządzeniami SCSI
Name:		perl-Device-SCSI
Version:	1.004
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MO/MOOLI/Device-SCSI-%{version}.tar.gz
# Source0-md5:	2c62ed5016d5f377d7870395e1932e5a
URL:		http://search.cpan.org/dist/Device-SCSI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl library uses Perl5 objects to make it easy to perform
low-level SCSI I/O from Perl, avoiding all the black magic and
fighting with C. The object-oriented interface allows for the
application to use more than one SCSI device simultaneously (although
this is more likely to be used by the application to cache the devices
it needs in a hash.)

As well as the general purpose execute() method, there are also a
number of other helper methods that can aid in querying the device and
debugging. Note that the goats and black candles usually required to
solve SCSI problems will need to be provided by yourself.

%description -l pl.UTF-8
Ta biblioteka perlowa wykorzystuje obiekty Perla 5 w celu ułatwienia
wykonywania niskopoziomowy operacji wejścia/wyjścia SCSI z poziomu
Perla, unikając całej czarnej magii i walki z C. Zorientowany
obiektowo interfejs pozwala aplikacji używać więcej niż jednego
urządzenia SCSI jednocześnie (choć bardziej prawdopodobne jest
wykorzystanie tego przez aplikację do zapamiętania potrzebnych
urządzeń w haszu).

Oprócz ogólnej metody execute() jest także wiele innych pomocniczych
metod, mogących pomóc w odpytywaniu urządzenia i diagnostyce. Należy
zauważyć, że kozły i czarne świece zwykle wymagane do rozwiązywania
problemów ze SCSI trzeba sobie zapewnić samemu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Device/*.pm
%{perl_vendorlib}/Device/SCSI
%{_mandir}/man3/*
