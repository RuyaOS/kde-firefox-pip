Name: kde-firefox-pip
Version: 1
Release: 1%{?dist}
Summary: Custumize Firefox PIP to close perfection in KDE plasma 
License: GPLv3
URL: https://parmg.sa
Source0: LICENSE
Source1: kwinrulesrc
BuildArch: noarch

%description
Custumize Firefox PIP to close perfection in KDE plasma 

%prep
cp %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/skel/.config

%files
%license LICENSE
%{_sysconfdir}/skel/.config/kwinrulesrc

%changelog
* Tue Oct 11 2022 Mosaab Alzoubi <mosaab[AT]parmg[DOT]sa> - 1-1
- Initial
