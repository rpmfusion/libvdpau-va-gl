Name:           libvdpau-va-gl
Version:        0.3.4
Release:        6%{?dist}
Summary:        VDPAU driver with OpenGL/VAAPI back-end

License:        LGPLv3
URL:            https://github.com/i-rinat/libvdpau-va-gl
Source0:        https://github.com/i-rinat/libvdpau-va-gl/archive/v%{version}.tar.gz

#Unlikely to have some meaning outside of intel driver
ExclusiveArch:  i686 x86_64 ia64

BuildRequires:  cmake
BuildRequires:  pkgconfig(vdpau)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)

Requires: libva-intel-driver



%description
VDPAU driver with OpenGL/VAAPI back-end.


%prep
%setup -q


%build
mkdir -p build
cd build
%{cmake} \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DLIB_INSTALL_DIR=%{_libdir}/vdpau \
   ..

make %{?_smp_mflags}


%install
cd build
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


#This should automatically enable vdpau backend on intel i965
#But xf86-intel doesn't want't to apply
#http://lists.freedesktop.org/archives/intel-gfx/2013-August/031872.html
ln -s libvdpau_va_gl.so.1 $RPM_BUILD_ROOT%{_libdir}/vdpau/libvdpau_i965.so.1


%files
%doc ChangeLog COPYING* README.md
%{_libdir}/vdpau/libvdpau_va_gl.so.1
%exclude %{_libdir}/vdpau/libvdpau_va_gl.so
#Hack - Will be removed
%{_libdir}/vdpau/libvdpau_i965.so.1



%changelog
* Sun Jan 04 2015 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-6
- Fix asserts in release package - rfbz#3419

* Tue Nov 04 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-5
- Rebuilt for vaapi 0.36

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.3.4-4
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-3
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 0.3.4-2
- Rebuilt for ffmpeg-2.3

* Sat Apr 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.3.4-1
- Update to 0.3.4

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 0.3.2-2
- Rebuilt for ffmpeg-2.2

* Sun Jan 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.3.2-1
- Update to 0.3.2

* Tue Nov 19 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.2.1-1
- Update to 0.2.1

* Thu Jul 18 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.1.0-1
- Initial spec file

