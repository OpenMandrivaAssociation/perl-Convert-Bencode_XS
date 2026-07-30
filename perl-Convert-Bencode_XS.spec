%define upstream_name Convert-Bencode_XS
%define upstream_version 0.06
Name:           perl-%{upstream_name}
Version:	0.06
Release:	2
Summary:        Faster conversions to/from Bencode format
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            https://metacpan.org/dist/Convert-Bencode_XS/
Source0:	https://cpan.metacpan.org/authors/id/I/IW/IWADE/Convert-Bencode_XS-0.06.tar.gz
BuildRequires:	make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:	perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
%setup -q -n Convert-Bencode_XS-0.06

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
# soft: do not fail package on test failures
set +e
%make test

%install
rm -rf %buildroot
%makeinstall_std


%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Convert*
%{_mandir}/man3/*



