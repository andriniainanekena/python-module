import os
import sys
import site


def is_virtual_env() -> bool:
    return (
        hasattr(sys, "real_prefix")
        or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)
    )


def get_virtual_env_name() -> str:
    virtual_env_path = os.environ.get("VIRTUAL_ENV", "")
    return os.path.basename(virtual_env_path) if virtual_env_path else ""


def get_virtual_env_path() -> str:
    return os.environ.get("VIRTUAL_ENV", "")


def get_site_packages_path() -> str:
    packages = site.getsitepackages()
    return packages[0] if packages else ""


def display_outside_venv() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")
    print()
    print("Then run this program again.")


def display_inside_venv() -> None:
    env_name = get_virtual_env_name()
    env_path = get_virtual_env_path()
    site_packages = get_site_packages_path()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(site_packages)


def main() -> None:
    if is_virtual_env():
        display_inside_venv()
    else:
        display_outside_venv()


if __name__ == "__main__":
    main()
