Name:		gnaural
Version:	1.0.20110606
Release:	2
Summary:	A multi-platform programmable binaural-beat generator
Group:		Sound
License:	GPLv2+
URL:		http://gnaural.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gnaural-1.0.20110215-icon.patch
Patch1:		gnaural-1.0.20110215-xdg-menu.patch
BuildRequires:	gtk2-devel
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  sndfile-devel
BuildRequires:  portaudio-devel
BuildRequires:	desktop-file-utils gettext-devel
Requires:	hicolor-icon-theme

%description
Gnaural is a multi-platform programmable binaural-beat generator. It
is actually brainwave entrainment software for creating binaural beats
intended to be used as personal brainwave synchronization software,
for scientific research, or by professionals. Gnaural allows for the
creation of binaural beat tracks specifying different frequencies and
exporting tracks into different audio formats. Gnaural runnings can
also be linked over the internet, allowing synchronous sessions
between many users.

%prep
%setup -q
%patch0 -p1 -b .icon~
%patch1 -p1 -b .xdg~
autoreconf -f

%build
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_iconsdir}/hicolor/48x48/apps/%{name}.png


%changelog
* Tue Nov 08 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.20110606-1
+ Revision: 729169
- use %%_iconsdir in stead..
- add 'gettext-devel' to buildrequires to make 'autoreconf' work..
- imported package gnaural


* Tue Jun  7 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0.20110215-1
- initial Mandriva packaging, adapted from Fedora

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20100408-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue May 04 2010 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20100408-1
- Updated to 1.0.20100408

* Tue Nov 10 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20090808-1
- Updated to 1.0.20090808

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20080808-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.20080808-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 05 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20080808-5
- Removed "Application" from .desktop Categories.

* Sun Jan 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20080808-4
- Fixed missing -p for install command.

* Sun Jan 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20080808-3
- Removed fedora as vendor - as per new guidelines.

* Sun Jan 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20080808-2
- Fixed %%version, %%description, timestamp, fixed icon path,
- Removed useless buildrequires, fixed .desktop file installation.

* Sat Dec 06 2008 Rakesh Pandit <rakesh@fedoraproject.org> 1.0-1.20080808
- Initial build.
