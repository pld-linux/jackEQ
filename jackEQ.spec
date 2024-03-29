Summary:	3-Band Equalizer for JACK
Summary(pl.UTF-8):	3-pasmowy korektor dla JACK-a
Name:		jackEQ
Version:	0.4.0
Release:	2
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/jackeq/%{name}-%{version}.tar.gz
# Source0-md5:	4e46452f2f562235b61aea05df9782b5
Source1:	%{name}.desktop
Source2:	jackeq.png
URL:		http://jackeq.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1.3.13
BuildRequires:	intltool
BuildRequires:	jack-audio-connection-kit-devel >= 0.50.0
BuildRequires:	ladspa-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
Requires:	ladspa-swh-plugins >= 0.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jackEQ is a tool for routing and manipulating audio from/to multiple
input/output sources. Is intended to provide an accessible method for
tweaking the treble, mid and bass of any JACK aware applications
output.

%description -l pl.UTF-8
jackEQ jest narzędziem do kierowania i manipulacji strumieni dźwięku
z/do wielokanałowych jego źródeł. W założeniu ma on w łatwy sposób
umożliwiać podkręcanie sopranów, środka i basów na wyjściach programów
korzystających z JACK-a.

%prep
%setup -q

%build
glib-gettextize --force --copy
%{__intltoolize} --automake
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install -c %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/jackeq
%{_datadir}/jackeq/*.png
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
