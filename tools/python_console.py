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
        self.resize(900, 700)
        self._setup_ui()

    def _setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        # Toolbar / Templates
        toolbar_layout = QtWidgets.QHBoxLayout()
        toolbar_layout.addWidget(QtWidgets.QLabel("Load Template:"))
        self.combo_templates = QtWidgets.QComboBox()
        self.combo_templates.addItems([
            "Empty Script",
            "Custom Curve Calculation",
            "Print Well Summary",
            "Basic Facies Classification (Example)"
        ])
        self.combo_templates.currentTextChanged.connect(self._load_template)
        toolbar_layout.addWidget(self.combo_templates)
        toolbar_layout.addStretch()
        
        self.btn_run = QtWidgets.QPushButton("▶ Run Script")
        self.btn_run.setStyleSheet("background-color: #2E7D32; color: white; font-weight: bold; padding: 5px 15px;")
        self.btn_run.clicked.connect(self._run_script)
        toolbar_layout.addWidget(self.btn_run)
        layout.addLayout(toolbar_layout)

        # Code Editor
        self.editor = QtWidgets.QTextEdit()
        self.editor.setFontFamily("Consolas, Courier New, monospace")
        self.editor.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.editor.setStyleSheet("background-color: #1E1E1E; color: #D4D4D4; font-size: 13px;")
        layout.addWidget(self.editor, stretch=2)

        # Console Output
        layout.addWidget(QtWidgets.QLabel("Console Output:"))
        self.console_output = QtWidgets.QTextEdit()
        self.console_output.setReadOnly(True)
        self.console_output.setFontFamily("Consolas, Courier New, monospace")
        self.console_output.setStyleSheet("background-color: #F4F6F9; color: #333333;")
        layout.addWidget(self.console_output, stretch=1)

        self._load_template("Empty Script")

    def _load_template(self, text):
        templates = {
            "Empty Script": "# Write your Python script here.\\n# The current well DataFrame is available as 'df'.\\n# The DataService is available as 'data'.\\n\\nprint('Hello from PetroARX Python Console!')",
            "Custom Curve Calculation": "# Example: Calculate a custom curve (e.g., PHIE)\\nif df is not None:\\n    if 'PHIT' in df.columns and 'VSH' in df.columns:\\n        df['PHIE_CUSTOM'] = df['PHIT'] * (1 - df['VSH'])\\n        print('Successfully calculated PHIE_CUSTOM!')\\n    else:\\n        print('Error: PHIT and VSH columns not found.')\\nelse:\\n    print('No active well data.')",
            "Print Well Summary": "# Print summary statistics for the active well\\nif df is not None:\\n    print(df.describe())\\nelse:\\n    print('No active well data.')",
            "Basic Facies Classification (Example)": "# Example structure for ML Facies Classification\\nprint('Loading Scikit-Learn...')\\n# from sklearn.ensemble import RandomForestClassifier\\nprint('Ready to classify based on GR, RHOZ, NPHI.')"
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

        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()

        self.console_output.clear()
        
        try:
            exec(script, env)
            output = redirected_output.getvalue()
            self.console_output.setText(output)
            self.console_output.setStyleSheet("background-color: #F4F6F9; color: #333333;")
            
            # If the dataframe was updated, mark project as modified
            if df is not None and well:
                setattr(well, "data", df)
                # Note: Ideally trigger a project modify signal here
                
        except Exception as e:
            output = redirected_output.getvalue()
            error_trace = traceback.format_exc()
            self.console_output.setText(output + "\\n--- ERROR ---\\n" + error_trace)
            self.console_output.setStyleSheet("background-color: #FFF1F2; color: #BE123C;")
        finally:
            sys.stdout = old_stdout
