import sys
import io
import traceback
from PyQt5 import QtWidgets, QtCore, QtGui
import pandas as pd
import numpy as np

class PythonConsoleDialog(QtWidgets.QDialog):
    def __init__(self, data_service, parent=None):
        super().__init__(parent)
        self.data_service = data_service
        self.setWindowTitle("Python Script Console")
        self.resize(1000, 750)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowMaximizeButtonHint)
        self._setup_ui()
        self._apply_theme()

    def _apply_theme(self):
        """Apply a sleek, modern dark theme similar to VS Code."""
        self.setStyleSheet("""
            QDialog {
                background-color: #1E1E1E;
            }
            QLabel {
                color: #CCCCCC;
                font-weight: 600;
                font-size: 12px;
            }
            QComboBox {
                background-color: #3C3C3C;
                color: #FFFFFF;
                border: 1px solid #555555;
                padding: 4px 8px;
                border-radius: 4px;
            }
            QComboBox:drop-down {
                border: none;
            }
            QPushButton {
                background-color: #0E639C;
                color: #FFFFFF;
                border: none;
                padding: 6px 16px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #1177BB;
            }
            QPushButton:pressed {
                background-color: #094771;
            }
            QSplitter::handle {
                background-color: #333333;
                margin: 2px 0px;
            }
        """)

    def _setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)

        # Toolbar / Templates
        toolbar_layout = QtWidgets.QHBoxLayout()
        toolbar_layout.addWidget(QtWidgets.QLabel("Snippet Templates:"))
        
        self.combo_templates = QtWidgets.QComboBox()
        self.combo_templates.setMinimumWidth(250)
        self.combo_templates.addItems([
            "Empty Script",
            "Custom Curve Calculation",
            "Print Well Summary",
            "Basic Facies Classification (Example)"
        ])
        self.combo_templates.currentTextChanged.connect(self._load_template)
        toolbar_layout.addWidget(self.combo_templates)
        
        toolbar_layout.addStretch()
        
        self.btn_run = QtWidgets.QPushButton("▶ Run Script (Ctrl+Enter)")
        self.btn_run.setShortcut("Ctrl+Return")
        self.btn_run.setStyleSheet("""
            QPushButton {
                background-color: #238636;
                color: white;
            }
            QPushButton:hover { background-color: #2EA043; }
        """)
        self.btn_run.clicked.connect(self._run_script)
        toolbar_layout.addWidget(self.btn_run)
        
        layout.addLayout(toolbar_layout)

        # Splitter to allow resizing editor vs output
        self.splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)
        layout.addWidget(self.splitter)

        # Code Editor
        editor_widget = QtWidgets.QWidget()
        editor_layout = QtWidgets.QVBoxLayout(editor_widget)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        
        lbl_editor = QtWidgets.QLabel("</> Python Editor")
        lbl_editor.setStyleSheet("color: #4EC9B0; font-size: 13px; font-weight: bold; margin-bottom: 2px;")
        editor_layout.addWidget(lbl_editor)

        self.editor = QtWidgets.QTextEdit()
        self.editor.setFontFamily("Consolas, Courier New, monospace")
        self.editor.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.editor.setTabStopDistance(QtGui.QFontMetricsF(self.editor.font()).horizontalAdvance(' ') * 4)
        self.editor.setStyleSheet("""
            QTextEdit {
                background-color: #1E1E1E; 
                color: #D4D4D4; 
                font-size: 14px;
                border: 1px solid #444444;
                border-radius: 4px;
                padding: 8px;
            }
        """)
        editor_layout.addWidget(self.editor)
        self.splitter.addWidget(editor_widget)

        # Console Output
        output_widget = QtWidgets.QWidget()
        output_layout = QtWidgets.QVBoxLayout(output_widget)
        output_layout.setContentsMargins(0, 0, 0, 0)

        lbl_console = QtWidgets.QLabel(">_ Terminal Output")
        lbl_console.setStyleSheet("color: #CE9178; font-size: 13px; font-weight: bold; margin-top: 5px; margin-bottom: 2px;")
        output_layout.addWidget(lbl_console)

        self.console_output = QtWidgets.QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setFontFamily("Consolas, Courier New, monospace")
        self.console_output.setStyleSheet("""
            QTextEdit {
                background-color: #111111; 
                color: #CCCCCC;
                font-size: 13px;
                border: 1px solid #333333;
                border-radius: 4px;
                padding: 8px;
            }
        """)
        output_layout.addWidget(self.console_output)
        self.splitter.addWidget(output_widget)

        # Set initial splitter sizes (2/3 editor, 1/3 console)
        self.splitter.setSizes([450, 200])

        self._load_template("Empty Script")

    def _load_template(self, text):
        templates = {
            "Empty Script": (
                "# Write your Python script here.\n"
                "# The current well DataFrame is available as 'df'.\n"
                "# The DataService is available as 'data'.\n\n"
                "print('Hello from PetroARX Python Console!')\n"
            ),
            "Custom Curve Calculation": (
                "# Example: Calculate a custom curve (e.g., PHIE)\n"
                "if df is not None:\n"
                "    if 'PHIT' in df.columns and 'VSH' in df.columns:\n"
                "        df['PHIE_CUSTOM'] = df['PHIT'] * (1 - df['VSH'])\n"
                "        print('Successfully calculated PHIE_CUSTOM!')\n"
                "        print(df[['PHIT', 'VSH', 'PHIE_CUSTOM']].head())\n"
                "    else:\n"
                "        print('Error: PHIT and VSH columns not found.')\n"
                "else:\n"
                "    print('No active well data.')\n"
            ),
            "Print Well Summary": (
                "# Print summary statistics for the active well\n"
                "if df is not None:\n"
                "    print('Well Data Summary:')\n"
                "    print('-' * 40)\n"
                "    print(df.describe())\n"
                "else:\n"
                "    print('No active well data.')\n"
            ),
            "Basic Facies Classification (Example)": (
                "# Example structure for ML Facies Classification\n"
                "print('Loading Scikit-Learn...')\n"
                "# from sklearn.ensemble import RandomForestClassifier\n"
                "print('Ready to classify based on GR, RHOZ, NPHI.')\n"
            )
        }
        self.editor.setPlainText(templates.get(text, ""))

    def _run_script(self):
        script = self.editor.toPlainText()
        
        # Setup environment variables for script execution
        well = self.data_service._get_current_well()
        df = getattr(well, "data", None) if well else None
        
        env = {
            "df": df,
            "data": self.data_service,
            "pd": pd,
            "np": np
        }

        # Redirect stdout and stderr to capture print statements
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = sys.stdout = sys.stderr = io.StringIO()

        self.console_output.clear()
        
        import ast
        try:
            # Parse the script into an AST
            tree = ast.parse(script, filename="<script>", mode="exec")
            
            if tree.body and isinstance(tree.body[-1], ast.Expr):
                # The last statement is an expression
                last_expr = tree.body.pop()
                
                # Execute everything except the last expression
                exec(compile(tree, filename="<script>", mode="exec"), env)
                
                # Evaluate the last expression and print it if not None
                expr_code = compile(ast.Expression(last_expr.value), filename="<script>", mode="eval")
                result = eval(expr_code, env)
                if result is not None:
                    print(result)
            else:
                # Normal execution
                exec(compile(tree, filename="<script>", mode="exec"), env)
            
            output = redirected_output.getvalue()
            if not output:
                output = "Script executed successfully. (No output printed)"
                
            self.console_output.setText(output)
            self.console_output.setStyleSheet("""
                QTextEdit { background-color: #111111; color: #4EC9B0; font-size: 13px; border: 1px solid #333333; }
            """)
            
            # If the dataframe was updated, save it back
            if df is not None and well:
                setattr(well, "data", df)
                
        except Exception as e:
            output = redirected_output.getvalue()
            error_trace = traceback.format_exc()
            self.console_output.setText(output + "\n--- ERROR ---\n" + error_trace)
            self.console_output.setStyleSheet("""
                QTextEdit { background-color: #2D0A0A; color: #F14C4C; font-size: 13px; border: 1px solid #F14C4C; }
            """)
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
