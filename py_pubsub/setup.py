from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='franhruskar',
    maintainer_email='hruskarf@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                 'talker =py_pubsub.publisher_member_function:main',
                 'listener =py_pubsub.subscriber_member_function:main',
                 'brojcanik = py_pubsub.publisher_broj:main',
                 'kvadriranje = py_pubsub.subscriber_kvadrat:main',
        ],
    },
)
