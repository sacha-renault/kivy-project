import os
import shutil
import argparse
import re

# Define the paths to the templates and target directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
TEMPLATE_DIR = os.path.join(BASE_DIR, "_templates")

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
    template_view = os.path.join(TEMPLATE_DIR, "view.kv")

    # Define target paths
    target_controller = os.path.join(CONTROLLERS_DIR, f"{module_snake_case}_controller.py")
    target_model = os.path.join(MODELS_DIR, f"{module_snake_case}_model.py")
    target_view = os.path.join(VIEWS_DIR, f"{module_snake_case}_view.kv")

    # Copy and rename the controller template
    if os.path.exists(template_controller):
        shutil.copy(template_controller, target_controller)
        with open(target_controller, 'r') as file:
            content = file.read()
        # Replace class names and import statements
        content = content.replace("src/views/template_view.kv", f"src/views/{module_snake_case}_view.kv") \
                         .replace("TemplateController", f"{module_pascal_case}Controller") \
                         .replace("TemplateView", f"{module_pascal_case}View") \
                         .replace("TemplateModel", f"{module_pascal_case}Model") \
                         .replace("from src.models.template_model import",
                                  f"from src.models.{module_snake_case}_model import")
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

    # Copy and rename the view template
    if os.path.exists(template_view):
        shutil.copy(template_view, target_view)
        with open(target_view, 'r') as file:
            content = file.read()
        content = content.replace("TemplateView", f"{module_pascal_case}View")
        with open(target_view, 'w') as file:
            file.write(content)
        print(f"View template copied to {target_view}")
    else:
        print("View template not found.")

def main():
    parser = argparse.ArgumentParser(description="Manage Kivy modules.")
    parser.add_argument('--add', type=str, help="Add a new module by specifying the module name.")

    args = parser.parse_args()

    if args.add:
        module_name = args.add
        copy_and_rename_template(module_name)

if __name__ == "__main__":
    main()
