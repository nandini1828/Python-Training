"""
Documentation Inspector

Tools for accessing and displaying Python object documentation.
"""

from typing import Dict, Any, Optional
import inspect
import pydoc


class DocInspector:
    """Tools for inspecting and displaying documentation."""

    @staticmethod
    def get_docstring(obj: Any) -> Optional[str]:
        """
        Get the docstring of any Python object.
        
        Args:
            obj: Object to get docstring from.
            
        Returns:
            Optional[str]: The docstring or None.
        """
        return inspect.getdoc(obj)

    @staticmethod
    def get_help_text(obj: Any) -> str:
        """
        Get comprehensive help text for an object.
        
        Args:
            obj: Object to get help for.
            
        Returns:
            str: Help text.
        """
        return pydoc.render_doc(obj, "Help for %s")

    @staticmethod
    def inspect_documentation() -> Dict[str, str]:
        """
        Demonstrate getting documentation from various objects.
        
        Returns:
            Dict[str, str]: Documentation examples.
        """
        class ExampleClass:
            """Example class for documentation."""
            
            def method(self) -> None:
                """Example method."""
                pass
        
        def example_function(x: int) -> int:
            """Example function that doubles input."""
            return x * 2
        
        return {
            "list_doc": inspect.getdoc(list),
            "dict_doc": inspect.getdoc(dict),
            "class_doc": inspect.getdoc(ExampleClass),
            "method_doc": inspect.getdoc(ExampleClass.method),
            "function_doc": inspect.getdoc(example_function),
        }

    @staticmethod
    def get_signature_info(obj: Any) -> Dict[str, Any]:
        """
        Get signature information for callables.
        
        Args:
            obj: Callable object.
            
        Returns:
            Dict[str, Any]: Signature information.
        """
        try:
            sig = inspect.signature(obj)
            
            return {
                "signature": str(sig),
                "parameters": list(sig.parameters.keys()),
                "return_annotation": str(sig.return_annotation) if sig.return_annotation != inspect.Signature.empty else None,
            }
        except (ValueError, TypeError):
            return {"signature": "Unable to get signature"}

    @staticmethod
    def get_source_code(obj: Any) -> Optional[str]:
        """
        Get source code of an object (if available).
        
        Args:
            obj: Object to get source from.
            
        Returns:
            Optional[str]: Source code or None if unavailable.
        """
        try:
            return inspect.getsource(obj)
        except (OSError, TypeError):
            return None

    @staticmethod
    def get_type_annotations(obj: Any) -> Dict[str, Any]:
        """
        Get type annotations from a function or class.
        
        Args:
            obj: Object to get annotations from.
            
        Returns:
            Dict[str, Any]: Type annotations.
        """
        if hasattr(obj, '__annotations__'):
            return obj.__annotations__
        return {}

    @staticmethod
    def document_builtin_functions() -> Dict[str, str]:
        """
        Get documentation for common built-in functions.
        
        Returns:
            Dict[str, str]: Built-in function documentation.
        """
        return {
            "len_doc": len.__doc__,
            "sum_doc": sum.__doc__,
            "map_doc": map.__doc__,
            "filter_doc": filter.__doc__,
            "zip_doc": zip.__doc__,
        }

    @staticmethod
    def document_methods(obj: Any) -> Dict[str, Optional[str]]:
        """
        Get documentation for object methods.
        
        Args:
            obj: Object to document.
            
        Returns:
            Dict[str, Optional[str]]: Method documentation.
        """
        methods = {
            "append": getattr(obj, "append", None),
            "extend": getattr(obj, "extend", None),
            "insert": getattr(obj, "insert", None),
            "remove": getattr(obj, "remove", None),
            "pop": getattr(obj, "pop", None),
        }
        
        result = {}
        for name, method in methods.items():
            if method:
                result[name] = inspect.getdoc(method)
            else:
                result[name] = None
        
        return result

    @staticmethod
    def get_all_docstrings(module: Any) -> Dict[str, Optional[str]]:
        """
        Get all docstrings from a module's public objects.
        
        Args:
            module: Module to document.
            
        Returns:
            Dict[str, Optional[str]]: Documentation for public objects.
        """
        result = {}
        
        for name in dir(module):
            if not name.startswith('_'):
                obj = getattr(module, name)
                doc = inspect.getdoc(obj)
                if doc:
                    result[name] = doc[:100] + "..." if len(doc) > 100 else doc
        
        return result

    @staticmethod
    def inspect_module_contents(module: Any) -> Dict[str, list]:
        """
        Get categorized contents of a module.
        
        Args:
            module: Module to inspect.
            
        Returns:
            Dict[str, list]: Categorized module contents.
        """
        all_items = dir(module)
        
        classes = []
        functions = []
        variables = []
        
        for name in all_items:
            if name.startswith('_'):
                continue
            
            obj = getattr(module, name)
            
            if inspect.isclass(obj):
                classes.append(name)
            elif inspect.isfunction(obj) or inspect.isbuiltin(obj):
                functions.append(name)
            else:
                variables.append(name)
        
        return {
            "classes": classes,
            "functions": functions,
            "variables": variables,
        }
