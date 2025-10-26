# Back: GUI

This folder contains a small Tkinter GUI for the sum / summation calculator implemented in `back.py`.

Run the GUI on Windows (PowerShell):

```powershell
python .\back\gui.py
```

Or from the repository root:

```powershell
python back\gui.py
```

The GUI supports:
- Sum numbers: enter numbers separated by spaces and click "Compute Sum".
- Summation Σ: enter an expression in `i` (e.g. `i**2 + 1`), start and end integers, then click "Compute Σ".

The GUI uses the existing safe evaluation logic from `back/back.py` for summation expressions.
