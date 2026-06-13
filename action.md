 # Agent Instructions: Tailor CV Generation

## Objective
Create a Tailor CV according to @Job_description.md with data from @ref/ following these requirements:
- Harvard Formatting          
- ATS Friendly                          
- Headhunter magnet

## Steps to Follow

1. **Read the Job Description**
   - Read ./job_description.md
   - Identify key skills, technologies, and requirements

2. **Update CV Data**
   - Update ./template/data_cv.json according to job_description requirements
   - ONLY use data from ./ref/ directory
   - Remove any information not relevant for the position
   - Tailor content to match job requirements DONT INVENT NOTING, if somthing is not in ref, explain my motivation to learn new tecnologies.

3. **Execute PDF Generation**
   - Run ./template/html2pdf.py
   - This will generate the tailored PDF based on updated data_cv.json

4. **Provide Summary**
   - Report what changes were made
   - Confirm PDF was generated successfully
   - List the output file path 