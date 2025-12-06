from setuptools import find_packages, setup

package_name = "diff_drive"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="user1",
    maintainer_email="ae23d203@smail.iitm.ac.in",
    description="TODO: Package description",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "drive = diff_drive.drive:main",
            "drivelog = diff_drive.drive_log:main",
        ],
    },
)
