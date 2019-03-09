from setuptools import setup, find_packages

setup(
    name="home-assistant-frontend",
    version="custom.20190305.1",
    description="The E-Fonenana frontend",
    url="https://gitlab.com/teamdown/smart-home/frontend",
    author="The E-Fonenana Authors",
    author_email="nyandrianinamamy@gmail.com",
    license="Apache License 2.0",
    packages=find_packages(
        include=[
            "hass_frontend",
            "hass_frontend_es5",
            "hass_frontend.*",
            "hass_frontend_es5.*",
        ]
    ),
    install_requires=["user-agents==1.1.0"],
    include_package_data=True,
    zip_safe=False,
)
