from st2actions.runners.pythonrunner import Action
import os
import jinja2

class ParseSearchKBAction(Action):
    TEMPLATE = """{% for article in articles %}
                 * {{ article['title'] }} :: {{ article['url'] }}
               {% endfor %}
               """

    def run(self, articles):
        template = jinja2.Template(self.trim(ParseSearchKBAction.TEMPLATE))
        return template.render(articles=articles)

    @staticmethod
    def trim(docstring):
        """From PEP-0257 : https://www.python.org/dev/peps/pep-0257/ """
        if not docstring:
            return ''
        # Convert tabs to spaces (following the normal Python rules)
        # and split into a list of lines:
        lines = docstring.expandtabs().splitlines()
        # Determine minimum indentation (first line doesn't count):
        indent = sys.maxint
        for line in lines[1:]:
            stripped = line.lstrip()
            if stripped:
                indent = min(indent, len(line) - len(stripped))
        # Remove indentation (first line is special):
        trimmed = [lines[0].strip()]
        if indent < sys.maxint:
            for line in lines[1:]:
                trimmed.append(line[indent:].rstrip())
        # Strip off trailing and leading blank lines:
        while trimmed and not trimmed[-1]:
            trimmed.pop()
        while trimmed and not trimmed[0]:
            trimmed.pop(0)
        # Return a single string:
        return '\n'.join(trimmed)
