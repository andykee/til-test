import os
import shuitl


GITHUB_WORKSPACE = os.environ['GITHUB_WORKSPACE']


shutil.copy(os.path.join(GITHUB_WORKSPACE, '.github/theme/_config.yml'), GITHUB_WORKSPACE)
