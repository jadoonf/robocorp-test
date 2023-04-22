
Steps to do a new release
---------------------------

- Open a shell at the proper place (something as `X:/robocorpws/draft-python-framework/robolog`)

- Create release branch (`git branch -D release-robocorp-robolog&git checkout -b release-robocorp-robolog`)

- When leaving pre-alpha: Update classifier in setup.py (currently in pre-alpha) and notes regarding being alpha in README.md.

- Update version (`python -m dev set-version 0.0.10`).

- Update README.md to add notes on features/fixes (on `robocorp-robolog`).

- Update changelog.md to add notes on features/fixes and set release date.

- Push contents, and check if tests passed in https://github.com/robocorp/robotframework-lsp/actions.
  - `mu acp robocorp-robolog release 0.0.10`

- Rebase with master (`git checkout master&git rebase release-robocorp-robolog`).

- Create a tag (`git tag robocorp-robolog-0.0.10`) and push it.

- After published in PyPi, head over to the core module and run: `poetry lock` (then a new core release may be done).

- Send release msg. i.e.:

Hi @channel,

I'm happy to announce the release of `Robocorp Logging 0.0.10`.

*## Changes*


`Robocorp Logging` may be installed with: `pip install robocorp-robolog`.
Links: [PyPI](https://pypi.org/project/robocorp-robolog/), [GitHub (sources)](https://github.com/robocorp/robocorp-robolog)