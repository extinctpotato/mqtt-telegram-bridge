import setuptools

setuptools.setup(
        name="tmbridge",
        version="0.1",
        author="Adam Olech",
        author_email="nddr89@gmail.com",
        description="MQTT to Telegram bridge",
        url="https://git.hopeburn.eu",
        packages=["tmbridge"],
        python_requires='>=3.6',
        entry_points={
            "console_scripts": ["tmbridge = tmbridge.tmbridge:main"]
            },
        install_requires=["paho-mqtt", "python-telegram-bot"],
        )
