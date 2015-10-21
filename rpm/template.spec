Name:           ros-jade-multisense
Version:        3.4.5
Release:        0%{?dist}
Summary:        ROS multisense package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/multisense
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-multisense-bringup
Requires:       ros-jade-multisense-cal-check
Requires:       ros-jade-multisense-description
Requires:       ros-jade-multisense-lib
Requires:       ros-jade-multisense-ros
BuildRequires:  ros-jade-catkin

%description
multisense catkin driver

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Oct 21 2015 Maintained by Carnegie Robotics LLC <support@carnegierobotics.com> - 3.4.5-0
- Autogenerated by Bloom

* Thu Jun 25 2015 Maintained by Carnegie Robotics LLC <support@carnegierobotics.com> - 3.4.4-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Maintained by Carnegie Robotics LLC <support@carnegierobotics.com> - 3.4.3-0
- Autogenerated by Bloom

