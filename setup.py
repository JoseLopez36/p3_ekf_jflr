from setuptools import find_packages, setup

package_name = 'p3_ekf_jflr'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jose Francisco López Ruiz',
    maintainer_email='josloprui6@alum.us.es',
    description='Practica 3: Extended Kalman Filter',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ekf_estimation_3d = p3_ekf_jflr.ekf_3d_state_estimation:main',
            'ekf_estimation_7d = p3_ekf_jflr.ekf_7d_state_estimation:main',
            'ekf_estimation_8d = p3_ekf_jflr.ekf_8d_state_estimation:main',
        ],
    },
)
