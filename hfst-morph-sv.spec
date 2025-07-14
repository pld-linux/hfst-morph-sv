Summary:	HFST morphological analysis transducer for Swedish language
Summary(pl.UTF-8):	Automat HFST do analizy morfologicznej dla języka szwedzkiego
Name:		hfst-morph-sv
# or 20110316?
Version:	0
Release:	1
License:	CC-SA v1.0
Group:		Applications/Text
# source is hfst-swedish.tar.gz, but it doesn't contain scripts
Source0:	http://downloads.sourceforge.net/hfst/hfst-swedish-installable.tar.gz
# Source0-md5:	fac0f40423b416c2d3bbd5ace51f25c3
Patch0:		%{name}-DESTDIR.patch
URL:		http://hfst.sourceforge.net/
Requires:	hfst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Swedish Swelex morphological transducer for HFST. It's based
on "Den stora svenska ordlistan" <http://dsso.se/>.

%description -l pl.UTF-8
Ten pakiet zawiera automat Swelex dla HFST do analizy morfologicznej
języka szwedzkiego. Jest oparty na "Den stora svenska ordlistan"
<http://dsso.se/>.

%prep
%setup -q -n hfst-swedish-installable
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/swedish-analyze.sh
%attr(755,root,root) %{_bindir}/swedish-generate.sh
%{_datadir}/hfst/sv
