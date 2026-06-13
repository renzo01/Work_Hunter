#!/usr/bin/env python3
"""
HTML to PDF Converter for CV Templates
Converts template.html with data from data_cv.json to PDF format
"""

import json
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS

def load_json_data(json_path):
    """Load data from JSON file."""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: JSON file not found at {json_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {json_path}: {e}")
        sys.exit(1)

def render_html(template_path, json_path, output_name=None):
    """Render HTML from template and JSON data."""
    data = load_json_data(json_path)
    
    # Setup Jinja2 environment
    template_dir = Path(template_path).parent
    env = Environment(loader=FileSystemLoader(str(template_dir)))
    
    # Load and render template
    template = env.get_template(Path(template_path).name)
    html_content = template.render(**data)
    
    return html_content, data

def html_to_pdf(template_path, json_path, output_path=None):
    """Convert HTML template to PDF."""
    # Render HTML
    html_content, data = render_html(template_path, json_path)
    
    # Determine output filename
    if output_path is None:
        name = data.get('personal_info', {}).get('name', 'output').replace(' ', '_')
        job_company = data.get('Job_Company', '').replace(' ', '_')
        
        # Create filename with name and job_company
        if job_company and job_company != 'Not_specified':
            filename = f"{name}_{job_company}.pdf"
        else:
            filename = f"{name}.pdf"
        
        output_dir = Path(template_path).parent.parent / "tailorCVs"
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / filename
    else:
        output_path = Path(output_path)
    
    # Create PDF
    try:
        HTML(string=html_content).write_pdf(output_path)
        print(f"✓ PDF generated successfully: {output_path}")
        return str(output_path)
    except Exception as e:
        print(f"Error: Failed to generate PDF: {e}")
        sys.exit(1)

def main():
    """Main function to handle command-line usage."""
    script_dir = Path(__file__).parent
    template_path = script_dir / "template.html"
    json_path = script_dir / "data_cv.json"
    
    # Check if custom paths are provided via command line
    if len(sys.argv) > 1:
        json_path = Path(sys.argv[1])
    if len(sys.argv) > 2:
        output_path = Path(sys.argv[2])
    else:
        output_path = None
    
    # Verify template exists
    if not template_path.exists():
        print(f"Error: Template file not found at {template_path}")
        sys.exit(1)
    
    # Convert HTML to PDF
    html_to_pdf(template_path, json_path, output_path)

if __name__ == "__main__":
    main()
