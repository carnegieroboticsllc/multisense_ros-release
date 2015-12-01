^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package multisense_lib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.4.6 (2015-12-01)
------------------

3.4.5 (2015-10-20)
------------------

3.4.4 (2015-06-25)
------------------

3.4.3 (2015-02-12)
------------------

3.4.2 (2015-01-30)
------------------
* Added launch_robot_state_publisher argument to multisense_bringup/multisense.launch. Added geometry_msgs/Vector3Stamped publishers for accelerometer, gyroscope, and magnetometer data. Updated LibMultiSense.
* Contributors: Matt Alvarado <malvarado@carnegierobotics.com>

3.4.1 (2014-12-30)
------------------

3.4.0 (2014-12-11)
------------------
* Updated LibMultiSense to version 3.5. Fixed camera_info publishing bug for non-standard cameras (BCAM, Multisense-M, ST21). Added HDR option to dynamic reconfigure.
* Contributors: Matt Alvarado <malvarado@carnegierobotics.com>

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

3.3.3 (2014-10-24)
------------------
* Updated CMakeLists.txt to resolve linker errors with Jenkins.
* Contributors: Matt Alvarado <malvarado@carnegierobotics.com>

3.3.2 (2014-10-23)
------------------
* Added colorized laser point cloud topic. Removed LIDAR streaming frequency warning. Updated build dependencies for Bloom. General interface cleanup.
* Contributors: Matt Alvarado <malvarado@carnegierobotics.com>

3.3.0 (2014-09-30)
------------------
* Updated LibMultiSense to build under C++11. Added URDF for the MultiSense S7/S7S and BCAM. Added support for 16 bit mono images. Added support for the MultiSense ST21 thermal stereo camera. Added organized pointcloud publishing. Changed laser and camera pointcloud color fields to FLOAT32 for PCL compatibility. Changed default color image encoding to BGR8. Added spindle joint publishing via the ROS joint_state_publisher. Updated multisense_cal_check to handle various serial number entires. Added the launch-file sensor parameter to load different URDF’s on startup. Published camera info topics for each image topic (for unrectified topics K, D, and R are populated). Added default laser transform publishing to keep the laser TF tree valid even when there are no subscriptions to laser topics.
* Changed license from LGPL to BSD in both the ROS Driver and LibMultiSense C++ library. Fixed bug in disparity image publishing.  Fixed bug in raw_cam_config publishing.  Fixed bug in building using rosbuild under Groovy, Hydro, Indigo, etc.  Fixed Jenkins linking issue with libpng. Fixed termination bug in process_bags.py.
* Remove '-march=native' compiler options as it is causing assembler errors on some platforms (specifically: Haswell/12.04_amd64/ROS Hydro)
* Add wire-protocol support for DirectedStreams on CRL's Monocular IP Camera. Misc. other bugfixes.
* Adding support files for MultiSense-S21 and Mono IP Camera products
* Add initial support for CRL's Mono IP Camera. Numerous fixes in catkin build infrastructure.
* Add support for catkin and rosbuild (Builds under Fuerte, Groovy, Hydro, and Indigo). Transitioned laser calibration from KDL and joint_state_publisher to pure ROS TF messages. Add support for multiple Multisene units via namespacing and tf_prefix's. Modified default topic names to reflect the new namespacing parameters (Default base namespace is now /multisense rather than /multisense_sl). Add support for 3.1_beta sensor firmware which includes support for Multisense-S21 units. Please note that the 3.1 ROS driver release is fully backwards compatible with all 2.X firmware versions.
* Release_3.0_beta: Add support for 3.0_beta sensor firmware (SGM hardware stereo core: disparity at all resolutions, 2:1 rectangular pixel modes, 64/128/256 disparity modes, hardware bi-lateral post-stereo disparity filter support with tuning), add colorized points2 topic, add pointcloud egde and range filtering, add raw left/right disparitiy image topics, add stereo-cost image topic, misc other feature enhancements and bugfixes.  Please note that the 3.0_beta release is fully backwards compatiblie with all 2.X firmware versions.
* Release_2.3: Add support for 2.3 sensor firmware (IMU / CMV4000 support), add 'MultiSenseUpdater' firmware upgrade tool, add smart dynamic_reconfigure presentation, remove multisense_diagnostics/multisense_dashboard, wire protocol to version 3.0 (w/ support for forthcoming SGM core), misc. other bugfixes and feature enhancements.
* Low-level c++ API to version 2.2
* -Add PPS topic: /multisense_sl/pps (std_msgs/Time)
  -Corrected step size of color images, which now display correctly using image_view
  -Add 'network_time_sync' option to dynamic reconfigure
* Imported Release 2.0 of MultiSense-SL ROS driver.
* Contributors: David LaRose <dlr@carnegierobotics.com>, Eric Kratzer <ekratzer@carnegierobotics.com>, Matt Alvarado <malvarado@carnegierobotics.com>
