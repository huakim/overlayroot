#
# Makefile  
#

build:

DRACUT_OVERLAYROOT_D = dracut/modules.d/50overlayroot

install:
	mkdir -p "$(BUILDROOT)/$(DESTDIR)/$(DRACUT_OVERLAYROOT_D)"
	for f in mount-overlayroot.sh module-setup.sh; do \
		install "overlayroot/$$f" \
			"$(BUILDROOT)/$(DESTDIR)/$(DRACUT_OVERLAYROOT_D)/" ; \
	done
	mkdir -p "$(BUILDROOT)/usr/sbin"
	for f in bin/*; do \
		install "$$f" \
			"$(BUILDROOT)/usr/sbin" ; \
	done
	mkdir -p "$(BUILDROOT)/etc"
	install "etc/overlayroot.conf" "$(BUILDROOT)/etc"

rpm:
	rpmbuild -ba specs/dracut-modules-overlayroot.spec

