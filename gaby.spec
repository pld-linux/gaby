Summary:	Gaby is a small personal databases manager
Name:		gaby
Version:	1.9.20
Release:	1
Group:		X11/GNOME/Applications
Group(pl):	X11/GNOME/Aplikacje
License:	GPL
Url:		http://gaby.netpedia.net
Source0:	%{name}-%{version}.tar.gz
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2.0

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gaby is a small personal databases manager using GTK+ and Gnome (if
available) for its GUI. It was designed to provide straight-forward
access to databases a 'normal' user would like (addresses, books, ...)
while keeping the ability to easily create databases for other needs.
On a technical side it was designed with extensibility in mind and
relies a lot on plug-ins.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install-strip
for F in `find $RPM_BUILD_ROOT%{_prefix} -perm -111`
do
	strip $F || true
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog Gabyrc INSTALL NEWS README 
%doc README.translations README.upgrading TODO TODO.more gaby.lsm 
%doc doc/*.sgml doc/C/*.sgml 
%%{_sysconfdir}/gaby
%{_libdir}/gaby
%{_datadir}/gaby
%attr(755,root,root) %{_bindir}/gaby 
%attr(755,root,root) %{_bindir}/gabyprint 
%attr(755,root,root) %{_bindir}/gbc 
%attr(755,root,root) %{_bindir}/gcd 
%attr(755,root,root) %{_bindir}/videobase 
%attr(755,root,root) %{_bindir}/gnomecard 
%attr(755,root,root) %{_bindir}/builder
%{_datadir}/locale/da/LC_MESSAGES/gaby.mo
%{_datadir}/locale/de/LC_MESSAGES/gaby.mo
%{_datadir}/locale/es/LC_MESSAGES/gaby.mo
%{_datadir}/locale/fi/LC_MESSAGES/gaby.mo
%{_datadir}/locale/fr/LC_MESSAGES/gaby.mo
%{_datadir}/locale/ja/LC_MESSAGES/gaby.mo
%{_datadir}/locale/nl/LC_MESSAGES/gaby.mo
%{_datadir}/locale/no/LC_MESSAGES/gaby.mo
%{_datadir}/locale/pl/LC_MESSAGES/gaby.mo
%{_datadir}/locale/sv/LC_MESSAGES/gaby.mo
