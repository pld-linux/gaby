#
# Conditional build:
# _without_gtk		- without gtk+-based gui (text only)
# _without_python	- plain gtk-based version without python support
# _without_gnome	- without gnome-based support
# _without_libglade	- without libglade config
# _without_xml		- without xml config
# _without_gdk_pixbuf	- without gdk-pixbuf
#
Summary:	Gaby is a small personal databases manager
Summary(pl):	Gaby - ma³y osobisty zarz±dca baz danych
Name:		gaby
Version:	2.0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gaby.sourceforge.net/archives/%{name}-%{version}.tar.gz
# Source0-md5:	1203f7a548e46bc0bf5987fb2e1508ee
Patch0:		%{name}-DESTDIR.patch
URL:		http://gaby.sourceforge.net/
BuildRequires:	bison
%{!?_without_gdk_pixbuf:BuildRequires:	gdk-pixbuf-devel}
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_gui:BuildRequires:		gtk+-devel >= 1.2.0}
%{!?_without_libglade:BuildRequires:	libglade-devel}
BuildRequires:	libtool
%{!?_without_libglade:BuildRequires:	libxml-devel}
%{!?_without_xml:BuildRequires:		libxml-devel}
%{!?_without_python:BuildRequires:	python-devel}
# python-pygtk and gtk+-devel require to be installed with the same prefix
# to be visible; currently not this case :(
%{!?_without_python:%{!?_without_gui:Requires:	python-pygtk}}
%{!?_without_gnome:Requires:	gnome-libs}
%{!?_without_gui:Requires:	gtk+ >= 1.2.0}
%{!?_without_python:Requires:	python}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gaby is a small personal databases manager using GTK+ and Gnome (if
available) for its GUI. It was designed to provide straight-forward
access to databases a 'normal' user would like (addresses, books, ...)
while keeping the ability to easily create databases for other needs.
On a technical side it was designed with extensibility in mind and
relies a lot on plug-ins.

%description -l pl
Gaby jest ma³ym osobistym zarz±dc± baz danych u¿ywaj±cym GTK+ i
GNOME. Zosta³ zaprojektowany aby udostêpniæ prosty dostêp do baz
danych, które "zwyk³y" u¿ytkownik chcia³by mieæ (adresy, ksi±¿ki...),
pozwalaj±c ³atwo tworzyæ bazy do innych celów. Od technicznej strony
zosta³ zaprojektowany tak, by byæ rozszerzalnym poprzez wtyczki.

%prep
%setup -q
%patch0 -p0

%build
CFLAGS="%{rpmcflags}" ./configure \
	--prefix=%{_prefix} \
	--sysconfdir=%{_sysconfdir} \
	%{?_without_gnome:--disable-gnome} \
	%{?_without_python:--disable-python} \
	%{?_without_gtk:--disable-gui} \
	%{?_without_libglade:--without-libglade-config} \
	%{?_without_xml:--without-xml-config} \
	%{?_without_gdk_pixbuf:--disable-gdk_pixbuftest} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO* Gabyrc 
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
