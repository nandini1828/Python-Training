# python_datatypes_mastery

Educational project demonstrating Python data types, introspection, dunder
methods, collections, classes, and testing with pytest.

Folder Structure

```
python_datatypes_mastery/
├── main.py
├── primitives/
├── collections/
├── classes/
├── inspectors/
├── exercises/
└── tests/
```

Concepts Covered

- Data types: primitives, lists, dicts, sets, tuples
- Introspection: `dir`, `type`, `isinstance`, `id`, `inspect`
- Type casting and safe conversions
- Dunder methods (`__add__`, `__str__`, `__repr__`, etc.)
- Collections APIs and common patterns
- Classes, objects, composition, `__dict__`, `__new__`
- Recursive object deconstruction to JSON-serializable structures
- Simple exercises for practice
- Tests written with `pytest`

Running

Run the demo script:

```bash
python main.py
```

Run tests:

```bash
pytest
```

Using the VS Code Output Channel Extension

An optional lightweight extension is included that runs the demo and streams
its stdout/stderr into a dedicated Output Channel named "Python Datatypes Demo".

To use it:

1. Open this workspace in VS Code.
2. Open the folder `.vscode/extensions/python-datatypes-output` in the Explorer.
3. Press `F5` to launch an Extension Development Host (a new VS Code window).
4. In the new window, open the Command Palette and run: `Python Datatypes: Run Demo to Output Channel`.

To run any open Python file into the Output Channel:

1. Open a Python file in the editor.
2. Right-click in the editor and choose "Run Active Python File to Output Channel" (or use the Command Palette and search for that command).
3. The Output panel will show the channel "Python Datatypes Demo" with the script's stdout/stderr.

Shortcut

You can press `Ctrl+Alt+R` (when the editor language is Python) to run the active file into the Output Channel.

This will execute `python3 -m python_datatypes_mastery.main` from the workspace root and display the live output in the Output panel under the channel "Python Datatypes Demo".

If you prefer not to run the extension, use the Terminal approach shown earlier or pipe output to a file:

```bash
python3 -m python_datatypes_mastery.main | tee demo_output.txt
code demo_output.txt
```
