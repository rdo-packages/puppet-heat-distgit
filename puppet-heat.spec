%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-heat
Version:        11.4.0
Release:        1%{?dist}
Summary:        Puppet module for OpenStack Heat
License:        ASL 2.0

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
%setup -q -n openstack-heat-%{upstream_version}

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
* Fri Dec 01 2017 RDO <dev@lists.rdoproject.org> 11.4.0-1
- Update to 11.4.0

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 11.3.0-1
- Update to 11.3.0



