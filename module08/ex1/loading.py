import sys
import importlib
from importlib.metadata import version, PackageNotFoundError


REQUIRED_PACKAGES = ["pandas", "numpy", "matplotlib"]


def check_dependency(package: str) -> tuple[bool, str]:
    try:
        pkg_version = version(package)
        return True, pkg_version
    except PackageNotFoundError:
        return False, ""


def display_dependencies_status() -> dict[str, bool]:
    print("Checking dependencies:")
    availability: dict[str, bool] = {}

    for package in REQUIRED_PACKAGES:
        available, pkg_version = check_dependency(package)
        availability[package] = available
        if available:
            label = _get_package_label(package)
            print(f"[OK] {package} ({pkg_version}) - {label}")
        else:
            print(f"[MISSING] {package} - Not installed")

    return availability


def _get_package_label(package: str) -> str:
    labels = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    return labels.get(package, "Ready")


def display_missing_instructions(missing: list[str]) -> None:
    print()
    print("Some dependencies are missing.")
    print(f"Missing: {', '.join(missing)}")
    print()
    print("Install them with:")
    print()
    print("  Using pip:")
    print("    pip install -r requirements.txt")
    print()
    print("  Using Poetry:")
    print("    poetry install")
    print()
    print("Then run this program again.")


def compare_pip_vs_poetry() -> None:
    print()
    print("Dependency management comparison:")
    print()
    print("  pip (requirements.txt):")
    print("    - Simple list of packages with versions")
    print("    - No lock file by default (use pip freeze)")
    print("    - Install: pip install -r requirements.txt")
    print()
    print("  Poetry (pyproject.toml):")
    print("    - Declarative dependency specification")
    print("    - Automatic lock file (poetry.lock)")
    print("    - Manages virtual env automatically")
    print("    - Install: poetry install")


def run_matrix_analysis() -> None:
    numpy = importlib.import_module("numpy")
    pandas = importlib.import_module("pandas")
    matplotlib_pyplot = importlib.import_module("matplotlib.pyplot")

    print()
    print("Analyzing Matrix data...")

    data_size = 1000
    print(f"Processing {data_size} data points...")

    rng = numpy.random.default_rng(seed=42)
    timestamps = numpy.arange(data_size)
    signal = numpy.sin(timestamps * 0.1) + rng.normal(0, 0.2, data_size)
    noise = rng.uniform(-0.5, 0.5, data_size)
    matrix_code = signal + noise

    df = pandas.DataFrame({
        "timestamp": timestamps,
        "signal": signal,
        "noise": noise,
        "matrix_code": matrix_code,
    })

    stats = df["matrix_code"].describe()
    print(f"  Mean: {stats['mean']:.4f}")
    print(f"  Std:  {stats['std']:.4f}")
    print(f"  Min:  {stats['min']:.4f}")
    print(f"  Max:  {stats['max']:.4f}")

    print("Generating visualization...")

    fig, axes = matplotlib_pyplot.subplots(2, 1, figsize=(10, 6))
    fig.suptitle("Matrix Data Analysis", fontsize=14)

    axes[0].plot(df["timestamp"], df["signal"], label="Signal", alpha=0.8)
    axes[0].plot(
        df["timestamp"], df["matrix_code"], label="Matrix Code", alpha=0.5
    )
    axes[0].set_title("Matrix Signal")
    axes[0].set_xlabel("Timestamp")
    axes[0].set_ylabel("Value")
    axes[0].legend()

    axes[1].hist(df["matrix_code"], bins=50, color="green", alpha=0.7)
    axes[1].set_title("Distribution of Matrix Code")
    axes[1].set_xlabel("Value")
    axes[1].set_ylabel("Frequency")

    matplotlib_pyplot.tight_layout()
    output_path = "matrix_analysis.png"
    matplotlib_pyplot.savefig(output_path)
    matplotlib_pyplot.close()

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_path}")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()

    availability = display_dependencies_status()
    missing = [pkg for pkg, ok in availability.items() if not ok]

    if missing:
        display_missing_instructions(missing)
        compare_pip_vs_poetry()
        sys.exit(1)

    compare_pip_vs_poetry()
    run_matrix_analysis()


if __name__ == "__main__":
    main()
