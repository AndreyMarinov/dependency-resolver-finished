'''Dependency resolver task by Misho'''

import json

FILE_NAME = "package.json"

packages_to_be_installed = []

def read_json_file(file_name):
    """Function that reads from json file"""
    with open(file_name) as read_file:
        return json.load(read_file)


def get_current_requirement(package_name) -> dict:
    """Function that is getting the needed required packages

    :return: package_name: if json_content is true , returns the required packages
    """
    json_content = read_json_file(FILE_NAME)
    for element in range(len(json_content['packages'])):
        if json_content['packages'][element]['name'] == package_name:
            return json_content['packages'][element]['requires']

def dependency_resolver(package_to_install) -> list:
    """Function that is returning packages that needs to be installed

    :param: package_to_install: dict with the packages for the install
    :return: package_to_install: list with the needed packages to install
    """
    current_required_packages = get_current_requirement(package_to_install)
    get_required_packages(current_required_packages)
    packages_to_be_installed.append(package_to_install)
    return packages_to_be_installed

def get_required_packages(packages_list):
    """Function that is getting the required packages and appends them to new list

    :param: packages_list:
    :return: packages_to_be_installed: list with the packages to be installed as require
    """
    for package in packages_list:
        all_required = get_current_requirement(package)
        get_required_packages(all_required)
        if package not in packages_to_be_installed:
            packages_to_be_installed.append(package)
        else:
            break
    return packages_to_be_installed
