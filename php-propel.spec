%define		pkgname	propel
Summary:	Object persistence and query service for PHP5
Summary(pl.UTF-8):	Usługa przechowywania i odpytywania obiektów dla PHP5
Name:		php-%{pkgname}
Version:	1.4.1
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://files.propelorm.org/%{pkgname}-%{version}.tar.gz
# Source0-md5:	aec7bef13252663e5ff0754582bd58f8
URL:		http://www.propelorm.org/
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 4:5.2.8-3
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

%package -n propel-gen
Summary:	propel-gen - DDL files generator
Summary(pl.UTF-8):	propel-gen - generator plików DDL
Group:		Development/Languages/PHP
Requires:	phing
Requires:	php-xsl

%description -n propel-gen
A generator that creates SQL definition files (DDL).

%description -n propel-gen -l pl.UTF-8
Generator tworzący pliki definicji SQL (DDL).

%prep
%setup -q -n %{pkgname}-%{version}
cat <<'EOF'> generator/pear/pear-propel-gen.sh
#!/bin/sh
exec phing -f %{php_pear_dir}/data/propel_generator/pear-build.xml -Dproject.dir=$*
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir}/propel,%{_bindir}}
cp -a runtime/classes/propel/* $RPM_BUILD_ROOT%{php_data_dir}/propel

cp -a generator/classes/propel/engine $RPM_BUILD_ROOT%{php_data_dir}/propel
cp -a generator/classes/propel/phing $RPM_BUILD_ROOT%{php_data_dir}/propel
install -p generator/pear/pear-propel-gen.sh $RPM_BUILD_ROOT%{_bindir}/propel-gen
install -d $RPM_BUILD_ROOT%{php_data_dir}/data/propel_generator
cp -a generator/{resources,build-propel.xml,*.properties} $RPM_BUILD_ROOT%{php_data_dir}/data/propel_generator
cp -a generator/pear/{pear-build.xml,*.properties} $RPM_BUILD_ROOT%{php_data_dir}/data/propel_generator

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_data_dir}/propel
%{php_data_dir}/propel/Propel.php
%{php_data_dir}/propel/PropelException.php
%{php_data_dir}/propel/adapter
%{php_data_dir}/propel/logger
%{php_data_dir}/propel/map
%{php_data_dir}/propel/om
%{php_data_dir}/propel/util
%{php_data_dir}/propel/validator

%files -n propel-gen
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/propel-gen
%{php_data_dir}/propel/engine
%{php_data_dir}/propel/phing

%dir %{php_data_dir}/data/propel_generator
%{php_data_dir}/data/propel_generator/resources
%{php_data_dir}/data/propel_generator/build-propel.xml
%{php_data_dir}/data/propel_generator/build.properties
%{php_data_dir}/data/propel_generator/default.properties
%{php_data_dir}/data/propel_generator/pear-build.xml
