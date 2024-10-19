from pathlib import Path

import frontmatter
from frontmatter import Post
from jinja2 import (
    Environment,
    FileSystemLoader,
    TemplateError,
    TemplateNotFound,
    StrictUndefined,
    Template,
)


class PromptManager:
    _env: Environment = None

    @classmethod
    def _get_env(
        cls, template_dirs: Path = Path(__file__).parent / "templates"
    ) -> Environment:
        if cls._env is None:
            cls._env: Environment = Environment(
                loader=FileSystemLoader(template_dirs),
                undefined=StrictUndefined,
            )

        return cls._env

    @staticmethod
    def get_prompt(template_name: str, **kwargs):
        try:
            env: Environment = PromptManager._get_env()
            template_file: str = f"{template_name}.j2"

            with open(env.loader.get_source(env, template_file)[1]) as file:
                post: Post = frontmatter.load(file)
                template: Template = env.from_string(post.content)
                return template.render(**kwargs)
        except TemplateNotFound:
            raise FileNotFoundError(f"{template_name}.j2 is not found.")
        except TemplateError as e:
            raise ValueError(f"Error while rendering {template_name}: {e}")
