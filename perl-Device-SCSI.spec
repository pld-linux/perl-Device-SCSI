#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Device
%define	pnam	SCSI
Summary:	Device::SCSI - Perl module to control SCSI devices
#Summary(pl):
Name:		perl-Device-SCSI
Version:	1.003
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MO/MOOLI/Device-SCSI-%{version}.tar.gz
# Source0-md5:	6d965728811b379b11f144a2caf85d8b
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
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


# %description -l pl # TODO

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
%doc CHANGES README
%{perl_vendorlib}/Device/*.pm
%{perl_vendorlib}/Device/SCSI
%{_mandir}/man3/*
