"""Tests related to pre- and post-hook scripts."""


import os


def test_cli_scripts_removed_in_hook(cookies):
    """Test the removal of cli scripts in post script."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "no"
    })
    assert result.exit_code == 0
    assert not os.path.exists(result.project.join('test_project').join('cli.py'))
    assert not os.path.exists(result.project.join('bin').join('test_project'))


def test_cli_scripts_kept_when_requested(cookies):
    """Test cli scripts are kept when requested."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "yes"
    })
    assert result.exit_code == 0
    assert os.path.exists(result.project.join('test_project').join('cli.py'))
    assert os.path.exists(result.project.join('bin').join('test_project'))


def test_dockerfile_removed_in_hook(cookies):
    """Test the removal of Dockerfiles in the post script."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "no",
        "dockerize_cli_script": "no",
    })
    assert result.exit_code == 0
    assert not os.path.exists(result.project.join('Dockerfile'))

    readme = result.project.join("README.md").read()
    assert "Docker" not in readme


def test_dockerfile_kept_when_requested(cookies):
    """Test dockerfiles are kept when requested."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "yes",
        "dockerize_cli_script": "yes",
    })
    assert result.exit_code == 0
    assert os.path.exists(result.project.join('Dockerfile'))

    readme = result.project.join("README.md").read()
    assert "Docker" in readme


def test_makefile_removed_in_hook(cookies):
    """Test the removal of Makefiles in the post script."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "no",
        "dockerize_cli_script": "no",
        "optional_makefile": "no",
    })
    assert result.exit_code == 0
    assert not os.path.exists(result.project.join('Makefile'))


def test_makefile_kept_when_requested(cookies):
    """Test Makefiles are kept when requested."""
    result = cookies.bake(extra_context={
        "package_name": "test_project",
        "package_slug": "test-project",
        "package_title": "Test Project",
        "package_short_description": "Short description.",
        "add_cli_script": "yes",
        "dockerize_cli_script": "yes",
        "optional_makefile": "yes",
    })
    assert result.exit_code == 0
    assert os.path.exists(result.project.join('Makefile'))
