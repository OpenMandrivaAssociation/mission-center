%define binary_name missioncenter
%define rdn_name io.missioncenter.MissionCenter

Name:		mission-center
Version:	1.0.2
Release:	1
Summary:	Mission Center
License:	GPL-3.0
Group:		Monitoring
Url:		https://missioncenter.io/
Source0:	https://gitlab.com/mission-center-devs/mission-center/-/archive/v%{version}/mission-center-v%{version}.tar.bz2
# clone source with submodules (alternative use git clone --recursive) the cd do /submodules/magpie and build vendor "cargo vendor"
Source1:	vendor.tar.xz
# Downloaded submodule. See hash in mission-center/subprojects
Source2:	https://gitlab.com/mission-center-devs/gng/-/archive/gng-319d95d29cbc3c373ae61cff228e8440fbaadbbb.tar.bz2

BuildRequires:	meson
BuildRequires:	rust-packaging
BuildRequires:	protobuf-compiler
BuildRequires:	pkgconfig(blueprint-compiler)
BuildRequires:	appstream
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	python3dist(sqlite3)
BuildRequires:	python-gi
# for magpie
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libglvnd)
Requires:	python-gi
Requires:	dconf
Requires:	dmidecode

%description
Monitor your CPU, Memory, Disk, Network and GPU usage with Mission Center.

%prep
%setup -q -n %{name}-v%{version} -a1 -a2
%cargo_prep -v vendor

cp -r gng-*/* subprojects/magpie

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{binary_name} --output %{name}.lang

%files -f %name.lang
%{_bindir}/%{binary_name}
%{_bindir}/%{binary_name}-magpie
%{_datadir}/applications/%{rdn_name}.desktop
%{_datadir}/%{binary_name}/
%{_datadir}/glib-2.0/schemas/%{rdn_name}.gschema.xml
%{_iconsdir}/hicolor/*/apps/%{rdn_name}*.svg
%{_datadir}/metainfo/%{rdn_name}.metainfo.xml
%doc README*
