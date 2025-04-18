Summary:	Dracut module to mount the root partition with a RW fs on top of a RO fs
Name:		dracut-modules-overlayroot
Version:	0.2
Release:	beta%{?dist}
License:	GPLv3
Group:		System Environment/Base
Source0:	https://github.com/zuhhaga/overlayroot/archive/refs/tags/v%{version}.tar.gz#/overlayroot-%{version}.tar.gz

Requires:	dracut
Requires:	util-linux
BuildRequires:  make

BuildArch:	noarch

%description
This dracut module will re-mount the root fs with overlayfs on top of the real  
root filesystem. Keeping the real root filesystem in read-only mode. All the 
writes and new data are written another filesystem (root-rw). 

%prep
# extract cloud-utils
%setup -q -n overlayroot-%{version}

%build

%install
make install BUILDROOT=%{buildroot} DESTDIR=%{_exec_prefix}/lib


%files
%doc README.md
%dir %{_prefix}/lib/dracut/modules.d/50overlayroot
%dir %{_prefix}/lib/dracut/modules.d/
%dir %{_prefix}/lib/dracut/
%{_prefix}/lib/dracut/modules.d/50overlayroot/mount-overlayroot.sh
%{_prefix}/lib/dracut/modules.d/50overlayroot/module-setup.sh
%{_sysconfdir}/overlayroot.conf
%{_prefix}/sbin/overlayroot-chroot

%post 


%changelog
* Wed Aug 02 2023 huakim tylyktar <zuhhaga@gmail.com> - 0.2-beta
- Minor fixes and updated spec file

* Sun Apr 09 2017 George Fleury <gfleury@gmail.com> - 0.1-beta
- First version 
