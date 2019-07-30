from jinja2 import Environment, FileSystemLoader


REQUIREMENTS_FILE = '../../../requirements.txt'
OUTPUT_FILE = '../../../conda/meta.yml'
TEMPLATE_PATH = '.'
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(TEMPLATE_PATH),
    trim_blocks=False
)

with open('../../../requirements.txt') as file:
    requirements = [line.strip() for line in file.readlines()]

numpy_version = next(package for package in requirements if 'numpy' in package)

context = {
    'requirements': requirements,
    'numpy_version': numpy_version
}

with open(OUTPUT_FILE, 'w') as out:
    meta = TEMPLATE_ENVIRONMENT.get_template('meta_template.yml').render(context)
    out.write(meta)
