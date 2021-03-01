from ed_engineer_shopping_list_builder import inputs
from ed_engineer_shopping_list_builder.ship_components import ALL_COMPONENTS

ENGINEER_FILE = '''"""
{engineer_name}
"""
from ed_engineer_shopping_list_builder.engineers.engineer import Engineer
from ed_engineer_shopping_list_builder.ship_components import (
    {imports}
)


# pylint: disable=too-few-public-methods
class {engineer_title}(Engineer):
    """
    {engineer_name}
    """

    name = "{engineer_name}"
    max_component_upgrade = {{
{max_components}
    }}
'''

component_map = {component.name: component for component in ALL_COMPONENTS}
while True:
    engineer_name = inputs.single_prompt("Engineer name")
    engineer_file = engineer_name.lower().replace(" ", "_")
    engineer_title = engineer_name.replace(" ", "")

    component_keys = list(component_map.keys())
    if "" in component_keys:
        component_keys.remove("")
    component_keys.sort()

    components = [
        component_map[component]
        for component in inputs.make_choices("components", component_keys)
    ]
    component_grades = ""
    for component in components:
        max_component_grade = inputs.single_prompt(
            f"Max grade for {component.name}? ",
            lambda _, grade: grade.isnumeric() and int(grade) > 0 and int(grade) < 6,
        )

        component_grades += 8 * " " + f"{component.__name__}: {max_component_grade},\n"

    component_grades.rstrip(",\n")
    component_imports = ",\n    ".join([component.__name__ for component in components])
    engineer_handle = open(engineer_file + ".py", "w")
    engineer_handle.write(
        ENGINEER_FILE.format(
            engineer_name=engineer_name,
            engineer_title=engineer_title,
            imports=component_imports,
            max_components=component_grades,
        )
    )
    engineer_handle.close()
