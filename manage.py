#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#!/usr/bin/env python
import os
import sys



from django.core.management import execute_from_command_line



if __name__ == "__main__": 

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  

    execute_from_command_line(sys.argv) 
