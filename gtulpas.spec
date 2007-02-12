Summary:	GNOME Tulpas pool game
Summary(pl.UTF-8):   GNOME Tulpas - gra w bilard
Name:		gtulpas
Version:	1.0.0
Release:	0
License:	GPL
Group:		X11/Applications/Games
Vendor:		SuSE GmbH, Nuernberg, Germany
Source0:	http://www.suse.cz/gtulpas/%{name}-%{version}.tar.gz
# Source0-md5:	cf208593998978c6c835e815508f20e7
Patch0:		%{name}-guileglue.patch
Patch1:		%{name}-guile-snarf.patch
Patch2:		%{name}-gcc33.patch
Patch3:		%{name}-glx.patch
Patch4:		%{name}-dif.patch
Patch5:		%{name}-DESTDIR.patch
URL:		http://www.suse.cz/gtulpas/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtkglarea1-devel
BuildRequires:	guile-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Tulpas pool game.

%description -l pl.UTF-8
GNOME Tulpas - gra w bilard.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_applnkdir}/Games

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gtulpas
%{_datadir}/gtulpas
%{_applnkdir}/Games/gtulpas.desktop
%{_pixmapsdir}/gtulpas.png
