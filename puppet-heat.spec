%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%{?dlrn: %global tarsources %{name}-%{upstream_version}}
%{!?dlrn: %global tarsources openstack-heat-%{upstream_version}}

Name:           puppet-heat
Version:        XXX
Release:        XXX
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
%setup -q -n %{tarsources}

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

