%{!?build_version: %global build_version 0}

Name:           eucalyptus-service-image
Version:        %{build_version}
Release:        0%{?build_id:.%build_id}%{?dist}
Summary:        Eucalyptus Service Image

Group:          Applications/System
# License needs to be the *distro's* license (Fedora is GPLv2, for instance)
License:        GPLv2
URL:            http://www.eucalyptus.com/

Source0:        %{name}-%{version}
# euimage metadata
Source1:        %{name}.yml
# Image's OS's license
Source2:        IMAGE-LICENSE
# Kickstart used to build the image (included as documentation)
Source3:        %{name}.ks

BuildRequires:  euca2ools >= 3.2

Obsoletes:      eucalyptus-imaging-worker-image < 1.1
Obsoletes:      eucalyptus-load-balancer-image < 1.2
Provides:       euclayptus-imaging-worker-image
Provides:       euclayptus-load-balancer-image


%description
This package contains a machine image for use in Eucalyptus to
instantiate multiple internal services.


%build
euimage-pack-image %{SOURCE0} %{SOURCE1}


%install
install -m 755 -d $RPM_BUILD_ROOT/usr/share/eucalyptus/service-images
install -m 644 *.euimage $RPM_BUILD_ROOT/usr/share/eucalyptus/service-images


%files
%defattr(-,root,root,-)
%doc IMAGE-LICENSE %{name}.ks
# Something else should probably own the service-images dir at some
# point, but we can deal with that later when we have more than one.
/usr/share/eucalyptus/service-images


%changelog
* Fri Dec 05 2014 Eucalyptus Release Engineering <support@eucalyptus.com> - 0.1-0
- Created
