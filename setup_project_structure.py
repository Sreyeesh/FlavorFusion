import os

# Root project directory
root_dir = os.getcwd()

# Folder structure
folders = {
    "backend": ["backend/recipes", "backend/recipes/migrations"],
    "frontend": ["frontend/src", "frontend/src/components", "frontend/src/styles", "frontend/src/utils", "frontend/public"],
}

# Backend-specific files
backend_files = {
    "backend": ["requirements.txt", ".env", "Dockerfile"],
    "backend/recipes": ["__init__.py"],
}

# Frontend-specific files
frontend_files = {
    "frontend": ["package.json", ".eslintrc.json", "Dockerfile"],
    "frontend/src": ["App.js"],
    "frontend/public": ["index.html"],
}

# Shared files
shared_files = ["docker-compose.yml"]

# Create folders first
for folder, subfolders in folders.items():
    folder_path = os.path.join(root_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created directory: {folder_path}")
    for subfolder in subfolders:
        subfolder_path = os.path.join(root_dir, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)
        print(f"Created subdirectory: {subfolder_path}")

# Create backend files
for folder, files in backend_files.items():
    folder_path = os.path.join(root_dir, folder)
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            if file == "requirements.txt":
                f.write("# Add Python dependencies here")
            elif file == ".env":
                f.write("SECRET_KEY=your-secret-key\nDEBUG=True\n")
            elif file == "Dockerfile":
                f.write("FROM python:3.9-slim\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD ['python', 'manage.py', 'runserver', '0.0.0.0:8000']")
            elif file == "__init__.py":
                f.write("")  # Empty init file
            print(f"Created file: {file_path}")

# Create frontend files
for folder, files in frontend_files.items():
    folder_path = os.path.join(root_dir, folder)
    for file in files:
        file_path = os.path.join(folder_path, file)
        with open(file_path, "w") as f:
            if file == "package.json":
                f.write("{}")  # Empty JSON placeholder
            elif file == ".eslintrc.json":
                f.write('{\n  "extends": "react-app"\n}')
            elif file == "App.js":
                f.write('import React from "react";\n\nfunction App() {\n  return <div>Welcome to FlavorFusion!</div>;\n}\n\nexport default App;')
            elif file == "Dockerfile":
                f.write("FROM node:14\nWORKDIR /app\nCOPY . .\nRUN npm install\nCMD ['npm', 'start']")
            elif file == "index.html":
                f.write("<!DOCTYPE html>\n<html>\n<head><title>FlavorFusion</title></head>\n<body><div id='root'></div></body>\n</html>")
            print(f"Created file: {file_path}")

# Create shared files
for file in shared_files:
    file_path = os.path.join(root_dir, file)
    with open(file_path, "w") as f:
        if file == "docker-compose.yml":
            f.write(
                "version: '3.7'\n"
                "services:\n"
                "  backend:\n"
                "    build: ./backend\n"
                "    ports:\n"
                "      - '8000:8000'\n"
                "    env_file:\n"
                "      - ./backend/.env\n"
                "  frontend:\n"
                "    build: ./frontend\n"
                "    ports:\n"
                "      - '3000:3000'\n"
            )
        print(f"Created file: {file_path}")

print("\nSetup complete!")
