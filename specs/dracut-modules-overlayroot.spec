Summary:	Dracut module to mount the root partition with a RW fs on top of a RO fs
Name:		dracut-modules-overlayroot
Version:	0.2
Release:	beta%{?dist}
License:	GPLv3
Group:		System Environment/Base
Source0:	dracut-modules-overlayroot-%{version}.tar.gz	

Requires:	dracut
Requires:	util-linux

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
%if 0%{?amzn} || 0%{?rhel} || 0%{?centos}
%dir %{_prefix}/lib/dracut/modules.d/50overlayroot
%{_prefix}/lib/dracut/modules.d/50overlayroot/mount-overlayroot.sh
%{_prefix}/lib/dracut/modules.d/50overlayroot/module-setup.sh
/etc/overlayroot.conf
%{_prefix}/sbin/overlayroot-chroot
%endif

%post 


%changelog
* Sun Apr 09 2017 George Fleury <gfleury@gmail.com> - 0.1-beta
- First version 
