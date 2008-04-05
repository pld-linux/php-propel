Summary:	Object persistence and query service for PHP5
Summary(pl.UTF-8):	Usługa przechowywania i odpytywania obiektów dla PHP5
Name:		php-propel
Version:	1.3.0
%define		_rc	beta4
Release:	0.%{_rc}.1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://propel.tigris.org/files/documents/1009/41440/propel-%{version}%{_rc}.tar.gz
# Source0-md5:	b39b77fc942ee892044b00735da77c68
URL:		http://propel.tigris.org/
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-creole
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Propel is an object persistence (object relational mapping) tool for
PHP5 based on Apache Torque. Propel generates PHP classes and SQL
definition files for your data model and provides a runtime
environment that transparently handles database operations.

%description -l pl.UTF-8
Propel to narzędzie do przechowywania obiektów (odwzorowań
obiektowo-relacyjnych) dla PHP5 oparty na Apache Torque. Propel
generuje klasy PHP i pliki definicji SQL dla danego modelu danych oraz
zapewnia środowisko uruchomieniowe obsługujące w sposób przezroczysty
operacje na bazie danych.

%prep
%setup -q -n propel-%{version}%{_rc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
cp -a runtime/classes/propel $RPM_BUILD_ROOT%{php_pear_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/*
