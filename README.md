# What is Conf
Conf manage secrets and non-secrets configurations.
It has a powerful and simple template rendering functionality.

## Example

This is a template file
TODO

How to render the template
Using input variable files

```
conf render -t template.tmpl -i dev.yml application.json --priority [ 'ssm' , 'file' ] --prefixes ['/dev/', '/default/']
```
By default renders using ssm then using files

Current version supports yaml input files
