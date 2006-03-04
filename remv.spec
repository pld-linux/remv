Summary:	Regular expression powered renaming tool
Name:		remv
Version:	0.4.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://labix.org/download/remv/%{name}-%{version}.tar.gz
# Source0-md5:	d5de032eadb412bf2b86629aa031ba89
URL:		http://labix.org/remv
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
That's a tool to rename files with the help of regular expressions. It allows
one to replace parts of filenames and/or directories, rename them completely,
remove files which match a given pattern, change the case of them, use help of
external programs, and more.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install remv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/remv
