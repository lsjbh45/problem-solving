import os
import re


class Directory():
    def __init__(self, directory):
        self.path = directory

    def get_solved_file_paths(self):
        file_paths = []
        for root, _, names in os.walk(self.path):
            for name in names:
                if not re.fullmatch(r'^[0-9]*.py$', name):
                    continue
                file_path = os.path.join(root, name)
                file_paths.append(file_path)
        return file_paths

    def get_categories_from_file(self, file_path):
        file = open(file_path, 'r', encoding='utf8')
        data = file.read()
        file.close()

        categories = re.findall(r'# Category: (.*)\n', data)
        return categories

    def get_category_data(self):
        category_data = {}
        file_paths = self.get_solved_file_paths()
        for file_path in file_paths:
            categories = self.get_categories_from_file(file_path)
            for category in categories:
                if category not in category_data:
                    category_data[category] = []
                category_data[category].append(file_path)
        return category_data

    def generate_readme(self):
        category_data = self.get_category_data()

        file = open(os.path.join(
            os.getcwd(), self.path, 'README.md'
        ), 'w', encoding='utf8')
        file.writelines('| Category | Problems |\n| --- | --- |\n')
        for c, paths in category_data.items():
            d = [(
                path.replace(self.path + '\\', '').replace('\\', '/'),
                '/' + path.replace('\\', '/')
            ) for path in paths]

            file.writelines(
                f'| {c} | {" ".join(f"[{n}]({p})" for n, p in d)} |\n'
            )
        file.close()


if __name__ == '__main__':
    for directory in ('boj', 'leetcode'):
        instance = Directory(directory)
        instance.generate_readme()
