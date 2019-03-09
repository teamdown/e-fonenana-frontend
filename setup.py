from setuptools import setup, find_packages

setup(
    name="home-assistant-frontend",
    version="20190305.1",
    description="The E-Fonenana frontend",
    url="https://github.com/home-assistant/home-assistant-polymer",
    author="The E-Fonenana Authors",
    author_email="hello@home-assistant.io",
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
