# TODO
# - better icon, placed in pixmapsdir (maybe)
#
Summary:	3 - Band Equalizer for JACK
Summary(pl):	3 - pasmowy korektor dla JACKa
Name:		jackEQ
Version:	0.3.6
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/jackeq/%{name}-%{version}.tar.gz
# Source0-md5:	8aafe8786066ebd0f1b36baa2612310e
Source1:	%{name}.desktop
Patch0:		%{name}-ladspa_plugins_path.patch
URL:		http://jackeq.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1.3.13
BuildRequires:	intltool
BuildRequires:	jack-audio-connection-kit-devel >= 0.50.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
Requires:	ladspa-swh-plugins >= 0.4.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jackEQ is a tool for routing and manipulating audio from/to multiple
input/output sources. Is intended to provide an accessible method
for tweaking the treble, mid and bass of any JACK aware applications
output.

%description -l pl
jackEQ jest narzêdziem do kierowania i manipulacji strumieni d¼wiêku
z/do wielokana³owych jego ¼róde³. W za³o¿eniu ma on w ³atwy sposób
umo¿liwiaæ podkêcanie sopranów, ¶rodka i basów na wyj¶ciach 
programów korzystaj±cych z JACKa.

%prep
%setup -q
%patch0 -p1

%build
glib-gettextize --force --copy
intltoolize --copy --force --automake
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -c %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/jackEQ/pixmaps/Make*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO 
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/jackEQ
%{_datadir}/jackEQ/pixmaps/*
%{_desktopdir}/*.desktop
