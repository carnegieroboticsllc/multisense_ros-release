^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package multisense_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.4.5 (2015-10-20)
------------------

3.4.4 (2015-06-25)
------------------

3.4.3 (2015-02-12)
------------------
* Removed URDF and xacro dependency from multisense_description. Fixed bitbucket issue #36 relating to point cloud size allocation.
* Contributors: Matt Alvarado <malvarado@carnegierobotics.com>

3.4.2 (2015-01-30)
------------------

3.4.1 (2014-12-30)
------------------

3.4.0 (2014-12-11)
------------------

3.3.9 (2014-12-08)
------------------

3.3.8 (2014-12-02)
------------------

3.3.7 (2014-11-25)
------------------

3.3.6 (2014-11-10)
------------------

3.3.5 (2014-11-03)
------------------

3.3.4 (2014-10-31)
------------------
* Added sensor_msgs::Imu message publishing. No orientation information is published. Updated URDF models to have consistent accelerometer, magnetometer, and gyroscope frame_ids.
* Contributors: Matt Alvarado <malvarado@carnegierobotics.com>

3.3.3 (2014-10-24)
------------------

3.3.2 (2014-10-23)
------------------
* Added colorized laser point cloud topic. Removed LIDAR streaming frequency warning. Updated build dependencies for Bloom. General interface cleanup.
* Contributors: Matt Alvarado <malvarado@carnegierobotics.com>

3.3.0 (2014-09-30)
------------------
* Updated LibMultiSense to build under C++11. Added URDF for the MultiSense S7/S7S and BCAM. Added support for 16 bit mono images. Added support for the MultiSense ST21 thermal stereo camera. Added organized pointcloud publishing. Changed laser and camera pointcloud color fields to FLOAT32 for PCL compatibility. Changed default color image encoding to BGR8. Added spindle joint publishing via the ROS joint_state_publisher. Updated multisense_cal_check to handle various serial number entires. Added the launch-file sensor parameter to load different URDF’s on startup. Published camera info topics for each image topic (for unrectified topics K, D, and R are populated). Added default laser transform publishing to keep the laser TF tree valid even when there are no subscriptions to laser topics.
* Changed license from LGPL to BSD in both the ROS Driver and LibMultiSense C++ library. Fixed bug in disparity image publishing.  Fixed bug in raw_cam_config publishing.  Fixed bug in building using rosbuild under Groovy, Hydro, Indigo, etc.  Fixed Jenkins linking issue with libpng. Fixed termination bug in process_bags.py.
* Adding support files for MultiSense-S21 and Mono IP Camera products
* Add initial support for CRL's Mono IP Camera. Numerous fixes in catkin build infrastructure.
* Add support for catkin and rosbuild (Builds under Fuerte, Groovy, Hydro, and Indigo). Transitioned laser calibration from KDL and joint_state_publisher to pure ROS TF messages. Add support for multiple Multisene units via namespacing and tf_prefix's. Modified default topic names to reflect the new namespacing parameters (Default base namespace is now /multisense rather than /multisense_sl). Add support for 3.1_beta sensor firmware which includes support for Multisense-S21 units. Please note that the 3.1 ROS driver release is fully backwards compatible with all 2.X firmware versions.
* Release_2.3: Add support for 2.3 sensor firmware (IMU / CMV4000 support), add 'MultiSenseUpdater' firmware upgrade tool, add smart dynamic_reconfigure presentation, remove multisense_diagnostics/multisense_dashboard, wire protocol to version 3.0 (w/ support for forthcoming SGM core), misc. other bugfixes and feature enhancements.
* Imported Release 2.0 of MultiSense-SL ROS driver.
* Contributors: David LaRose <dlr@carnegierobotics.com>, Eric Kratzer <ekratzer@carnegierobotics.com>, Matt Alvarado <malvarado@carnegierobotics.com>
