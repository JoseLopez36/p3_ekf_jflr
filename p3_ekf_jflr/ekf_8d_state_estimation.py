import rclpy

import numpy as np

# Import the correct motion and observation models for the 8D case
from .motion_models.acceleration_motion_models import acceleration_motion_model_linearized_2
from .observation_models.odometry_imu_observation_models import odometry_imu_observation_model_with_acceleration_motion_model_linearized_2


from .filters.ekf import ExtendedKalmanFilter
from .kf_node import KalmanFilterFusionNode as ExtendedKalmanFilterFusionNode


def main(args=None):
    # Initialize the Kalman Filter

    mu0 = np.zeros(8)
    Sigma0 = np.eye(8)
    # Noise configurations
    # Balanced
    proc_noise_std = [1.0, 1.0, 0.5, 0.3, 0.3, 0.5, 0.5, 0.5]
    obs_noise_std = [1.0, 1.0, 0.5, 0.3, 0.3, 0.5, 0.5]
    # High observation noise
    # proc_noise_std = [1.0, 1.0, 0.5, 0.3, 0.3, 0.5, 0.5, 0.5]
    # obs_noise_std = [2.0, 2.0, 1.0, 0.6, 0.6, 1.0, 1.0]
    # High process noise
    # proc_noise_std = [2.0, 2.0, 1.0, 0.6, 0.6, 1.0, 1.0, 1.0]
    # obs_noise_std = [1.0, 1.0, 0.5, 0.3, 0.3, 0.5, 0.5]

    ekf = ExtendedKalmanFilter(mu0, Sigma0,
                               acceleration_motion_model_linearized_2,
                               odometry_imu_observation_model_with_acceleration_motion_model_linearized_2,
                               proc_noise_std=proc_noise_std,
                               obs_noise_std=obs_noise_std)
    # ===================================================================


    rclpy.init(args=args)
    kalman_filter_node = ExtendedKalmanFilterFusionNode(ekf)
    rclpy.spin(kalman_filter_node)
    kalman_filter_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
