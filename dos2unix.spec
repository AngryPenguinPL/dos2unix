Summary:	Converts DOS-style EOLs to UNIX-style EOLs and vice versa
Name:		dos2unix
Version:	1.0.0
Release:	%mkrel 3
License:	GPL
Group:		Text tools
URL:		http://www.megaloman.com/~hany/software/hd2u/
Source:		hd2u-%{version}.tar.bz2
BuildRequires:	popt-devel
BuildRoot:	%{_tmppath}/%{name}-root

%description
hd2u is "Hany's Dos2Unix converter". It provides 'dos2unix'.

'dos2unix' is filter used to convert DOS-style EOLs to UNIX-style
EOLs and vice versa (EOL - End Of Line character).

%prep

%setup -q -n hd2u-%{version}

%build

%configure

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m755 dos2unix %{buildroot}%{_bindir}/

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CREDITS ChangeLog INSTALL NEWS README TODO
%{_bindir}/dos2unix


