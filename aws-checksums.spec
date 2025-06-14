#
# Conditional build:
%bcond_without	tests		# unit tests
#
Summary:	AWS Checksums library
Summary(pl.UTF-8):	Biblioteka AWS Checksums
Name:		aws-checksums
Version:	0.2.7
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/awslabs/aws-checksums
Source0:	https://github.com/awslabs/aws-checksums/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ff17a2ef6ee81d1564de4184dd8e7ac2
URL:		https://github.com/awslabs/aws-checksums
BuildRequires:	aws-c-common-devel
BuildRequires:	cmake >= 3.9
BuildRequires:	gcc >= 5:3.2
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cross-Platform hardware accelerated CRC32c and CRC32 with fallback to
efficient software implementations. C interface with language bindings
for each of AWS SDKs.

%description -l pl.UTF-8
Wieloplatformowe implementacje CRC32c i CRC32 ze sprzętową akceleracją
i wydajnymi zamiennikami programowymi. Interfejs C z wiązaniami innych
języków dla wszystkich AWS SDK.

%package devel
Summary:	Header files for AWS Checksums library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AWS Checksums
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aws-c-common-devel

%description devel
Header files for AWS Checksums library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AWS Checksums.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/checksum-profile
%attr(755,root,root) %{_libdir}/libaws-checksums.so.1.0.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libaws-checksums.so
%{_includedir}/aws/checksums
%{_libdir}/cmake/aws-checksums
