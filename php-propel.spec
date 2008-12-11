Summary:	Object persistence and query service for PHP5
Summary(pl.UTF-8):	Usługa przechowywania i odpytywania obiektów dla PHP5
Name:		php-propel
Version:	1.3.0
Release:	0.2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.phpdb.org/get/propel_runtime-%{version}.tgz
# Source0-md5:	d2c888e0ce21f776d3ad932ec9cd47e7
Source1:	http://pear.phpdb.org/get/propel_generator-%{version}.tgz
# Source1-md5:	18dd61f9a11145424c2ca3a3f54989bb
URL:		http://propel.phpdb.org/
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
%setup -qc -a1
mv propel_generator-%{version} generator
mv propel_runtime-%{version} runtime
%{__sed} -i -e 's,@DATA-DIR@,%{php_pear_dir}/data,g' generator/pear/pear-propel-gen
cat <<'EOF'> generator/pear/pear-propel-gen.sh
#!/bin/sh
exec phing -f /usr/share/pear/data/propel_generator/pear-build.xml -Dproject.dir=$*
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir}/propel,%{_bindir}}
cp -a runtime/* $RPM_BUILD_ROOT%{php_pear_dir}/propel

cp -a generator/engine $RPM_BUILD_ROOT%{php_pear_dir}/propel
cp -a generator/phing $RPM_BUILD_ROOT%{php_pear_dir}/propel
install generator/pear/pear-propel-gen.sh $RPM_BUILD_ROOT%{_bindir}/propel-gen
install -d $RPM_BUILD_ROOT%{php_pear_dir}/data/propel_generator
cp -a generator/{projects,resources,*.xml,*.properties} $RPM_BUILD_ROOT%{php_pear_dir}/data/propel_generator

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/propel
%{php_pear_dir}/propel/Propel.php
%{php_pear_dir}/propel/PropelException.php
%{php_pear_dir}/propel/adapter
%{php_pear_dir}/propel/logger
%{php_pear_dir}/propel/map
%{php_pear_dir}/propel/om
%{php_pear_dir}/propel/util
%{php_pear_dir}/propel/validator

%files -n propel-gen
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/propel-gen
%{php_pear_dir}/propel/engine
%{php_pear_dir}/propel/phing

%dir %{php_pear_dir}/data/propel_generator
%{php_pear_dir}/data/propel_generator/projects
%{php_pear_dir}/data/propel_generator/resources
%{php_pear_dir}/data/propel_generator/build-propel.xml
%{php_pear_dir}/data/propel_generator/build.properties
%{php_pear_dir}/data/propel_generator/default.properties
%{php_pear_dir}/data/propel_generator/pear-build.xml
