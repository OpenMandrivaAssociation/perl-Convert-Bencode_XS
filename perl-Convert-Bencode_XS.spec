%define upstream_name Convert-Bencode_XS
%define upstream_version 0.06

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1
Summary:        Faster conversions to/from Bencode format
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Convert-Bencode_XS/
Source0:        http://www.cpan.org/authors/id/I/IW/IWADE/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:	perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor 
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Convert*
%{_mandir}/man3/*

