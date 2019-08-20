#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-httpcomponents-parent
Version  : 10
Release  : 2
URL      : https://github.com/apache/httpcomponents-parent/archive/10.tar.gz
Source0  : https://github.com/apache/httpcomponents-parent/archive/10.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/apache/httpcomponents/project/7/project-7.pom
Source2  : https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-parent/10/httpcomponents-parent-10.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-httpcomponents-parent-data = %{version}-%{release}
Requires: mvn-httpcomponents-parent-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-httpcomponents-parent package.
Group: Data

%description data
data components for the mvn-httpcomponents-parent package.


%package license
Summary: license components for the mvn-httpcomponents-parent package.
Group: Default

%description license
license components for the mvn-httpcomponents-parent package.


%prep
%setup -q -n httpcomponents-parent-10

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-httpcomponents-parent
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-httpcomponents-parent/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7/project-7.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-parent/10
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-parent/10/httpcomponents-parent-10.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/httpcomponents/httpcomponents-parent/10/httpcomponents-parent-10.pom
/usr/share/java/.m2/repository/org/apache/httpcomponents/project/7/project-7.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-httpcomponents-parent/LICENSE.txt
