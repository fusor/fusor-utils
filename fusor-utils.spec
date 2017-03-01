Summary: Fusor Server Utilities
Name:    fusor-utils
Version: 1.2.0
Release: 0%{?dist}
Group:   Applications/Internet 
License: Distributable
URL: https://github.com/fusor/fusor_utils
Source0: fusor-utils-sudoers
Source1: safe-mount.sh
Source2: safe-umount.sh

BuildArch: noarch
Requires: glusterfs-fuse

%description
Fusor Server Utilities

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/sudoers.d
cp -a %{SOURCE0} %{buildroot}%{_sysconfdir}/sudoers.d/%{name}
cp -a %{SOURCE1} %{SOURCE2} %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%{_bindir}/safe-mount.sh
%{_bindir}/safe-umount.sh
%{_sysconfdir}/sudoers.d/%{name}

%changelog
