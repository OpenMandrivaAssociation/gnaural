Name:		gnaural
Version:	1.0.20110606
Release:	1
Summary:	A multi-platform programmable binaural-beat generator
Group:		Sound
License:	GPLv2+
URL:		http://gnaural.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		gnaural-1.0.20110215-icon.patch
Patch1:		gnaural-1.0.20110215-xdg-menu.patch
BuildRequires:	gtk2-devel libglade2-devel libsndfile-devel portaudio-devel
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
%{_icons48dir}/%{name}.png
