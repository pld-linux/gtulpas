#
# spec file for package gtulpas (Version 1.0.0)
# 
# Copyright  (c)  2000  SuSE GmbH  Nuernberg, Germany.
#
# please send bugfixes or comments to feedback@suse.de.
#

# neededforbuild  autoconf automake indent orbit orbitdev guile gnlibs gnlibsd gnobjc gpp libgpp gtk gtkdev glib glibdev imlib imlibdev imlibcfe xpm gettext libtiff libjpeg libpng libungif esound audiofil guile gtkglare mesa mesasoft
# usedforbuild    aaa_base aaa_dir audiofil autoconf automake base bash bindutil binutils bison bzip compress cpio cracklib devs diff egcs esound ext2fs file fileutil find flex gawk gdbm gettext glib glibdev gnlibs gnlibsd gnobjc gpm gpp gppshare groff gtk gtkdev gtkglare guile gzip imlib imlibcfe imlibdev indent kbd ldso less libc libgpp libjpeg libpng libtiff libungif libz lx_suse make mesa mesasoft mktemp modules ncurses net_tool netcfg nkita nkitb nssv1 orbit orbitdev pam patch perl pgp ps rcs rpm sendmail sh_utils shadow shlibs strace syslogd sysvinit texinfo textutil timezone unzip util vim xdevel xf86 xpm xshared

Vendor:       SuSE GmbH, Nuernberg, Germany
Distribution: SuSE Linux 6.3 (i386)
Name:         gtulpas
Release:      0
Packager:     feedback@suse.de

Copyright:    GPL
Autoreqprov:  on
Version:      1.0.0
Summary:      Gnome Tulpas pool game
Source: gtulpas-%{version}.tar.gz
Group:          X11/Games
Prefix:         /opt/gnome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome Tulpas pool game

Authors:
--------
    Tomas Bily <tomby@suse.cz>
    Jan Bily <bilyj@seznam.cz>
    Radek Doulik <rodo@suse.cz>
    Daniel Skarda <0rfelyus@suse.cz>

%prep
%setup

%build
CFLAGS=${RPM_OPT_FLAGS} \
./configure --prefix=/opt/gnome %{_target_cpu}-suse-linux
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{prefix}/{lib,gtulpas},%{docdir}}
make install prefix=$RPM_BUILD_ROOT/opt/gnome
ln -s %{prefix}/share/gnome/help/gtulpas/C $RPM_BUILD_ROOT%{docdir}/gtulpas/userdoc
%{?suse_check}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README ChangeLog
%{prefix}/bin/gtulpas
%{prefix}/gtulpas
%{prefix}/share/locale/cs/LC_MESSAGES/gtulpas.mo
%{prefix}/share/gnome/help/gtulpas
%{prefix}/share/gnome/apps/Games/gtulpas.desktop
%{prefix}/share/gtulpas
%{prefix}/share/pixmaps/gtulpas.png
