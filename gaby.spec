#
# Conditional build:
%bcond_without	gtk		# without gtk+-based gui (text only)
%bcond_without	python		# plain gtk-based version without python support
%bcond_without	gnome		# without gnome-based support
%bcond_without	libglade	# without libglade config
%bcond_without	xml		# without xml config
%bcond_without	gdk_pixbuf	# without gdk-pixbuf
#
Summary:	Gaby is a small personal databases manager
Summary(pl.UTF-8):	Gaby - mały osobisty zarządca baz danych
Name:		gaby
Version:	2.0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://gaby.sourceforge.net/archives/%{name}-%{version}.tar.gz
# Source0-md5:	1203f7a548e46bc0bf5987fb2e1508ee
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-gcc33.patch
Patch2:		%{name}-doc.patch
URL:		http://gaby.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
%{?with_gdk_pixbuf:BuildRequires:	gdk-pixbuf-devel >= 0.7.0}
BuildRequires:	gettext-tools
%{?with_gnome:BuildRequires:	gnome-libs-devel}
%{?with_gui:BuildRequires:		gtk+-devel >= 1.2.5}
%{?with_libglade:BuildRequires:	libglade-devel}
BuildRequires:	libtool
%{?with_libglade:BuildRequires:	libxml-devel}
%{?with_xml:BuildRequires:		libxml-devel}
%{?with_python:BuildRequires:	python-devel}
%{?with_python:BuildRequires:	python-pygtk < 1.99}
# python-pygtk and gtk+-devel require to be installed with the same prefix
# to be visible; currently not this case :(
%{?with_python:%{?with_gui:Requires:	python-pygtk < 1.99}}
%{?with_gui:Requires:	gtk+ >= 1.2.5}
%{?with_python:Requires:	python}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gaby is a small personal databases manager using GTK+ and GNOME (if
available) for its GUI. It was designed to provide straight-forward
access to databases a 'normal' user would like (addresses, books, ...)
while keeping the ability to easily create databases for other needs.
On a technical side it was designed with extensibility in mind and
relies a lot on plug-ins.

%description -l pl.UTF-8
Gaby jest małym osobistym zarządcą baz danych używającym GTK+ i
GNOME. Został zaprojektowany aby udostępnić prosty dostęp do baz
danych, które "zwykły" użytkownik chciałby mieć (adresy, książki...),
pozwalając łatwo tworzyć bazy do innych celów. Od technicznej strony
został zaprojektowany tak, by być rozszerzalnym poprzez wtyczki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="`gdk-pixbuf-config --cflags` `libglade-config --cflags` `orbit-config --cflags client`"
%configure \
	%{!?with_gnome:--disable-gnome} \
	%{!?with_python:--disable-python} \
	%{!?with_gtk:--disable-gui} \
	%{!?with_libglade:--without-libglade-config} \
	%{!?with_xml:--without-xml-config} \
	%{!?with_gdk_pixbuf:--disable-gdk_pixbuftest} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{_libdir}/%{name} -name '*.a' -o -name '*.la' | xargs rm -f

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README* TODO* misc/Gabyrc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}
%{_sysconfdir}/gaby
%dir %{_datadir}/gaby
%{_datadir}/gaby/glade
%{_datadir}/gaby/scripts
%{_datadir}/gaby/gaby_tips.txt
%lang(de) %{_datadir}/gaby/gaby_tips_de.txt
%lang(fi) %{_datadir}/gaby/gaby_tips_fi.txt
%lang(fr) %{_datadir}/gaby/gaby_tips_fr.txt
%lang(nb) %{_datadir}/gaby/gaby_tips_no.txt
%{_mandir}/man1/*
