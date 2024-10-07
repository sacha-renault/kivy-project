# Using This Template

To use this repository as a starting point for your own project:

1. Clone the repository without linking to the original remote:
    ```bash
    git clone --depth=1 https://github.com/sacha-renault/kivy-project your-new-project-name
    cd your-new-project-name
    ```

2. Remove the existing Git history:
    ```bash
    rm -rf .git
    ```

3. Initialize a new Git repository:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

4. Link to your own remote repository (replace `your-repo-url` with your new repository URL):
    ```bash
    git remote add origin your-repo-url
    ```

5. Push your changes:
    ```bash
    git push -u origin main
    ```

# Simple Kivy Project

- Add a new component (MVC):
    ```bash
    python3 kivy_app.py --add module_name
    ```

