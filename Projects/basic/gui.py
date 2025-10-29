import tkinter as tk
from tkinter import ttk, messagebox

from back.back import sum_list, sigma


class CalculatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sum / Summation Calculator")
        self.resizable(False, False)

        # Mode selection
        mode_frame = ttk.Frame(self, padding=8)
        mode_frame.grid(row=0, column=0, sticky="ew")

        self.mode = tk.StringVar(value="sum")
        ttk.Radiobutton(mode_frame, text="Sum numbers", variable=self.mode, value="sum", command=self._show_frame).grid(row=0, column=0, sticky="w")
        ttk.Radiobutton(mode_frame, text="Summation Σ", variable=self.mode, value="sigma", command=self._show_frame).grid(row=0, column=1, sticky="w")

        # Container for frames
        container = ttk.Frame(self, padding=8)
        container.grid(row=1, column=0)

        # Sum frame
        self.sum_frame = ttk.Frame(container)
        ttk.Label(self.sum_frame, text="Enter numbers separated by spaces:").grid(row=0, column=0, sticky="w")
        self.nums_entry = ttk.Entry(self.sum_frame, width=40)
        self.nums_entry.grid(row=1, column=0, pady=6)
        ttk.Button(self.sum_frame, text="Compute Sum", command=self.compute_sum).grid(row=2, column=0, sticky="e")

        # Sigma frame
        self.sigma_frame = ttk.Frame(container)
        ttk.Label(self.sigma_frame, text="Expression in i (e.g. i**2 + 1):").grid(row=0, column=0, sticky="w")
        self.expr_entry = ttk.Entry(self.sigma_frame, width=40)
        self.expr_entry.grid(row=1, column=0, pady=6)

        limits = ttk.Frame(self.sigma_frame)
        limits.grid(row=2, column=0, pady=4, sticky="w")
        ttk.Label(limits, text="Start:").grid(row=0, column=0)
        self.start_entry = ttk.Entry(limits, width=8)
        self.start_entry.grid(row=0, column=1, padx=(4, 12))
        ttk.Label(limits, text="End:").grid(row=0, column=2)
        self.end_entry = ttk.Entry(limits, width=8)
        self.end_entry.grid(row=0, column=3, padx=(4, 0))

        ttk.Button(self.sigma_frame, text="Compute Σ", command=self.compute_sigma).grid(row=3, column=0, sticky="e", pady=(6, 0))

        # Result display
        result_frame = ttk.Frame(self, padding=(8, 4))
        result_frame.grid(row=2, column=0, sticky="ew")
        ttk.Label(result_frame, text="Result:").grid(row=0, column=0, sticky="w")
        self.result_var = tk.StringVar(value="")
        self.result_label = ttk.Label(result_frame, textvariable=self.result_var, foreground="blue")
        self.result_label.grid(row=1, column=0, sticky="w")

        # pack initial frame
        self._show_frame()

    def _show_frame(self):
        # hide both
        for child in (self.sum_frame, self.sigma_frame):
            child.grid_forget()

        if self.mode.get() == "sum":
            self.sum_frame.grid(row=0, column=0)
        else:
            self.sigma_frame.grid(row=0, column=0)

    def compute_sum(self):
        s = self.nums_entry.get().strip()
        try:
            nums = [float(x) for x in s.split()] if s else []
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid numbers separated by spaces.")
            return
        try:
            res = sum_list(nums)
        except Exception as e:
            messagebox.showerror("Computation error", str(e))
            return
        self.result_var.set(str(res))

    def compute_sigma(self):
        expr = self.expr_entry.get().strip()
        start_s = self.start_entry.get().strip()
        end_s = self.end_entry.get().strip()
        if not expr:
            messagebox.showerror("Input error", "Expression is required.")
            return
        try:
            start = int(start_s)
            end = int(end_s)
        except ValueError:
            messagebox.showerror("Input error", "Start and End must be integers.")
            return
        try:
            res = sigma(expr, start, end)
        except Exception as e:
            messagebox.showerror("Computation error", str(e))
            return
        self.result_var.set(str(res))


def main():
    app = CalculatorGUI()
    app.mainloop()


if __name__ == "__main__":
    main()
