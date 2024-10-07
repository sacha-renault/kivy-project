import os
import shutil
import argparse
import re

# Define the paths to the templates and target directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
TEMPLATE_DIR = os.path.join(BASE_DIR, "_templates")
COMPONENTS_DIR = os.path.join(SRC_DIR, "components")

CONTROLLERS_DIR = os.path.join(SRC_DIR, "controllers")
MODELS_DIR = os.path.join(SRC_DIR, "models")
VIEWS_DIR = os.path.join(SRC_DIR, "views")

# Convert module name to snake_case for filenames and PascalCase for class names
def to_snake_case(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def to_pascal_case(name):
    return ''.join(word.capitalize() for word in name.split('_'))

def copy_and_rename_template(module_name):
    # Convert module_name to snake_case and PascalCase
    module_snake_case = to_snake_case(module_name)
    module_pascal_case = to_pascal_case(module_snake_case)

    # Define template paths
    template_controller = os.path.join(TEMPLATE_DIR, "controller.py")
    template_model = os.path.join(TEMPLATE_DIR, "model.py")
    template_view_py = os.path.join(TEMPLATE_DIR, "view.py")  # Add template for view Python file
    template_view_kv = os.path.join(TEMPLATE_DIR, "view.kv")

    # Define target paths
    target_controller = os.path.join(CONTROLLERS_DIR, f"{module_snake_case}_controller.py")
    target_model = os.path.join(MODELS_DIR, f"{module_snake_case}_model.py")
    target_view_py = os.path.join(VIEWS_DIR, f"{module_snake_case}_view.py")
    target_view_kv = os.path.join(VIEWS_DIR, f"{module_snake_case}_view.kv")

    # Copy and rename the controller template
    if os.path.exists(template_controller):
        shutil.copy(template_controller, target_controller)
        with open(target_controller, 'r') as file:
            content = file.read()
        # Replace class names and import statements
        content = content \
                         .replace("TemplateController", f"{module_pascal_case}Controller") \
                         .replace("TemplateView", f"{module_pascal_case}View") \
                         .replace("TemplateModel", f"{module_pascal_case}Model") \
                         .replace("from src.models.template_model import",
                                  f"from src.models.{module_snake_case}_model import") \
                         .replace("from src.views.template_view import",
                                  f"from src.views.{module_snake_case}_view import")
        with open(target_controller, 'w') as file:
            file.write(content)
        print(f"Controller template copied to {target_controller}")
    else:
        print("Controller template not found.")

    # Copy and rename the model template
    if os.path.exists(template_model):
        shutil.copy(template_model, target_model)
        with open(target_model, 'r') as file:
            content = file.read()
        content = content.replace("TemplateModel", f"{module_pascal_case}Model")
        with open(target_model, 'w') as file:
            file.write(content)
        print(f"Model template copied to {target_model}")
    else:
        print("Model template not found.")

    # Copy and rename the view Python template
    if os.path.exists(template_view_py):
        shutil.copy(template_view_py, target_view_py)
        with open(target_view_py, 'r') as file:
            content = file.read()
        # Replace class names and related imports
        content = content \
            .replace("src/views/template_view.kv", f"src/views/{module_snake_case}_view.kv") \
            .replace("TemplateView", f"{module_pascal_case}View")
        with open(target_view_py, 'w') as file:
            file.write(content)
        print(f"View Python template copied to {target_view_py}")
    else:
        print("View Python template not found.")

    # Copy and rename the view KV template
    if os.path.exists(template_view_kv):
        shutil.copy(template_view_kv, target_view_kv)
        with open(target_view_kv, 'r') as file:
            content = file.read()
        content = content.replace("TemplateView", f"{module_pascal_case}View")
        with open(target_view_kv, 'w') as file:
            file.write(content)
        print(f"View KV template copied to {target_view_kv}")
    else:
        print("View KV template not found.")

def add_component(component_name):
    # Convert component_name to snake_case and PascalCase
    component_snake_case = to_snake_case(component_name)
    component_pascal_case = to_pascal_case(component_snake_case)

    # Define template paths
    template_component_py = os.path.join(TEMPLATE_DIR, "component.py")
    template_component_kv = os.path.join(TEMPLATE_DIR, "component.kv")

    # Define target paths
    target_component_py = os.path.join(COMPONENTS_DIR, f"{component_snake_case}.py")
    target_component_kv = os.path.join(COMPONENTS_DIR, f"{component_snake_case}.kv")

    # Copy and rename the component Python template
    if os.path.exists(template_component_py):
        shutil.copy(template_component_py, target_component_py)
        with open(target_component_py, 'r') as file:
            content = file.read()
        # Replace class names and related references
        content = content.replace("TemplateComponent", component_pascal_case) \
                         .replace("template_component.kv", f"{component_snake_case}.kv")
        with open(target_component_py, 'w') as file:
            file.write(content)
        print(f"Component Python template copied to {target_component_py}")
    else:
        print("Component Python template not found.")

    # Copy and rename the component KV template
    if os.path.exists(template_component_kv):
        shutil.copy(template_component_kv, target_component_kv)
        with open(target_component_kv, 'r') as file:
            content = file.read()
        content = content.replace("TemplateComponent", component_pascal_case)
        with open(target_component_kv, 'w') as file:
            file.write(content)
        print(f"Component KV template copied to {target_component_kv}")
    else:
        print("Component KV template not found.")


def main():
    parser = argparse.ArgumentParser(description="Manage Kivy modules.")
    parser.add_argument('--add', type=str, help="Add a new module by specifying the module name.")
    parser.add_argument('--add-comp', type=str, help="Add a new component by specifying the component name.")

    args = parser.parse_args()

    if args.add:
        module_name = args.add
        copy_and_rename_template(module_name)

    if args.add_comp:
        component_name = args.add_comp
        add_component(component_name)

if __name__ == "__main__":
    main()
