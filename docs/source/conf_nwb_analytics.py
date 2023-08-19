"""
Configure and build the nwb project analytics sources
"""
import os


def build_project_analytics(target_dir=None):
    """
    Clone the nwb-project-analytics repo and build the documentation

    :param target_dir: Directory where to clone the repo or None if the repo should be
                       cloned in the same directory as this file.
    :return: Path where the generated rst sources are located
    """
    # Clone the project analytics repo
    target_dir = os.path.join(os.path.dirname(__file__), "nwb-project-analytics")
    if not os.path.exists(target_dir):
        repo_url = "https://github.com/NeurodataWithoutBorders/nwb-project-analytics.git"
        clone_command = f"git clone {repo_url} {target_dir}"
        os.system(clone_command)
    else:
        print(f"{target_dir} already checked out. Use 'make clean' to do a full rebuild.")

    # Build the project analytics docs (assuming all dependencies are installed)
    docs_dir = os.path.join(target_dir, "docs")
    build_command = f"cd {docs_dir}; make html;"
    os.system(build_command)

    # Return the location of the rst sources
    source_dir = os.path.join(docs_dir, "source")
    return source_dir
