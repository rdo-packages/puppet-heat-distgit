%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-heat
Version:        9.4.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Heat
License:        Apache-2.0

URL:            https://launchpad.net/puppet-heat

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Heat

%prep
%setup -q -n openstack-heat-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/heat/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/heat/



%files
%{_datadir}/openstack-puppet/modules/heat/


%changelog
* Thu Sep 29 2016 Alfredo Moralejo <amoralej@redhat.com> 9.4.0-1
- Update to 9.4.0

* Wed Sep 21 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.3.0-1
- Update to 9.3.0

* Fri Sep 16 2016 Haikel Guemar <hguemar@fedoraproject.org> 9.2.0-1
- Update to 9.2.0


# REMOVEME: error caused by commit http://git.openstack.org/cgit/openstack/puppet-heat/commit/?id=a0432b3228301bf947f659ac1fa807f9de9099f5
