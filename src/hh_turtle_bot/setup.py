from setuptools import find_packages, setup

package_name = 'hh_turtle_bot'

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
    maintainer='hrishikesh',
    maintainer_email='hrishikesh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "turtlesim_controller = hh_turtle_bot.turtle_controller:main",
            "turtle_spawner = hh_turtle_bot.turtle_spawner:main"
        ],
    },
)
