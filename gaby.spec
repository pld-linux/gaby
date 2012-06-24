Summary:	Gaby is a small personal databases manager
Name:		gaby
Version:	1.9.20
Release:	1
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
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
CFLAGS="%{rpmcflags}" ./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf AUTHORS BUGS ChangeLog NEWS README* TODO*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.gz BUGS.gz ChangeLog.gz Gabyrc NEWS.gz README.gz
%doc README.translations.gz README.upgrading.gz TODO.gz TODO.more.gz 
%doc doc/*.sgml doc/C/*.sgml 
%{_sysconfdir}/gaby
%{_libdir}/gaby
%{_datadir}/gaby
%attr(755,root,root) %{_bindir}/gaby 
%attr(755,root,root) %{_bindir}/gabyprint 
%attr(755,root,root) %{_bindir}/gbc 
%attr(755,root,root) %{_bindir}/gcd 
%attr(755,root,root) %{_bindir}/videobase 
%attr(755,root,root) %{_bindir}/gnomecard 
%attr(755,root,root) %{_bindir}/builder
%lang(da) %{_datadir}/locale/da/LC_MESSAGES/gaby.mo
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/gaby.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/gaby.mo
%lang(fi) %{_datadir}/locale/fi/LC_MESSAGES/gaby.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/gaby.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/gaby.mo
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/gaby.mo
%lang(no) %{_datadir}/locale/no/LC_MESSAGES/gaby.mo
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/gaby.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/gaby.mo
