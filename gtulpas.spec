Summary:	Gnome Tulpas pool game
Summary(pl):	Gnome Tulpas - gra w bilard
Name:		gtulpas
Version:	1.0.0
Release:	0
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Vendor:		SuSE GmbH, Nuernberg, Germany
Source0:	http://www.suse.cz/gtulpas/%{name}-%{version}.tar.gz
URL:		http://www.suse.cz/gtulpas/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gnome-libs-devel
BuildRequires:	OpenGL-devel
BuildRequires:	gtkglarea-devel
BuildRequires:	guile-devel
Autoreqprov:	on

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gnome Tulpas pool game.

%description -l pl
Gnome Tulpas - gra w bilard.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" \
./configure --prefix=/opt/gnome %{_target_cpu}-suse-linux

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/{lib,gtulpas},%{docdir}}
%{__make} install prefix=$RPM_BUILD_ROOT/opt/gnome
ln -sf %{_datadir}/gnome/help/gtulpas/C $RPM_BUILD_ROOT%{docdir}/gtulpas/userdoc
%{?suse_check}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/gtulpas
%{_prefix}/gtulpas
%{_datadir}/locale/cs/LC_MESSAGES/gtulpas.mo
%{_datadir}/gnome/help/gtulpas
%{_applnkdir}/Games/gtulpas.desktop
%{_datadir}/gtulpas
%{_pixmapsdir}/gtulpas.png
