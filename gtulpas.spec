Vendor:		SuSE GmbH, Nuernberg, Germany
Name:		gtulpas
Release:	0
License:	GPL
Autoreqprov:	on
Version:	1.0.0
Summary:	Gnome Tulpas pool game
Source0:	gtulpas-%{version}.tar.gz
Group:		X11/Games
Group(pl):	X11/Gry
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gnome Tulpas pool game

Authors:
- -------- Tomas Bily <tomby@suse.cz> Jan Bily <bilyj@seznam.cz> Radek
  Doulik <rodo@suse.cz> Daniel Skarda <0rfelyus@suse.cz>

%prep
%setup -q

%build
CFLAGS=${RPM_OPT_FLAGS} \
./configure --prefix=/opt/gnome %{_target_cpu}-suse-linux
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/{lib,gtulpas},%{docdir}}
%{__make} install prefix=$RPM_BUILD_ROOT/opt/gnome
ln -s %{_datadir}/gnome/help/gtulpas/C $RPM_BUILD_ROOT%{docdir}/gtulpas/userdoc
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
%{_datadir}/pixmaps/gtulpas.png
