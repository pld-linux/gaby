%define name gaby
%define version 1.9.20
%define release 1
%define prefix /usr
%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Gaby is a small personal databases manager. 
Name: %{name}
Version: %{version}
Release: %{release}
Group: X11/Gnome/Applications/Graphics/Productivity
Copyright: GPL
Url: http://gaby.netpedia.net
Packager: Dag Wieers <dag@life.be>
Distribution: N/A 
Source: %{name}-%{version}.tar.gz
Buildroot: /var/tmp/%{name}-%{version}-%{release}-root
Requires: gtk+ >= 1.2.0

%description
Gaby is a small personal databases manager using GTK+ and Gnome (if available) 
for its GUI. It was designed to provide straight-forward access to databases a
'normal' user would like (addresses, books, ...) while keeping the ability to 
easily create databases for other needs. On a technical side it was designed 
with extensibility in mind and relies a lot on plug-ins. 

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix} --sysconfdir=/etc
make

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install-strip
for F in `find $RPM_BUILD_ROOT%{prefix} -perm -111`
do
	strip $F || true
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root)
%doc AUTHORS BUGS COPYING ChangeLog Gabyrc INSTALL NEWS README 
%doc README.translations README.upgrading TODO TODO.more gaby.lsm 
%doc doc/*.sgml doc/C/*.sgml 
%/etc/gaby
%{prefix}/lib/gaby
%{prefix}/share/gaby
%attr(755,root,root) %{prefix}/bin/gaby 
%attr(755,root,root) %{prefix}/bin/gabyprint 
%attr(755,root,root) %{prefix}/bin/gbc 
%attr(755,root,root) %{prefix}/bin/gcd 
%attr(755,root,root) %{prefix}/bin/videobase 
%attr(755,root,root) %{prefix}/bin/gnomecard 
%attr(755,root,root) %{prefix}/bin/builder
%{prefix}/share/locale/da/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/de/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/es/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/fi/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/fr/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/ja/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/nl/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/no/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/pl/LC_MESSAGES/gaby.mo
%{prefix}/share/locale/sv/LC_MESSAGES/gaby.mo
