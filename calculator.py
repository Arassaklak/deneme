"""Simple calculator script with a GUI."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


class CalculatorApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Simple Calculator")
        self.resizable(False, False)

        self.first_var = tk.StringVar()
        self.second_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Result: ")

        self._build_ui()

    def _build_ui(self) -> None:
        input_frame = tk.Frame(self, padx=12, pady=12)
        input_frame.grid(row=0, column=0)

        tk.Label(input_frame, text="First number").grid(row=0, column=0, sticky="w")
        tk.Entry(input_frame, textvariable=self.first_var, width=20).grid(
            row=0, column=1, pady=4
        )

        tk.Label(input_frame, text="Second number").grid(row=1, column=0, sticky="w")
        tk.Entry(input_frame, textvariable=self.second_var, width=20).grid(
            row=1, column=1, pady=4
        )

        button_frame = tk.Frame(self, padx=12, pady=4)
        button_frame.grid(row=1, column=0)

        tk.Button(button_frame, text="+", width=5, command=self._add).grid(
            row=0, column=0, padx=4
        )
        tk.Button(button_frame, text="-", width=5, command=self._subtract).grid(
            row=0, column=1, padx=4
        )
        tk.Button(button_frame, text="*", width=5, command=self._multiply).grid(
            row=0, column=2, padx=4
        )
        tk.Button(button_frame, text="/", width=5, command=self._divide).grid(
            row=0, column=3, padx=4
        )

        tk.Label(self, textvariable=self.result_var, padx=12, pady=8).grid(
            row=2, column=0, sticky="w"
        )

    def _parse_inputs(self) -> tuple[float, float]:
        try:
            first = float(self.first_var.get())
            second = float(self.second_var.get())
        except ValueError as exc:
            raise ValueError("Please enter valid numbers.") from exc
        return first, second

    def _update_result(self, value: float) -> None:
        self.result_var.set(f"Result: {value}")

    def _handle_operation(self, operation: str) -> None:
        try:
            first, second = self._parse_inputs()
            if operation == "+":
                result = add(first, second)
            elif operation == "-":
                result = subtract(first, second)
            elif operation == "*":
                result = multiply(first, second)
            elif operation == "/":
                result = divide(first, second)
            else:
                raise ValueError("Unsupported operation.")
            self._update_result(result)
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))

    def _add(self) -> None:
        self._handle_operation("+")

    def _subtract(self) -> None:
        self._handle_operation("-")

    def _multiply(self) -> None:
        self._handle_operation("*")

    def _divide(self) -> None:
        self._handle_operation("/")


def main() -> None:
    app = CalculatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
