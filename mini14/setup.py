from distutils.core import setup, Extension


def main():
    setup(
        name="foreign",
        version="1.0.0",
        description="",
        author="Nikitat0",
        author_email="nikitatzero@yandex.ru",
        ext_modules=[
            Extension("foreign", ["foreign.c"]),
        ],
    )


if __name__ == "__main__":
    main()
