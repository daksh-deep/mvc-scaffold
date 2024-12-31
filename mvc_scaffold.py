import os
import subprocess
import sys

def install_package(package):
    """Install a Python package using pip without showing the installation process."""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def create_file(path, content=""):
    """Helper function to create a file with optional content."""
    try:
        with open(path, 'w') as file:
            file.write(content)
        print(f"Created file: {path}")
    except Exception as e:
        print(f"Error creating file {path}: {e}")

def generate_database_config(language="js"):
    """Generate MongoDB connection config code for JS or TS."""
    if language == "ts":
        return '''import mongoose from 'mongoose';
import dotenv from 'dotenv';
dotenv.config();

const connectToDatabase = async (): Promise<void> => {
    try {
        if (!process.env.DATABASE_URL) {
            console.error("DATABASE_URL is not defined in the environment variables.");
            process.exit(1);
        }
        console.log("Attempting to connect to the database...");
        await mongoose.connect(process.env.DATABASE_URL);
        console.log("Database connected successfully.");
    } catch (error) {
        console.error("Database connection failed:", (error as Error).message);
        console.error("Error details:", error);
    }
};

export { connectToDatabase };'''
    else:
        return '''const mongoose = require('mongoose');
const dotenv = require('dotenv');
dotenv.config();

const connectToDatabase = async () => {
    try {
        if (!process.env.DATABASE_URL) {
            console.error("DATABASE_URL is not defined in the environment variables.");
            process.exit(1);
        }
        console.log("Attempting to connect to the database...");
        await mongoose.connect(process.env.DATABASE_URL);
        console.log("Database connected successfully.");
    } catch (error) {
        console.error("Database connection failed:", error.message);
        console.error("Error details:", error);
    }
};

module.exports = { connectToDatabase };'''

def run_command(command, success_message, error_message):
    """Run a shell command, hiding output unless there's an error."""
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(success_message)
        else:
            print(f"{error_message}\nError details: {result.stderr.decode().strip()}")
    except Exception as e:
        print(f"{error_message}\nException details: {e}")

def main():
    try:
        import inquirer
    except ImportError:
        print("Installing dependencies silently...")
        install_package("inquirer")
        import inquirer

    # Step 1: Prompt for language and port
    questions = [
        inquirer.List('language',
                      message="Do you want to work with JavaScript or TypeScript?",
                      choices=['JavaScript', 'TypeScript'],
                      default='JavaScript'),
        inquirer.Text('port',
                      message="Enter the port number to use for the application",
                      validate=lambda _, x: x.isdigit() and 0 < int(x) <= 65535)
    ]
    answers = inquirer.prompt(questions)
    language = 'ts' if answers['language'] == 'TypeScript' else 'js'
    port = answers['port']

    # Define folder structure
    folders = ['controllers', 'views', 'routes', 'models', 'config', 'logs']
    for folder in folders:
        try:
            os.makedirs(folder, exist_ok=True)
            print(f"Created folder: {folder}")
        except Exception as e:
            print(f"Error creating folder {folder}: {e}")

    # Create files
    create_file(f'app.{language}', f"// Developer: Daksh Deep\n// LinkedIn: https://www.linkedin.com/in/daksh-deep-791a1a298/\n// GitHub: https://github.com/daksh-deep\n// Happy coding!\n \nconsole.log('hello world');")
    create_file('.env', f"PORT={port}\nDATABASE_URL=<your_mongo_connection>")
    create_file(f'config/database_config.{language}', generate_database_config(language))
    create_file('README.md', "# Project Documentation\n\n## How to Use\n\n1. Run `npm start` to begin the server.\n2. Make sure the `.env` file contains the correct `PORT` and `DATABASE_URL`.\n")
    create_file('logs/app.log')

    # Step 2: Initialize npm and install dependencies
    print("Initializing npm...")
    run_command("npm init -y", "npm initialized successfully.", "npm init failed. Please ensure npm is installed and try again.")

    print("Installing Express, mongoose, and dotenv...")
    run_command("npm install express mongoose dotenv", "Dependencies installed successfully.", "Failed to install dependencies. Please check your npm setup.")

    print(f"MVC structure created successfully with {answers['language']}.")

if __name__ == '__main__':
    main()
