#!/usr/bin/env python3
"""
Setup script for Composio integrations.

Usage:
  python composio_setup.py --check-auth
  python composio_setup.py --install-deps
"""

import os
import sys
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if composio-core is installed."""
    try:
        import composio
        print(f"✓ composio-core {composio.__version__} installed")
        return True
    except ImportError:
        print("✗ composio-core not installed")
        return False


def install_dependencies():
    """Install composio-core."""
    print("Installing composio-core...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "composio-core>=0.7.0", "-q"],
        capture_output=True
    )
    if result.returncode == 0:
        print("✓ composio-core installed successfully")
        return True
    else:
        print(f"✗ Installation failed: {result.stderr.decode()}")
        return False


def check_api_key():
    """Check if COMPOSIO_API_KEY is set."""
    api_key = os.getenv("COMPOSIO_API_KEY")
    if api_key:
        masked = api_key[:8] + "..." + api_key[-4:]
        print(f"✓ COMPOSIO_API_KEY found: {masked}")
        return True
    else:
        print("✗ COMPOSIO_API_KEY not set in ~/.hermes/.env")
        return False


def check_auth():
    """Check authentication status for all integrations."""
    if not check_dependencies():
        print("\n  Install with: python composio_setup.py --install-deps")
        return False
    
    if not check_api_key():
        print("\n  1. Go to https://composio.dev")
        print("  2. Sign up (free tier)")
        print("  3. Copy your API key")
        print("  4. Add to ~/.hermes/.env:")
        print("     COMPOSIO_API_KEY=your_key_here")
        return False
    
    print("\n✓ Setup complete!")
    print("\n  Integrations will request OAuth on first use:")
    print("  - Linear")
    print("  - Notion")
    print("  - Gmail")
    print("\n  Approve in browser when prompted. Credentials cached locally.")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python composio_setup.py --check-auth | --install-deps")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "--check-auth":
        success = check_auth()
        sys.exit(0 if success else 1)
    
    elif command == "--install-deps":
        success = install_dependencies()
        sys.exit(0 if success else 1)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
