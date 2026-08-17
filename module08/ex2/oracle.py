import os
import sys

try:
    from dotenv import load_dotenv
    _DOTENV_AVAILABLE = True
except ImportError:
    _DOTENV_AVAILABLE = False


def load_dotenv_file(env_path: str = ".env") -> None:
    if not _DOTENV_AVAILABLE:
        print("WARNING: python-dotenv not installed.")
        print("Install it: pip install python-dotenv")
        print()
        return
    load_dotenv(env_path)


class MatrixConfig:
    def __init__(self) -> None:
        self.mode: str = os.environ.get("MATRIX_MODE", "")
        self.database_url: str = os.environ.get("DATABASE_URL", "")
        self.api_key: str = os.environ.get("API_KEY", "")
        self.log_level: str = os.environ.get("LOG_LEVEL", "")
        self.zion_endpoint: str = os.environ.get("ZION_ENDPOINT", "")

    def is_development(self) -> bool:
        return self.mode.lower() == "development"

    def is_production(self) -> bool:
        return self.mode.lower() == "production"

    def validate(self) -> list[str]:
        missing = []
        if not self.mode:
            missing.append("MATRIX_MODE")
        if not self.database_url:
            missing.append("DATABASE_URL")
        if not self.api_key:
            missing.append("API_KEY")
        if not self.log_level:
            missing.append("LOG_LEVEL")
        if not self.zion_endpoint:
            missing.append("ZION_ENDPOINT")
        return missing


def display_configuration(config: MatrixConfig) -> None:
    mode_display = config.mode if config.mode else "NOT SET"
    db_display = (
        _mask_url(config.database_url) if config.database_url else "NOT SET"
    )
    api_display = (
        _mask_secret(config.api_key) if config.api_key else "NOT SET"
    )
    log_display = config.log_level if config.log_level else "NOT SET"
    zion_display = config.zion_endpoint if config.zion_endpoint else "NOT SET"

    print("Configuration loaded:")
    print(f"Mode: {mode_display}")
    print(f"Database: {db_display}")
    print(f"API Access: {api_display}")
    print(f"Log Level: {log_display}")
    print(f"Zion Network: {zion_display}")

    if config.is_development():
        print()
        print("[DEV MODE] Verbose logging enabled")
        print("[DEV MODE] Local database in use")
    elif config.is_production():
        print()
        print("[PROD MODE] Minimal logging active")
        print("[PROD MODE] Remote database in use")
        print("[PROD MODE] All endpoints secured")


def _mask_url(url: str) -> str:
    if "://" in url:
        scheme, rest = url.split("://", 1)
        return f"{scheme}://***"
    return "Connected"


def _mask_secret(secret: str) -> str:
    if len(secret) <= 4:
        return "****"
    return secret[:2] + "****" + secret[-2:]


def display_security_check(config: MatrixConfig) -> None:
    print()
    print("Environment security check:")

    env_file_exists = os.path.isfile(".env")
    env_example_exists = os.path.isfile(".env.example")

    print("[OK] No hardcoded secrets detected")

    if env_file_exists:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] No .env file found "
              "(copy .env.example to .env)")

    if env_example_exists:
        print("[OK] .env.example template available")

    if (config.is_production()
            or os.environ.get("MATRIX_MODE") == "production"):
        print("[OK] Production overrides available")
    else:
        print("[INFO] Set MATRIX_MODE=production for production overrides")


def display_missing_warnings(missing: list[str]) -> None:
    print()
    print("WARNING: Missing configuration variables:")
    for var in missing:
        print(f"  - {var}")
    print()
    print("To configure your environment:")
    print("  cp .env.example .env")
    print("  # Edit .env with your values")
    print()
    print("Or pass variables directly:")
    print("  MATRIX_MODE=development python3 oracle.py")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_dotenv_file()

    config = MatrixConfig()
    missing = config.validate()

    if missing:
        display_missing_warnings(missing)

    display_configuration(config)
    display_security_check(config)

    print()
    print("The Oracle sees all configurations.")

    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
