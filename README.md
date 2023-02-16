# analyze-github

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets for `tap-github` variant `meltanolabs`. These datasets are automatically added to your Matatika workspace when you initialize a `tap-github` pipeline.

Files:
- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

### Adding this file bundle to your own Meltano project

Add plugin to `discovery.yml`:
```yaml
files:
- name: analyze-github
  namespace: tap_github
  repo: https://github.com/Matatika/analyze-github.git
  pip_url: git+https://github.com/Matatika/analyze-github.git
```

Add plugin to your Meltano project:
```bash
# Add only the file bundle
meltano add files analyze-github

# Add the file bundle as a related plugin through adding the extractor
meltano add extractor --include-related tap-github
```
