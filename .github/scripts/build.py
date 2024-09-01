import os
import shutil


GITHUB_WORKSPACE = os.environ['GITHUB_WORKSPACE']


shutil.copy(os.path.join(GITHUB_WORKSPACE, '.github/theme/_config.yml'), GITHUB_WORKSPACE)
shutil.copy(os.path.join(GITHUB_WORKSPACE, '.github/theme/index.md'), GITHUB_WORKSPACE)
