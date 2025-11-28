"""Plot monitor displacement components from SEM monitor files.

This script locates monitor files (e.g. `monitor00001.d`) and plots the
three displacement components (u_x, u_y, u_z) for a configurable set of
monitors. The plotting logic is wrapped in a reusable function with type
hints so it can be imported or executed as a script.
"""

from __future__ import annotations
from pathlib import Path

from functions import plot_monitors


if __name__ == "__main__":
    # Resolve default monitors directory relative to this script
    current_file = Path(__file__).resolve()
    current_dir = current_file.parent
    default_monitors = current_dir.joinpath("../speed_tests/MONITOR/")

    # Default parameters (previous script behavior)
    plot_monitors(default_monitors, num_mon=4, t0=0.0, T=10.0)
