Summary:	Regular expression powered renaming tool
Summary(pl):	Narz�dzie do zmiany nazw plik�w z u�yciem wyra�e� regularnych
Name:		remv
Version:	0.4.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://labix.org/download/remv/%{name}-%{version}.tar.gz
# Source0-md5:	d5de032eadb412bf2b86629aa031ba89
URL:		http://labix.org/remv
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
That's a tool to rename files with the help of regular expressions. It
allows one to replace parts of filenames and/or directories, rename
them completely, remove files which match a given pattern, change the
case of them, use help of external programs, and more.

%description -l pl
Jest to narz�dzie do zmiany nazw plik�w przy wykorzystaniu wyra�e�
regularnych. Pozwala ono: zmieni� cz�� nazwy pliku lub katalogu,
zmieni� ca�kowicie jego nazw�, usun�� pliki pasuj�ce do zadanego
wzorca, zmieni� wielko�� liter w nazwie, korzysta� z zewn�trznych
program�w itp.

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
